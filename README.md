# Portfolio Planner for Freelance AI Engineers

A Claude Code skill that research the current freelance AI market and creates a personalized portfolio and upskilling strategy.

## What It Does

The `/portfolio-planner` skill helps you discover:

- **The best portfolio project to build** — aligned with current market trends, your technical stack, and what clients are actively hiring for
- **In-demand skills & specializations** — what AI capabilities maximize your freelance mission acquisition
- **Certification roadmap** — which credentials (if any) provide genuine ROI in the 2025-2026 freelance market
- **Quick wins** — skills to highlight immediately on your freelance profiles to attract clients

All research is scoped to **2025-2026 only** (no stale data) and focuses on **European market** opportunities and rates.

## How It Works

### One Command

```bash
/portfolio-planner
```

### Three Research Phases

#### Phase 1: Profile & Scope

- Loads your background (skills, experience, focus areas)
- Asks you to confirm research timeframe (6-12 months) and project constraints

#### Phase 2: Parallel Market Research

Three agents research simultaneously:

1. **Market Trends** — Current freelance AI rates, in-demand skills, market saturation
2. **Portfolio Ideas** — Project concepts that impress clients and fit your stack
3. **Certifications & Skills** — Which credentials matter for freelance work

#### Phase 3: Synthesis & Report

- Generates a single markdown report with your top portfolio project recommendation
- Includes a certification roadmap (if relevant)
- Lists quick wins: skills to showcase now without new training
- All sources dated and cited

### Output

```bash
./portfolio-plan/portfolio-report-{date}.md
```

A markdown report ready to guide your next 3-6 months of portfolio and skill development.

## Installation

### Prerequisites

- Claude Code (2.1.0+) with web search enabled

### Quick Install (Recommended)

Clone the repo and run the install script:

```bash
git clone https://github.com/opsabarsec/portfolio_planner
cd portfolio_planner
```

**Using PowerShell (Windows):**

```powershell
.\install-skill.ps1
```

**Using Python (All platforms):**

```bash
python install_skill.py
```

The script automatically:

- Reads your Claude Code directory from `.env` (or uses system defaults)
- Creates necessary directories
- Installs the skill, agent, and modules

**Run tests to verify installation:**

```bash
# Using pytest (recommended)
pytest tests/test_skill_install.py -v

# Using Python directly
python tests/test_skill_install.py

# Using PowerShell
.\tests\test-skill-install.ps1
```

**Run profile manager tests:**

```bash
pytest tests/test_profile_manager.py -v
```

**Requirements for testing:**

```bash
pip install pytest
```

### Manual Install

If you prefer to install manually:

#### macOS / Linux

```bash
git clone https://github.com/opsabarsec/portfolio_planner
cd portfolio_planner

# Copy the portfolio-planner skill
cp -r skills/research-en/portfolio-planner ~/.claude/skills/

# Copy the web search agent and market research module
cp agents/web-search-agent.md ~/.claude/agents/
cp -r agents/web-search-modules ~/.claude/agents/
```

#### Windows (PowerShell)

```powershell
git clone https://github.com/opsabarsec/portfolio_planner
cd portfolio_planner

# Copy the portfolio-planner skill
Copy-Item -Path "skills/research-en/portfolio-planner" -Destination "$env:USERPROFILE\.claude\skills\" -Recurse -Force

# Copy the web search agent and market research module
Copy-Item -Path "agents/web-search-agent.md" -Destination "$env:USERPROFILE\.claude\agents\"
Copy-Item -Path "agents/web-search-modules" -Destination "$env:USERPROFILE\.claude\agents\" -Recurse -Force
```

## Usage

From your working directory:

```bash
/portfolio-planner
```

Respond to the scope questions (timeframe, build constraints, target client type), then watch as 3 parallel agents research the market. The skill synthesizes their findings into one actionable report.

The research focuses on:

- **Freelance job boards**: Upwork, Malt, Toptal, LinkedIn, Y Combinator, Hacker News
- **Community insights**: Reddit, Dev.to, X/Twitter, Substack newsletters
- **Rate & trend data**: Recent salary surveys, hiring manager commentary, skill demand metrics

## Configuration

Copy `.env.example` to `.env` and customize:

```bash
cp .env.example .env
```

Available options:

- `USERRPROFILE` — Path to your home directory (auto-detected, usually not needed)
- `PORTFOLIO` — Link to your GitHub/portfolio (optional, for context)
- `SAVE_REPORTS_TO_DATA` — Save report copies to `data/` folder (default: false)
  - Set to `true` to keep reports organized with your profile data

## Profile Management

Manage your AI engineering profile with the `profile_manager.py` tool:

```bash
# List all profiles
python profile_manager.py list

# Check a profile
python profile_manager.py check <profile_name>

# Create a profile from template
python profile_manager.py template <profile_name>

# Update an existing profile
python profile_manager.py update <profile_name>
```

**Examples:**

```bash
# Create a new profile from template
python profile_manager.py template marco_profile

# View your profile
python profile_manager.py check marco_profile

# Update your profile details
python profile_manager.py update marco_profile
```

## What Data You Need

Create a profile file in the data folder. For example `data/marco_ai_profile_llm_ready.md` with:

- Your role and experience level
- Technical stack preferences (e.g., Python, FastAPI, Docker, LLMs)
- Career goals (e.g., enterprise roles, startup advisory, open-source)
- Key specializations (e.g., MCP, RAG, agentic AI, production ML)

The portfolio planner uses this to personalize research recommendations so you get advice that actually matches your strengths and market positioning.

### Report Output

Reports are saved to `./portfolio-plan/portfolio-report-{date}.md` by default.

If `SAVE_REPORTS_TO_DATA=true` in `.env`, a copy is also saved to `./data/portfolio-report-{date}.md` for easy access alongside your profile.

## Example Output Structure

```markdown
# Portfolio & Career Strategy Report
Generated 2025-01-15

## Executive Summary
- Top recommended portfolio project
- Top 2 certifications to pursue
- Key market insight

## 1. Market Landscape
- Current in-demand AI skills (ranked)
- Freelance rate ranges by specialization
- Regional differences (Europe)

## 2. Portfolio Project Recommendations
- Primary recommendation (why it matters, tech stack, build time)
- 2 alternative projects

## 3. Certifications & Skills Roadmap
- 3 cert options with ROI estimate
- Quick wins: skills to highlight NOW

## 4. Implementation Timeline
- What to do this month, next quarter, 6-month plan

## Sources
All sources cited with publication dates (2025-2026 only)
```

## Architecture

This skill is built on a modular web-search framework:

- **Skill**: `portfolio-planner/SKILL.md` — orchestrates research flow
- **Agent**: `web-search-agent.md` — performs web research with routing logic
- **Modules**: `web-search-modules/freelance-market.md` — strategy for freelance market research

The system enforces recency (2025-2026 sources only) and uses human-in-the-loop confirmations at each stage to keep research aligned with your goals.

## For Developers

See `archived/` for the original deep-research-skills framework. This project specializes that framework for portfolio planning.

## License

MIT
