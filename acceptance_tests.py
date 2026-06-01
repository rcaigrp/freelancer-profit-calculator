import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calculator import parse_expenses, calculate_metrics

def create_csv(content):
    f = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    f.write(content)
    f.close()
    return f.name

def test_parse_expenses():
    csv_content = "date,description,amount,type\n2023-01-01,Client A,1000,business_income\n2023-01-02,Software,200,business_expense\n2023-01-03,Groceries,100,personal_expense"
    path = create_csv(csv_content)
    try:
        expenses = parse_expenses(path)
        assert len(expenses) == 3
        assert expenses[0]['amount'] == 1000
        assert expenses[0]['type'] == 'business_income'
        assert expenses[1]['type'] == 'business_expense'
        assert expenses[2]['type'] == 'personal_expense'
    finally:
        os.unlink(path)

def test_calculate_metrics():
    expenses = [
        {'amount': 1000, 'type': 'business_income'},
        {'amount': 200, 'type': 'business_expense'},
        {'amount': 100, 'type': 'personal_expense'}
    ]
    metrics = calculate_metrics(expenses, tax_rate=0.2, hours=40)
    assert metrics['business_income'] == 1000
    assert metrics['business_expenses'] == 200
    assert metrics['personal_expenses'] == 100
    assert metrics['taxable_income'] == 800
    assert metrics['tax_amount'] == 160
    assert metrics['net_profit'] == 640
    assert metrics['effective_hourly'] == 16.0

def test_calculate_metrics_no_hours():
    expenses = [{'amount': 1000, 'type': 'business_income'}]
    metrics = calculate_metrics(expenses, tax_rate=0.2, hours=None)
    assert metrics['effective_hourly'] is None

def test_parse_expenses_skips_malformed():
    csv_content = "date,description,amount,type\n2023-01-01,Client A,not_a_number,business_income\n2023-01-02,Software,200,business_expense"
    path = create_csv(csv_content)
    try:
        expenses = parse_expenses(path)
        assert len(expenses) == 1
        assert expenses[0]['amount'] == 200
    finally:
        os.unlink(path)
