# Research Memory Guide
## Using Portfolio Research Archives as Agent Memory

This guide explains how to leverage your portfolio research archives (`research_results_DD_MM_YYYY.md`) as persistent memory for future research and analysis tasks.

---

## What is a Research Archive?

A **research archive** is a structured markdown file that captures:
- **Raw findings** from market, hiring, GitHub, and freelance demand research
- **Complete source citations** with dates and URLs
- **Unfiltered evidence** suitable for NotebookLM analysis
- **Consistent metadata tags** for easy filtering and cross-referencing

Unlike the polished portfolio report (which is editorial and action-focused), the research archive is a preservation layer—it's designed to be ingested by AI agents in future research runs to identify patterns, avoid duplicate work, and build confidence in recommendations over time.

---

## File Structure & Naming

### Location
```
data/research_results_DD_MM_YYYY.md
```
- `DD` = day (01-31)
- `MM` = month (01-12)
- `YYYY` = year (e.g., 19-07-2026)

### Example
```
data/research_results_19_07_2026.md
```

---

## How to Use Research Archives

### 1. **Load as Agent Context for Next Research Run**

When you run `/portfolio-planner` again, you can ask agents to:

```
Load the previous research archive (data/research_results_19_07_2026.md) 
and identify what's changed since then. Flag new trends, areas where 
confidence has increased, and any contradictions in the evidence.
```

This turns your previous research into a **baseline** for incremental research.

### 2. **Upload to NotebookLM for Deeper Analysis**

1. Open [NotebookLM](https://notebooklm.google.com)
2. Create a new notebook
3. Upload your research archive file
4. Ask NotebookLM to:
   - Summarize cross-portfolio trends
   - Identify skill clusters and career paths
   - Spot contradictions between market and hiring signals
   - Generate podcast scripts or learning guides
   - Create interactive study materials

Example prompts:
- "Across all archived research runs, which skills show consistent growth?"
- "What emerging opportunities appear in multiple research cycles?"
- "Where is there disagreement between freelance demand and hiring data?"

### 3. **Build a Research Memory Folder**

Over time, create an archive:

```
data/
├── research_results_19_07_2026.md
├── research_results_25_06_2026.md
├── research_results_12_05_2026.md
└── research_results_README.md (your index)
```

Each file is a snapshot of market conditions at that moment. Together, they show:
- Trend trajectories (which skills are accelerating?)
- Market saturation (which categories are cooling off?)
- Timing (when did this trend emerge?)

### 4. **Query Archives with Claude Code**

Use Claude Code to search and analyze multiple archives:

```bash
# Find all mentions of "RAG" across all research runs
grep -r "RAG\|Retrieval" data/research_results_*.md

# Extract only the ranked opportunities from all archives
grep -A 5 "Ranked Portfolio Opportunities" data/research_results_*.md
```

Or ask Claude to load and compare:
```
Load research_results_19_07_2026.md and research_results_12_05_2026.md. 
What's new in hiring demand? What skills no longer appear?
```

---

## Metadata & Tagging System

Research archives use consistent tags for filtering:

| Tag | Purpose | Example |
|-----|---------|---------|
| `#market-signals` | Market trends, adoption, funding | Investment in AI, sector movement |
| `#hiring-demand` | Job market signals, skills, roles | "LLM engineer" postings up 40% |
| `#europe-jobs` | European-specific hiring data | German AI job postings |
| `#github-trends` | Trending repos, star growth, categories | Agent evaluation frameworks |
| `#freelance-demand` | Freelance rates, services, buyer pain | Upwork RAG projects @ €45-70/hr |
| `#skills` | Emerging or high-demand capabilities | Prompt engineering, vector DBs |
| `#adoption` | Real-world usage signals | Production deployment patterns |
| `#projects` | Portfolio project ideas & analysis | Multi-agent systems for workflows |
| `#services` | Consulting/service opportunities | LLM fine-tuning advisory |

### How to Use Tags

**In NotebookLM:**
- Upload archive and ask: "Show me all findings tagged #github-trends and #europe-jobs"
- Create a custom guide filtered by tags

**In Claude Code:**
```bash
# Extract all freelance demand findings
grep "#freelance-demand" data/research_results_19_07_2026.md
```

---

## Best Practices for Research Archives

### ✅ Do

- **Be exhaustive** — include all findings, even conflicting ones
- **Date everything** — every source should have an access or publication date
- **Link all sources** — URLs should be complete and clickable
- **Use consistent structure** — follow the template exactly so parsing is reliable
- **Tag generously** — one finding can have multiple tags
- **Preserve original quotes** — when noting evidence, include key phrases verbatim
- **Note confidence levels** — flag if evidence is from one source vs. multiple confirmations

### ❌ Don't

- **Edit out disagreements** — if two sources conflict, keep both and note the discrepancy
- **Remove "weak" findings** — let NotebookLM and future agents decide what matters
- **Consolidate findings prematurely** — preserve raw sources even if they overlap
- **Skip metadata** — dates and URLs are as important as the findings themselves
- **Lose source context** — always include what type of source it is (hiring platform, GitHub, freelance board, etc.)

---

## Creating Research Memories for Agents

Once you've accumulated 2-3 research archives, you can create a **research memory** for agents:

### Step 1: Create a Research Memory File

Create `memory/research_trends_portfolio.md`:

```markdown
---
name: portfolio_research_trends
description: Accumulated portfolio research findings across multiple market cycles
metadata:
  type: reference
---

## Established Trends (Consistent Across ≥2 Research Cycles)

### AI Engineering Skills
- LLM prompt engineering: Emerging consistently since 05-2026
- RAG systems: High demand both freelance (€45-70/hr) and hiring (50+ postings)
- Agent frameworks: Strong GitHub momentum + growing freelance demand
- Vector databases: Stable high demand in hiring, growing in freelance

### Market Patterns
- European AI talent concentration: Germany, UK, France
- AI roles shift from "ML Engineer" to "LLM Engineer" or "AI Systems Engineer"
- Freelance rates: €50-100/hr for specialized AI work, growing YoY

### Portfolio Recommendation Confidence
- Multi-agent workflow automation: HIGH (hiring + freelance + GitHub signals)
- RAG evaluation frameworks: MEDIUM (hiring + GitHub, but narrow freelance appeal)
- Agentic workflow tools: HIGH (consistent cross-signal evidence)

## Research Methodology Notes
- Timeframe bias: Most data skews last 6 months
- Geographic bias: European data is strongest; global data more sparse
- Platform bias: LinkedIn/Upwork heavily overweight hiring vs. market reality
- Recency requirement: Always filter for data < 6 months old
```

### Step 2: Save to Your Memory System

Place this in your Claude Code memory folder so it loads automatically in future conversations. Claude Code will then reference accumulated research trends when you ask for portfolio advice.

---

## Example: Delta Research Workflow

Here's how to use archives for incremental research:

### First Research Run (19-07-2026)
1. Run `/portfolio-planner`
2. Get: `portfolio-report-2026-07-19.md` + `data/research_results_19_07_2026.md`
3. Action: Build the recommended portfolio project

### Second Research Run (3 months later, 19-10-2026)
1. Run `/portfolio-planner` again
2. Before starting, provide previous archive:
   ```
   Load data/research_results_19_07_2026.md as baseline. 
   Research what's changed in the last 3 months. Flag:
   - New trends that weren't present before
   - Skills that have accelerated or cooled
   - Markets where demand has shifted
   - Competitive landscape changes
   ```
3. Get: New `portfolio-report-2026-10-19.md` + `data/research_results_19_10_2026.md`
4. Compare: NotebookLM can highlight the delta between the two archives

---

## Troubleshooting

**Q: My research archive is too large for NotebookLM**

A: NotebookLM has file size limits. If your archive exceeds 100KB:
- Split by geography or category
- Create separate archives for "market trends" vs. "hiring data"
- Reference `research_results_19_07_2026.md` in your NotebookLM instructions: "This is a research archive with the following structure..." and upload specific sections

**Q: I'm not sure what to tag each finding with**

A: Use this heuristic:
- What *type* of source is this? (hiring board, GitHub, freelance platform, market report) → That's your primary tag
- What *decision* does this help with? (what to build, what skill to learn, where to focus) → Add secondary tags
- Example: "Upwork postings for RAG projects at €50/hr" → `#freelance-demand`, `#skills`, `#projects`

**Q: Should I keep old archives or delete them?**

A: **Keep all of them.** They're valuable for:
- Trend analysis (which skills are accelerating?)
- Confidence building (are findings consistent over time?)
- Timing decisions (when did this trend start?)
- Historical context (why did I make that decision back in May?)

---

## Next Steps

1. **Run `/portfolio-planner`** and check that both outputs are generated
2. **Upload the research archive to NotebookLM** and explore it
3. **Create a research memory file** linking to your most important findings
4. **Plan incremental research** — set a reminder to re-run `/portfolio-planner` every 3 months

Your research archives will become increasingly valuable as they accumulate—they're the foundation for making confident, evidence-based portfolio decisions.
