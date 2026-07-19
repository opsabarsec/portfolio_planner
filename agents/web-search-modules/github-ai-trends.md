# GitHub AI Trends Module

## Purpose
Use this module to identify the latest AI project trends on GitHub by combining recency, star growth, repository activity, and practical relevance. The goal is not to list famous repositories, but to detect which AI project categories show GitHub momentum now and whether they suggest strong portfolio opportunities.

## Why This Module Matters
GitHub Trending provides a live view of repositories gaining attention now, while GitHub search supports sorting by stars, forks, and recently updated repositories.[1][2] External trend trackers also rank repositories by star growth velocity over daily, weekly, and monthly windows, which is useful when total stars alone hide newer breakout projects.[3][4][5]

## Core Principle
Do not confuse popularity with opportunity.
A useful signal comes from combining:
- recency, meaning new or recently updated repositories
- momentum, meaning rapid star growth over a short period
- maintenance health, meaning recent commits and active discussion
- category relevance, meaning whether the project maps to a real engineering or market theme
- portfolio fit, meaning whether the idea can inspire a differentiated project rather than a copycat clone

## Best Use Cases
Use this module when you need to:
- find the latest AI project categories with GitHub momentum
- detect breakout repositories before they become saturated
- understand which AI tooling themes are accelerating
- compare older high-star repositories with newer fast-growth repositories
- translate GitHub momentum into portfolio opportunities

## Search Focus
Search for:
- GitHub trending AI repositories
- GitHub AI repositories stars this week
- GitHub AI repositories stars this month
- GitHub AI repositories recently updated
- GitHub AI agents trending GitHub
- GitHub MCP repositories trending
- GitHub RAG repositories trending
- GitHub AI evaluation repositories trending
- GitHub AI observability repositories trending
- GitHub AI workflow repositories trending

## Source Priority
Use these sources in order:
1. GitHub Trending pages for immediate momentum
2. GitHub repository search with sorting by stars or recently updated
3. GitHub topic pages where useful
4. External GitHub trend trackers that expose star velocity
5. Curated ecosystem writeups only as supporting context

## Search Strategy
### Pass 1: Immediate Momentum
Check GitHub Trending and similar trend surfaces for:
- repositories appearing today
- repeated AI subcategories appearing across the week or month
- projects with strong short-term star velocity

### Pass 2: Recency Filter
Favor repositories that satisfy at least one of these:
- created recently
- updated recently
- gained strong stars in the last week or month
- show visible momentum despite lower total stars

### Pass 3: Maintenance Check
For each candidate repository, inspect:
- recent commit activity
- release cadence if visible
- issues or discussions activity
- contributor depth if visible
- whether the repo looks actively maintained or just briefly viral

### Pass 4: Category Extraction
Group repositories into themes such as:
- agent frameworks
- MCP tooling
- retrieval and RAG systems
- evaluation and benchmarks
- observability and tracing
- coding agents
- multimodal pipelines
- workflow automation
- private or local AI tooling
- vertical AI apps

### Pass 5: Portfolio Translation
For each category with GitHub momentum, answer:
- Does this trend have market impact or is it mostly developer curiosity?
- Is the space already overcrowded with clones?
- Can the user build a more focused or more practical version?
- Does the GitHub momentum suggest a tooling gap, reliability gap, integration gap, or UX gap?

## Ranking Rules
For each repository or category, score from 0 to 5 on:
- Star momentum
- Recency
- Maintenance health
- Engineering depth
- Market relevance
- Portfolio differentiation potential

Suggested interpretation:
- High stars + low recency = mature signal, useful but possibly crowded
- Lower total stars + very high recent growth = breakout signal worth watching
- High recency + low maintenance = weak signal unless reinforced elsewhere
- High market relevance + medium GitHub momentum = often better for a practical portfolio than a purely viral repo

## Red Flags
Be cautious when:
- a repository is trending but has weak maintenance signals
- star count is old and growth has flattened
- the project is mostly hype bait or prompt-wrapper duplication
- the repo is impressive but impossible to reproduce meaningfully
- the trend is dominated by clones with little room for differentiation

## Output Template
For each trend with GitHub momentum, return:
- Repository or category name
- Theme
- Why it is trending
- Recency signal
- Star or momentum signal
- Maintenance signal
- Practical takeaway
- Portfolio opportunity it suggests
- Risk of saturation or low defensibility

## Preferred Conclusions
The module should not end with “these are the most starred AI repos.”
It should end with conclusions like:
- “MCP infrastructure shows stronger GitHub momentum than generic chat apps.”
- “Evaluation and observability repos have lower GitHub momentum but stronger engineering depth.”
- “Coding-agent ecosystems show momentum but workflow guardrails remain underbuilt.”
- “Multimodal workflow projects show GitHub momentum but are weak on deployment realism.”

## Portfolio Opportunity Examples
Strong patterns derived from GitHub momentum include:
- an MCP observability or governance layer inspired by multiple trending repos
- an evaluation harness for agent workflows where current repos are fragmented
- a multilingual enterprise retrieval system that improves on generic RAG demos
- a local-first or private AI workflow tool for SMEs
- a workflow reliability dashboard for agentic systems

## Decision Rule
Prefer categories, not exact clones.
If a repository is trending, ask what broader capability is rising and what missing layer could become a better portfolio project.