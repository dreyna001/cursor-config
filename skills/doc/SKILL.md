---
name: doc
description: "Use for reading, creating, or editing `.docx` documents when formatting or layout fidelity matters."
---
# DOCX Skill

## When to use
- Read or review DOCX content where layout matters (tables, diagrams, pagination).
- Create or edit DOCX files with professional formatting.
- Validate visual layout before delivery.

## Workflow
1. Prefer visual review (layout, tables, diagrams).
   - If `soffice` and `pdftoppm` are available, convert DOCX -> PDF -> PNGs.
   - Or use the bundled renderer under this skill's `scripts/` directory (requires `pdf2image` and Poppler); resolve its installed path rather than assuming it is under the project working directory.
   - If rendering tools are unavailable, extract text as a fallback and report that visual layout was not verified. Do not install system tools just for this step unless requested.
2. Use `python-docx` for edits and structured creation (headings, styles, tables, lists).
3. After each meaningful change, re-render and inspect the pages.
4. If visual review is not possible, extract text with `python-docx` as a fallback and call out layout risk.
5. Keep intermediate outputs organized and clean them up after verification; preserve user artifacts.

## Temp and output conventions
- Follow the project's existing output conventions. Use a temporary directory for intermediate files and a project-approved destination for final artifacts.
- Do not force `tmp/docs/` or `output/doc/` on repositories that do not use them.
- Keep filenames stable and descriptive.

## Dependencies
Prefer `uv` for dependency management.

Python packages:
```
uv pip install python-docx pdf2image
```
If `uv` is unavailable:
```
python3 -m pip install python-docx pdf2image
```
System tools (for rendering):
```
# macOS (Homebrew)
brew install libreoffice poppler

# Ubuntu/Debian
sudo apt-get install -y libreoffice poppler-utils
```

Use already-installed dependencies and project environments first. If a dependency is missing and installation is outside the requested scope, report what could not be rendered and which dependency is needed.

## Environment
No required environment variables.

## Rendering commands
DOCX -> PDF:
```
soffice -env:UserInstallation=file:///tmp/lo_profile_$$ --headless --convert-to pdf --outdir $OUTDIR $INPUT_DOCX
```

PDF -> PNGs:
```
pdftoppm -png $OUTDIR/$BASENAME.pdf $OUTDIR/$BASENAME
```

Bundled helper: resolve `scripts/render_docx.py` relative to the installed `doc` skill directory, then pass the source file and output directory.

## Quality expectations
- Deliver a client-ready document: consistent typography, spacing, margins, and clear hierarchy.
- Avoid formatting defects: clipped/overlapping text, broken tables, unreadable characters, or default-template styling.
- Charts, tables, and visuals must be legible in rendered pages with correct alignment.
- Use ASCII hyphens only. Avoid U+2011 (non-breaking hyphen) and other Unicode dashes.
- Citations and references must be human-readable; never leave tool tokens or placeholder strings.

## Final checks
- Re-render and inspect every page at 100% zoom before final delivery.
- Fix any spacing, alignment, or pagination issues and repeat the render loop.
- Confirm there are no leftovers (temp files, duplicate renders) unless the user asks to keep them.
