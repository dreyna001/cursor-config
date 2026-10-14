---
name: cursor-cloud-config
description: >-
  Manage personal Cursor skills and rules stored in this repository. Use when
  the user mentions cloud agents, installing personal rules, syncing local
  Cursor config, or cursor-cloud-config.
disable-model-invocation: true
---
# Cursor Cloud Config

Personal skills and rules live locally at `~/.cursor/skills/` and `~/.cursor/rules/`. Cloud agents cannot read those paths.

## Source of truth

Canonical repo: `/home/dreyna/cursor-config` (clone URL: `https://github.com/dreyna001/cursor-config.git`)

- `skills/` — personal Agent Skills
- `rules/` — personal `.mdc` rules
- `sync-from-local.ps1` — copy the current user's Cursor home into this repo
- `install-to-user-cursor.ps1` — copy this repo into the current user's Cursor home

## Workflows

### After editing local skills or rules

```powershell
cd /home/dreyna/cursor-config
./sync-from-local.ps1
```

Review the diff, then commit and push only if the user asked for a commit.

### Install this repo into the local Cursor profile

```powershell
cd /home/dreyna/cursor-config
./install-to-user-cursor.ps1
```

On this WSL machine, copy `rules/` into `~/.cursor/rules` and `skills/` into `~/.cursor/skills` after source edits when the PowerShell installer is not used. Also copy `rules/*.mdc` into `/mnt/c/Users/Daniel.Reyna/.cursor/rules` so Windows Cursor sees the same standing rules. Codex does not read those `.mdc` files; update `codex/global-instructions.md` and run `python3 codex/global_setup.py sync --apply` for Codex.

### Cloud mode

Cloud agents see only files in the project checkout. To make these global rules or skills available there, copy the needed files into that project's `.cursor/` tree and commit them in the project repository. This repo does not provide `install-to-project.ps1`.

## What cloud gets without a project copy

- Built-in Cursor skills (`/review`, `/automate`, etc.)
- User Rules from Cursor Settings → Customize
- Team rules and plugins (if configured)

## What cloud does NOT get

- `~/.cursor/skills/` on disk
- `~/.cursor/rules/` on disk
- `~/.cursor/hooks.json`
- Global `~/.cursor/mcp.json` (configure MCP at cursor.com/agents instead)
