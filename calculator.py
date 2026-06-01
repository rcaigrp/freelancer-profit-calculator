import csv
from dataclasses import dataclass

@dataclass
class FinancialMetrics:
    income: float
    total_expenses: float
    gross_profit: float
    tax_deduction: float
    net_profit: float
    hours: float
    hourly_rate: float

def parse_expenses(filepath):
    expenses = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                amount = float(row.get('amount', 0))
                expenses.append(amount)
            except ValueError:
                continue
    return expenses

def calculate_metrics(income, expenses, tax_rate, hours):
    total_expenses = sum(expenses)
    gross_profit = income - total_expenses
    tax_deduction = max(0, gross_profit * (tax_rate / 100))
    net_profit = max(0, gross_profit - tax_deduction)
    
    hourly_rate = 0
    if hours > 0:
        hourly_rate = net_profit / hours
        
    return FinancialMetrics(
        income=income,
        total_expenses=total_expenses,
        gross_profit=gross_profit,
        tax_deduction=tax_deduction,
        net_profit=net_profit,
        hours=hours,
        hourly_rate=hourly_rate
    )
