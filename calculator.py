import csv
import os

def parse_expenses(filepath):
    if not os.path.exists(filepath):
        return [], [], 0.0
        
    incomes = []
    expenses = []
    total_hours = 0.0
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    amount = float(row.get('amount', 0))
                    hours = float(row.get('hours', 0))
                    total_hours += hours
                    if row.get('type', '').lower() == 'income':
                        incomes.append({'amount': amount, 'hours': hours})
                    else:
                        expenses.append({'amount': amount, 'hours': hours})
                except (ValueError, KeyError):
                    continue
    except Exception as e:
        print(f"Error reading CSV: {e}")
        
    return incomes, expenses, total_hours

def calculate_metrics(incomes, expenses, tax_rate=25, total_hours=0.0):
    total_income = sum(i['amount'] for i in incomes)
    total_expenses = sum(e['amount'] for e in expenses)
    taxable_income = total_income - total_expenses
    tax_liability = max(0, taxable_income * (tax_rate / 100))
    net_profit = taxable_income - tax_liability
    
    hourly_rate = net_profit / total_hours if total_hours > 0 else 0.0
    
    return {
        'business_income': total_income,
        'business_expenses': total_expenses,
        'personal_expenses': 0.0,
        'taxable_income': taxable_income,
        'tax_liability': tax_liability,
        'net_profit': net_profit,
        'hourly_rate': hourly_rate
    }
