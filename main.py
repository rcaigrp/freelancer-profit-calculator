import click
import os
from calculator import parse_expenses, calculate_metrics

@click.command()
@click.option('--income', required=True, type=float, help='Total income')
@click.option('--expenses', required=True, type=click.Path(exists=True), help='Path to expenses CSV')
@click.option('--tax-rate', default=0.0, type=float, help='Tax rate percentage')
@click.option('--hours', default=0.0, type=float, help='Hours worked')
def main(income, expenses, tax_rate, hours):
    """Freelancer Profit Calculator"""
    try:
        expenses_list = parse_expenses(expenses)
        metrics = calculate_metrics(income, expenses_list, tax_rate, hours)
        
        click.echo(f"Income: ${metrics.income:,.2f}")
        click.echo(f"Expenses: ${metrics.total_expenses:,.2f}")
        click.echo(f"Net Profit: ${metrics.net_profit:,.2f}")
        if metrics.hours > 0:
            click.echo(f"Hourly Rate: ${metrics.hourly_rate:,.2f}/hr")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.exceptions.Exit(1)

if __name__ == '__main__':
    main()
