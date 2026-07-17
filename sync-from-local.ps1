#Requires -Version 5.1
<#
.SYNOPSIS
  Pulls the current user's Cursor rules and skills into this repo without duplicates.
#>
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$cursorHome = Join-Path $env:USERPROFILE ".cursor"
$codexSkills = Join-Path $env:USERPROFILE ".codex\skills"

$destRules = Join-Path $repoRoot "rules"
$destSkills = Join-Path $repoRoot "skills"
$destSkillsCursor = Join-Path $repoRoot "skills-cursor"

function Reset-Dir([string]$Path) {
    if (Test-Path $Path) {
        Remove-Item -Path $Path -Recurse -Force
    }
    New-Item -ItemType Directory -Force -Path $Path | Out-Null
}

function Copy-SkillTree([string]$SourceDir, [string]$DestDir) {
    if (-not (Test-Path $SourceDir)) {
        return
    }

    Get-ChildItem -Path $SourceDir -Directory | ForEach-Object {
        $target = Join-Path $DestDir $_.Name
        New-Item -ItemType Directory -Force -Path $target | Out-Null
        Copy-Item -Path (Join-Path $_.FullName "*") -Destination $target -Recurse -Force
    }
}

Write-Host "Syncing rules..."
Reset-Dir $destRules
Get-ChildItem -Path (Join-Path $cursorHome "rules") -Filter "*.mdc" -File |
    Copy-Item -Destination $destRules -Force

Write-Host "Syncing user skills..."
Reset-Dir $destSkills
Copy-SkillTree (Join-Path $cursorHome "skills") $destSkills

Write-Host "Syncing Cursor-managed skills..."
Reset-Dir $destSkillsCursor
Get-ChildItem -Path (Join-Path $cursorHome "skills-cursor") -Directory |
    Where-Object { -not $_.Name.StartsWith(".") } |
    ForEach-Object {
        $target = Join-Path $destSkillsCursor $_.Name
        New-Item -ItemType Directory -Force -Path $target | Out-Null
        Copy-Item -Path (Join-Path $_.FullName "*") -Destination $target -Recurse -Force
    }

Write-Host "Adding Codex-only skills..."
$present = @{}
Get-ChildItem -Path $destSkills, $destSkillsCursor -Directory -ErrorAction SilentlyContinue |
    ForEach-Object { $present[$_.Name] = $true }

Get-ChildItem -Path $codexSkills -Directory |
    Where-Object {
        $_.Name -ne ".system" -and
        -not $_.Name.StartsWith(".") -and
        -not $present.ContainsKey($_.Name)
    } |
    ForEach-Object {
        $unprefixed = $_.Name -replace "^cursor-", ""
        if ($present.ContainsKey($unprefixed)) {
            return
        }

        $target = Join-Path $destSkills $_.Name
        New-Item -ItemType Directory -Force -Path $target | Out-Null
        Copy-Item -Path (Join-Path $_.FullName "*") -Destination $target -Recurse -Force
        $present[$_.Name] = $true
        Write-Host "  + $($_.Name)"
    }

$envSource = Join-Path $cursorHome "environment.json"
$envDest = Join-Path $repoRoot "environment.json"
if (Test-Path $envSource) {
    Copy-Item -Path $envSource -Destination $envDest -Force
}

$ruleCount = (Get-ChildItem $destRules -Filter "*.mdc").Count
$skillCount = (Get-ChildItem $destSkills -Directory).Count
$managedCount = (Get-ChildItem $destSkillsCursor -Directory).Count

Write-Host ""
Write-Host "Done: $ruleCount rules, $skillCount user skills, $managedCount Cursor-managed skills."
