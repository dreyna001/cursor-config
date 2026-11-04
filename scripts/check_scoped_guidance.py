#!/usr/bin/env python3
"""Check scope separation, source manifests and shared harness mirrors."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
APPS = ("ai-enabled-ato", "ai-enabled-threathunting", "llm_notable_analysis")
PROMOTED = ("report-export-parity", "evidence-field-mapping", "agentic-security-workflows")


def check() -> dict:
    checked = 0
    for scope in ("global", *APPS):
        assert (ROOT / scope).is_dir(), f"Missing scope {scope}"
    for old in ("rules", "skills", "skills-cursor"):
        assert not (ROOT / old).exists(), f"Duplicate legacy global directory {old}"
    for name in PROMOTED:
        canonical = ROOT / "global/codex/skills" / name / "SKILL.md"
        assert canonical.read_bytes() == (ROOT / "global/skills" / name / "SKILL.md").read_bytes(), f"Shared mirror drift: {name}"
    # Global routes must not link to app policy that has been moved out.
    for path in (ROOT / "global").rglob("*.md"):
        content = path.read_text()
        for link in re.findall(r"\]\(([^)\s]+)\)", content):
            if any(name in link for name in ("api-project-checkpoints.md", "ato-runtime-deployment-contract.md")):
                raise AssertionError(f"Global route retains removed app-only contract: {path}: {link}")
    shared_refs = ("shared-frontend-foundations.md", "safe-reuse-and-preparation.md",
                   "llm-efficiency.md", "reliability-and-performance.md",
                   "api-data-and-distributed.md")
    for name in shared_refs:
        refs = Path("references") / name
        canonical = ROOT / "global/codex/skills/engineering-guidance" / refs
        mirror = ROOT / "global/skills/cursor-rules" / refs
        assert canonical.read_bytes() == mirror.read_bytes(), f"Shared reference drift: {name}"
        for path in (canonical, mirror):
            for link in re.findall(r"\]\(([^)\s]+)\)", path.read_text()):
                if link.startswith(("#", "http:", "https:", "mailto:", "C:")):
                    continue
                assert (path.parent / link.split("#")[0]).exists(), f"Broken shared reference: {path}: {link}"
    for app in APPS:
        package = ROOT / app
        manifest = json.loads((package / "source-manifest.json").read_text())
        assert manifest["scope"] == "project_only" and manifest["project"] == app
        expected = {item["path"] for item in manifest["files"]}
        actual = {str(p.relative_to(package)) for p in package.rglob("*") if p.is_file() and p.name != "source-manifest.json"}
        assert actual == expected, f"Manifest inventory differs: {app}"
        for item in manifest["files"]:
            path = package / item["path"]
            assert path.resolve().is_relative_to(package.resolve()), f"Escaping manifest path: {path}"
            assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"Modified package: {path}"
            checked += 1
            # Full source snapshots keep original-app links as provenance; normalized
            # package entrypoints must instead resolve within their own package.
            if path.suffix == ".mdc" or path.name == "SKILL.md":
                for link in re.findall(r"\]\(([^)\s]+)\)", path.read_text()):
                    if link.startswith(("#", "http:", "https:", "mailto:")):
                        continue
                    assert (path.parent / link.split("#")[0]).exists(), f"Broken package entrypoint link: {path}: {link}"
    for root in (ROOT / "global/codex/skills/engineering-guidance", ROOT / "global/skills/cursor-rules"):
        assert not (root / "references/ato-runtime-deployment-contract.md").exists(), "ATO contract leaked globally"
        assert not (root / "references/api-project-checkpoints.md").exists(), "App checkpoint leaked globally"
        assert "## Project Review Checkpoints" not in (root / "references/api-abuse-and-exposure.md").read_text()
    return {"valid": True, "scopes": ["global", *APPS], "app_files_checked": checked, "promoted_shared_skills": list(PROMOTED)}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
