#Requires -Version 5.1
<#
.SYNOPSIS
  One-time: log into GitHub CLI, then create github.com/<you>/cursor-config and push main.

PREREQ: Run `gh auth login` once in this terminal (browser or token), then run this script.
#>
$ErrorActionPreference = "Stop"
$env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

gh auth status 2>&1 | Out-Host
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Not logged in. Run:  gh auth login" -ForegroundColor Yellow
    Write-Host "Then run this script again." -ForegroundColor Yellow
    exit 1
}

# Creates private repo named cursor-config under your GitHub user, adds origin, pushes main.
gh repo create cursor-config --private --source=. --remote=origin --push

Write-Host "Done. Remote:" -ForegroundColor Green
git remote -v
