---
name: cursor-cloud-config
description: >-
  Manage personal Cursor skills and rules for Cloud mode. Use when the user
  mentions cloud agents, syncing skills to cloud, installing personal rules
  into a project, or cursor-cloud-config.
disable-model-invocation: true
---
# Cursor Cloud Config

Personal skills and rules live locally at `~/.cursor/skills/` and `~/.cursor/rules/`. Cloud agents cannot read those paths.

## Source of truth

Git repo: `C:\Users\dreyn\Projects\cursor-cloud-config`

- `skills/` — personal Agent Skills
- `rules/` — personal `.mdc` rules
- `scripts/` — sync and install helpers

## Workflows

### After editing local skills or rules

```powershell
cd C:\Users\dreyn\Projects\cursor-cloud-config
.\scripts\sync-from-local.ps1
git add -A && git commit -m "Sync skills and rules from local" && git push
```

### Before using Cloud mode on a project

```powershell
cd C:\Users\dreyn\Projects\cursor-cloud-config
.\scripts\install-to-project.ps1 -ProjectPath C:\path\to\project
```

Then commit and push the **project** repo so the cloud VM clones the updated `.cursor/` tree.

### First-time setup

1. Push `cursor-cloud-config` to a private GitHub repo
2. Run `install-to-project.ps1` on each project used in cloud
3. Copy the `AGENTS.md` cloud section template into each project if missing

## What cloud gets without this repo

- Built-in Cursor skills (`/review`, `/automate`, etc.)
- User Rules from Cursor Settings → Customize
- Team rules and plugins (if configured)

## What cloud does NOT get

- `~/.cursor/skills/` on disk
- `~/.cursor/rules/` on disk
- `~/.cursor/hooks.json`
- Global `~/.cursor/mcp.json` (configure MCP at cursor.com/agents instead)
