# gdb/domain/savings_account.py
from gdb.domain.account import Account
from gdb.exceptions import (
    AccountException,
    InactiveAccountException,
    InvalidAmountException,
    MinimumBalanceViolationException
)

class SavingsAccount(Account):
    """Savings Account enforcing minimum balance on withdrawal."""
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", interest_rate: float = 4.0, minimum_balance: float = 1000.0) -> None:
        super().__init__(account_number, name, age, balance, "Savings", status, pin)
        self._interest_rate = interest_rate
        self._minimum_balance = minimum_balance

    def withdraw(self, amount: float) -> None:
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot withdraw from inactive account: {self._account_number}")
        if amount <= 0:
            raise InvalidAmountException(f"Withdrawal amount must be strictly positive: {amount}")
        if (self._balance - amount) < self._minimum_balance:
            raise MinimumBalanceViolationException(f"Withdrawal would violate minimum balance requirement of Rs {self._minimum_balance}")
        super().withdraw(amount)

    def calculate_interest(self) -> float:
        return (self._balance * self._interest_rate) / 100.0

    @property
    def minimum_balance(self) -> float: return self._minimum_balance
