"""Core budget transaction operations."""

from typing import Any


Transaction = dict[str, Any]


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
