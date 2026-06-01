import unittest
import sys
import os
import json
import tempfile
import csv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.calculator import read_csv, calculate
from src.formatter import format_json, format_csv

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.sample_incomes = [
            {'date': '2023-01-01', 'amount': 1000, 'description': 'Job 1'},
            {'date': '2023-01-02', 'amount': 500, 'description': 'Job 2'}
        ]
        self.sample_expenses = [
            {'date': '2023-01-01', 'amount': 200, 'description': 'Expense 1'},
            {'date': '2023-01-02', 'amount': 100, 'description': 'Expense 2'}
        ]

    def test_calculation_logic(self):
        result = calculate(self.sample_incomes, self.sample_expenses, 0.25)
        self.assertEqual(result['total_income'], 1500)
        self.assertEqual(result['total_expenses'], 300)
        self.assertEqual(result['gross_profit'], 1200)
        self.assertEqual(result['tax_liability'], 300)
        self.assertEqual(result['net_profit'], 900)

    def test_csv_parsing(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'amount', 'description'])
            writer.writerow(['2023-01-01', '100', 'Test'])
            temp_path = f.name
        
        data = read_csv(temp_path)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['amount'], 100.0)
        os.unlink(temp_path)

class TestFormatter(unittest.TestCase):
    def test_json_format(self):
        data = {'key': 'value'}
        output = format_json(data)
        self.assertIn('key', output)

    def test_csv_format(self):
        data = {'key': 'value'}
        output = format_csv(data)
        self.assertIn('key', output)

if __name__ == '__main__':
    unittest.main()