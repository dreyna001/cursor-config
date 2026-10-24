"""Validate released UI baseline sources; this does not replace rendered UI tests."""
from __future__ import annotations

import argparse
import hashlib
import html
from pathlib import Path
import re
import subprocess

AUTHORITY = "https://github.com/dreyna001/ai-enabled-threathunting/blob/main/docs/suite-ui-standard.md"
VARIANTS = ("s3_notable_pipeline", "s3_notable_pipeline_commercial", "azure_notable_pipeline", "llm_notable_analysis_onprem_systemd")


def frontends(root: Path) -> list[Path]:
    return [path for path in [root / "frontend", root / "portal", *(root / name / "frontend/analyst-portal" for name in VARIANTS)] if (path / "src/suite-workspace.css").is_file()]


def read_release(root: Path) -> tuple[str, str, str]:
    doc = (root / "docs/suite-ui-standard.md").read_text(encoding="utf-8")
    version = re.search(r"Version: \*\*(\d+\.\d+\.\d+)\*\*", doc)
    if not version or AUTHORITY not in doc or "## Start here: the UI/UX index" not in doc:
        raise ValueError(f"{root}: missing central authority/index/version")
    paths = frontends(root)
    if not paths:
        raise ValueError(f"{root}: no suite frontends found")
    css = [p.joinpath("src/suite-workspace.css").read_text(encoding="utf-8") for p in paths]
    if len(set(css)) != 1 or f"Suite Workspace UI v{version[1]}." not in css[0]:
        raise ValueError(f"{root}: stylesheet copies or version disagree")
    for required in ("--workspace-motion-duration: 150ms", "--workspace-motion-ease:", "--workspace-motion-spinner-duration:", "--workspace-motion-pulse-duration:", "--workspace-motion-typing-duration:", "prefers-reduced-motion: reduce", "animation: none !important", "transition: none !important"):
        if required not in css[0]:
            raise ValueError(f"{root}: missing shared motion contract: {required}")
    for required in ("--workspace-color-control-border: #6e7b8d", ".workspace-skip-link", ".workspace-confirm-dialog::backdrop", "forced-colors: active"):
        if required not in css[0]:
            raise ValueError(f"{root}: missing shared accessibility role: {required}")
    if "## Interaction and accessibility" not in doc or "loading-to-content" not in doc.lower():
        raise ValueError(f"{root}: missing interaction/accessibility verification contract")
    instructions = root.joinpath("AGENTS.md").read_text(encoding="utf-8")
    if "docs/suite-ui-standard.md" not in instructions or "authoritative" not in instructions:
        raise ValueError(f"{root}: AGENTS.md does not route to the central baseline")
    if "Interaction and accessibility" not in instructions:
        raise ValueError(f"{root}: AGENTS.md does not require the interaction coverage checks")
    for relative in ("design-previews/20261018/unified/visual-reference.html", "docs/mockups/ssp-ui-explorations/10-unified-workspace-reference.html"):
        path = root / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if f'name="suite-ui-baseline" content="{version[1]}"' not in text or AUTHORITY not in text:
            raise ValueError(f"{path}: missing baseline version/backlink")
        if html.escape(doc) not in text:
            raise ValueError(f"{path}: embedded baseline is stale")
        screen_css = re.sub(r"@font-face\s*\{[^}]*\}", "", css[0])
        if screen_css not in text:
            raise ValueError(f"{path}: current shared CSS is missing")
        if "single current visual source of truth" in text:
            raise ValueError(f"{path}: retired competing-authority claim")
    return doc, css[0], version[1]


def preserve_runtime(root: Path, ref: str) -> None:
    changed = subprocess.check_output(["git", "-C", str(root), "diff", "--name-only", ref], text=True).splitlines()
    prefixes = [str(path.relative_to(root)).replace("\\", "/") + "/src/" for path in frontends(root)]
    for relative in changed:
        if not any(relative.startswith(prefix) for prefix in prefixes):
            continue
        before = subprocess.check_output(["git", "-C", str(root), "show", f"{ref}:{relative}"])
        after = (root / relative).read_bytes()
        normalize = lambda content: re.sub(rb"Suite Workspace UI v\d+\.\d+\.\d+", b"Suite Workspace UI VERSION", content, count=1)
        if normalize(before) != normalize(after):
            raise ValueError(f"{root / relative}: runtime source changed beyond baseline version marker")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--peer", type=Path, action="append", default=[], help="Other suite checkout; repeat for both peers")
    parser.add_argument("--preserve-ref", help="Also require frontend runtime source to match this Git ref except the baseline version marker")
    args = parser.parse_args()
    try:
        releases = [read_release(root) for root in [args.root, *args.peer]]
        if len({release[:2] for release in releases}) != 1:
            raise ValueError("Suite release documents/stylesheets differ across repositories")
        if args.preserve_ref:
            for root in [args.root, *args.peer]:
                preserve_runtime(root, args.preserve_ref)
        checksum = hashlib.sha256(releases[0][1].encode()).hexdigest()[:12]
        print(f"Suite UI baseline {releases[0][2]}: source/link/version parity passed ({len(releases)} repos; CSS {checksum}).")
        if args.preserve_ref:
            print("Frontend runtime preserved: login/account, layout, fonts, colors and behavior sources unchanged except version markers.")
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Suite UI baseline check failed: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
