import argparse
import json
import sys
import os
from calculator import parse_expenses, calculate_metrics

def format_output(metrics, hours):
    print("=" * 45)
    print("Freelancer Profit Calculator")
    print("=" * 45)
    print(f"Business Income:      ${metrics['business_income']:,.2f}")
    print(f"Business Expenses:    ${metrics['business_expenses']:,.2f}")
    print(f"Personal Expenses:    ${metrics.get('personal_expenses', 0.0):,.2f}")
    print("-" * 45)
    print(f"Taxable Income:       ${metrics['taxable_income']:,.2f}")
    print(f"Estimated Tax (25%):  ${metrics['tax_liability']:,.2f}")
    print("-" * 45)
    print(f"Net Profit:           ${metrics['net_profit']:,.2f}")
    print(f"Hourly Rate:          ${metrics['hourly_rate']:,.2f}")
    print(f"Total Hours Worked:   {hours}")
    print("=" * 45)

def main():
    parser = argparse.ArgumentParser(description="Freelancer Profit Calculator")
    parser.add_argument('--input', required=True, help='Path to CSV file')
    parser.add_argument('--tax-rate', type=float, default=25, help='Tax rate percentage')
    parser.add_argument('--output', help='Path to save JSON report')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File not found at {args.input}")
        sys.exit(1)

    incomes, expenses, hours = parse_expenses(args.input)
    metrics = calculate_metrics(incomes, expenses, args.tax_rate, hours)
    format_output(metrics, hours)

    if args.output:
        report = {**metrics, 'hours': hours}
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\nReport saved to {args.output}")

if __name__ == '__main__':
    main()
