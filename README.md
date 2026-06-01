# Freelancer-Profit-Calculator

A CLI tool that calculates true freelancer profitability by analyzing income, expenses, and hours to determine effective hourly rate, tax estimates, and project margins.

## What it does
Scans your transaction history, separates income from expenses, tracks billable hours, and outputs a clear profitability report so you stop underpricing your work.

## Installation
```bash
pip install rich
```

## Usage
```bash
python main.py --data data/transactions.csv
python main.py --data data/transactions.csv --tax-rate 30
```

## Configuration
- `--data`: Path to your transaction CSV file (required). CSV must include columns: `date`, `type`, `category`, `amount`, `hours`, `project`.
- `--tax-rate`: Optional custom tax rate percentage (default: 25%).
- Output: Formatted terminal table with project breakdown, total hours, net profit, effective hourly rate, and estimated taxes.
- Logs: Success/failure entries written to `logs/profit_log.txt`.