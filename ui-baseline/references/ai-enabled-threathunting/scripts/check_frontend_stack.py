"""Check the suite's explicit frontend pins without contacting a package registry."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

VARIANTS = ("azure_notable_pipeline", "llm_notable_analysis_onprem_systemd", "s3_notable_pipeline", "s3_notable_pipeline_commercial")


def check_root(root: Path, installed: bool = False) -> int:
    contract = json.loads((root / "docs/suite-frontend-stack.json").read_text())
    candidates = [root / "portal", root / "frontend", *(root / v / "frontend/analyst-portal" for v in VARIANTS)]
    frontends = [p for p in candidates if (p / "src/suite-workspace.css").is_file()]
    if not frontends:
        raise ValueError(f"No suite frontends in {root}")
    for frontend in frontends:
        package = json.loads((frontend / "package.json").read_text())
        dependencies = {**package.get("dependencies", {}), **package.get("devDependencies", {})}
        lock = json.loads((frontend / "package-lock.json").read_text())
        locked_root = lock["packages"][""]
        if package.get("packageManager") != contract["packageManager"]:
            raise ValueError(f"{frontend}: package manager differs from the suite contract")
        if package.get("engines") != contract["engines"]:
            raise ValueError(f"{frontend}: Node/npm engine contract differs")
        if (frontend / ".nvmrc").read_text().strip() != contract["node"]:
            raise ValueError(f"{frontend}: Node version differs")
        for name in contract["requiredPackages"]:
            if name not in dependencies:
                raise ValueError(f"{frontend}: missing shared package {name}")
        if "react-router-dom" in dependencies:
            raise ValueError(f"{frontend}: use react-router; v8 removed the compatibility package")
        for name, declared in dependencies.items():
            expected = contract["packages"].get(name)
            if expected is None:
                continue  # Product-specific packages remain local unless standardized.
            if declared != expected:
                raise ValueError(f"{frontend}: {name} declares {declared}, expected exact {expected}")
            actual = lock["packages"].get(f"node_modules/{name}", {}).get("version")
            if actual != expected:
                raise ValueError(f"{frontend}: {name} lock resolves {actual}, expected {expected}")
            if installed:
                actual = json.loads((frontend / "node_modules" / name / "package.json").read_text())["version"]
                if actual != expected:
                    raise ValueError(f"{frontend}: installed {name} is {actual}, expected {expected}")
        for section in ("dependencies", "devDependencies"):
            if package.get(section, {}) != locked_root.get(section, {}):
                raise ValueError(f"{frontend}: manifest/lock {section} differ; regenerate the lock normally")
    return len(frontends)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--installed", action="store_true")
    args = parser.parse_args()
    try:
        count = check_root(args.root, args.installed)
    except (ValueError, OSError, KeyError) as error:
        print(f"Frontend stack check failed: {error}")
        return 1
    print(f"Frontend stack pins verified for {count} frontend(s); installed={args.installed}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
