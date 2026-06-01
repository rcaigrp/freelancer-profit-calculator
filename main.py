import argparse
import csv
import json
import os
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Freelancer Profit Calculator")
    parser.add_argument("--input", required=True, help="Path to income/expense CSV")
    parser.add_argument("--output", help="Path to output report JSON")
    parser.add_argument("--tax-rate", type=float, default=0.25, help="Tax rate (default 25%)")
    return parser.parse_args()

def read_csv(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    income = 0.0
    expenses = 0.0
    categories = {}
    
    with open(filepath, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                amount = float(row['amount'])
                row_type = row['type'].strip().lower()
                if row_type == 'income':
                    income += amount
                elif row_type == 'expense':
                    expenses += amount
                    cat = row.get('category', 'Uncategorized')
                    categories[cat] = categories.get(cat, 0) + amount
            except (ValueError, KeyError) as e:
                print(f"Warning: Skipping row due to invalid data: {row}")
                
    return income, expenses, categories

def calculate_profit(income, expenses, tax_rate, categories):
    gross_profit = income
    net_profit = income - expenses
    tax_amount = net_profit * tax_rate if net_profit > 0 else 0
    take_home = net_profit - tax_amount
    return {
        "gross_profit": round(gross_profit, 2),
        "total_expenses": round(expenses, 2),
        "net_profit": round(net_profit, 2),
        "estimated_tax": round(tax_amount, 2),
        "take_home_pay": round(take_home, 2),
        "expense_breakdown": {k: round(v, 2) for k, v in categories.items()}
    }

def main():
    args = parse_args()
    try:
        income, expenses, categories = read_csv(args.input)
        report = calculate_profit(income, expenses, args.tax_rate, categories)
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(report, f, indent=2)
            print(f"Report saved to {args.output}")
        else:
            print("\n--- Freelancer Profit Report ---")
            print(f"Gross Income: ${report['gross_profit']}")
            print(f"Total Expenses: ${report['total_expenses']}")
            print(f"Net Profit: ${report['net_profit']}")
            print(f"Estimated Tax ({args.tax_rate*100}%): ${report['estimated_tax']}")
            print(f"Take-Home Pay: ${report['take_home_pay']}")
            if categories:
                print("\nExpense Breakdown:")
                for cat, amt in categories.items():
                    print(f"  {cat}: ${amt}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()