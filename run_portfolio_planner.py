#!/usr/bin/env python3
"""
Portfolio Planner Runner
Executes portfolio planning research and saves reports to configured output folder.
"""

import sys
import json
from pathlib import Path
from utils.report_manager import ReportManager


class PortfolioPlanner:
    """Main portfolio planner coordinator."""

    def __init__(self, profile_path: str = "data/marco_ai_profile_llm_ready.md"):
        """Initialize planner with profile."""
        self.manager = ReportManager()
        self.profile_path = Path(profile_path)
        self.research_results = {}

    def load_profile(self) -> str:
        """Load and return user profile."""
        if not self.profile_path.exists():
            raise FileNotFoundError(f"Profile not found at {self.profile_path}")

        with open(self.profile_path, "r", encoding="utf-8") as f:
            return f.read()

    def save_research_data(self, freelance_report: str, hiring_report: str, github_report: str) -> None:
        """
        Save individual research reports.

        Args:
            freelance_report: Freelance market research (markdown)
            hiring_report: EU hiring market research (markdown)
            github_report: GitHub trends research (markdown)
        """
        self.manager.save_report("freelance_market_research", freelance_report, "md")
        self.manager.save_report("eu_hiring_market_research", hiring_report, "md")
        self.manager.save_report("github_trends_research", github_report, "md")

    def save_strategy_report(self, strategy: str) -> Path:
        """Save final portfolio strategy report."""
        return self.manager.save_portfolio_strategy(strategy)

    def get_output_folder(self) -> Path:
        """Return output folder path."""
        return self.manager.get_output_folder()


def create_sample_strategy_report() -> str:
    """Create a sample portfolio strategy report (for demonstration)."""
    return """# Personalized Portfolio Strategy: Marco Berta

## Executive Summary

Over the next 6–12 months, build a **single, cohesive flagship project** that signals expertise across freelance, hiring, and open-source communities. Focus on **compliance-auditable agentic RAG**—a narrow, high-value niche where your Actemium + CHAI experience directly translates to client and hiring manager needs.

**Geography focus**: EU-centric market research emphasizes compliance, GDPR, and regulated industries—Marco's existing experience is a major asset.

## Recommended Primary Project: Compliance-Aware Agentic RAG System with MCP Integration

**Scope**: 2–4 weeks (40–80 hours), Python + FastAPI + Docker

### What you'll build:
1. FastAPI backend for regulatory document ingestion
2. MCP-enabled agent orchestration for dynamic retrieval strategies
3. Multi-agent workflow with subject-matter-specific sub-agents
4. Compliance audit layer with decision trails
5. Docker containerized deployment ready for production

### Why this project:
- **Freelance positioning**: Directly addresses multi-agent orchestration niche (£1,500–£20K+ per project)
- **Hiring signal**: Demonstrates production RAG hardship, end-to-end delivery, multi-agent orchestration
- **Open-source momentum**: Reference MCP server for agentic retrieval control with minimal competition
- **Portfolio narrative**: Extends Actemium + CHAI case studies into reusable platform

## Implementation Roadmap (2–4 Weeks)

### Week 1: MVP (Core Agentic RAG)
- FastAPI skeleton + Pydantic schemas
- Document ingestion + hybrid RAG
- Multi-agent router
- Basic audit trail logging

### Week 2: MCP Integration + Compliance
- MCP server scaffolding
- Compliance rule engine
- Sub-agent specialization
- Docker containerization

### Week 3–4: Polish + Documentation
- Production-ready error handling
- End-to-end test scenario
- README, architecture diagram, deployment guide
- GitHub repo submission to MCP registry

## Market Positioning & Pricing

**Freelance positioning**: "Compliance-auditable AI systems. I build multi-agent RAG for regulatory and financial workflows."

**Freelance rate target**: €80–€150/hr or £1,500–£5,000 per project

**Hiring positioning**: "AI Platform Engineer with production agentic RAG and MCP infrastructure expertise."

**Target hiring roles**: Senior AI Platform Engineer, RAG/LLM Infrastructure Engineer (€80k–€130k range in EU)

## Next Steps (This Month)

1. Fork or reference LangGraph + MCP examples to scaffold architecture
2. Publish a 2-min demo showing the agent triage workflow
3. Write the README before writing code
4. Target ship date: mid-August 2026
5. Pitch to 3 freelance prospects during build week 3–4

---

Generated: 2026-07-19
"""


def main():
    """Run portfolio planner and save reports."""
    print("🚀 Portfolio Planner Runner")
    print("-" * 60)

    try:
        planner = PortfolioPlanner()
        output_folder = planner.get_output_folder()

        print(f"✓ Output folder: {output_folder}")

        # Load profile
        profile = planner.load_profile()
        print(f"✓ Profile loaded from: {planner.profile_path}")

        # Create sample strategy report (in real usage, this would come from agent results)
        strategy = create_sample_strategy_report()

        # Save reports
        strategy_path = planner.save_strategy_report(strategy)
        print(f"✓ Strategy report saved to: {strategy_path}")

        # Display summary
        print("\n" + "=" * 60)
        print("Reports saved to output folder:")
        print("=" * 60)
        for report in sorted(planner.manager.list_reports()):
            print(f"  📄 {report}")

        print(f"\nOutput folder: {output_folder}")
        return 0

    except FileNotFoundError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
