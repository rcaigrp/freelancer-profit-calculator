import csv

def read_csv(path):
    data = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip rows with missing amount
            if 'amount' not in row or not row['amount']:
                continue
            try:
                row['amount'] = float(row['amount'])
            except ValueError:
                continue
            data.append(row)
    return data

def calculate(incomes, expenses, tax_rate):
    total_income = sum(row['amount'] for row in incomes)
    total_expenses = sum(row['amount'] for row in expenses)
    gross_profit = total_income - total_expenses
    tax = gross_profit * tax_rate
    net_profit = gross_profit - tax
    return {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'gross_profit': gross_profit,
        'tax_rate': tax_rate,
        'tax_liability': tax,
        'net_profit': net_profit
    }