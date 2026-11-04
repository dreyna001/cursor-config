---
name: windows-agent-shell-fallback
description: Run Cursor Agent shell commands on Windows when integrated terminal fails by using powershell.exe, cmd /c, or wsl.exe bash -lc explicitly. Use on managed Windows/VDI hosts, Constrained Language Mode errors, WSL workspaces, or when Shell output is garbled or unreliable.
---

# Windows Agent Shell Fallback

## Purpose

Cursor Agent on Windows can invoke commands even when the integrated Shell tool misbehaves. On managed VMs, the wrapper often runs PowerShell in **Constrained Language Mode**, which breaks Cursor's bootstrap script but still allows explicit calls to `powershell.exe`, `cmd.exe`, and `wsl.exe`.

Use this skill whenever shell output is untrustworthy or commands fail without a clear application error.

## Detect the problem

Treat shell integration as degraded if you see any of:

- `MethodInvocationNotSupportedInConstrainedLanguage`
- Repeated `Cannot invoke method` errors from `ps-script-*.ps1`
- Real command output buried in hundreds of wrapper errors
- `Failed to attach disk ... ext4.vhdx ... Access is denied` from WSL (separate issue; may be transient)
- Workspace on `\\wsl.localhost\Ubuntu\...` but agent CWD is `C:\Users\...`

Exit code `0` with noisy output still counts as a successful fallback path.

## Command runners (in order of preference)

### 1. PowerShell for Windows-native work

```powershell
powershell.exe -NoProfile -Command "Set-Content -Path $env:TEMP\probe.txt -Value 'ok'; Get-Content $env:TEMP\probe.txt"
```

Use for:

- Windows paths (`C:\...`)
- .NET / PowerShell tooling
- `wsl.exe` orchestration itself

### 2. WSL for Linux workspace work

```powershell
wsl.exe bash -lc "uname -a; pwd; whoami"
```

Use for:

- Repos under `/home/dreyna/...`
- Linux packages, bash scripts, make, docker inside WSL
- Git operations when the canonical repo lives in WSL

Quote carefully:

- Wrap the Linux script in double quotes for PowerShell
- Use single quotes inside bash when possible

Examples:

```powershell
wsl.exe bash -lc "cd ~/my-repo && git status --short"
wsl.exe bash -lc "python3 --version"
wsl.exe bash -lc "echo 'wsl-ok' > ~/probe.txt && cat ~/probe.txt"
```

### 3. cmd.exe for minimal probes

```powershell
cmd /c "echo SHELL=cmd && cd && where powershell && where wsl"
```

Use when PowerShell wrapper noise makes output hard to parse and you only need simple stdout.

## Decision table

| Task | Runner |
|------|--------|
| Read/write Windows files | `powershell.exe -NoProfile -Command` |
| Read/write WSL files | `wsl.exe bash -lc` or editor tools on `\\wsl.localhost\...` |
| Install/run Linux CLI tools | `wsl.exe bash -lc` |
| Diagnose shell environment | `cmd /c` first, then explicit `powershell.exe` / `wsl.exe` |
| Integrated Shell tool noisy but exit 0 | Continue with explicit runners; report wrapper issue briefly |

## What not to do

- Do not conclude terminal access is missing after one failed integrated Shell call
- Do not ask the user to run probes the agent can run
- Do not assume `terminal.integrated.defaultProfile.windows` fixes agent execution on constrained hosts
- Avoid deeply nested `powershell -Command "cmd /c \"wsl ...\""` unless necessary

## Cursor settings (supporting, not sufficient)

User settings file: `%APPDATA%\Cursor\User\settings.json`

```json
{
  "terminal.integrated.useWslProfiles": false,
  "terminal.integrated.defaultProfile.windows": "PowerShell"
}
```

Also consider **Legacy Terminal Tool** in Cursor Settings → Agent → Terminal if shell detection remains broken.

These help interactive terminals; they may not fix constrained-language agent wrappers. Still use explicit `powershell.exe` / `wsl.exe` when needed.

## Verified on Daniel's Windows/WSL setup

These commands succeeded from Cursor Agent even with wrapper noise:

```powershell
powershell.exe -NoProfile -Command "Set-Content -Path $env:TEMP\cursor-agent-ps-test.txt -Value 'powershell-ok'; Get-Content $env:TEMP\cursor-agent-ps-test.txt"

wsl.exe bash -lc "echo 'wsl-ok' > ~/cursor-agent-wsl-test.txt && cat ~/cursor-agent-wsl-test.txt && pwd"
```

Observed WSL identity: user `dreyna`, distro Ubuntu on WSL2.

## Reporting

When this skill was needed, tell the user briefly:

1. Integrated Shell wrapper was degraded (likely Constrained Language Mode)
2. Which explicit runner worked (`powershell.exe`, `wsl.exe`, or `cmd /c`)
3. Any remaining blocker (e.g. WSL disk mount errors) separate from shell fallback
