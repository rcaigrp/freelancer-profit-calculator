import unittest
import os
import tempfile
import sys
import click

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import parse_expenses, calculate_metrics
from main import main

class TestCalculatorLogic(unittest.TestCase):
    def test_calculate_metrics(self):
        metrics = calculate_metrics(income=1000, expenses=[200, 300], tax_rate=10, hours=40)
        self.assertEqual(metrics.total_expenses, 500)
        self.assertEqual(metrics.gross_profit, 500)
        self.assertAlmostEqual(metrics.tax_deduction, 50)
        self.assertAlmostEqual(metrics.net_profit, 450)
        self.assertAlmostEqual(metrics.hourly_rate, 450/40)

    def test_parse_expenses(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write("amount\n100\n200\n300\n")
            temp_path = f.name
        try:
            expenses = parse_expenses(temp_path)
            self.assertEqual(expenses, [100.0, 200.0, 300.0])
        finally:
            os.unlink(temp_path)

class TestCLIRunner(unittest.TestCase):
    def test_cli_successful_run(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write("amount\n100\n")
            temp_csv = f.name
        try:
            runner = click.testing.CliRunner()
            result = runner.invoke(main, ['--income', '1000', '--expenses', temp_csv, '--tax-rate', '0', '--hours', '10'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('1000', result.output)
        finally:
            os.unlink(temp_csv)

    def test_cli_missing_file(self):
        runner = click.testing.CliRunner()
        result = runner.invoke(main, ['--income', '1000', '--expenses', 'nonexistent.csv'])
        self.assertNotEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main()
