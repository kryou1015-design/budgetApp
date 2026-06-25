"""Core budget transaction operations."""

import csv
from pathlib import Path
from typing import Any


Transaction = dict[str, Any]
MonthlySummary = dict[str, dict[str, int]]


def load_transactions_from_csv(file_path: str | Path) -> list[Transaction]:
    """Read transaction dictionaries from a UTF-8 BOM-compatible CSV file."""
    with Path(file_path).open(encoding="utf-8-sig", newline="") as csv_file:
        return [
            {**row, "amount": int(row["amount"])}
            for row in csv.DictReader(csv_file)
        ]


def add_transaction(
    transactions: list[Transaction],
    transaction: Transaction,
) -> list[Transaction]:
    """Return a transaction list with the new transaction added."""
    stored_transaction: Transaction = {
        "date": transaction["date"],
        "type": transaction["type"],
        "category": transaction["category"],
        "description": transaction["description"],
        "amount": transaction["amount"],
        "memo": transaction["memo"],
    }
    return [*transactions, stored_transaction]


def get_balance(transactions: list[Transaction]) -> float:
    """Return the sum of income and expense transaction amounts."""
    return float(sum(transaction["amount"] for transaction in transactions))


def filter_by_category(
    transactions: list[Transaction],
    category: str,
) -> list[Transaction]:
    """Return transactions matching a category without case sensitivity."""
    target_category = category.casefold()
    return [
        transaction.copy()
        for transaction in transactions
        if str(transaction["category"]).casefold() == target_category
    ]


def monthly_summary(transactions: list[Transaction]) -> MonthlySummary:
    """Return income, expense, and net totals grouped by transaction month."""
    summary: MonthlySummary = {}
    for transaction in transactions:
        month = str(transaction["date"])[:7]
        amount = int(transaction["amount"])
        if month not in summary:
            summary[month] = {"income": 0, "expense": 0, "net": 0}
        if amount >= 0:
            summary[month]["income"] += amount
        else:
            summary[month]["expense"] += amount
        summary[month]["net"] += amount
    return summary


def calculate_balance(transactions: list[Transaction]) -> int:
    """Return the current balance from income and expense transactions."""
    pass


def summarize_by_category(transactions: list[Transaction]) -> dict[str, int]:
    """Return total transaction amounts grouped by category."""
    pass


def filter_transactions_by_type(
    transactions: list[Transaction],
    transaction_type: str,
) -> list[Transaction]:
    """Return transactions matching the requested transaction type."""
    pass
