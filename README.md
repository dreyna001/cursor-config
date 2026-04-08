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

## Push to GitHub (first time)

Git user in this repo is configured as **dreyna001**. The repo is already initialized with branch **main**.

### Option A — GitHub CLI (recommended)

1. Install [GitHub CLI](https://cli.github.com/) if needed (`winget install GitHub.cli`).
2. Log in once (browser or token):

```powershell
gh auth login
```

3. From this folder, create the remote repo and push:

```powershell
cd "C:\Users\dreyn\OneDrive\Desktop\Cursor\cursor-config"
.\publish-to-github.ps1
```

That creates a **private** repo `cursor-config` under your GitHub user, sets `origin`, and pushes `main`.

### Option B — GitHub website

1. Create an empty repository named `cursor-config` under your account (no README).
2. Then:

```powershell
cd "C:\Users\dreyn\OneDrive\Desktop\Cursor\cursor-config"
git remote add origin https://github.com/dreyna001/cursor-config.git
git push -u origin main
```

Adjust the URL if your GitHub username is not `dreyna001`.

## Workflow

1. Change files under `rules/` or `skills/` here.
2. `git commit` and `git push`.
3. On another machine: `git pull`, then run `install-to-user-cursor.ps1`.

Project-specific rules stay in each repo’s `.cursor/`; this repo is for **global** Cursor config you want versioned and portable.
