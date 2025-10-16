import pytest
from bank_account import BankAccount


def test_initial_balance_default():
    acc = BankAccount("Alice")
    assert acc.owner == "Alice"
    assert acc.balance == 0.0


def test_initial_balance_negative_raises():
    with pytest.raises(ValueError, match="negative"):
        BankAccount("Bob", -50)


def test_deposit_increases_balance():
    acc = BankAccount("Carol", 100)
    new_balance = acc.deposit(50)
    assert new_balance == 150
    assert acc.balance == 150


def test_deposit_negative_raises():
    acc = BankAccount("Dan")
    with pytest.raises(ValueError, match="positive"):
        acc.deposit(-10)


def test_withdraw_valid_amount():
    acc = BankAccount("Eve", 200)
    new_balance = acc.withdraw(50)
    assert new_balance == 150
    assert acc.balance == 150


def test_withdraw_insufficient_funds():
    acc = BankAccount("Frank", 30)
    with pytest.raises(ValueError, match="Insufficient"):
        acc.withdraw(100)


def test_withdraw_negative_amount_raises():
    acc = BankAccount("Grace", 50)
    with pytest.raises(ValueError, match="positive"):
        acc.withdraw(0)


def test_is_overdrawn_false_when_positive_balance():
    acc = BankAccount("Heidi", 10)
    assert not acc.is_overdrawn()


def test_is_overdrawn_true_when_negative_balance(monkeypatch):
    acc = BankAccount("Ivan", 10)
    # Force a negative balance for test purposes
    acc.balance = -5
    assert acc.is_overdrawn()

