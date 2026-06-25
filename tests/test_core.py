import csv
from pathlib import Path

from budget.core import (
    add_transaction,
    filter_by_category,
    get_balance,
    load_transactions_from_csv,
)


STEP1_TRANSACTIONS = Path("data/step1_transactions.csv")
STEP2_TRANSACTIONS = Path("data/step2_transactions.csv")


def load_step2_transactions() -> list[dict[str, object]]:
    with STEP2_TRANSACTIONS.open(encoding="utf-8", newline="") as csv_file:
        return [
            {**row, "amount": int(row["amount"])}
            for row in csv.DictReader(csv_file)
        ]


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
    assert get_balance(load_step2_transactions()) == 24285027.0


def test_filter_by_category_matches_step2_case_insensitively() -> None:
    transactions = load_step2_transactions()

    filtered_transactions = filter_by_category(transactions, "여행")

    assert len(filtered_transactions) == 6
    assert all(
        transaction["category"].casefold() == "여행".casefold()
        for transaction in filtered_transactions
    )


def test_filter_by_category_returns_empty_list_for_missing_category() -> None:
    transactions = load_step2_transactions()

    filtered_transactions = filter_by_category(transactions, "없는카테고리")

    assert filtered_transactions == []


def test_filter_by_category_returns_independent_results() -> None:
    transactions = load_step2_transactions()

    filtered_transactions = filter_by_category(transactions, "여행")
    filtered_transactions[0]["description"] = "변경된 설명"

    assert transactions[0]["description"] == "항공권"


def test_load_transactions_from_csv_reads_step1_transactions() -> None:
    transactions = load_transactions_from_csv(STEP1_TRANSACTIONS)

    assert len(transactions) == 10
    assert transactions[0] == {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }


def test_load_transactions_from_csv_converts_amount_to_int() -> None:
    transactions = load_transactions_from_csv(STEP1_TRANSACTIONS)

    assert isinstance(transactions[0]["amount"], int)
    assert transactions[1]["amount"] == 3500000
