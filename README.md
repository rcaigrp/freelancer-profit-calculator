# Freelancer-Profit-Calculator

A Python CLI tool to track income, expenses, and taxes, helping freelancers calculate true net profit.

## Installation
```bash
pip install freelancer-profit-calculator
```
Or run directly from source:
```bash
git clone <repo-url>
cd Freelancer-Profit-Calculator
pip install -r requirements.txt
```

## Usage
1. Prepare a `data.csv` with columns: `date, type, description, amount`
2. Run the tool:
```bash
python main.py --input data.csv
```
3. View the profit breakdown and tax estimates in your terminal.

## Configuration
- `--tax-rate`: Set custom tax rate (e.g., `--tax-rate 30`)
- `--output`: Save report to file (e.g., `--output report.json`)
