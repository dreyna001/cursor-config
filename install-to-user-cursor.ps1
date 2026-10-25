#Requires -Version 5.1
<#
.SYNOPSIS
  Copies this repo's rules, skills, and environment.json into the current user's Cursor home.
#>
param([string]$DestinationRoot = (Join-Path $env:USERPROFILE ".cursor"))

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$destRoot = [System.IO.Path]::GetFullPath($DestinationRoot)
$destRules = Join-Path $destRoot "rules"
$destSkills = Join-Path $destRoot "skills"
$destSkillsCursor = Join-Path $destRoot "skills-cursor"

if ((Test-Path -LiteralPath (Join-Path $destSkills "contextual-learning")) -or (Test-Path -LiteralPath (Join-Path $destSkillsCursor "contextual-learning"))) {
    throw "Contextual learning is Linux-only. Preserve the existing Windows package outside active skill roots before installing."
}
New-Item -ItemType Directory -Force -Path $destRules, $destSkills, $destSkillsCursor | Out-Null

$utf8 = New-Object System.Text.UTF8Encoding($false)
$startMarker = "<!-- BEGIN contextual-learning managed section -->"
$endMarker = "<!-- END contextual-learning managed section -->"
Get-ChildItem -Path (Join-Path $repoRoot "rules\*.mdc") -File | ForEach-Object {
    $content = [System.IO.File]::ReadAllText($_.FullName)
    if ($content.Contains($startMarker) -or $content.Contains($endMarker)) {
        if ([regex]::Matches($content, [regex]::Escape($startMarker)).Count -ne 1 -or
            [regex]::Matches($content, [regex]::Escape($endMarker)).Count -ne 1 -or
            $content.IndexOf($endMarker) -lt $content.IndexOf($startMarker)) {
            throw "Malformed contextual-learning section in $($_.Name)"
        }
        $content = $content.Substring(0, $content.IndexOf($startMarker)).TrimEnd() + "`n`n" +
            $content.Substring($content.IndexOf($endMarker) + $endMarker.Length).TrimStart()
    }
    [System.IO.File]::WriteAllText((Join-Path $destRules $_.Name), $content, $utf8)
}

Get-ChildItem -Path (Join-Path $repoRoot "skills") -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    if ($_.Name -eq "contextual-learning") { return }
    $targetDir = Join-Path $destSkills $_.Name
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
    Copy-Item -Path (Join-Path $_.FullName "*") -Destination $targetDir -Recurse -Force
}

Get-ChildItem -Path (Join-Path $repoRoot "skills-cursor") -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    if ($_.Name -eq "contextual-learning") { return }
    $targetDir = Join-Path $destSkillsCursor $_.Name
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
    Copy-Item -Path (Join-Path $_.FullName "*") -Destination $targetDir -Recurse -Force
}

$envFile = Join-Path $repoRoot "environment.json"
if (Test-Path $envFile) {
    Copy-Item -Path $envFile -Destination (Join-Path $destRoot "environment.json") -Force
}

Write-Host "Installed to $destRoot"
