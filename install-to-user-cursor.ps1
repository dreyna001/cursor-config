#Requires -Version 5.1
<#
.SYNOPSIS
  Copies this repo's rules, skills, and environment.json into the current user's Cursor home.
#>
$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$destRoot = Join-Path $env:USERPROFILE ".cursor"
$destRules = Join-Path $destRoot "rules"
$destSkills = Join-Path $destRoot "skills"

New-Item -ItemType Directory -Force -Path $destRules, $destSkills | Out-Null

Copy-Item -Path (Join-Path $repoRoot "rules\*.mdc") -Destination $destRules -Force

Get-ChildItem -Path (Join-Path $repoRoot "skills") -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    $targetDir = Join-Path $destSkills $_.Name
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
    Copy-Item -Path (Join-Path $_.FullName "*") -Destination $targetDir -Force
}

$envFile = Join-Path $repoRoot "environment.json"
if (Test-Path $envFile) {
    Copy-Item -Path $envFile -Destination (Join-Path $destRoot "environment.json") -Force
}

Write-Host "Installed to $destRoot"
