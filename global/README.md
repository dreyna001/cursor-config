# Global rules and skills

- `rules/`: Cursor activation stubs and standing policies.
- `skills/`: Cursor user packages.
- `skills-cursor/`: preserved managed-skill archive.
- `codex/`: native Codex global instructions, skills and install manifest.

Use the matching harness router and load only relevant references. Generic guidance may route
to an app's local contract but must not embed that app's runtime values or approval exceptions.
Promoted shared skill packages are mirrored for harness compatibility and checked for drift;
their semantics are maintained once. App-only packages never install here.

Repository tools remain at `../codex/` and `../scripts/`. Follow the root README for installation.
