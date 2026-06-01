# Freelancer-Profit-Calculator

## What the app does
A CLI tool that calculates freelancer profit margins, effective hourly rates, and estimated tax liabilities based on CSV imports of revenue and expenses.

## Installation/setup steps
1. Ensure Python 3.11+ is installed.
2. Clone or download the project.
3. Install dependencies: `pip install -r requirements.txt` (uses only standard library modules: `csv`, `datetime`, `argparse`, `os`).
4. Create a `data/` directory and place your `income_expenses.csv` file there.

## Usage examples
Calculate profit with a custom tax rate:
```bash
python main.py --data data/income_expenses.csv --tax-rate 0.30
```
View help:
```bash
python main.py --help
```

## Configuration
- `--data`: Path to the CSV file containing transactions.
- `--tax-rate`: Estimated tax rate (decimal, e.g., 0.25 for 25%). Defaults to 0.25.
- `--hours`: Total billable hours worked (optional, calculates effective hourly rate).
- `data/income_expenses.csv`: Expected columns: `date`, `type` (income/expense), `amount`, `description`.
