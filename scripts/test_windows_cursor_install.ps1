#Requires -Version 5.1
param([Parameter(Mandatory=$true)][string]$ScratchRoot, [string]$RepositoryRoot = (Split-Path -Parent $PSScriptRoot))
$ErrorActionPreference = "Stop"
$repoRoot = $RepositoryRoot
$fixture = Join-Path ([System.IO.Path]::GetFullPath($ScratchRoot)) ([guid]::NewGuid().ToString())
$source = Join-Path $fixture "source"
$destination = Join-Path $fixture "destination"
New-Item -ItemType Directory -Force -Path $source | Out-Null
Copy-Item -LiteralPath (Join-Path $repoRoot "install-to-user-cursor.ps1") -Destination (Join-Path $source "install.ps1")
foreach ($relative in @("rules", "skills\regular", "skills\contextual-learning", "skills-cursor\contextual-learning")) {
    New-Item -ItemType Directory -Force -Path (Join-Path $source $relative) | Out-Null
}
$content = "before`n<!-- BEGIN contextual-learning managed section -->`nlearning activation`n<!-- END contextual-learning managed section -->`nafter`n"
[System.IO.File]::WriteAllText((Join-Path $source "rules\global.mdc"), $content)
foreach ($relative in @("skills\regular\SKILL.md", "skills\contextual-learning\SKILL.md", "skills-cursor\contextual-learning\SKILL.md")) {
    [System.IO.File]::WriteAllText((Join-Path $source $relative), "fixture skill")
}
& (Join-Path $source "install.ps1") -DestinationRoot $destination
$installed = [System.IO.File]::ReadAllText((Join-Path $destination "rules\global.mdc"))
if ($installed -match "learning activation|contextual-learning" -or $installed -notmatch "before" -or $installed -notmatch "after") { throw "Windows activation-section filtering failed" }
if (-not (Test-Path -LiteralPath (Join-Path $destination "skills\regular\SKILL.md"))) { throw "Normal skill was excluded" }
foreach ($root in @("skills", "skills-cursor")) {
    if (Test-Path -LiteralPath (Join-Path $destination "$root\contextual-learning")) { throw "Linux-only skill installed on Windows" }
}
$existing = Join-Path $fixture "existing"
New-Item -ItemType Directory -Force -Path (Join-Path $existing "skills\contextual-learning") | Out-Null
[System.IO.File]::WriteAllText((Join-Path $existing "skills\contextual-learning\keep.txt"), "personal work")
$refused = $false
try { & (Join-Path $source "install.ps1") -DestinationRoot $existing } catch { $refused = $_.Exception.Message -like "*Linux-only*" }
if (-not $refused -or (Test-Path -LiteralPath (Join-Path $existing "rules"))) { throw "Existing Windows learning did not block installation before writes" }
if ([System.IO.File]::ReadAllText((Join-Path $existing "skills\contextual-learning\keep.txt")) -ne "personal work") { throw "Existing work was altered" }
[System.IO.File]::WriteAllText((Join-Path $source "rules\global.mdc"), "<!-- BEGIN contextual-learning managed section -->`ninvalid")
$refused = $false
try { & (Join-Path $source "install.ps1") -DestinationRoot (Join-Path $fixture "malformed") } catch { $refused = $_.Exception.Message -like "*Malformed*" }
if (-not $refused) { throw "Malformed activation section was accepted" }
Write-Output "PASS: native Windows installer excludes Linux learning, strips activation, preserves ordinary rules/skills, rejects malformed sections, and preserves conflicting local work."
