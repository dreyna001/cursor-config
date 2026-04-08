# cursor-config

Canonical copy of Cursor **user-level** rules and skills. Edit here, commit, push to GitHub, then install (or sync) into `%USERPROFILE%\.cursor\` on each machine.

## Layout

- `rules/` — `.mdc` rule files (same as `C:\Users\<you>\.cursor\rules\`)
- `skills/` — one folder per skill, each with `SKILL.md`
- `environment.json` — optional; Cursor may read this from the user `.cursor` folder if present

## Install onto this PC (after `git pull`)

From PowerShell, in this repo root:

```powershell
.\install-to-user-cursor.ps1
```

That copies `rules\`, `skills\`, and `environment.json` into `%USERPROFILE%\.cursor\` (creates folders if missing). Existing files with the same name are overwritten.

## New GitHub remote (first time)

1. On GitHub: **New repository** (e.g. `cursor-config`), empty, no README (this repo already has one).
2. In this folder:

```powershell
cd "C:\Users\dreyn\OneDrive\Desktop\Cursor\cursor-config"
git init
git add .
git commit -m "Initial cursor rules and skills"
git branch -M main
git remote add origin https://github.com/<your-user>/cursor-config.git
git push -u origin main
```

Replace `<your-user>` and the repo URL with yours.

## Workflow

1. Change files under `rules/` or `skills/` here.
2. `git commit` and `git push`.
3. On another machine: `git pull`, then run `install-to-user-cursor.ps1`.

Project-specific rules stay in each repo’s `.cursor/`; this repo is for **global** Cursor config you want versioned and portable.
