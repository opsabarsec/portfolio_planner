param(
    [switch]$Force
)

$envFile = ".env"
$userProfile = $null

if (Test-Path $envFile) {
    $envLines = @(Get-Content $envFile)
    foreach ($line in $envLines) {
        if ($line -like "*USERRPROFILE*") {
            $userProfile = ($line -split "=")[1].Trim().Trim([char]34)
            Write-Host "Found USERRPROFILE in .env: $userProfile"
            break
        } elseif ($line -like "*USERPROFILE*" -and $line -notlike "*USERRPROFILE*") {
            $userProfile = ($line -split "=")[1].Trim().Trim([char]34)
            Write-Host "Found USERPROFILE in .env: $userProfile"
            break
        }
    }
}

if (-not $userProfile) {
    $userProfile = $env:USERPROFILE
    Write-Host "Using system USERPROFILE: $userProfile"
}

$claudeSkillsDir = "$userProfile\.claude\skills"
$claudeAgentsDir = "$userProfile\.claude\agents"

$skillSource = ".\skills\research-en\portfolio-planner"
$agentSource = ".\agents\web-search-agent.md"
$modulesSource = ".\agents\web-search-modules"

$missingFiles = @()
if (-not (Test-Path $skillSource)) {
    $missingFiles += "Skill: $skillSource"
}
if (-not (Test-Path $agentSource)) {
    $missingFiles += "Agent: $agentSource"
}
if (-not (Test-Path $modulesSource)) {
    $missingFiles += "Modules: $modulesSource"
}

if ($missingFiles.Count -gt 0) {
    Write-Host "Error: Missing source files:" -ForegroundColor Red
    $missingFiles | ForEach-Object { Write-Host "  - $_" }
    exit 1
}

Write-Host "`nCreating directories..."
if (-not (Test-Path $claudeSkillsDir)) {
    New-Item -ItemType Directory -Path $claudeSkillsDir -Force | Out-Null
    Write-Host "  Created: $claudeSkillsDir"
}
if (-not (Test-Path $claudeAgentsDir)) {
    New-Item -ItemType Directory -Path $claudeAgentsDir -Force | Out-Null
    Write-Host "  Created: $claudeAgentsDir"
}

Write-Host "`nInstalling portfolio-planner skill..."
$skillDest = "$claudeSkillsDir\portfolio-planner"
if ((Test-Path $skillDest) -and -not $Force) {
    Write-Host "  Skill already exists at $skillDest" -ForegroundColor Yellow
    Write-Host "  Use -Force flag to overwrite"
} else {
    Copy-Item -Path $skillSource -Destination $skillDest -Recurse -Force
    Write-Host "  Installed to: $skillDest"
}

Write-Host "`nInstalling web search agent..."
Copy-Item -Path $agentSource -Destination $claudeAgentsDir -Force
Write-Host "  Installed to: $claudeAgentsDir\web-search-agent.md"

Write-Host "`nInstalling web search modules..."
$modulesDest = "$claudeAgentsDir\web-search-modules"
if ((Test-Path $modulesDest) -and -not $Force) {
    Write-Host "  Modules already exist at $modulesDest" -ForegroundColor Yellow
    Write-Host "  Use -Force flag to overwrite"
} else {
    Copy-Item -Path $modulesSource -Destination $modulesDest -Recurse -Force
    Write-Host "  Installed to: $modulesDest"
}

Write-Host "`nInstallation complete!" -ForegroundColor Green
Write-Host "`nYou can now run: /portfolio-planner" -ForegroundColor Green
