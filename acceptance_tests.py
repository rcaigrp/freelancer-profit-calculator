import pytest
import subprocess
import os

PROJECT_DIR = "/workspace/projects/Freelancer-Profit-Calculator"
DATA_DIR = os.path.join(PROJECT_DIR, "data")
LOGS_DIR = os.path.join(PROJECT_DIR, "logs")

@pytest.fixture(autouse=True)
def setup_test_env(tmp_path):
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(LOGS_DIR, exist_ok=True)
    csv_content = """date,type,amount,description
2024-01-15,income,2000,Web Design
2024-01-20,expense,500,Software License
2024-02-10,income,1500,Consulting
"""
    with open(os.path.join(DATA_DIR, "income_expenses.csv"), "w") as f:
        f.write(csv_content)
    yield


def test_criterion_1_run_command():
    result = subprocess.run(
        ["python", os.path.join(PROJECT_DIR, "main.py"), "--data", os.path.join(DATA_DIR, "income_expenses.csv"), "--tax-rate", "0.25"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Command failed: {result.stderr}"


def test_criterion_2_reads_csv():
    result = subprocess.run(
        ["python", os.path.join(PROJECT_DIR, "main.py"), "--data", os.path.join(DATA_DIR, "income_expenses.csv"), "--tax-rate", "0.25"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert "Income" in result.stdout or "Revenue" in result.stdout


def test_criterion_3_calculates_profit():
    result = subprocess.run(
        ["python", os.path.join(PROJECT_DIR, "main.py"), "--data", os.path.join(DATA_DIR, "income_expenses.csv"), "--tax-rate", "0.25"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert "3000" in result.stdout or "3500" in result.stdout


def test_criterion_4_estimates_tax():
    result = subprocess.run(
        ["python", os.path.join(PROJECT_DIR, "main.py"), "--data", os.path.join(DATA_DIR, "income_expenses.csv"), "--tax-rate", "0.25"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert "750" in result.stdout or "Tax" in result.stdout


def test_criterion_5_outputs_summary():
    result = subprocess.run(
        ["python", os.path.join(PROJECT_DIR, "main.py"), "--data", os.path.join(DATA_DIR, "income_expenses.csv"), "--tax-rate", "0.25"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert "Profit" in result.stdout or "Margin" in result.stdout


def test_criterion_6_writes_log():
    result = subprocess.run(
        ["python", os.path.join(PROJECT_DIR, "main.py"), "--data", os.path.join(DATA_DIR, "income_expenses.csv"), "--tax-rate", "0.25"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    log_path = os.path.join(LOGS_DIR, "profit_report.txt")
    assert os.path.exists(log_path), "Log file was not created"
    with open(log_path) as f:
        content = f.read()
    assert len(content) > 0
