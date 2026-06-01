import pytest
import csv
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from main import read_csv, calculate_profit

TEST_DATA = [
    ["date", "description", "category", "amount", "type"],
    ["2024-01-01", "Client A", "Services", "1000", "income"],
    ["2024-01-02", "Software", "Tools", "50", "expense"],
    ["2024-01-03", "Client B", "Services", "500", "income"],
    ["2024-01-04", "Rent", "Office", "200", "expense"],
]

@pytest.fixture
def csv_file(tmp_path):
    f = tmp_path / "test.csv"
    with open(f, "w", newline="") as file:
        writer = csv.writer(file)
        for row in TEST_DATA:
            writer.writerow(row)
    return str(f)

def test_read_csv_valid_data(csv_file):
    income, expenses, categories = read_csv(csv_file)
    assert income == 1500.0
    assert expenses == 250.0
    assert categories == {"Tools": 50.0, "Office": 200.0}

def test_read_csv_invalid_amount():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("date,description,category,amount,type\n2024-01-01,Test,,abc,expense\n")
        f.flush()
        income, expenses, categories = read_csv(f.name)
        assert income == 0.0
        assert expenses == 0.0
    os.unlink(f.name)

def test_calculate_profit():
    income, expenses, categories = 1500.0, 250.0, {"Tools": 50.0, "Office": 200.0}
    report = calculate_profit(income, expenses, 0.25, categories)
    assert report["gross_profit"] == 1500.0
    assert report["total_expenses"] == 250.0
    assert report["net_profit"] == 1250.0
    assert report["estimated_tax"] == 312.5
    assert report["take_home_pay"] == 937.5

def test_calculate_profit_negative_net():
    income, expenses, categories = 100.0, 200.0, {}
    report = calculate_profit(income, expenses, 0.25, categories)
    assert report["estimated_tax"] == 0.0
    assert report["take_home_pay"] == -100.0