import argparse
from calculator import parse_expenses, calculate_metrics

def format_output(metrics, hours):
    print("=" * 45)
    print("Freelancer Profit Calculator")
    print("=" * 45)
    print(f"Business Income:      ${metrics['business_income']:,.2f}")
    print(f"Business Expenses:    ${metrics['business_expenses']:,.2f}")
    print(f"Personal Expenses:    ${metrics['personal_expenses']:,.2f}")
    print("-" * 45)
    print(f"Taxable Income:       ${metrics['taxable_income']:,.2f}")
    print(f"Tax Amount:           ${metrics['tax_amount']:,.2f}")
    print(f"Net Profit:           ${metrics['net_profit']:,.2f}")
    if hours is not None:
        print(f"Effective Hourly Rate:${metrics['effective_hourly']:,.2f}")
    print("=" * 45)

def main():
    parser = argparse.ArgumentParser(
        description="Calculate freelancer profit, taxes, and effective hourly rate."
    )
    parser.add_argument('--input', default='data/expenses.csv', help='Path to expenses CSV')
    parser.add_argument('--tax-rate', type=float, default=0.2, help='Tax rate (e.g., 0.2 for 20%)')
    parser.add_argument('--hours', type=float, default=None, help='Billable hours for effective rate calculation')
    
    args = parser.parse_args()
    
    print(f"Reading expenses from: {args.input}")
    expenses = parse_expenses(args.input)
    
    if not expenses:
        print("No valid expenses found. Exiting.")
        return
        
    metrics = calculate_metrics(expenses, args.tax_rate, args.hours)
    format_output(metrics, args.hours)

if __name__ == '__main__':
    main()
