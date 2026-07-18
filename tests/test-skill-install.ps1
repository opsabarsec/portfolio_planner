param(
    [switch]$Verbose
)

$ErrorActionPreference = "Stop"

function Assert-FileExists {
    param([string]$Path, [string]$Description)
    if (-not (Test-Path $Path)) {
        Write-Error "FAILED: $Description - File not found: $Path"
        exit 1
    }
    Write-Host "PASS: $Description"
}

function Assert-DirectoryExists {
    param([string]$Path, [string]$Description)
    if (-not (Test-Path $Path -PathType Container)) {
        Write-Error "FAILED: $Description - Directory not found: $Path"
        exit 1
    }
    Write-Host "PASS: $Description"
}

function Assert-ContentContains {
    param([string]$Path, [string]$ExpectedContent, [string]$Description)
    if (-not (Test-Path $Path)) {
        Write-Error "FAILED: $Description - File not found: $Path"
        exit 1
    }
    $content = Get-Content $Path -Raw
    if ($content -notmatch [regex]::Escape($ExpectedContent)) {
        Write-Error "FAILED: $Description - Expected content not found: $ExpectedContent"
        exit 1
    }
    Write-Host "PASS: $Description"
}

Write-Host "`nPortfolio Planner Skill Installation Test`n" -ForegroundColor Cyan

$tempDir = New-TemporaryFile | ForEach-Object { Remove-Item $_; New-Item -ItemType Directory -Path $_.FullName }
$claudeDir = Join-Path $tempDir ".claude"
$skillsDir = Join-Path $claudeDir "skills"
$agentsDir = Join-Path $claudeDir "agents"

$envFile = ".env"
$envContent = "USERPROFILE = `"$tempDir`""
Set-Content -Path $envFile -Value $envContent

Write-Host "Using temporary directory: $tempDir`n"

try {
    Write-Host "Running install-skill.ps1..."
    & ".\install-skill.ps1"
    Write-Host ""

    Write-Host "Verifying installation...`n"

    Assert-DirectoryExists "$skillsDir" "Skills directory created"
    Assert-DirectoryExists "$skillsDir\portfolio-planner" "portfolio-planner skill installed"

    $skillPath = "$skillsDir\portfolio-planner"
    $skillFiles = @(Get-ChildItem -Path $skillPath -Filter "*.md" -ErrorAction SilentlyContinue)
    if ($skillFiles.Count -eq 0) {
        Write-Error "FAILED: No markdown files found in portfolio-planner skill directory"
        exit 1
    }
    Write-Host "PASS: Skill contains markdown documentation"

    Assert-DirectoryExists "$agentsDir" "Agents directory created"
    Assert-FileExists "$agentsDir\web-search-agent.md" "web-search-agent.md installed"

    Assert-ContentContains "$agentsDir\web-search-agent.md" "web-search" "web-search-agent has expected content"

    Assert-DirectoryExists "$agentsDir\web-search-modules" "web-search-modules directory installed"

    $moduleFiles = @(Get-ChildItem -Path "$agentsDir\web-search-modules" -Filter "*.md" -ErrorAction SilentlyContinue)
    if ($moduleFiles.Count -eq 0) {
        Write-Error "FAILED: No markdown files found in web-search-modules directory"
        exit 1
    }
    Write-Host "PASS: web-search-modules contains configuration files"

    Write-Host "`nTesting idempotency (running install again)..."
    & ".\install-skill.ps1" 2>&1 | Out-Null

    Assert-DirectoryExists "$skillsDir\portfolio-planner" "portfolio-planner skill still present"
    Assert-FileExists "$agentsDir\web-search-agent.md" "web-search-agent.md still present"
    Assert-DirectoryExists "$agentsDir\web-search-modules" "web-search-modules still present"

    Write-Host "`nAll installation tests passed!`n" -ForegroundColor Green

} finally {
    Remove-Item -Path $envFile -Force -ErrorAction SilentlyContinue
    Remove-Item -Path $tempDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "Cleaned up temporary files`n"
}

exit 0
