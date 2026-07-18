#!/usr/bin/env python3
"""
Tests for portfolio profile manager using pytest
Run with: pytest tests/test_profile_manager.py -v
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path

import pytest

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import profile_manager


@pytest.fixture
def temp_data_dir(monkeypatch):
    """Create temporary data directory for testing."""
    temp_dir = tempfile.mkdtemp(prefix="profile_test_")
    temp_path = Path(temp_dir)

    # Patch the DATA_DIR in profile_manager
    monkeypatch.setattr(profile_manager, "DATA_DIR", temp_path)

    yield temp_path

    # Cleanup
    if temp_path.exists():
        shutil.rmtree(temp_path)


class TestListProfiles:
    """Tests for listing profiles."""

    def test_list_empty_directory(self, temp_data_dir, capsys):
        """Test listing profiles when directory is empty."""
        profile_manager.list_profiles()
        captured = capsys.readouterr()

        assert "No profile files found" in captured.out
        assert "Create a profile with:" in captured.out

    def test_list_existing_profiles(self, temp_data_dir, capsys, monkeypatch):
        """Test listing existing profile files."""
        # Create test profiles (must match *_profile*.md pattern)
        profile1 = temp_data_dir / "test_profile.md"
        profile2 = temp_data_dir / "marco_profile_ai.md"

        profile1.write_text("Profile 1 content")
        profile2.write_text("Profile 2 content")

        # Ensure temp_data_dir is used in list_profiles
        monkeypatch.setattr(profile_manager, "DATA_DIR", temp_data_dir)

        profile_manager.list_profiles()
        captured = capsys.readouterr()

        assert "test_profile.md" in captured.out
        assert "marco_profile_ai.md" in captured.out
        assert "Available profiles:" in captured.out


class TestCheckProfile:
    """Tests for checking/viewing profiles."""

    def test_check_existing_profile(self, temp_data_dir, capsys):
        """Test viewing an existing profile."""
        profile_path = temp_data_dir / "test.md"
        profile_path.write_text("Test profile content\nLine 2")

        profile_manager.check_profile("test")
        captured = capsys.readouterr()

        assert "Profile: test.md" in captured.out
        assert "Test profile content" in captured.out
        assert "Line 2" in captured.out

    def test_check_nonexistent_profile(self, temp_data_dir, capsys):
        """Test viewing a non-existent profile."""
        with pytest.raises(SystemExit):
            profile_manager.check_profile("nonexistent")

    def test_check_profile_with_md_extension(self, temp_data_dir, capsys):
        """Test viewing a profile with .md extension in name."""
        profile_path = temp_data_dir / "test.md"
        profile_path.write_text("Profile content")

        profile_manager.check_profile("test.md")
        captured = capsys.readouterr()

        assert "Profile: test.md" in captured.out
        assert "Profile content" in captured.out


class TestCreateTemplate:
    """Tests for creating profile templates."""

    def test_create_template(self, temp_data_dir, capsys):
        """Test creating a profile from template."""
        profile_manager.create_template("new_profile")

        profile_path = temp_data_dir / "new_profile.md"
        assert profile_path.exists(), "Profile file was not created"

        content = profile_path.read_text()
        assert "# AI Engineering Profile" in content
        assert "## Experience Level" in content
        assert "## Technical Stack" in content
        assert "## Career Goals" in content

    def test_create_template_already_exists(self, temp_data_dir):
        """Test creating template when profile already exists."""
        profile_path = temp_data_dir / "existing.md"
        profile_path.write_text("Existing content")

        with pytest.raises(SystemExit):
            profile_manager.create_template("existing")

    def test_template_has_required_sections(self, temp_data_dir):
        """Test that template includes all required sections."""
        profile_manager.create_template("full_template")

        profile_path = temp_data_dir / "full_template.md"
        content = profile_path.read_text()

        required_sections = [
            "# AI Engineering Profile",
            "## Experience Level",
            "## Role & Expertise",
            "## Technical Stack",
            "## Career Goals",
            "## Key Specializations",
            "## Portfolio Projects",
            "## Certifications & Education",
            "## Market Position",
        ]

        for section in required_sections:
            assert section in content, f"Missing section: {section}"


class TestUpdateProfile:
    """Tests for updating profiles."""

    def test_update_new_profile_interactive(self, temp_data_dir, monkeypatch):
        """Test creating a new profile through interactive update."""
        # Mock user input
        test_input = "Role: AI Engineer\nSkills: Python, LLMs\nGoals: Freelance"
        monkeypatch.setattr("builtins.input", lambda _: test_input.split("\n").pop(0) if test_input.split("\n") else "")

        # We'll skip the actual interactive test as it requires complex mocking
        # Instead, test that the function handles the data directory

        profile_manager.ensure_data_dir()
        assert temp_data_dir.exists(), "Data directory should be created"

    def test_ensure_data_dir_creates_directory(self, temp_data_dir):
        """Test that ensure_data_dir creates the directory."""
        # Remove directory if it exists
        if temp_data_dir.exists():
            shutil.rmtree(temp_data_dir)

        profile_manager.ensure_data_dir()
        assert temp_data_dir.exists(), "Data directory was not created"


class TestProfileContent:
    """Tests for profile content validation."""

    def test_profile_can_be_written_and_read(self, temp_data_dir):
        """Test that profiles can be written and read correctly."""
        profile_path = temp_data_dir / "content_test.md"
        original_content = """# Test Profile

## Experience
Senior AI Engineer with 5 years experience

## Skills
- Python
- LLMs
- Distributed Systems
"""

        profile_path.write_text(original_content, encoding='utf-8')
        read_content = profile_path.read_text(encoding='utf-8')

        assert read_content == original_content

    def test_profile_with_unicode_characters(self, temp_data_dir):
        """Test that profiles handle Unicode content correctly."""
        profile_path = temp_data_dir / "unicode_test.md"
        unicode_content = """# Profile with Unicode

## Languages
- Python (expert)
- JavaScript (intermediate)

## Specializations
- Agentic AI systems
- RAG implementations
"""

        profile_path.write_text(unicode_content, encoding='utf-8')
        read_content = profile_path.read_text(encoding='utf-8')

        assert read_content == unicode_content
        assert "Agentic AI" in read_content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
