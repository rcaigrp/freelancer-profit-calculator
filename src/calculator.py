import csv
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class FinancialMetrics:
    total_income: float
    total_expenses: float
    net_profit: float
    tax_rate: float
    tax_liability: float
    hourly_rate: float

def read_csv(path: str) -> List[Dict]:
    data = []
    try:
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if 'amount' not in row or not row['amount']:
                    continue
                try:
                    row['amount'] = float(row['amount'])
                except ValueError:
                    continue
                data.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {path}")
    return data

def calculate_metrics(incomes: List[Dict], expenses: List[Dict], tax_rate: float, hours_worked: float = 0.0) -> FinancialMetrics:
    total_income = sum(item['amount'] for item in incomes)
    total_expenses = sum(item['amount'] for item in expenses)
    net_profit = total_income - total_expenses
    tax_liability = net_profit * (tax_rate / 100.0)
    
    # Handle zero hours to avoid division by zero
    hourly_rate = (total_income / hours_worked) if hours_worked > 0 else 0.0
    
    return FinancialMetrics(
        total_income=total_income,
        total_expenses=total_expenses,
        net_profit=net_profit,
        tax_rate=tax_rate,
        tax_liability=tax_liability,
        hourly_rate=hourly_rate
    )
