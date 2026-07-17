# cursor-config

Canonical copy of Cursor **user-level** rules and skills. Edit here, commit, push to GitHub, then install on other machines.

## Layout

- `rules/` — global `.mdc` rule files (`%USERPROFILE%\.cursor\rules\`)
- `skills/` — user skills (`%USERPROFILE%\.cursor\skills\`)
- `skills-cursor/` — Cursor-managed skills (`%USERPROFILE%\.cursor\skills-cursor\`)
- `environment.json` — optional Cursor environment config

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
