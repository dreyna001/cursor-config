# cursor-config

Canonical, versioned Cursor rules/skills and Codex guidance, separated into four policy scopes:

- [global/](global/): shared guidance usable across projects.
- [ai-enabled-ato/](ai-enabled-ato/): SSP app rules, runtime and field contracts, revision/authority safeguards.
- [ai-enabled-threathunting/](ai-enabled-threathunting/): hunt workflow, reporting exceptions and saved-export safeguards.
- [llm_notable_analysis/](llm_notable_analysis/): four-product case contracts and commercial/GovCloud boundaries.

## Global scope

`global/rules/` contains Cursor activation rules; `global/skills/` contains Cursor user skills; `global/skills-cursor/` retains the existing managed-skill archive.
`global/codex/` contains Codex global instructions, user skills and the install manifest.
Repository tools remain in `codex/` and `scripts/`; the versioned offline UI bundle remains in `ui-baseline/`.
Installed user paths do not change.

For coding, read only matching references through Cursor's `cursor-rules` or Codex's `engineering-guidance` router.
Use the existing `llm-evidence-regression` for reusable analysis fixes; do not duplicate that policy.
New `report-export-parity` and `evidence-field-mapping` skills contain reusable contracts.
Shared frontend changes use `shared-frontend-foundations` while keeping domain adapters and independent app deployments.
Application labels, field meanings, runtime exceptions and approval/release gates stay in project packages.
`scripts/check_scoped_guidance.py` checks the four scopes, app manifests, package links and the promoted shared mirrors.

### Codex installation

Use Python 3.12 or newer. Preview, then install into the current profile:

```sh
python3 codex/global_setup.py plan
python3 codex/global_setup.py sync --apply
python3 codex/global_setup.py verify
```

The script now resolves sources from `global/codex/`. It backs up conflicting managed paths,
preserves unowned/system/plugin skills and rejects a masking global override.
Linux-only contextual learning remains excluded on other platforms.
The shared `agentic-security-workflows` package is already in the managed inventory; use the
runtime check to establish actual discovery rather than guessing from a missing Windows catalog.

For a bounded skill-discovery check without model/provider calls:

```sh
python3 codex/global_setup.py verify --runtime --cwd /path/to/project-one --cwd /path/to/project-two
```

This change's active installation is WSL only. It does not authorize installing skills in Windows
or copying private lesson stores, credentials, customer data or runtime state into Git.

### Cursor installation

On Windows, `.\install-to-user-cursor.ps1` installs only `global/` into the current Cursor profile;
`.\sync-from-local.ps1` refreshes only that global archive. It never sweeps project packages.
The installer retains its Linux-only learning safeguards.

On Linux/WSL, review and copy the required global files into `~/.cursor/rules/` and
`~/.cursor/skills/`, preserving and backing up changed local files first.
Do not copy the three app folders into user-level/global discovery roots.
The promoted shared skill mirrors in Cursor and Codex packaging must remain identical;
the checker verifies this rather than maintaining independent policies. The existing agentic-security-workflows package is also mirrored for Cursor discovery.

## Project-only installation and duplicate consolidation

Read the matching app folder's README. Review its `rules/` and complete `skills/` packages,
then copy only those into that application's `.cursor/rules/` and `.cursor/skills/`.
Current root/nested `AGENTS.md` and normative app source remain authoritative.
Packaged full AGENTS files are provenance snapshots, never replacement global or app harnesses.
App packages include source revisions, source/output hashes, excerpt boundaries and dirty-source markers;
a snapshot is not proof of deployed behavior or live qualification.

When consolidating an old app copy of global guidance, first verify the corresponding current global
rule/skill is actually available in that harness. Preserve the original outside active discovery,
record hashes and the replacement, and retain all unique app safeguards locally.
Do not remove unknown packages merely because their names look generic.

## Verification

```sh
python3 scripts/check_scoped_guidance.py
python3 -m unittest discover -s codex/tests
python3 scripts/sync_ui_templates.py --check
```

These checks cover configuration packaging, installer preservation and retained source contracts.
They do not run app suites, live searches, model evaluations or production deployment checks.
Use the permanent UI baseline for actual UI work; this reorganization changes no app UI or baseline.
Historical release records under `docs/` retain the commands that were valid at their recorded revision.

On WSL, native Codex project discovery uses `.agents/skills/`. Link each app-only package there to its matching `.cursor/skills/<name>` package (a relative `../../.cursor/skills/<name>` symlink from the project skill directory), so both harnesses read the same local body. Never link an app-only skill into the user global root.
