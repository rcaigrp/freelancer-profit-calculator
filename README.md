# Freelancer-Profit-Calculator

A CLI tool that turns your raw transaction CSVs into clear profit reports, helping you understand your true take-home pay and avoid tax surprises.

## What it does
Calculates net profit, tracks expenses by category, and estimates tax liability from a simple CSV file. Designed for freelancers who already track income/expenses in spreadsheets.

## Installation
No external dependencies required. Uses Python 3.11+ standard library only.
```bash
# Clone or copy the project directory
cd Freelancer-Profit-Calculator
```

## Usage
1. Prepare your CSV (`data/transactions.csv`) with columns: `date, description, amount, category`
2. Run the calculator:
```bash
python main.py --input data/transactions.csv --tax-rate 25
```
3. View the summary in your terminal.

## Configuration
- `--input`: Path to your transaction CSV file.
- `--tax-rate`: Estimated tax percentage (default: 25).
- `--output`: Path to save the detailed report (e.g., `report.csv`).

## Troubleshooting
- **CSV Format Error**: Ensure your CSV has exactly these headers: `date, description, amount, category`.
- **Missing Data**: Rows with missing amounts are skipped with a warning.
