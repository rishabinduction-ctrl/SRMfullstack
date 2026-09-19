# gdb/domain/current_account.py
from gdb.domain.account import Account

# TODO (Step 2): Make CurrentAccount inherit from Account -> class CurrentAccount(Account):
class CurrentAccount:
    """Current Account specialization adding overdraft limit."""
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", overdraft_limit: float = 10000.0) -> None:
        # TODO (Step 2): Call super().__init__(...) with the same arguments, passing account_type="Current",
        #   then store overdraft_limit in self._overdraft_limit.
        pass

    @property
    def overdraft_limit(self) -> float: return self._overdraft_limit
