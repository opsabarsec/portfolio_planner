#!/usr/bin/env python3
"""
Portfolio Planner Skill Installer
Reads USERPROFILE from .env and installs the skill to Claude Code
"""

import argparse
import os
import sys
import shutil
from pathlib import Path


def read_env_file(env_file=".env"):
    """Read .env file and extract USERPROFILE."""
    user_profile = None

    if not Path(env_file).exists():
        return None

    try:
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                # Handle both USERPROFILE and USERRPROFILE (typo variant)
                if 'USERRPROFILE' in line:
                    parts = line.split('=', 1)
                    if len(parts) == 2:
                        user_profile = parts[1].strip().strip('"')
                        print(f"Found USERRPROFILE in .env: {user_profile}")
                        break
                elif 'USERPROFILE' in line and 'USERRPROFILE' not in line:
                    parts = line.split('=', 1)
                    if len(parts) == 2:
                        user_profile = parts[1].strip().strip('"')
                        print(f"Found USERPROFILE in .env: {user_profile}")
                        break
    except Exception as e:
        print(f"Error reading .env file: {e}", file=sys.stderr)
        return None

    return user_profile


def get_user_profile():
    """Get USERPROFILE from .env or environment variable."""
    # Try reading from .env first
    user_profile = read_env_file(".env")

    # Fallback to environment variable
    if not user_profile:
        user_profile = os.environ.get('USERPROFILE')
        if user_profile:
            print(f"Using system USERPROFILE: {user_profile}")

    if not user_profile:
        print("Error: Could not determine USERPROFILE", file=sys.stderr)
        sys.exit(1)

    return user_profile


def verify_source_files(skill_source, agent_source, modules_source):
    """Verify that all source files exist."""
    missing_files = []

    if not Path(skill_source).exists():
        missing_files.append(f"Skill: {skill_source}")
    if not Path(agent_source).exists():
        missing_files.append(f"Agent: {agent_source}")
    if not Path(modules_source).exists():
        missing_files.append(f"Modules: {modules_source}")

    if missing_files:
        print("Error: Missing source files:", file=sys.stderr)
        for f in missing_files:
            print(f"  - {f}", file=sys.stderr)
        sys.exit(1)


def create_directories(skills_dir, agents_dir):
    """Create necessary directories."""
    print("\nCreating directories...")

    for directory in [skills_dir, agents_dir]:
        if not Path(directory).exists():
            Path(directory).mkdir(parents=True, exist_ok=True)
            print(f"  Created: {directory}")


def install_skill(skill_source, skill_dest, force=False):
    """Install the portfolio-planner skill."""
    print("\nInstalling portfolio-planner skill...")

    if Path(skill_dest).exists() and not force:
        print(f"  Skill already exists at {skill_dest}")
        print("  Use --force flag to overwrite")
    else:
        if Path(skill_dest).exists():
            shutil.rmtree(skill_dest)
        shutil.copytree(skill_source, skill_dest)
        print(f"  Installed to: {skill_dest}")


def install_agent(agent_source, agents_dir):
    """Install the web search agent."""
    print("\nInstalling web search agent...")

    agent_dest = Path(agents_dir) / "web-search-agent.md"
    shutil.copy2(agent_source, agent_dest)
    print(f"  Installed to: {agent_dest}")


def install_modules(modules_source, modules_dest, force=False):
    """Install the web search modules."""
    print("\nInstalling web search modules...")

    if Path(modules_dest).exists() and not force:
        print(f"  Modules already exist at {modules_dest}")
        print("  Use --force flag to overwrite")
    else:
        if Path(modules_dest).exists():
            shutil.rmtree(modules_dest)
        shutil.copytree(modules_source, modules_dest)
        print(f"  Installed to: {modules_dest}")


def main():
    parser = argparse.ArgumentParser(
        description="Portfolio Planner Skill Installer"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing installations"
    )

    args = parser.parse_args()

    # Get user profile
    user_profile = get_user_profile()

    # Define paths
    claude_skills_dir = os.path.join(user_profile, ".claude", "skills")
    claude_agents_dir = os.path.join(user_profile, ".claude", "agents")

    skill_source = os.path.join(".", "skills", "research-en", "portfolio-planner")
    agent_source = os.path.join(".", "agents", "web-search-agent.md")
    modules_source = os.path.join(".", "agents", "web-search-modules")

    # Verify source files
    verify_source_files(skill_source, agent_source, modules_source)

    # Create directories
    create_directories(claude_skills_dir, claude_agents_dir)

    # Install components
    skill_dest = os.path.join(claude_skills_dir, "portfolio-planner")
    install_skill(skill_source, skill_dest, force=args.force)

    install_agent(agent_source, claude_agents_dir)

    modules_dest = os.path.join(claude_agents_dir, "web-search-modules")
    install_modules(modules_source, modules_dest, force=args.force)

    # Success message
    print("\nInstallation complete!")
    print("\nYou can now run: /portfolio-planner")


if __name__ == "__main__":
    main()
