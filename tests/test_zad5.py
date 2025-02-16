import pytest
from solutions.zad5 import BankAccount


@pytest.mark.parametrize(
    "initial_balance, amount, balance_after_operation",
    [(1000, 100, 900), (1000, 20, 980)],
)
def test_bank_account_withdraw_should_return_proper_balance(
    initial_balance: float, amount: float, balance_after_operation: float
):
    account = BankAccount()
    account._balance = initial_balance
    assert account.withdraw(amount) == balance_after_operation


@pytest.mark.parametrize(
    "initial_balance, amount, error",
    [
        (1, 100, ValueError("Not enough money!")),
        (19, 20, ValueError("Not enough money!")),
    ],
)
def test_bank_account_withdraw_should_raise_error(
    initial_balance: float, amount: float, error: ValueError
):
    account = BankAccount()
    account._balance = initial_balance
    with pytest.raises(type(error), match=str(error)):
        assert account.withdraw(amount)


@pytest.mark.parametrize(
    "initial_balance, amount, balance_after_operation",
    [(1000, 100, 1100), (1000, 20, 1020)],
)
def test_bank_account_deposit_should_return_proper_balance(
    initial_balance: float, amount: float, balance_after_operation: float
):
    account = BankAccount()
    account._balance = initial_balance
    assert account.deposit(amount) == balance_after_operation


@pytest.mark.parametrize(
    "initial_balance, amount, error",
    [
        (5, -100, ValueError("Amount must be positive!")),
        (10, 0, ValueError("Amount must be positive!")),
    ],
)
def test_bank_account_withdraw_should_raise_error(
    initial_balance: float, amount: float, error: ValueError
):
    account = BankAccount()
    account._balance = initial_balance
    with pytest.raises(type(error), match=str(error)):
        assert account.deposit(amount)
