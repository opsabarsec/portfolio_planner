"""
Report manager for portfolio planner.
Reads OUTPUT_FOLDER from .env and saves research reports.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv


class ReportManager:
    """Manages saving research reports to configured output folder."""

    def __init__(self, env_path: str = ".env", default_output: str = "./data"):
        """
        Initialize report manager.

        Args:
            env_path: Path to .env file (relative to current working directory)
            default_output: Default output folder if OUTPUT_FOLDER not in .env
        """
        self.env_path = env_path
        self.default_output = default_output
        self.output_folder = self._get_output_folder()
        self._ensure_output_folder()

    def _get_output_folder(self) -> Path:
        """Read OUTPUT_FOLDER from .env, fallback to default."""
        # Load environment variables from .env
        if os.path.exists(self.env_path):
            load_dotenv(self.env_path)

        output_dir = os.getenv("OUTPUT_FOLDER", self.default_output)
        return Path(output_dir).resolve()

    def _ensure_output_folder(self) -> None:
        """Create output folder if it doesn't exist."""
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def save_report(self, report_name: str, content: str, report_type: str = "md") -> Path:
        """
        Save a text report (markdown or plain text).

        Args:
            report_name: Name of the report (without extension)
            content: Report content
            report_type: File extension ('md', 'txt', or 'json')

        Returns:
            Path to saved file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{report_name}_{timestamp}.{report_type}"
        filepath = self.output_folder / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        return filepath

    def save_json_report(self, report_name: str, data: dict) -> Path:
        """
        Save a JSON report.

        Args:
            report_name: Name of the report (without extension)
            data: Dictionary to save as JSON

        Returns:
            Path to saved file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{report_name}_{timestamp}.json"
        filepath = self.output_folder / filename

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return filepath

    def save_research_results(self, results: dict) -> Path:
        """
        Save all research results in a structured format.

        Args:
            results: Dictionary containing freelance, hiring, and github research

        Returns:
            Path to saved consolidated report
        """
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "research_timeframe": results.get("timeframe", "Last 6 months"),
            "build_time": results.get("build_time", "2–4 weeks"),
            "opportunity_type": results.get("opportunity_type", "Freelance clients"),
            "freelance_market": results.get("freelance_market"),
            "eu_hiring_market": results.get("eu_hiring_market"),
            "github_trends": results.get("github_trends"),
        }

        return self.save_json_report("portfolio_research_results", report_data)

    def save_portfolio_strategy(self, strategy_content: str) -> Path:
        """
        Save the final portfolio strategy report.

        Args:
            strategy_content: Full markdown content of strategy report

        Returns:
            Path to saved file
        """
        return self.save_report("portfolio_strategy_report", strategy_content, "md")

    def get_output_folder(self) -> Path:
        """Get the configured output folder path."""
        return self.output_folder

    def list_reports(self) -> list:
        """List all saved reports in output folder."""
        if not self.output_folder.exists():
            return []
        return sorted([f.name for f in self.output_folder.glob("*")])


def main():
    """Example usage."""
    manager = ReportManager()

    print(f"Output folder: {manager.get_output_folder()}")
    print(f"Reports saved to: {manager.output_folder}")

    # Example: save a sample report
    sample_report = """
# Portfolio Strategy Report

Generated: 2026-07-19

## Executive Summary
This is a sample portfolio strategy report.
"""

    filepath = manager.save_portfolio_strategy(sample_report)
    print(f"Saved report to: {filepath}")

    print("\nExisting reports:")
    for report in manager.list_reports():
        print(f"  - {report}")


if __name__ == "__main__":
    main()
