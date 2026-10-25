# cursor-config

Canonical versioned source for the user's global Cursor configuration and Codex instructions and skills. Cursor assets keep their existing layout; Codex assets live under `codex/` and install through native user-level entry points.

## Layout

- `rules/` — global `.mdc` rule files (`~/.cursor/rules/` on Linux, `%USERPROFILE%\.cursor\rules\` on Windows)
- `skills/` — user skills (`~/.cursor/skills/`)
- `skills-cursor/` — Cursor-managed skills (`~/.cursor/skills-cursor/`)
- `environment.json` — optional Cursor environment config
- `codex/global-instructions.md` — global Codex instructions, linked to `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`)
- `codex/skills/` — portable Codex user skills, linked individually under `~/.agents/skills/`
- `codex/install-manifest.json` — the expected global Codex skill inventory
- `codex/global_setup.py` — read-only planning, local installation/sync, and app-server verification

## Permanent local UI/UX baseline

`ui-baseline/README.md` is the versioned, offline reading bundle for the suite UI
standard, with its companion, source snapshots and alignment record. Install it
at `$HOME/.agents/ui-baseline/` (`%USERPROFILE%\.agents\ui-baseline\` on Windows):

```sh
python3 scripts/sync_ui_baseline.py check
python3 scripts/sync_ui_baseline.py install
python3 scripts/sync_ui_baseline.py check --installed
```

Open the installed `README.md` first for every UI/UX task. The current workstation
uses one physical Windows bundle through a WSL alias. Other machines use their
own user-profile copy. No GitHub sign-in is required to read an installed bundle.

Approved shared UI changes are incomplete until the three app releases (six
frontends), versioned baseline/companion, this bundle and installed copies agree.
Follow [Keeping one baseline](ui-baseline/README.md#keeping-one-baseline), including
app-specific exceptions and rendered/workflow validation. Preserve newer approved
login/account behavior, sidebar spacing, typography, colors, layouts and features.

The [alignment analysis](ui-baseline/verification.md) and release qualification
records describe the covered browser and workflow checks; they do not claim live-cloud
qualification. New changes need their own relevant validation record.

## How Cursor uses this

Cursor loads `~/.cursor/rules/*.mdc` from the user profile. `alwaysApply: true` rules are standing policy for every chat. Other rules apply when their `globs` match open files, or when the agent is told to load them. Project-specific rules stay in each application repo's `.cursor/rules/`.

For coding, review, or refactoring, use the `cursor-rules` skill as the router and read only the matching references. Do not load the whole collection. Named skills under `skills/` are used when their description matches the task. `windows-agent-shell-fallback` is Cursor-only: if the Windows integrated shell is Constrained Language Mode, retry with `powershell.exe` or `wsl.exe`.

Contextual learning is enabled for Ubuntu Cursor through `skills/contextual-learning/` and the Linux-only section of `rules/global-operating-baseline.mdc`. It reuses the existing `${CODEX_HOME:-$HOME/.codex}/learning/` collection and locked revision helper. Install this skill and rule section only into the Ubuntu profile; Windows contextual learning remains disabled unless separately requested. Keep the helper, template, and tests aligned with `codex/skills/contextual-learning/`; only the Cursor entry point and invocation path differ.

On Linux/WSL, install Cursor rules and the Linux-only learning skill into the Linux profile:

```sh
mkdir -p ~/.cursor/rules ~/.cursor/skills
cp -a rules/*.mdc ~/.cursor/rules/
cp -a skills/contextual-learning ~/.cursor/skills/
```

On Windows, use `.\install-to-user-cursor.ps1`; it excludes contextual learning and strips its managed activation section. Do not copy the Linux rule bundle directly into Windows. An existing Windows learning package must be reviewed and preserved outside the active skill roots before installation.

## How Codex uses this

Codex does not read Cursor `.mdc` files. Its always-on harness is `codex/global-instructions.md`, installed as `~/.codex/AGENTS.md`. Skills come from `codex/skills/` and appear under `~/.agents/skills/` after `python3 codex/global_setup.py sync --apply`.

For coding, review, or refactoring, use the `engineering-guidance` skill as the router and read only the matching references. Follow this file's install commands; do not assume Cursor tools exist in Codex.

## Refresh this repo from the current PC

```powershell
.\sync-from-local.ps1
git add -A
git commit -m "Sync rules and skills from local Cursor config"
git push
```

## Install on a machine (after `git clone` or `git pull`)

```powershell
.\install-to-user-cursor.ps1
```

That copies the applicable rules, skills, and environment configuration into `%USERPROFILE%\.cursor\`; contextual learning is excluded. Existing same-name files are overwritten.

## Clone elsewhere

```powershell
git clone https://github.com/dreyna001/cursor-config.git
cd cursor-config
.\install-to-user-cursor.ps1
```

Project-specific rules stay in each repo's `.cursor/` folder. This repo is for global Cursor config you want versioned and portable.

## Shared backup guidance

`skills/cloud-native-platform-architecture/references/data-protection.md` is the Cursor authoring source for conditional backup decisions. Its byte-identical Codex distribution is `codex/skills/cloud-native-platform-architecture/references/data-protection.md`. Edit the shared reference and mirror it; architecture/Terraform skills, engineering routers and existing rules link to it instead of copying provider policy. Both installers include the reference as part of the existing skill package; no new skill or manifest entry is needed. This documentation update does not install, publish or deploy anything.

## Install global Codex configuration

The Codex source collection contains 58 custom skills; Linux installs all 58 and non-Linux installs exclude contextual learning (57). Overlapping planning, debugging, cybersecurity, and review workflows share retained entry points; tool-specific production guidance lives in ten conditional references, with official vendor sources, rather than additional skills. The engineering router links directly to those references for existing integrations; stack-selection defaults are not prerequisites for routine implementation. The focused `llm-evidence-regression` workflow pairs unsupported rejection with supported evidence/decision retention, while keeping captured recovery separate from live model quality. The `boundary-failure-regressions` skill checks reproduced parser, API, timeout/cancellation, and persistence failures while protecting adjacent supported behavior.

Model routing follows the user/session choice. A Sol 6.1 high or Astra high primary can work directly; bounded independent work can use subagents when that improves speed or quality. This follows OpenAI's [subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents) and [Astra skill-writing guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). Repository instructions should add project constraints without copying or overriding this global routing policy.

Use Python 3.12 or newer. From this checkout, preview the local changes first:

```sh
python3 codex/global_setup.py plan
```

Then install or sync the current canonical sources into the local Codex home:

```sh
python3 codex/global_setup.py sync --apply
python3 codex/global_setup.py verify
```

The setup links `codex/global-instructions.md` on Linux, or its generated `global-instructions.nonlinux.md` edition without learning activation on other platforms, to the native global `AGENTS.md` path and links each skill package separately into `~/.agents/skills/`. It leaves unowned skill names and platform-managed `.system` and plugin skills in place. When it replaces an existing global instruction file or a same-name skill, it moves the original into a dated `~/.codex/backups/cursor-config-migration-*` directory and records file hashes in a backup manifest. Re-running the command is safe; after pulling source updates, run `sync --apply` again.

To check discovery across projects without making a model or provider call, query the installed Codex app-server from two unrelated working directories:

```sh
python3 codex/global_setup.py verify --runtime \
  --cwd /path/to/project-one \
  --cwd /path/to/project-two
```

The runtime check also checks the canonical `codex/` source directory, confirms every managed skill appears once with user scope and its complete description, and reports discovery errors. A global `AGENTS.override.md` must be reviewed before installation because it can override `AGENTS.md`.

Codex Cloud environments can reuse this canonical repository through the same user-level setup. Clone it alongside the application repositories, run plan, sync --apply, and verify in the cloud user profile; preserve each application repository AGENTS.md. Initialize a new private learning store only when absent, using the packaged contextual-learning lesson template and an empty schema-1 index. Existing personal lesson records, credentials, local databases, and recovery artifacts are not part of this repository and must not be copied into public Git. The learning helper honors CODEX_HOME, falling back to the current home .codex directory.

Generated skill HTML companions come from `ui-baseline/visual-reference.html`. Run
`python3 scripts/sync_ui_templates.py` after a baseline release and
`python3 scripts/sync_ui_templates.py --check` to detect stale copies. The
versioned baseline and its source manifest remain authoritative.

The Codex link installer requires the host to permit symbolic-link creation.
Native Windows planning and Linux-only exclusions can be verified without that
privilege; a full link install must be reported as unavailable if the host refuses
it. Do not change security policy or privileges as part of configuration sync.

See [configuration release verification](docs/configuration-release-2026-10-24.md)
for executed checks, backup-source review and platform limitations.

For this workstation, Codex runs in WSL/Linux. Native Windows Codex installation
is outside the required scope. The user has deferred the configuration release's
FedRAMP control/compliance mapping; it is not an outstanding release blocker.
