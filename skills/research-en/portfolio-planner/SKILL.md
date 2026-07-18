---
name: portfolio-planner
description: Plan an AI engineering portfolio project based on current freelance market trends and skills demand
user-invocable: true
allowed-tools: Read, Write, Glob, WebSearch, Task, AskUserQuestion
---

# Portfolio Planner Skill

Research the current freelance AI market and generate a personalized portfolio strategy with recommended project ideas and certifications.

## Workflow

### Phase 1: Load Profile & Confirm Scope

1. Read the Marco Berta profile file (`data/marco_ai_profile_llm_ready.md` relative to current working directory).
   - If file not found, ask user for the path to their profile file.
   - Extract the compact agent context block (lines beginning with `Name:`, `Location:`, etc.)

2. Ask user to confirm research scope via AskUserQuestion:
   ```
   Question: "Freelance Market Scope"
   Header: "Market Timeframe"
   Options:
   - "Last 6 months (July 2024 - Dec 2024)" (Recommended)
   - "Last 12 months (Jan 2024 - Dec 2024)"
   - "Last 3 months (Oct 2024 - Dec 2024)"
   
   Question: "Portfolio Project Constraints"
   Header: "Build Time & Complexity"
   Options:
   - "Rapid prototype (1-2 weeks work)" (Recommended)
   - "Medium project (3-8 weeks work)"
   - "Ambitious project (8+ weeks work)"
   
   Question: "Target Freelance Client Type"
   Header: "Client Focus"
   Options:
   - "B2B enterprises & startups" (Recommended)
   - "Mid-market companies"
   - "Agencies & consultancies"
   - "No preference - cast wide net"
   ```

3. Store user responses for use in Phase 2 prompt templates.

### Phase 2: Parallel Research (3 Background web-search-agent Tasks)

Launch 3 parallel background tasks (set `background: true`, no task output capture). Each agent will:
- Read the `freelance-market.md` module from `~/.claude/agents/web-search-modules/`
- Inject the user's Marco Berta profile (from Phase 1)
- Follow strict search queries scoped to user's time range

#### Hard Constraint Template for All Agents

Reproduce this exactly in each agent task prompt:

```
MANDATORY: Before conducting any web search or fetch, read this file:
~/.claude/agents/web-search-modules/freelance-market.md

This module defines:
- Where to search (job boards, communities, trend sources)
- How to structure queries
- Recency requirements (ONLY 2025-2026 sources)
- What signals indicate market demand

Use the strategies in this file for all searches.

HARD CONSTRAINT: Search ONLY for sources published in 2024 or 2025. 
Every finding must include publication date. Exclude undated content.
```

---

#### Agent A: Market Trends Research

**Task Prompt Template** (fill in {time_range}, {profile_context}):

```
# Research Task: Freelance AI Market Trends

## Mandate
Research the current freelance AI market landscape for {time_range}.
Time period: {time_range}
Research focus: AI/ML, agents, RAG, LLM applications

## Profile Context
{profile_context}

## Key Questions to Answer
1. What are the top 5 most in-demand AI skills for freelance work RIGHT NOW?
2. What hourly/project rates are clients offering in 2025-2026? (Differentiate by skill level and region if possible)
3. What's the market sentiment: oversaturated, growing, or emerging opportunities?
4. Which technologies/specializations have the highest rates or most open positions?
5. Are MCP, agentic systems, and RAG seeing increased freelance demand?

## Search Queries (use these as starting points, adapt as needed)
- "AI engineer freelance rates 2025"
- "most in-demand AI skills freelance 2025-2026"
- "Upwork AI engineer earnings 2025"
- "LLM consultant market demand 2025"
- "agentic RAG freelance opportunities"
- "MCP adoption freelance market"
- "Reddit r/freelance AI engineer 2025"

## Output Format
Executive Summary
- Top 5 most in-demand skills (ranked by demand signal)
- Current market saturation level
- Rate ranges observed

Detailed Findings
- Job board analysis (Upwork, Malt, Toptal, LinkedIn)
- Skill demand breakdown
- Rate trends by specialization
- Regional differences (Europe vs global)

Sources (REQUIRED)
- Every claim must cite source + publication date
```

Launch with:
```
name: web-search-agent
background: true
task_output: disabled
```

---

#### Agent B: Portfolio Project Ideas Research

**Task Prompt Template** (fill in {time_range}, {build_time}, {profile_context}):

```
# Research Task: AI Portfolio Project Recommendations

## Mandate
Identify the best portfolio projects for a freelance AI engineer to build in {time_range}.
Build time constraint: {build_time}
Stack preference: Python, FastAPI, Docker, MongoDB, vector databases, LLM APIs, MCP

## Profile Context
{profile_context}

## Key Questions to Answer
1. What portfolio projects are currently getting AI engineers hired by clients?
2. Which project types show the strongest ROI for freelance positioning?
3. What B2B/B2C AI automation ideas are clients actively seeking?
4. How do MCP and agentic systems fit into portfolio projects in 2025-2026?
5. What are the "killer features" that make a portfolio project stand out?

## Search Queries (use these as starting points)
- "AI engineer portfolio projects 2025 that get hired"
- "agentic RAG portfolio ideas"
- "MCP server portfolio project example"
- "B2B AI automation portfolio projects"
- "best AI projects to build for freelance 2025"
- "portfolio project teardown AI engineer"
- "what do clients hire portfolio AI projects for"
- "Upwork AI portfolio projects that win bids"

## Output Format
Executive Summary
- 3 recommended projects (ranked by freelance potential)
- Expected build time for each
- Why each aligns with current market demand

Detailed Analysis (for each of 3 projects)
- Project concept & core idea
- Core technical components needed
- Why it impresses clients / improves hiring chances
- Estimated build time
- How to present it to potential clients
- Market demand signals (job postings, client feedback, trend data)
- Potential monetization (portfolio entry point vs paid service)

Sources (REQUIRED)
- Every recommendation must cite source + publication date
```

Launch with:
```
name: web-search-agent
background: true
task_output: disabled
```

---

#### Agent C: Certifications & Skills Research

**Task Prompt Template** (fill in {time_range}, {profile_context}):

```
# Research Task: AI Certifications & Skills Roadmap

## Mandate
Identify certifications and skills that will increase freelance AI mission acquisition in {time_range}.

## Profile Context
{profile_context}

## Key Questions to Answer
1. Which AI certifications have actual freelance market value in 2025-2026?
2. What's the ROI on certifications (cost, time, freelance salary/rate uplift)?
3. Which credentials do clients specifically require or strongly prefer?
4. What non-cert skills can be demonstrated immediately to boost credibility?
5. Are there emerging certifications in MCP, agents, or LLM deployment?

## Search Queries (use these as starting points)
- "AI certifications worth it freelance 2025"
- "Google AI certificate freelance value 2025"
- "AWS AI practitioner certification market demand"
- "Coursera ML engineer certificate freelance ROI"
- "LLM engineering certifications 2025-2026"
- "MCP certification available"
- "agent engineering credentials market value"
- "fast AI deep learning certificate freelance demand"

## Output Format
Executive Summary
- Top 3 recommended certifications (ranked by freelance value)
- Estimated time & cost for each
- Quick wins: skills to demonstrate NOW

Certifications Deep-Dive (for each of 3 certifications)
- Certification name & provider
- Time to complete
- Cost
- Freelance signal strength (low / medium / high)
- Client recognition & demand signals
- Alternative (faster) ways to demonstrate same skill
- ROI estimate (rate increase or mission volume increase)

Quick Wins (Skills to Highlight Immediately, No Cert Needed)
- Top 5 technologies/skills to emphasize in profiles RIGHT NOW
- How to demonstrate each (open-source, portfolio, testimonials)
- Expected impact on mission acquisition

Sources (REQUIRED)
- Every certification & skill claim must cite source + publication date
```

Launch with:
```
name: web-search-agent
background: true
task_output: disabled
```

---

### Phase 3: Wait for Results & Synthesize

1. Wait for all 3 agents to complete (monitor task output).

2. Collect results from each agent:
   - Agent A output (save as `market_trends_{timestamp}.md`)
   - Agent B output (save as `portfolio_ideas_{timestamp}.md`)
   - Agent C output (save as `skills_certs_{timestamp}.md`)

3. Synthesize all findings into a single cohesive report (skill does this, not a subagent):

### Phase 4: Generate & Save Report

Generate markdown report with this structure:

```markdown
# Portfolio & Career Strategy Report
Marco Berta | Generated {date}

## Executive Summary

**Top Recommended Portfolio Project**
[Project name and 1-sentence description from Agent B]
- Why it fits your stack and market demand: [2-3 sentences explaining rationale]
- Core technologies: [list]
- Estimated build time: [time]

**Top 2 Certifications to Pursue**
1. [Cert name] ({provider}) — [brief why it matters for your market positioning]
2. [Cert name] ({provider}) — [brief why it matters for your market positioning]

**Key Market Insight**
[One powerful observation from Agent A that contextualizes the recommendations]

---

## 1. Market Landscape (Current Trends)

[Synthesized from Agent A findings]

### In-Demand AI Skills for Freelance Work (2025-2026)
[Top 5 skills with demand ranking]

### Current Rates & Market State
[Rate ranges, regional context, saturation assessment]

### Emerging Opportunities
[Areas with growing demand but less competition]

---

## 2. Portfolio Project Recommendations

### Primary Recommendation: {Project Name}

**Concept**
[What the project does and who benefits]

**Why This Project**
- Market demand: [Evidence from client job posts, trends]
- Your fit: [How it aligns with Marco's Python/FastAPI/Docker/MCP focus]
- Client appeal: [Why freelance clients care about this project]
- Build time: {X weeks}

**Core Technical Components**
- [Component 1]: [Technology stack]
- [Component 2]: [Technology stack]
- [Component 3]: [Technology stack]

**How to Present It to Clients**
- Portfolio narrative: [What story does this project tell about your capabilities?]
- Key metrics: [What should you measure to impress clients? (speed, accuracy, cost savings)]
- Demo approach: [How to showcase it?]

---

### Alternative Project 1: {Project Name}
[Repeat above structure]

---

### Alternative Project 2: {Project Name}
[Repeat above structure]

---

## 3. Certifications & Skills Roadmap

### Recommended Certifications

| Certification | Provider | Time | Cost | Freelance Signal | ROI Estimate |
|---|---|---|---|---|---|
| [Cert] | [Provider] | [time] | [cost] | [High/Medium/Low] | [Brief ROI desc] |
| [Cert] | [Provider] | [time] | [cost] | [High/Medium/Low] | [Brief ROI desc] |
| [Cert] | [Provider] | [time] | [cost] | [High/Medium/Low] | [Brief ROI desc] |

### Why These 3?
[Explanation connecting to market trends from Agent A and portfolio project from Agent B]

---

## 4. Quick Wins (Skills to Demonstrate Immediately)

### Top 5 In-Demand Skills — Do These NOW
1. [Skill]: How to demonstrate [what to show in profiles/GitHub]
2. [Skill]: How to demonstrate [what to show]
3. [Skill]: How to demonstrate [what to show]
4. [Skill]: How to demonstrate [what to show]
5. [Skill]: How to demonstrate [what to show]

**Expected impact**: [Estimated uplift in mission acquisition or rates]

---

## 5. Implementation Timeline

### Immediate (This Month)
- [Quick win 1]
- [Quick win 2]

### Short Term (1-3 Months)
- [Certification 1 or Project kickoff]

### Medium Term (3-6 Months)
- [Portfolio project build]
- [Certification 2]

### Long Term (6+ Months)
- [Certification 3]
- [Secondary project or advanced specialization]

---

## Sources

[Compiled list of all sources from Agents A, B, C, with publication dates]

**All sources verified as published 2025-2026.**
```

4. Save report to:
   ```
   ./portfolio-plan/portfolio-report-{YYYY-MM-DD}.md
   ```
   (Create `portfolio-plan/` directory if needed)

5. Ask user (AskUserQuestion) to confirm save location or provide alternative path.

6. Show user the generated report file path and key highlights.

---

## Next Steps (User Guidance)

After report generation, suggest:
- Review the primary portfolio project recommendation in detail
- Start with one "quick win" skill to highlight in profiles immediately
- Decide which certification (if any) to pursue first
- Consider prototyping the portfolio project idea with a small MVP
- Use project as subject for case study / thought leadership post

---

## Notes

- **Profile Injection**: The compact agent context block ensures all research is personalized to Marco's experience level, stack, and market positioning.
- **Recency Enforcement**: Hard constraint on 2025-2026 sources only ensures recommendations reflect current market state, not stale trends.
- **No JSON Output**: Unlike `/research-deep`, this skill outputs a human-readable markdown report directly. The synthesis layer runs in the skill (not a subagent), so final report reflects coherent narrative rather than just concatenated agent outputs.
- **Parallel Agents**: 3 agents run in parallel for speed. Each is narrowly scoped so search queries stay focused and results are distinct.
