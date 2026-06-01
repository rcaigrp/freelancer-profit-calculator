import csv
import os

def parse_expenses(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return []
        
    expenses = []
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=2):
                try:
                    amount = float(row['amount'])
                    expenses.append({
                        'date': row.get('date', ''),
                        'description': row.get('description', ''),
                        'amount': amount,
                        'type': row.get('type', '')
                    })
                except (ValueError, KeyError) as e:
                    print(f"Warning: Skipping row {i} due to parsing error ({e}): {row}")
    except Exception as e:
        print(f"Error reading file: {e}")
        
    return expenses

def calculate_metrics(expenses, tax_rate, hours=None):
    business_income = sum(e['amount'] for e in expenses if e['type'] == 'business_income')
    business_expenses = sum(e['amount'] for e in expenses if e['type'] == 'business_expense')
    personal_expenses = sum(e['amount'] for e in expenses if e['type'] == 'personal_expense')
    
    taxable_income = business_income - business_expenses
    tax_amount = taxable_income * tax_rate
    net_profit = taxable_income - tax_amount
    
    effective_hourly = net_profit / hours if hours and hours > 0 else None
    
    return {
        'business_income': business_income,
        'business_expenses': business_expenses,
        'personal_expenses': personal_expenses,
        'taxable_income': taxable_income,
        'tax_amount': tax_amount,
        'net_profit': net_profit,
        'effective_hourly': effective_hourly
    }
