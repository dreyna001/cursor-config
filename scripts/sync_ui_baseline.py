#!/usr/bin/env python3
"""Validate and install the versioned offline UI baseline without changing apps."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

APP_CSS = {
    "ai-enabled-threathunting": ["frontend/src/suite-workspace.css"],
    "ai-enabled-ato": ["portal/src/suite-workspace.css"],
    "llm_notable_analysis": [
        f"{variant}/frontend/analyst-portal/src/suite-workspace.css"
        for variant in (
            "s3_notable_pipeline", "s3_notable_pipeline_commercial",
            "azure_notable_pipeline", "llm_notable_analysis_onprem_systemd",
        )
    ],
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def version_tuple(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def validate(bundle: Path) -> dict:
    manifest = json.loads((bundle / "manifest.json").read_text(encoding="utf-8"))
    seen = set()
    for item in manifest["files"]:
        name = item["path"]
        path = bundle / name
        if name in seen or Path(name).is_absolute() or not path.resolve().is_relative_to(bundle.resolve()):
            raise ValueError(f"Invalid or duplicate manifest path: {name}")
        seen.add(name)
        if digest(path) != item["local_sha256"]:
            raise ValueError(f"Modified baseline file: {path}")
    text = (bundle / "README.md").read_text(encoding="utf-8")
    if f'Version: **{manifest["version"]}**' not in text:
        raise ValueError("Manifest and baseline versions differ")
    for repo in APP_CSS:
        snapshot = bundle / "references" / repo / "docs/suite-ui-standard.md"
        if snapshot.read_bytes() != (bundle / "references/ai-enabled-threathunting/docs/suite-ui-standard.md").read_bytes():
            raise ValueError(f"Released baseline differs for {repo}")
    for name in ("README.md", "verification.md", "visual-reference.html"):
        text = (bundle / name).read_text(encoding="utf-8")
        links = re.findall(r"\]\(([^)\s]+)\)", text)
        if name.endswith(".html"):
            links += re.findall(r'''(?:href|src)=["']([^"']+)''', text)
        for link in links:
            if link.startswith(("#", "http:", "https:", "mailto:", "data:")):
                continue
            if not (bundle / link.split("#")[0]).exists():
                raise ValueError(f"Broken local link in {name}: {link}")
    return manifest


def compare_apps(bundle: Path, roots: list[Path], ref: str | None) -> int:
    by_name = {root.resolve().name: root for root in roots}
    if set(by_name) != set(APP_CSS) or len(roots) != 3:
        raise ValueError("Supply all three distinct app repository roots")
    baseline = (bundle / "references/ai-enabled-threathunting/docs/suite-ui-standard.md").read_bytes()
    css = (bundle / "references/ai-enabled-threathunting/frontend/src/suite-workspace.css").read_bytes()
    checked = 0
    for name, root in by_name.items():
        def read(relative: str) -> bytes:
            if ref:
                return subprocess.check_output(["git", "-C", str(root), "show", f"{ref}:{relative}"])
            return (root / relative).read_bytes()
        if read("docs/suite-ui-standard.md") != baseline:
            raise ValueError(f"Baseline drift in {name}")
        for relative in APP_CSS[name]:
            if read(relative) != css:
                raise ValueError(f"Stylesheet drift in {name}/{relative}")
            checked += 1
    return checked


def compare_installed(source: Path, destination: Path) -> None:
    manifest = validate(destination)
    expected = validate(source)
    if manifest != expected:
        raise ValueError("Installed baseline manifest differs from the versioned bundle")


def install(source: Path, destination: Path) -> None:
    manifest = validate(source)
    if source.resolve() == destination.resolve():
        return
    known = set()
    if destination.exists():
        # Preserve local edits and prevent a stale checkout from downgrading users.
        previous = validate(destination)
        if version_tuple(previous["version"]) > version_tuple(manifest["version"]):
            raise ValueError("Refusing to downgrade a newer installed baseline")
        known = {item["path"] for item in previous["files"]}
    # Preflight the complete write set before modifying any installed file.
    for item in manifest["files"]:
        target = destination / item["path"]
        if not target.resolve().is_relative_to(destination.resolve()):
            raise ValueError(f"Destination escapes the baseline folder: {target}")
        if (target.exists() and item["path"] not in known
                and (not target.is_file() or digest(target) != item["local_sha256"])):
            raise ValueError(f"Refusing to overwrite an untracked local file: {target}")
    destination.mkdir(parents=True, exist_ok=True)
    for item in manifest["files"]:
        target = destination / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / item["path"], target)
    # Publish the manifest last. Unknown local files are intentionally preserved.
    shutil.copy2(source / "manifest.json", destination / "manifest.json")
    compare_installed(source, destination)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "install"))
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1] / "ui-baseline")
    parser.add_argument("--destination", type=Path, default=Path.home() / ".agents/ui-baseline")
    parser.add_argument("--installed", action="store_true")
    parser.add_argument("--app-root", type=Path, action="append", default=[])
    parser.add_argument("--ref", help="Read approved app Git refs instead of working files; fetch before use")
    args = parser.parse_args()
    try:
        manifest = validate(args.source)
        checked = compare_apps(args.source, args.app_root, args.ref) if args.app_root else 0
        if args.ref and not args.app_root:
            raise ValueError("--ref requires all three --app-root values")
        if args.command == "install":
            install(args.source, args.destination)
        if args.installed:
            compare_installed(args.source, args.destination)
        print(json.dumps({"valid": True, "version": manifest["version"], "frontends_checked": checked,
                          "installed": args.command == "install" or args.installed}))
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Baseline check failed: {exc}\n")


if __name__ == "__main__":
    main()
