# gdb/domain/current_account.py
from gdb.domain.account import Account
from gdb.exceptions import (
    AccountException,
    InactiveAccountException,
    InvalidAmountException,
    InsufficientBalanceException
)

class CurrentAccount(Account):
    """Current Account allowing overdraft up to overdraft_limit."""
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", overdraft_limit: float = 10000.0) -> None:
        super().__init__(account_number, name, age, balance, "Current", status, pin)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot withdraw from inactive account: {self._account_number}")
        if amount <= 0:
            raise InvalidAmountException(f"Withdrawal amount must be strictly positive: {amount}")
        if amount > (self._balance + self._overdraft_limit):
            raise InsufficientBalanceException(f"Withdrawal exceeds balance + overdraft limit of Rs {self._balance + self._overdraft_limit}")
        self._balance -= amount

    @property
    def overdraft_limit(self) -> float: return self._overdraft_limit
