# gdb/domain/savings_account.py
from gdb.domain.account import Account

# TODO (Step 1): Make SavingsAccount inherit from Account -> class SavingsAccount(Account):
class SavingsAccount:
    """Savings Account specialization adding interest rate and interest calculation."""
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", interest_rate: float = 4.0) -> None:
        # TODO (Step 1): Call super().__init__(...) with the same arguments, passing account_type="Savings"
        #   (Account expects: account_number, name, age, balance, account_type, status, pin),
        #   then store interest_rate in self._interest_rate.
        pass

    def calculate_interest(self) -> float:
        # TODO (Step 1): Return the yearly interest: balance * interest_rate / 100.
        raise NotImplementedError("TODO: implement SavingsAccount.calculate_interest()")

    @property
    def interest_rate(self) -> float: return self._interest_rate
    @interest_rate.setter
    def interest_rate(self, rate: float) -> None: self._interest_rate = rate
