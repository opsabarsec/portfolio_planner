#!/usr/bin/env bash

# Test script for verifying portfolio-planner skill installation
# Usage: ./test-skill-install.sh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Helper functions
assert_file_exists() {
  local path="$1"
  local description="$2"
  if [[ ! -f "$path" ]]; then
    echo "❌ FAILED: $description - File not found: $path" >&2
    exit 1
  fi
  echo "✓ $description"
}

assert_dir_exists() {
  local path="$1"
  local description="$2"
  if [[ ! -d "$path" ]]; then
    echo "❌ FAILED: $description - Directory not found: $path" >&2
    exit 1
  fi
  echo "✓ $description"
}

assert_contains() {
  local path="$1"
  local expected="$2"
  local description="$3"
  if ! grep -q "$expected" "$path" 2>/dev/null; then
    echo "❌ FAILED: $description - Expected content not found: $expected" >&2
    exit 1
  fi
  echo "✓ $description"
}

echo ""
echo "🧪 Portfolio Planner Skill Installation Test"
echo ""

# Create temporary home directory for testing
TMP_HOME="$(mktemp -d)"
trap 'rm -rf "$TMP_HOME"' EXIT

# Create .env for test
ENV_FILE="$ROOT_DIR/.env"
echo "USERPROFILE=\"$TMP_HOME\"" > "$ENV_FILE"

echo "📁 Using temporary directory: $TMP_HOME"
echo ""

# Define paths
SKILLS_DIR="$TMP_HOME/.claude/skills"
AGENTS_DIR="$TMP_HOME/.claude/agents"

# Run the install script using PowerShell if available (Windows Git Bash)
# Or use bash for pure Unix systems
if command -v pwsh &> /dev/null; then
  echo "📦 Running install-skill.ps1..."
  pwsh "$ROOT_DIR/install-skill.ps1" > /dev/null
elif command -v powershell &> /dev/null; then
  echo "📦 Running install-skill.ps1..."
  powershell "$ROOT_DIR/install-skill.ps1" > /dev/null
else
  echo "❌ FAILED: PowerShell not found. This test requires PowerShell to run install-skill.ps1" >&2
  exit 1
fi

echo ""
echo "🔍 Verifying installation..."
echo ""

# Verify installations
assert_dir_exists "$SKILLS_DIR" "Skills directory created"
assert_dir_exists "$SKILLS_DIR/portfolio-planner" "portfolio-planner skill installed"

# Check skill contains expected files
if [[ ! -f "$SKILLS_DIR/portfolio-planner"/*.md ]]; then
  echo "❌ FAILED: No markdown files found in portfolio-planner skill directory" >&2
  exit 1
fi
echo "✓ Skill contains markdown documentation"

# Check agent directory
assert_dir_exists "$AGENTS_DIR" "Agents directory created"
assert_file_exists "$AGENTS_DIR/web-search-agent.md" "web-search-agent.md installed"

# Check agent content
assert_contains "$AGENTS_DIR/web-search-agent.md" "web-search" "web-search-agent has expected content"

# Check modules directory
assert_dir_exists "$AGENTS_DIR/web-search-modules" "web-search-modules directory installed"

# Check for module files
MODULE_FILE_COUNT=$(find "$AGENTS_DIR/web-search-modules" -name "*.md" | wc -l)
if [[ $MODULE_FILE_COUNT -eq 0 ]]; then
  echo "❌ FAILED: No markdown files found in web-search-modules directory" >&2
  exit 1
fi
echo "✓ web-search-modules contains configuration files"

# Test idempotency - run install again
echo ""
echo "🔄 Testing idempotency (running install again)..."
if command -v pwsh &> /dev/null; then
  pwsh "$ROOT_DIR/install-skill.ps1" > /dev/null 2>&1 || true
elif command -v powershell &> /dev/null; then
  powershell "$ROOT_DIR/install-skill.ps1" > /dev/null 2>&1 || true
fi

# Re-verify after second run
assert_dir_exists "$SKILLS_DIR/portfolio-planner" "portfolio-planner skill still present"
assert_file_exists "$AGENTS_DIR/web-search-agent.md" "web-search-agent.md still present"
assert_dir_exists "$AGENTS_DIR/web-search-modules" "web-search-modules still present"

echo ""
echo "✓ All installation tests passed!"
echo ""

# Cleanup .env
rm -f "$ENV_FILE"
