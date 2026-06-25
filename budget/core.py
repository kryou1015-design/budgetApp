"""Core budget transaction operations."""

from typing import Any


Transaction = dict[str, Any]


def add_transaction(
    transactions: list[Transaction],
    transaction: Transaction,
) -> list[Transaction]:
    """Return a transaction list with the new transaction added."""
    pass


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
