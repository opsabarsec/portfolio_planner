---
name: portfolio-planner
description: Plan an AI engineering portfolio project based on current freelance and hiring trends, with a focus on high-signal skills and project types for the next 6–12 months.
user-invocable: true
allowed-tools: Read, Write, Glob, WebSearch, Task, AskUserQuestion
---

# Portfolio Planner Skill

Research the current freelance and hiring market for AI engineers and generate a personalized portfolio strategy with recommended project ideas and, where justified, certifications.

## Workflow

### Phase 1: Load Profile & Confirm Scope

1. Read the Marco Berta profile file (`data/marco_ai_profile_llm_ready.md` relative to current working directory).
   - If file not found, ask user for the path to their profile file.
   - Extract the compact agent context block (lines beginning with `Name:`, `Location:`, etc.)

2. Ask user to confirm research scope via AskUserQuestion:
   - Keep the three-question structure (timeframe, build time, client type) as-is.
   - Update labels if needed to reflect current years (e.g. “Last 6 months”, “Last 12 months”) rather than hardcoding 2024 ranges.

3. Store user responses for use in Phase 2 prompt templates.

### Phase 2: Parallel Research (3 Background web-search-agent Tasks)

- Keep the three-agent layout as-is.
- Frame research tasks around the web-search-agent's core evidence layers: market impact, hiring demand, freelance demand, GitHub momentum, and portfolio opportunity.
- Each task should load the appropriate module (`freelance-market.md`, `eu-ai-market-signals.md`, `github-ai-trends.md`) before searching.
- Ensure synthesis pulls together findings using consistent vocabulary: **market impact** (commercial signals), **GitHub momentum** (open-source trends), **hiring demand** (recruiter signals), **freelance demand** (client pain points), **portfolio opportunity** (actionable projects).

### Phase 3 & 4: Synthesis and Dual Output

Generate two complementary documents:

#### 3a. **Polished Final Report** (`portfolio-report-YYYY-MM-DD.md`)
Focus on:
- Executive summary with clear recommendation
- One primary portfolio project
- Top certifications
- Quick-win skills
- Implementation timeline
- Actionable next steps

Add a one-line note in the Executive Summary section template:

```md
**Geography focus**: [If applicable, note whether findings are European-focused or global.]
**Research date**: [Date of research completion]
```

#### 3b. **Raw Research Archive** (`data/research_results_DD_MM_YYYY.md`)
A NotebookLM-friendly archive containing:

**Metadata block:**
```md
---
date: DD-MM-YYYY
scope: [user's selected timeframe, e.g., "Last 6 months"]
geography: [Europe/Global/Specific region]
focus_areas: [Build time, client type constraints]
---
```

**Content structure:**
- Executive summary (concise, non-polished)
- **Market Signals** section with all findings, dates, and sources
- **Hiring Demand** section with role/skill patterns
- **GitHub Trends** section with repos, star counts, timestamps
- **Freelance Demand** section with buyer pain points
- **Ranked Opportunities** section with all project ideas and scoring
- **Raw Source List** with full URLs and extraction dates
- **Tags** for easy categorization: #github-trends, #freelance, #europe-jobs, #market-signals, etc.

This archive becomes the "memory" for research agents in future runs—it captures the full evidence base without editorial filtering, making it suitable for NotebookLM ingestion and future reference.

---

Overall, the portfolio planner skill drives three parallel, time-bounded, portfolio-oriented research tasks and then synthesizes into both a narrative report (for human action) and an evidence archive (for future AI research and memory). This dual output supports both immediate decision-making and long-term research continuity.