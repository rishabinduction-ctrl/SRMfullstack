# gdb/domain/current_account.py
from gdb.domain.account import Account

class CurrentAccount(Account):
    """Current Account specialization adding overdraft limit."""
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", overdraft_limit: float = 10000.0) -> None:
        super().__init__(account_number, name, age, balance, "Current", status, pin)
        self._overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self) -> float: return self._overdraft_limit
