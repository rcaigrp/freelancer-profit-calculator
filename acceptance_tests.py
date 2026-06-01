import sys
import os
import pytest
import json
import tempfile
import csv
from click.testing import CliRunner

# Fix import path for src/ modules
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from calculator import read_csv, calculate_metrics, FinancialMetrics
from main import main

class TestCalculatorLogic:
    def test_calculate_metrics(self):
        incomes = [{'amount': 1000}]
        expenses = [{'amount': 200}]
        metrics = calculate_metrics(incomes, expenses, 25.0, 10.0)
        assert metrics.total_income == 1000
        assert metrics.total_expenses == 200
        assert metrics.net_profit == 800
        assert metrics.tax_liability == 200
        assert metrics.hourly_rate == 100.0

    def test_criterion_2_handle_zero_hours(self):
        incomes = [{'amount': 1000}]
        expenses = [{'amount': 200}]
        metrics = calculate_metrics(incomes, expenses, 25.0, 0.0)
        assert metrics.hourly_rate == 0.0

    def test_criterion_1_csv_parsing(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'type', 'description', 'amount'])
            writer.writerow(['2023-01-01', 'Income', 'Client A', '1000'])
            writer.writerow(['2023-01-02', 'Expense', 'Software', '200'])
            f.flush()
            data = read_csv(f.name)
            assert len(data) == 2
            assert data[0]['amount'] == 1000
            os.unlink(f.name)

class TestCLICriteria:
    def test_criterion_3_tax_rate_output(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'type', 'description', 'amount'])
            writer.writerow(['2023-01-01', 'Income', 'Client A', '1000'])
            writer.writerow(['2023-01-02', 'Expense', 'Software', '200'])
            f.flush()
            runner = CliRunner()
            result = runner.invoke(main, ['--input', f.name, '--tax-rate', '30'])
            assert result.exit_code == 0
            assert 'Tax Rate:          30%' in result.output
            os.unlink(f.name)

    def test_criterion_4_summary_format(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'type', 'description', 'amount'])
            writer.writerow(['2023-01-01', 'Income', 'Client A', '1000'])
            writer.writerow(['2023-01-02', 'Expense', 'Software', '200'])
            f.flush()
            runner = CliRunner()
            result = runner.invoke(main, ['--input', f.name])
            assert result.exit_code == 0
            assert 'Net Profit:' in result.output
            assert 'Tax Liability:' in result.output
            os.unlink(f.name)
