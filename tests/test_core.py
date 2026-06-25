import csv
from pathlib import Path

from budget.core import add_transaction, get_balance


STEP2_TRANSACTIONS = Path("data/step2_transactions.csv")


def test_add_transaction_increases_length() -> None:
    transactions = []
    transaction = {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }

    updated_transactions = add_transaction(transactions, transaction)

    assert len(updated_transactions) == 1


def test_add_transaction_stores_negative_expense_amount() -> None:
    transactions = []
    transaction = {
        "date": "2026-01-10",
        "type": "지출",
        "category": "교통",
        "description": "지하철",
        "amount": -1500,
        "memo": "",
    }

    updated_transactions = add_transaction(transactions, transaction)

    assert updated_transactions[0]["amount"] == -1500


def test_add_transaction_stores_positive_income_amount() -> None:
    transactions = []
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    updated_transactions = add_transaction(transactions, transaction)

    assert updated_transactions[0]["amount"] == 3500000


def test_add_transaction_allows_empty_description() -> None:
    transactions = []
    transaction = {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "",
        "amount": 25000,
        "memo": "중고마켓",
    }

    updated_transactions = add_transaction(transactions, transaction)

    assert updated_transactions[0]["description"] == ""


def test_get_balance_returns_zero_for_empty_transactions() -> None:
    assert get_balance([]) == 0.0


def test_get_balance_sums_income_and_expense_amounts() -> None:
    transactions = [
        {
            "date": "2026-01-01",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 10000,
            "memo": "",
        },
        {
            "date": "2026-01-02",
            "type": "지출",
            "category": "식비",
            "description": "점심",
            "amount": -3000,
            "memo": "",
        },
    ]

    assert get_balance(transactions) == 7000.0


def test_get_balance_matches_step2_transaction_total() -> None:
    with STEP2_TRANSACTIONS.open(encoding="utf-8", newline="") as csv_file:
        transactions = [
            {**row, "amount": int(row["amount"])}
            for row in csv.DictReader(csv_file)
        ]

    assert get_balance(transactions) == 24285027.0
