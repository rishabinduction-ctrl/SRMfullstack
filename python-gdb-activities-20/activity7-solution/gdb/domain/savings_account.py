# gdb/domain/savings_account.py
from gdb.domain.account import Account

class SavingsAccount(Account):
    """Savings Account specialization adding interest rate and interest calculation."""
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", interest_rate: float = 4.0) -> None:
        super().__init__(account_number, name, age, balance, "Savings", status, pin)
        self._interest_rate = interest_rate

    def calculate_interest(self) -> float:
        return (self._balance * self._interest_rate) / 100.0

    @property
    def interest_rate(self) -> float: return self._interest_rate
    @interest_rate.setter
    def interest_rate(self, rate: float) -> None: self._interest_rate = rate
