# Freelancer-Profit-Calculator

A fast, offline CLI tool that turns your income and expense CSVs into clear profit reports with tax estimates.

## What It Does
Freelancers often confuse gross revenue with take-home pay. This tool calculates your true net profit after expenses and taxes, so you can set aside the right amount and avoid cash-flow surprises.

## Installation
No external dependencies required. Works out of the box with Python 3.11+.

```bash
# Clone or download the project
cd Freelancer-Profit-Calculator

# Verify Python version
python3 --version
```

## Usage Examples

### Basic Profit Report
```bash
python src/main.py --income data/sample_incomes.csv --expenses data/sample_expenses.csv --tax-rate 0.25
```

### Save to JSON
```bash
python src/main.py --income data/sample_incomes.csv --expenses data/sample_expenses.csv --tax-rate 0.25 --output report.json
```

### Output to CSV
```bash
python src/main.py --income data/sample_incomes.csv --expenses data/sample_expenses.csv --tax-rate 0.25 --output report.csv --format csv
```

## Configuration
- `--income`: Path to income CSV (columns: date, amount, description)
- `--expenses`: Path to expense CSV (columns: date, amount, description)
- `--tax-rate`: Percentage of gross profit to set aside for taxes (e.g., 0.25 for 25%)
- `--output`: Path for the output file (defaults to terminal print)
- `--format`: Output format: `json` (default) or `csv`

## Troubleshooting
- **CSV errors**: Ensure your files have headers matching `date`, `amount`, `description`. Extra columns are ignored.
- **Missing files**: The tool will print a clear error if files aren't found.
- **Python version**: Requires Python 3.11 or newer.