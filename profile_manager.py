#!/usr/bin/env python3
"""
Portfolio Profile Manager
Manage user profile files stored in the data folder
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime


DATA_DIR = Path("./data")


def ensure_data_dir():
    """Ensure data directory exists."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def list_profiles():
    """List all profile files in data folder."""
    ensure_data_dir()

    profiles = list(DATA_DIR.glob("*_profile*.md"))

    if not profiles:
        print("No profile files found in ./data/")
        print("\nCreate a profile with: python profile_manager.py update <profile_name>")
        return

    print("Available profiles:\n")
    for profile in sorted(profiles):
        file_size = profile.stat().st_size
        mod_time = datetime.fromtimestamp(profile.stat().st_mtime)
        print(f"  - {profile.name}")
        print(f"    Size: {file_size} bytes | Modified: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}\n")


def check_profile(profile_name):
    """Display contents of a profile file."""
    ensure_data_dir()

    # Find profile by name (with or without .md extension)
    if not profile_name.endswith(".md"):
        profile_path = DATA_DIR / f"{profile_name}.md"
    else:
        profile_path = DATA_DIR / profile_name

    if not profile_path.exists():
        print(f"Error: Profile not found: {profile_path}", file=sys.stderr)
        print("\nAvailable profiles:", file=sys.stderr)
        list_profiles()
        sys.exit(1)

    print(f"\nProfile: {profile_path.name}\n")
    print("=" * 70)
    try:
        with open(profile_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e:
        print(f"Error reading profile: {e}", file=sys.stderr)
        sys.exit(1)
    print("=" * 70 + "\n")


def update_profile(profile_name):
    """Interactively update or create a profile."""
    ensure_data_dir()

    if not profile_name.endswith(".md"):
        profile_path = DATA_DIR / f"{profile_name}.md"
    else:
        profile_path = DATA_DIR / profile_name

    # Check if profile exists
    existing_content = ""
    if profile_path.exists():
        print(f"Profile already exists: {profile_path.name}")
        try:
            with open(profile_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            print("\nCurrent content:")
            print("-" * 70)
            print(existing_content)
            print("-" * 70)
        except Exception as e:
            print(f"Error reading existing profile: {e}", file=sys.stderr)
            return

        choice = input("\nDo you want to (e)dit or (r)eplace this profile? [e/r]: ").lower()
        if choice not in ['e', 'r']:
            print("Cancelled.")
            return

        if choice == 'r':
            existing_content = ""

    print("\nEnter profile information (press Ctrl+D when done, or Ctrl+Z then Enter on Windows):")
    print("Include:")
    print("  - Your role and experience level")
    print("  - Technical stack preferences (e.g., Python, FastAPI, Docker, LLMs)")
    print("  - Career goals (e.g., enterprise roles, startup advisory, open-source)")
    print("  - Key specializations (e.g., MCP, RAG, agentic AI, production ML)")
    print()

    try:
        lines = []
        while True:
            try:
                line = input()
                lines.append(line)
            except EOFError:
                break
        new_content = "\n".join(lines)
    except KeyboardInterrupt:
        print("\n\nCancelled.")
        return

    if not new_content.strip():
        print("No content provided. Cancelled.", file=sys.stderr)
        return

    # Save profile
    try:
        with open(profile_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"\n[OK] Profile saved to: {profile_path}")
        print(f"  Path: {profile_path.resolve()}")
    except Exception as e:
        print(f"Error saving profile: {e}", file=sys.stderr)
        sys.exit(1)


def create_template(profile_name):
    """Create a profile from template."""
    ensure_data_dir()

    if not profile_name.endswith(".md"):
        profile_path = DATA_DIR / f"{profile_name}.md"
    else:
        profile_path = DATA_DIR / profile_name

    if profile_path.exists():
        print(f"Profile already exists: {profile_path}")
        sys.exit(1)

    template = """# AI Engineering Profile

## Experience Level
[Your experience level - e.g., Senior, Mid-level, Junior]

## Role & Expertise
[Your primary role and areas of expertise]

## Technical Stack
- **Languages**: Python, JavaScript, Go, Rust, etc.
- **Frameworks**: FastAPI, Django, Node.js, etc.
- **Tools**: Docker, Kubernetes, AWS, GCP, etc.
- **Specializations**: LLMs, RAG, MCP, Agentic AI, Production ML, etc.

## Career Goals
[Your career aspirations and target opportunities]
- e.g., Enterprise AI engineering roles
- e.g., Startup advisory and technical leadership
- e.g., Open-source contributions and thought leadership
- e.g., Freelance/contract work with high-value clients

## Key Specializations
[Your key areas where you add the most value]
1. [Specialization 1]
2. [Specialization 2]
3. [Specialization 3]

## Portfolio Projects
[Notable projects you've built or contributed to]
- Project 1: [Description and impact]
- Project 2: [Description and impact]

## Certifications & Education
[Relevant certifications, degrees, or training]

## Market Position
[How you want to position yourself in the market]
"""

    try:
        with open(profile_path, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"[OK] Profile template created: {profile_path}")
        print(f"\nEdit the file to customize your profile, then run:")
        print(f"  python profile_manager.py check {profile_name}")
    except Exception as e:
        print(f"Error creating template: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Portfolio Profile Manager - Manage your AI engineering profile"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list command
    subparsers.add_parser(
        "list",
        help="List all profile files in data folder"
    )

    # check command
    check_parser = subparsers.add_parser(
        "check",
        help="Display a profile"
    )
    check_parser.add_argument(
        "profile",
        nargs="?",
        help="Profile name (without .md extension)"
    )

    # update command
    update_parser = subparsers.add_parser(
        "update",
        help="Create or update a profile"
    )
    update_parser.add_argument(
        "profile",
        help="Profile name (without .md extension)"
    )

    # template command
    template_parser = subparsers.add_parser(
        "template",
        help="Create a new profile from template"
    )
    template_parser.add_argument(
        "profile",
        help="Profile name (without .md extension)"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "list":
        list_profiles()
    elif args.command == "check":
        if not args.profile:
            print("Error: profile name required")
            sys.exit(1)
        check_profile(args.profile)
    elif args.command == "update":
        update_profile(args.profile)
    elif args.command == "template":
        create_template(args.profile)


if __name__ == "__main__":
    main()
