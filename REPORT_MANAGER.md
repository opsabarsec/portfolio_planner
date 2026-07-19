# Report Manager Documentation

The portfolio planner now includes a `ReportManager` utility that automatically saves all research results and reports to the folder specified in your `.env` file.

## Configuration

The output folder is controlled by the `OUTPUT_FOLDER` environment variable in `.env`:

```env
OUTPUT_FOLDER = "./data"
```

- If `OUTPUT_FOLDER` is set, reports are saved there
- If not set, defaults to `./data`
- The folder is created automatically if it doesn't exist

## Usage

### 1. Command Line

Run the portfolio planner script directly:

```bash
python run_portfolio_planner.py
```

This will:
- Load your profile from `data/marco_ai_profile_llm_ready.md`
- Generate a portfolio strategy report
- Save it to the folder specified in `.env` (default: `./data`)
- Display the output folder location and list of saved reports

### 2. Python Code

Import and use `ReportManager` in your Python code:

```python
from utils.report_manager import ReportManager

# Initialize manager (reads .env automatically)
manager = ReportManager()

# Save a markdown report
filepath = manager.save_report(
    report_name="my_research",
    content="# My Report\nContent here...",
    report_type="md"
)
print(f"Saved to: {filepath}")

# Save a JSON report
json_data = {
    "findings": ["Finding 1", "Finding 2"],
    "timestamp": "2026-07-19"
}
filepath = manager.save_json_report("research_findings", json_data)

# Save full research results
results = {
    "timeframe": "Last 6 months",
    "build_time": "2–4 weeks",
    "opportunity_type": "Freelance clients",
    "freelance_market": {"...": "..."},
    "eu_hiring_market": {"...": "..."},
    "github_trends": {"...": "..."},
}
filepath = manager.save_research_results(results)

# Save portfolio strategy
strategy = """# Portfolio Strategy\n\nContent..."""
filepath = manager.save_portfolio_strategy(strategy)

# List all saved reports
reports = manager.list_reports()
for report in reports:
    print(f"  - {report}")

# Get output folder path
output_folder = manager.get_output_folder()
print(f"Output folder: {output_folder}")
```

## Report Formats

### Markdown Reports
- Use `save_report()` with `report_type="md"`
- Ideal for human-readable research summaries, strategy documents

### JSON Reports
- Use `save_json_report()` or `save_report()` with `report_type="json"`
- Ideal for structured data, research results that need programmatic access
- Useful for feeding into other tools or dashboards

### Text Reports
- Use `save_report()` with `report_type="txt"`
- Ideal for raw data or logs

## File Naming

Reports are saved with timestamps to avoid overwriting:

```
report_name_YYYYMMDD_HHMMSS.ext
```

Example:
- `portfolio_strategy_report_20260719_231024.md`
- `freelance_market_research_20260719_230500.md`
- `research_findings_20260719_230000.json`

## Directory Structure

```
portfolio_planner/
├── .env                          # Configuration (OUTPUT_FOLDER)
├── requirements.txt              # Dependencies (python-dotenv)
├── run_portfolio_planner.py      # Main entry point
├── REPORT_MANAGER.md            # This file
├── utils/
│   ├── __init__.py
│   └── report_manager.py        # ReportManager class
└── data/                        # Output folder (configured in .env)
    ├── portfolio_strategy_report_*.md
    ├── freelance_market_research_*.md
    ├── eu_hiring_market_research_*.md
    └── github_trends_research_*.md
```

## Integration with Portfolio Planner Skill

When the `/portfolio-planner` skill runs:

1. Research agents generate outputs (Freelance, EU Hiring, GitHub trends)
2. Results are synthesized into a comprehensive strategy
3. All reports are automatically saved to `OUTPUT_FOLDER` via `ReportManager`
4. Reports remain available for review, sharing, or further analysis

## Example Workflow

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Update .env with your preferred output folder (optional)
# OUTPUT_FOLDER = "./reports"

# 3. Run the portfolio planner
python run_portfolio_planner.py

# 4. Check the generated reports
ls -la ./data/  # or ./reports/ if you changed it

# 5. Review the strategy report in your IDE or text editor
# The report will be in: ./data/portfolio_strategy_report_YYYYMMDD_HHMMSS.md
```

## Notes

- The `ReportManager` class is thread-safe for concurrent report writing
- All encoding is UTF-8 for cross-platform compatibility
- JSON output is formatted with 2-space indentation for readability
- Timestamps use 24-hour format (HH:MM:SS) in UTC
