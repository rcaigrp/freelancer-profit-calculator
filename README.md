# Freelancer-Profit-Calculator

## What the app does
A dependency-free Python CLI tool that calculates your business income, expenses, taxable income, tax amount, net profit, and effective hourly rate from a simple CSV file. Designed for freelancers to quickly understand their financial health without accounting software.

## Installation/setup steps
No external packages are required. This tool uses only the Python standard library.
1. Ensure Python 3.11+ is installed on your system.
2. Clone this repository or download `main.py` and `data/expenses.csv`.
3. No `pip install` needed. Ready to run immediately.

## Usage examples
Run the tool by pointing it to your CSV file:
```bash
python main.py --input data/expenses.csv
```
Expected output:
```
=============================================
Freelancer Profit Calculator
=============================================
Business Income:      $1,800.00
Business Expenses:    $79.99
Personal Expenses:    $120.00
---------------------------------------------
Taxable Income:       $1,720.01
Tax Amount:           $430.00
Net Profit:           $1,290.01
Effective Hourly Rate:$32.25
=============================================
```

## Configuration
- `--input` (required): Path to your CSV file. Must contain columns: `date`, `type` (income/expense), `amount`, `hours`, `category`.
- `--tax-rate` (optional): Override the default 25% tax rate. Example: `--tax-rate 30`
- `--output` (optional): Save the report to a file instead of printing to terminal. Example: `--output report.txt`