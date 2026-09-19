# gdb/domain/current_account.py
from gdb.domain.bank_account import BankAccount
from gdb.exceptions import (
    InactiveAccountException,
    InvalidAmountException,
    InsufficientBalanceException
)

class CurrentAccount(BankAccount):
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", overdraft_limit: float = 10000.0) -> None:
        super().__init__(account_number, name, age, balance, status, pin)
        self._overdraft_limit = overdraft_limit

    def calculate_interest(self) -> float:
        return 0.0

    def get_account_type(self) -> str:
        return "Current"

    def withdraw(self, amount: float) -> None:
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot withdraw from inactive account: {self._account_number}")
        if amount <= 0:
            raise InvalidAmountException(f"Withdrawal amount must be strictly positive: {amount}")
        if amount > (self._balance + self._overdraft_limit):
            raise InsufficientBalanceException(f"Withdrawal exceeds balance + overdraft limit")
        self._balance -= amount
