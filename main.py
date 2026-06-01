import click
import csv
import json
import sys
import os

# Ensure src/ is in path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from calculator import read_csv, calculate_metrics

@click.command()
@click.option('--input', 'csv_path', required=True, help='Path to CSV file with income/expense data')
@click.option('--tax-rate', 'tax_rate', default=25.0, type=float, help='Tax rate percentage (default 25)')
@click.option('--hours', 'hours', default=0.0, type=float, help='Hours worked for hourly rate calculation')
@click.option('--output', 'output_path', default=None, help='Path to save report (JSON format)')
def main(csv_path, tax_rate, hours, output_path):
    try:
        data = read_csv(csv_path)
        incomes = [row for row in data if row.get('type', '').lower() == 'income']
        expenses = [row for row in data if row.get('type', '').lower() == 'expense']
        
        metrics = calculate_metrics(incomes, expenses, tax_rate, hours)
        
        report = {
            "Total Income": metrics.total_income,
            "Total Expenses": metrics.total_expenses,
            "Net Profit": metrics.net_profit,
            "Tax Rate": f"{metrics.tax_rate}%",
            "Tax Liability": metrics.tax_liability,
            "Hourly Rate": metrics.hourly_rate
        }
        
        click.echo("\n=== Freelancer Profit Calculator ===")
        click.echo(f"Total Income:      ${metrics.total_income:,.2f}")
        click.echo(f"Total Expenses:    ${metrics.total_expenses:,.2f}")
        click.echo(f"Net Profit:        ${metrics.net_profit:,.2f}")
        click.echo(f"Tax Rate:          {metrics.tax_rate}%")
        click.echo(f"Tax Liability:     ${metrics.tax_liability:,.2f}")
        if metrics.hourly_rate > 0:
            click.echo(f"Hourly Rate:       ${metrics.hourly_rate:,.2f}")
        
        if output_path:
            with open(output_path, 'w') as f:
                json.dump(report, f, indent=2)
            click.echo(f"\nReport saved to {output_path}")
            
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
