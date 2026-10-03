# cursor-config

Canonical versioned source for the user's global Cursor configuration and Codex instructions and skills. Cursor assets keep their existing layout; Codex assets live under `codex/` and install through native user-level entry points.

## Layout

- `rules/` — global `.mdc` rule files (`%USERPROFILE%\.cursor\rules\`)
- `skills/` — user skills (`%USERPROFILE%\.cursor\skills\`)
- `skills-cursor/` — Cursor-managed skills (`%USERPROFILE%\.cursor\skills-cursor\`)
- `environment.json` — optional Cursor environment config
- `codex/global-instructions.md` — global Codex instructions, linked to `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`)
- `codex/skills/` — portable Codex user skills, linked individually under `~/.agents/skills/`
- `codex/install-manifest.json` — the expected global Codex skill inventory
- `codex/global_setup.py` — read-only planning, local installation/sync, and app-server verification

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

That copies `rules/`, `skills/`, `skills-cursor/`, and `environment.json` into `%USERPROFILE%\.cursor\`. Existing files with the same name are overwritten.

## Clone elsewhere

```powershell
git clone https://github.com/dreyna001/cursor-config.git
cd cursor-config
.\install-to-user-cursor.ps1
```

Project-specific rules stay in each repo's `.cursor/` folder. This repo is for global Cursor config you want versioned and portable.

## Install global Codex configuration

The Codex collection contains 52 custom skills. Overlapping planning, debugging, cybersecurity, and review workflows share retained entry points; tool-specific production guidance lives in ten conditional references, with official vendor sources, rather than additional skills. The engineering router links directly to those references for existing integrations; stack-selection defaults are not prerequisites for routine implementation.

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

The setup links `codex/global-instructions.md` to the native global `AGENTS.md` path and links each skill package separately into `~/.agents/skills/`. It leaves unowned skill names and platform-managed `.system` and plugin skills in place. When it replaces an existing global instruction file or a same-name skill, it moves the original into a dated `~/.codex/backups/cursor-config-migration-*` directory and records file hashes in a backup manifest. Re-running the command is safe; after pulling source updates, run `sync --apply` again.

To check discovery across projects without making a model or provider call, query the installed Codex app-server from two unrelated working directories:

```sh
python3 codex/global_setup.py verify --runtime \
  --cwd /path/to/project-one \
  --cwd /path/to/project-two
```

The runtime check also checks the canonical `codex/` source directory, confirms every managed skill appears once with user scope and its complete description, and reports discovery errors. A global `AGENTS.override.md` must be reviewed before installation because it can override `AGENTS.md`.

This local setup does not configure Codex Cloud environments. Cloud setup can be handled separately if needed.
