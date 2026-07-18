#!/usr/bin/env python3
"""
Test suite for portfolio-planner skill installation using pytest
Run with: pytest tests/test_skill_install.py -v
"""

import os
import sys
import shutil
import tempfile
import subprocess
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir():
    """Create and cleanup a temporary directory for testing."""
    temp_path = tempfile.mkdtemp(prefix="portfolio_planner_test_")
    print(f"\nUsing temporary directory: {temp_path}")
    yield temp_path
    # Cleanup
    if Path(temp_path).exists():
        shutil.rmtree(temp_path)
        print("Cleaned up temporary files")


@pytest.fixture
def env_file(temp_dir):
    """Create .env file with temporary directory."""
    env_path = ".env"
    with open(env_path, 'w') as f:
        f.write(f'USERPROFILE = "{temp_dir}"\n')
    yield env_path
    # Cleanup
    if Path(env_path).exists():
        os.remove(env_path)


@pytest.fixture
def run_install(env_file, temp_dir):
    """Run the install script."""
    print("Running install_skill.py...")
    result = subprocess.run(
        [sys.executable, "install_skill.py"],
        capture_output=True,
        text=True,
        check=False
    )

    # Print output for debugging
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    assert result.returncode == 0, f"Install script failed with code {result.returncode}"
    yield result


class TestSkillInstallation:
    """Tests for skill installation."""

    def test_directories_created(self, run_install, temp_dir):
        """Test that required directories are created."""
        skills_dir = Path(temp_dir) / ".claude" / "skills"
        agents_dir = Path(temp_dir) / ".claude" / "agents"

        assert skills_dir.exists(), f"Skills directory not created: {skills_dir}"
        assert agents_dir.exists(), f"Agents directory not created: {agents_dir}"

    def test_skill_installed(self, run_install, temp_dir):
        """Test that portfolio-planner skill is installed."""
        skill_dir = Path(temp_dir) / ".claude" / "skills" / "portfolio-planner"
        assert skill_dir.exists(), f"Skill directory not found: {skill_dir}"

    def test_skill_contains_markdown(self, run_install, temp_dir):
        """Test that skill contains markdown documentation."""
        skill_dir = Path(temp_dir) / ".claude" / "skills" / "portfolio-planner"
        skill_files = list(skill_dir.glob("*.md"))
        assert len(skill_files) > 0, f"No markdown files found in {skill_dir}"

    def test_agent_installed(self, run_install, temp_dir):
        """Test that web-search-agent is installed."""
        agent_file = Path(temp_dir) / ".claude" / "agents" / "web-search-agent.md"
        assert agent_file.exists(), f"Agent file not found: {agent_file}"

    def test_agent_has_content(self, run_install, temp_dir):
        """Test that agent file contains expected content."""
        agent_file = Path(temp_dir) / ".claude" / "agents" / "web-search-agent.md"
        content = agent_file.read_text(encoding='utf-8')
        assert "web-search" in content, "Agent file missing 'web-search' content"

    def test_modules_installed(self, run_install, temp_dir):
        """Test that web-search-modules are installed."""
        modules_dir = Path(temp_dir) / ".claude" / "agents" / "web-search-modules"
        assert modules_dir.exists(), f"Modules directory not found: {modules_dir}"

    def test_modules_contain_markdown(self, run_install, temp_dir):
        """Test that modules directory contains markdown files."""
        modules_dir = Path(temp_dir) / ".claude" / "agents" / "web-search-modules"
        module_files = list(modules_dir.glob("*.md"))
        assert len(module_files) > 0, f"No markdown files found in {modules_dir}"


class TestIdempotency:
    """Tests for idempotent installation."""

    def test_install_twice_is_safe(self, run_install, temp_dir, env_file):
        """Test that running install twice doesn't fail."""
        print("\nTesting idempotency (running install again)...")
        result = subprocess.run(
            [sys.executable, "install_skill.py"],
            capture_output=True,
            text=True,
            check=False
        )

        # Print output for debugging
        if result.stdout:
            print(result.stdout)

        assert result.returncode == 0, f"Second install failed with code {result.returncode}"

    def test_files_still_present_after_reinstall(self, run_install, temp_dir, env_file):
        """Test that files are still present after running install twice."""
        # Run install again
        subprocess.run(
            [sys.executable, "install_skill.py"],
            capture_output=True,
            text=True,
            check=True
        )

        # Verify files still exist
        skill_dir = Path(temp_dir) / ".claude" / "skills" / "portfolio-planner"
        agent_file = Path(temp_dir) / ".claude" / "agents" / "web-search-agent.md"
        modules_dir = Path(temp_dir) / ".claude" / "agents" / "web-search-modules"

        assert skill_dir.exists(), "Skill missing after second install"
        assert agent_file.exists(), "Agent missing after second install"
        assert modules_dir.exists(), "Modules missing after second install"


class TestForceFlag:
    """Tests for the --force flag."""

    def test_force_flag_exists(self):
        """Test that --force flag is available."""
        result = subprocess.run(
            [sys.executable, "install_skill.py", "--help"],
            capture_output=True,
            text=True,
            check=True
        )

        assert "--force" in result.stdout, "--force flag not found in help"

    def test_force_flag_overwrites(self, temp_dir, env_file):
        """Test that --force flag overwrites existing installation."""
        # First install
        subprocess.run(
            [sys.executable, "install_skill.py"],
            capture_output=True,
            text=True,
            check=True
        )

        skill_dir = Path(temp_dir) / ".claude" / "skills" / "portfolio-planner"
        assert skill_dir.exists(), "First install failed"

        # Install with --force should succeed
        result = subprocess.run(
            [sys.executable, "install_skill.py", "--force"],
            capture_output=True,
            text=True,
            check=False
        )

        assert result.returncode == 0, f"Force install failed with code {result.returncode}"
        assert skill_dir.exists(), "Skill missing after force install"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
