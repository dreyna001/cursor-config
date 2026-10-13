#!/usr/bin/env python3
"""Install and verify the canonical user-level Codex configuration."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import queue
import re
import shutil
import subprocess
import sys
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


OWNER = "dreyna001/cursor-config"
SOURCE_MANIFEST = "install-manifest.json"
INSTALLED_MANIFEST = "cursor-config-install-manifest.json"
BACKUP_PARENT = "backups"
BACKUP_PREFIX = "cursor-config-migration-"


class SetupError(RuntimeError):
    """Raised when a safe, unambiguous install cannot be completed."""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def item_sha256(path: Path) -> str:
    """Hash a file, symlink, or directory without following symlink targets."""
    digest = hashlib.sha256()
    if path.is_symlink():
        digest.update(b"symlink\0")
        digest.update(os.readlink(path).encode("utf-8", errors="surrogateescape"))
        return digest.hexdigest()
    if path.is_file():
        digest.update(b"file\0")
        digest.update(path.read_bytes())
        return digest.hexdigest()
    if path.is_dir():
        digest.update(b"directory\0")
        for child in sorted(path.rglob("*"), key=lambda item: item.relative_to(path).as_posix()):
            rel = child.relative_to(path).as_posix().encode("utf-8", errors="surrogateescape")
            digest.update(rel + b"\0")
            if child.is_symlink():
                digest.update(b"symlink\0" + os.readlink(child).encode("utf-8", errors="surrogateescape"))
            elif child.is_file():
                digest.update(b"file\0" + child.read_bytes())
            elif child.is_dir():
                digest.update(b"directory\0")
        return digest.hexdigest()
    raise SetupError(f"Cannot hash missing path: {path}")


def parse_frontmatter(skill_file: Path) -> dict[str, str]:
    content = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", content, re.DOTALL)
    if not match:
        raise SetupError(f"Missing YAML frontmatter: {skill_file}")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, raw_value = line.partition(":")
        if separator and key.strip() in {"name", "description"}:
            value = raw_value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
                value = value[1:-1]
            result[key.strip()] = value
    if not result.get("name") or not result.get("description"):
        raise SetupError(f"Skill must declare nonempty name and description: {skill_file}")
    return result


def discover_skills(source_root: Path) -> dict[str, dict[str, str]]:
    skills_root = source_root / "skills"
    if not skills_root.is_dir() or skills_root.is_symlink():
        raise SetupError(f"Expected a regular canonical skills directory: {skills_root}")
    skills: dict[str, dict[str, str]] = {}
    for package in sorted(skills_root.iterdir(), key=lambda item: item.name):
        if package.name.startswith("."):
            continue
        if package.is_symlink() or not package.is_dir():
            raise SetupError(f"Skill package must be a regular directory: {package}")
        skill_file = package / "SKILL.md"
        if not skill_file.is_file() or skill_file.is_symlink():
            raise SetupError(f"Skill package is missing a regular SKILL.md: {package}")
        metadata = parse_frontmatter(skill_file)
        if metadata["name"] != package.name:
            raise SetupError(
                f"Skill name {metadata['name']!r} does not match its directory {package.name!r}"
            )
        skills[package.name] = metadata
    if not skills:
        raise SetupError(f"No skill packages found under {skills_root}")
    return skills


def source_manifest_path(source_root: Path) -> Path:
    return source_root / SOURCE_MANIFEST


def make_source_manifest(source_root: Path, skills: dict[str, dict[str, str]]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "owner": OWNER,
        "global_instructions": "global-instructions.md",
        "skills_root": "skills",
        "skill_count": len(skills),
        "skills": sorted(skills),
        "runtime_entrypoints": {
            "instructions": "$CODEX_HOME/AGENTS.md (default ~/.codex/AGENTS.md)",
            "skills": "$HOME/.agents/skills",
            "legacy_skill_root": "$CODEX_HOME/skills (preserved, conflicting managed skills backed up)",
        },
    }


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SetupError(f"Cannot read JSON manifest {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SetupError(f"Manifest must contain a JSON object: {path}")
    return value


def load_source_manifest(source_root: Path, *, require_current: bool = True) -> tuple[dict[str, Any], dict[str, dict[str, str]]]:
    instructions = source_root / "global-instructions.md"
    if not instructions.is_file() or instructions.is_symlink():
        raise SetupError(f"Missing regular canonical global instruction file: {instructions}")
    skills = discover_skills(source_root)
    expected = make_source_manifest(source_root, skills)
    path = source_manifest_path(source_root)
    if not path.is_file():
        raise SetupError(f"Missing source manifest: {path}; run `sync --apply` to create it")
    actual = read_json(path)
    if require_current and actual != expected:
        raise SetupError(f"Source manifest is stale: {path}; run `sync --apply` after reviewing skill changes")
    return actual, skills


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if path.is_file() and path.read_text(encoding="utf-8") == rendered:
        return
    temp = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    temp.write_text(rendered, encoding="utf-8")
    os.replace(temp, path)


def tree_digest(source_root: Path, skill_names: list[str]) -> str:
    digest = hashlib.sha256()
    paths = [source_root / "global-instructions.md"]
    for name in skill_names:
        paths.extend(sorted((source_root / "skills" / name).rglob("*"), key=lambda item: item.relative_to(source_root).as_posix()))
    for path in sorted(paths, key=lambda item: item.relative_to(source_root).as_posix()):
        relative = path.relative_to(source_root).as_posix()
        digest.update(relative.encode("utf-8", errors="surrogateescape") + b"\0")
        if path.is_symlink():
            digest.update(b"symlink\0" + os.readlink(path).encode("utf-8", errors="surrogateescape"))
        elif path.is_file():
            digest.update(b"file\0" + path.read_bytes())
        elif path.is_dir():
            digest.update(b"directory\0")
    return digest.hexdigest()


def default_codex_home() -> Path:
    override = os.environ.get("CODEX_HOME")
    return Path(override).expanduser().resolve() if override else (Path.home() / ".codex").resolve()


def default_agents_home() -> Path:
    return (Path.home() / ".agents").resolve()


def path_exists(path: Path) -> bool:
    return path.exists() or path.is_symlink()


def backup_directory(codex_home: Path, *, create: bool) -> Path:
    parent = codex_home / BACKUP_PARENT
    if path_exists(parent) and (parent.is_symlink() or not parent.is_dir()):
        raise SetupError(f"Refusing unexpected backup parent: {parent}")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    candidate = parent / f"{BACKUP_PREFIX}{stamp}"
    suffix = 1
    while path_exists(candidate):
        candidate = parent / f"{BACKUP_PREFIX}{stamp}-{suffix:02d}"
        suffix += 1
    if create:
        candidate.mkdir(parents=True, exist_ok=False)
    return candidate


def backup_slot(backup_root: Path, codex_home: Path, agents_home: Path, path: Path) -> Path:
    if path == codex_home / "AGENTS.md":
        relative = Path("codex/AGENTS.md")
    elif path.is_relative_to(agents_home / "skills"):
        relative = Path("agents/skills") / path.name
    elif path.is_relative_to(codex_home / "skills"):
        relative = Path("legacy-codex-skills") / path.name
    elif path == codex_home / INSTALLED_MANIFEST:
        relative = Path(INSTALLED_MANIFEST)
    else:
        raise SetupError(f"No safe backup mapping for {path}")
    return backup_root / relative


def is_owned_installed_manifest(path: Path) -> bool:
    if not path_exists(path):
        return True
    if path.is_symlink() or not path.is_file():
        return False
    try:
        value = read_json(path)
    except SetupError:
        return False
    return value.get("owner") == OWNER and value.get("schema_version") == 1


def is_same_symlink(path: Path, target: Path) -> bool:
    return path.is_symlink() and path.resolve(strict=False) == target.resolve(strict=False)


def plan_install(source_root: Path, codex_home: Path, agents_home: Path) -> dict[str, Any]:
    source_root = source_root.resolve()
    codex_home = codex_home.resolve()
    agents_home = agents_home.resolve()
    source_manifest, skill_metadata = load_source_manifest(source_root)
    if (codex_home / "AGENTS.override.md").exists():
        raise SetupError(
            f"{codex_home / 'AGENTS.override.md'} overrides global instructions; resolve it before installing"
        )
    for root, label in ((codex_home, "Codex home"), (agents_home, "agents home")):
        if path_exists(root) and (root.is_symlink() or not root.is_dir()):
            raise SetupError(f"Refusing unexpected {label}: {root}")
    codex_skills = codex_home / "skills"
    official_root = agents_home / "skills"
    for root, label in ((codex_skills, "legacy skill root"), (official_root, "official skill root")):
        if path_exists(root) and (root.is_symlink() or not root.is_dir()):
            raise SetupError(f"Refusing unexpected {label}: {root}")

    installed_manifest_path = codex_home / INSTALLED_MANIFEST
    if not is_owned_installed_manifest(installed_manifest_path):
        raise SetupError(f"Refusing to overwrite unowned install manifest: {installed_manifest_path}")
    prior_manifest: dict[str, Any] = {}
    if path_exists(installed_manifest_path):
        prior_manifest = read_json(installed_manifest_path)

    source_instructions = source_root / str(source_manifest["global_instructions"])
    instruction_target = codex_home / "AGENTS.md"
    skill_targets = {
        name: (official_root / name, source_root / str(source_manifest["skills_root"]) / name)
        for name in skill_metadata
    }
    backup_paths: list[Path] = []
    if path_exists(instruction_target) and not is_same_symlink(instruction_target, source_instructions):
        backup_paths.append(instruction_target)
    for target, source in skill_targets.values():
        if path_exists(target) and not is_same_symlink(target, source):
            backup_paths.append(target)

    # A same-named package in the legacy tree would be discovered a second time.
    if path_exists(codex_skills):
        for name in skill_metadata:
            conflict = codex_skills / name
            if path_exists(conflict):
                backup_paths.append(conflict)

    old_managed = set(prior_manifest.get("managed_skills", []))
    new_managed = set(skill_metadata)
    for stale_name in sorted(old_managed - new_managed):
        stale = official_root / stale_name
        if path_exists(stale) and stale.is_symlink() and stale.resolve(strict=False) == (source_root / "skills" / stale_name).resolve(strict=False):
            backup_paths.append(stale)

    unique_backup_paths = list(dict.fromkeys(backup_paths))
    return {
        "source_root": source_root,
        "codex_home": codex_home,
        "agents_home": agents_home,
        "source_manifest": source_manifest,
        "skill_metadata": skill_metadata,
        "instruction_source": source_instructions,
        "instruction_target": instruction_target,
        "skill_targets": skill_targets,
        "backup_paths": unique_backup_paths,
        "prior_manifest": prior_manifest,
        "manifest_path": installed_manifest_path,
    }


def install(source_root: Path, codex_home: Path, agents_home: Path, *, apply: bool) -> dict[str, Any]:
    plan = plan_install(source_root, codex_home, agents_home)
    source_root = plan["source_root"]
    codex_home = plan["codex_home"]
    agents_home = plan["agents_home"]
    skill_metadata = plan["skill_metadata"]
    names = sorted(skill_metadata)
    changes = []
    if path_exists(plan["instruction_target"]):
        if not is_same_symlink(plan["instruction_target"], plan["instruction_source"]):
            changes.append({"action": "backup-and-link", "target": str(plan["instruction_target"]), "source": str(plan["instruction_source"])})
    else:
        changes.append({"action": "link", "target": str(plan["instruction_target"]), "source": str(plan["instruction_source"])})
    for name, (target, source) in plan["skill_targets"].items():
        if not is_same_symlink(target, source):
            changes.append({"action": "backup-and-link" if path_exists(target) else "link", "target": str(target), "source": str(source)})
    for path in plan["backup_paths"]:
        changes.append({"action": "backup-conflict", "target": str(path)})

    if not apply:
        return {"applied": False, "changes": changes, "skill_count": len(names), "source_sha256": tree_digest(source_root, names)}

    codex_home.mkdir(parents=True, exist_ok=True)
    agents_home.mkdir(parents=True, exist_ok=True)
    official_root = agents_home / "skills"
    official_root.mkdir(parents=True, exist_ok=True)
    backup_root: Path | None = None
    moved: list[tuple[Path, Path, str]] = []
    created_links: list[tuple[Path, Path]] = []
    backup_entries: list[dict[str, str]] = []
    previous_backups = list(plan["prior_manifest"].get("backups", []))
    try:
        if plan["backup_paths"]:
            backup_root = backup_directory(codex_home, create=True)
            for path in plan["backup_paths"]:
                destination = backup_slot(backup_root, codex_home, agents_home, path)
                if path_exists(destination):
                    raise SetupError(f"Backup destination already exists: {destination}")
                destination.parent.mkdir(parents=True, exist_ok=True)
                before = item_sha256(path)
                os.replace(path, destination)
                moved.append((path, destination, before))
                after = item_sha256(destination)
                if before != after:
                    raise SetupError(f"Backup hash mismatch after moving {path}")
                backup_entries.append({"original_path": str(path), "backup_path": str(destination), "sha256": before})

        instruction = plan["instruction_target"]
        source_instructions = plan["instruction_source"]
        if not is_same_symlink(instruction, source_instructions):
            instruction.parent.mkdir(parents=True, exist_ok=True)
            os.symlink(source_instructions, instruction)
            created_links.append((instruction, source_instructions))
        for name, (target, source) in plan["skill_targets"].items():
            if not is_same_symlink(target, source):
                target.parent.mkdir(parents=True, exist_ok=True)
                os.symlink(source, target, target_is_directory=True)
                created_links.append((target, source))

        if backup_root:
            atomic_write_json(backup_root / "manifest.json", {
                "schema_version": 1,
                "owner": OWNER,
                "created_at": utc_now(),
                "items": backup_entries,
            })

        source_hash = tree_digest(source_root, names)
        old_manifest = plan["prior_manifest"]
        old_hash = old_manifest.get("source_sha256")
        installed_at = old_manifest.get("installed_at") if old_hash == source_hash else utc_now()
        configuration_changed = bool(changes) or any(
            old_manifest.get(key) != value
            for key, value in (
                ("source_checkout", str(source_root)),
                ("codex_home", str(codex_home)),
                ("official_skill_root", str(official_root)),
                ("legacy_skill_root", str(codex_home / "skills")),
                ("managed_skills", names),
            )
        ) or old_hash != source_hash
        manifest = {
            "schema_version": 1,
            "owner": OWNER,
            "source_checkout": str(source_root),
            "source_sha256": source_hash,
            "global_instructions": str(source_instructions),
            "codex_home": str(codex_home),
            "official_skill_root": str(official_root),
            "legacy_skill_root": str(codex_home / "skills"),
            "managed_skills": names,
            "installed_at": installed_at,
            "updated_at": utc_now() if configuration_changed else old_manifest.get("updated_at", utc_now()),
            "backups": previous_backups + backup_entries,
        }
        manifest_path = plan["manifest_path"]
        if not path_exists(manifest_path) or read_json(manifest_path) != manifest:
            atomic_write_json(manifest_path, manifest)
    except Exception:
        for path, target in reversed(created_links):
            if is_same_symlink(path, target):
                path.unlink()
        for original, backup, _ in reversed(moved):
            if not path_exists(original) and path_exists(backup):
                original.parent.mkdir(parents=True, exist_ok=True)
                os.replace(backup, original)
        raise

    return {
        "applied": True,
        "changes": changes,
        "skill_count": len(names),
        "source_sha256": tree_digest(source_root, names),
        "backup_directory": str(backup_root) if backup_root else None,
        "installed_manifest": str(plan["manifest_path"]),
    }


def verify_static(source_root: Path, codex_home: Path, agents_home: Path) -> dict[str, Any]:
    plan = plan_install(source_root, codex_home, agents_home)
    errors: list[str] = []
    instruction = plan["instruction_target"]
    if not is_same_symlink(instruction, plan["instruction_source"]):
        errors.append(f"Global AGENTS.md is not linked to the canonical source: {instruction}")
    official_root = plan["agents_home"] / "skills"
    legacy_root = plan["codex_home"] / "skills"
    for name, (target, source) in plan["skill_targets"].items():
        if not is_same_symlink(target, source):
            errors.append(f"Skill is not linked to canonical source: {target}")
        legacy = legacy_root / name
        if path_exists(legacy):
            errors.append(f"Duplicate managed skill remains in legacy skill root: {legacy}")
    manifest_path = plan["manifest_path"]
    if not path_exists(manifest_path):
        errors.append(f"Missing active installation manifest: {manifest_path}")
    else:
        installed = read_json(manifest_path)
        if installed.get("owner") != OWNER or installed.get("managed_skills") != sorted(plan["skill_metadata"]):
            errors.append(f"Active installation manifest does not match canonical skills: {manifest_path}")
        current_hash = tree_digest(plan["source_root"], sorted(plan["skill_metadata"]))
        if installed.get("source_sha256") != current_hash:
            errors.append(f"Installed source fingerprint is stale: {manifest_path}")
    if (plan["codex_home"] / "AGENTS.override.md").exists():
        errors.append(f"Global override can mask canonical instructions: {plan['codex_home'] / 'AGENTS.override.md'}")
    return {
        "valid": not errors,
        "errors": errors,
        "skill_count": len(plan["skill_metadata"]),
        "global_instructions": str(instruction),
        "official_skill_root": str(official_root),
        "legacy_skill_root": str(legacy_root),
    }


def app_server_skills(command: list[str], cwds: list[Path], timeout: float = 45) -> tuple[list[dict[str, Any]], dict[str, Any], list[str]]:
    process = subprocess.Popen(
        [*command, "app-server", "--stdio"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        bufsize=1,
    )
    assert process.stdin and process.stdout and process.stderr
    output_queue: queue.Queue[str | None] = queue.Queue()
    stderr_lines: list[str] = []

    def read_stdout() -> None:
        for line in process.stdout:
            output_queue.put(line)
        output_queue.put(None)

    def read_stderr() -> None:
        stderr_lines.extend(process.stderr)

    threading.Thread(target=read_stdout, daemon=True).start()
    threading.Thread(target=read_stderr, daemon=True).start()
    next_id = 1

    def send(payload: dict[str, Any]) -> None:
        process.stdin.write(json.dumps(payload, separators=(",", ":")) + "\n")
        process.stdin.flush()

    def await_response(request_id: int) -> dict[str, Any]:
        deadline = datetime.now().timestamp() + timeout
        while True:
            remaining = deadline - datetime.now().timestamp()
            if remaining <= 0:
                raise SetupError(f"Timed out waiting for app-server response id={request_id}")
            try:
                line = output_queue.get(timeout=remaining)
            except queue.Empty as exc:
                raise SetupError(f"Timed out waiting for app-server response id={request_id}") from exc
            if line is None:
                raise SetupError("Codex app-server exited before returning the requested skill list")
            try:
                value = json.loads(line)
            except json.JSONDecodeError:
                continue
            if value.get("id") == request_id:
                if "error" in value:
                    raise SetupError(f"Codex app-server request failed: {value['error']}")
                return value.get("result", {})

    try:
        send({
            "method": "initialize",
            "id": next_id,
            "params": {"clientInfo": {"name": "cursor-config-verifier", "version": "1"}},
        })
        initialize_result = await_response(next_id)
        next_id += 1
        send({"method": "initialized", "params": {}})
        send({
            "method": "skills/list",
            "id": next_id,
            "params": {"cwds": [str(cwd.resolve()) for cwd in cwds], "forceReload": True},
        })
        response = await_response(next_id)
        entries = response.get("data")
        if not isinstance(entries, list):
            raise SetupError("Codex app-server returned an invalid skills/list response")
        return entries, initialize_result, stderr_lines
    finally:
        try:
            process.stdin.close()
            process.wait(timeout=5)
        except (BrokenPipeError, subprocess.TimeoutExpired):
            process.kill()
            process.wait(timeout=5)


def verify_runtime(source_root: Path, codex_home: Path, agents_home: Path, cwd_list: list[Path], codex_command: str) -> dict[str, Any]:
    static = verify_static(source_root, codex_home, agents_home)
    if not static["valid"]:
        raise SetupError("Static installation verification failed: " + "; ".join(static["errors"]))
    _, metadata = load_source_manifest(source_root.resolve())
    managed_names = set(metadata)
    chosen_cwds = list(cwd_list)
    if not chosen_cwds:
        chosen_cwds = [Path.cwd()]
    for cwd in chosen_cwds:
        if not cwd.is_dir():
            raise SetupError(f"Verification CWD does not exist: {cwd}")
    # The canonical source directory is a third context: it must not turn global skills into repo skills.
    source_cwd = source_root.resolve()
    if source_cwd.is_dir() and source_cwd not in [cwd.resolve() for cwd in chosen_cwds]:
        chosen_cwds.append(source_cwd)
    entries, initialize_result, stderr = app_server_skills([codex_command], chosen_cwds)
    issues: list[str] = []
    actual_codex_home = initialize_result.get("codexHome")
    if actual_codex_home and Path(actual_codex_home).resolve() != codex_home.resolve():
        issues.append(f"app-server used Codex home {actual_codex_home}, expected {codex_home.resolve()}")
    if agents_home.resolve() != default_agents_home():
        issues.append(
            f"app-server discovery uses the native global skill home {default_agents_home()}, not test path {agents_home.resolve()}"
        )
    per_cwd: list[dict[str, Any]] = []
    expected_paths = {name: (source_root.resolve() / "skills" / name / "SKILL.md").resolve() for name in managed_names}
    for entry in entries:
        cwd = str(entry.get("cwd", "<unknown>"))
        for error in entry.get("errors", []):
            issues.append(f"{cwd}: skill discovery error: {error}")
        skills = entry.get("skills", [])
        counts: dict[str, int] = {}
        managed_seen: set[str] = set()
        skill_details: list[dict[str, Any]] = []
        for skill in skills:
            name = skill.get("name", "")
            counts[name] = counts.get(name, 0) + 1
            if name not in managed_names:
                continue
            managed_seen.add(name)
            resolved = Path(skill.get("path", "")).resolve(strict=False)
            expected = expected_paths[name]
            if skill.get("scope") != "user":
                issues.append(f"{cwd}: managed skill {name!r} has scope {skill.get('scope')!r}, expected 'user'")
            if skill.get("enabled") is not True:
                issues.append(f"{cwd}: managed skill {name!r} is not enabled")
            if resolved != expected:
                issues.append(f"{cwd}: managed skill {name!r} resolves to {resolved}, expected {expected}")
            actual_description = skill.get("description", "")
            expected_description = metadata[name]["description"]
            if actual_description != expected_description:
                issues.append(f"{cwd}: runtime description differs from canonical SKILL.md for {name!r}")
            skill_details.append({"name": name, "path": str(resolved), "scope": skill.get("scope"), "description_chars": len(actual_description)})
        duplicates = sorted(name for name, count in counts.items() if count != 1 and name in managed_names)
        for duplicate in duplicates:
            issues.append(f"{cwd}: managed skill {duplicate!r} appears {counts[duplicate]} times")
        missing = sorted(managed_names - managed_seen)
        for name in missing:
            issues.append(f"{cwd}: managed skill {name!r} is missing from app-server catalog")
        per_cwd.append({"cwd": cwd, "total_catalog_entries": len(skills), "managed_skill_count": len(managed_seen), "managed_skills": skill_details})
    if len(entries) != len(chosen_cwds):
        issues.append(f"app-server returned {len(entries)} CWD entries for {len(chosen_cwds)} requested CWDs")
    return {
        "valid": not issues,
        "issues": issues,
        "cli": codex_command,
        "app_server_user_agent": initialize_result.get("userAgent"),
        "codex_home": initialize_result.get("codexHome"),
        "stderr_line_count": len(stderr),
        "skill_count": len(managed_names),
        "cwd_results": per_cwd,
    }


def write_source_manifest(source_root: Path, *, apply: bool) -> dict[str, Any]:
    skills = discover_skills(source_root.resolve())
    data = make_source_manifest(source_root, skills)
    path = source_manifest_path(source_root)
    if not apply:
        return {"applied": False, "path": str(path), "skill_count": len(skills), "skill_names": sorted(skills)}
    atomic_write_json(path, data)
    return {"applied": True, "path": str(path), "skill_count": len(skills), "skill_names": sorted(skills)}


def parser() -> argparse.ArgumentParser:
    default_source = Path(__file__).resolve().parent
    root = argparse.ArgumentParser(description="Install and verify the canonical global Codex instructions and skills.")
    root.add_argument("--source", type=Path, default=default_source, help="Canonical codex/ source directory (default: this script's directory).")
    root.add_argument("--codex-home", type=Path, default=default_codex_home(), help="Codex home (default: CODEX_HOME or ~/.codex).")
    root.add_argument("--agents-home", type=Path, default=default_agents_home(), help="Global skills home (default: ~/.agents).")
    commands = root.add_subparsers(dest="command", required=True)
    commands.add_parser("plan", help="Validate sources and print install changes without writing.")
    install_parser = commands.add_parser("install", help="Install links; use --apply to write changes.")
    install_parser.add_argument("--apply", action="store_true", help="Create links, backups, and the local install manifest.")
    sync_parser = commands.add_parser("sync", help="Refresh the source manifest and synchronize global links.")
    sync_parser.add_argument("--apply", action="store_true", help="Refresh manifest and install the current canonical sources.")
    verify_parser = commands.add_parser("verify", help="Check links and optionally the live Codex skill catalog.")
    verify_parser.add_argument("--runtime", action="store_true", help="Query app-server skills/list (no model/provider call).")
    verify_parser.add_argument("--cwd", action="append", type=Path, default=[], help="CWD to include in runtime verification; repeat for multiple projects.")
    verify_parser.add_argument("--codex-command", default=shutil.which("codex") or str(Path.home() / ".local/bin/codex"), help="Codex executable used for app-server verification.")
    refresh_parser = commands.add_parser("refresh-manifest", help="Show or write the source skill-name manifest.")
    refresh_parser.add_argument("--apply", action="store_true", help="Write codex/install-manifest.json from current skill packages.")
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "refresh-manifest":
            result = write_source_manifest(args.source, apply=args.apply)
        elif args.command == "sync":
            if args.apply:
                write_source_manifest(args.source, apply=True)
            result = install(args.source, args.codex_home, args.agents_home, apply=args.apply)
        elif args.command in {"plan", "install"}:
            result = install(args.source, args.codex_home, args.agents_home, apply=args.command == "install" and args.apply)
        elif args.command == "verify":
            result = verify_static(args.source, args.codex_home, args.agents_home)
            if args.runtime:
                runtime = verify_runtime(args.source, args.codex_home, args.agents_home, args.cwd, args.codex_command)
                result["runtime"] = runtime
                result["valid"] = bool(result["valid"] and runtime["valid"])
            if not result.get("valid", True):
                print(json.dumps(result, indent=2, sort_keys=True))
                return 1
        else:
            raise SetupError(f"Unknown command: {args.command}")
    except SetupError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
