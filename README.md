# Freelancer-Profit-Calculator

A simple Python CLI tool to calculate your net profit, estimated taxes, and take-home pay from a CSV of income and expenses.

## Installation
No external dependencies required. Uses Python 3.11+ standard library (`csv`, `argparse`, `json`).

```bash
git clone <repo-url>
cd Freelancer-Profit-Calculator
```

## Usage
Prepare a CSV file (`data/sample.csv`) with columns: `date,description,category,amount,type` (type is `income` or `expense`).

Run the calculator:
```bash
python main.py --input data/sample.csv
```

To save a JSON report:
```bash
python main.py --input data/sample.csv --output report.json
```

## Configuration
- `--tax-rate`: Estimated tax percentage (default: 25%). Example: `--tax-rate 0.30` for 30%.
- `--output`: Path to save JSON report. Omit to print to console.

## Troubleshooting
- **Missing columns**: Ensure your CSV has `date,description,category,amount,type` headers.
- **Invalid amounts**: Rows with non-numeric amounts are skipped with a warning.
- **Negative profit**: Tax is calculated as $0 if net profit is negative.