from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    transactions = []
    transaction = {
        "date": "2026-06-25",
        "type": "expense",
        "category": "food",
        "amount": 12000,
        "memo": "lunch",
    }

    updated_transactions = add_transaction(transactions, transaction)

    assert len(updated_transactions) == 1
