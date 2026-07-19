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
- Replace references like “current freelance AI market landscape” with “current freelance and hiring market landscape” where appropriate, to reflect that `web-search-agent` now also routes to hiring and general market modules.
- Ensure the hard constraint block explicitly mentions that each agent must load `freelance-market.md` before searching.

### Phase 3 & 4: Synthesis and Report

- The report already focuses on:
  - One primary portfolio project
  - Top certifications
  - Quick-win skills
  - Implementation timeline

That structure is fully compatible with the updated `web-search-agent` persona and modules; no structural change is necessary. You can optionally add a one-line note in the Executive Summary section template:

```md
**Geography focus**: [If applicable, note whether findings are European-focused or global.]
```

This keeps the skill compatible with both Europe-focused and broader searches.

---

Overall, the portfolio planner skill is already very close to what your new `web-search-agent` plus `freelance-market.md` module expects: it drives three parallel, time-bounded, portfolio-oriented research tasks and then synthesizes into a narrative report. [page:29] The main improvement is to slightly widen the description and phrasing so it reflects both freelance and hiring demand, not only freelance, and to avoid hardcoding past timeframe labels.