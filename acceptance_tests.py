import subprocess
import sys
import os
import csv
import tempfile

def run_main(args):
    cmd = [sys.executable, "/workspace/projects/Freelancer-Profit-Calculator/main.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def test_criterion_1_calculate_profit():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'type', 'amount', 'hours', 'category'])
        writer.writerow(['2024-01-01', 'income', '1800', '40', 'client-work'])
        writer.writerow(['2024-01-02', 'expense', '80', '0', 'software'])
        writer.writerow(['2024-01-03', 'expense', '120', '0', 'personal'])
        tmp_path = f.name
    try:
        res = run_main(['--input', tmp_path])
        assert res.returncode == 0
        assert 'Business Income:' in res.stdout
        assert 'Net Profit:' in res.stdout
    finally:
        os.unlink(tmp_path)

def test_criterion_2_handle_zero_hours():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'type', 'amount', 'hours', 'category'])
        writer.writerow(['2024-01-01', 'income', '1000', '0', 'client-work'])
        tmp_path = f.name
    try:
        res = run_main(['--input', tmp_path])
        assert res.returncode == 0
        assert 'Effective Hourly Rate' in res.stdout
        assert '0.00' in res.stdout or 'N/A' in res.stdout
    finally:
        os.unlink(tmp_path)

def test_criterion_3_skip_malformed_rows():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'type', 'amount', 'hours', 'category'])
        writer.writerow(['2024-01-01', 'income', '1000', '10', 'work'])
        writer.writerow(['invalid_row', 'bad'])
        writer.writerow(['2024-01-02', 'expense', '50', '0', 'misc'])
        tmp_path = f.name
    try:
        res = run_main(['--input', tmp_path])
        assert res.returncode == 0
        assert 'Business Income: $1,000.00' in res.stdout
    finally:
        os.unlink(tmp_path)