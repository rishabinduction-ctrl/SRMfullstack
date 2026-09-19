# gdb/domain/fixed_deposit_account.py
from gdb.domain.bank_account import BankAccount

class FixedDepositAccount(BankAccount):
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", tenure_months: int = 12, interest_rate: float = 6.5) -> None:
        super().__init__(account_number, name, age, balance, status, pin)
        self._tenure_months = tenure_months
        self._interest_rate = interest_rate

    def calculate_interest(self) -> float:
        return (self._balance * self._interest_rate * (self._tenure_months / 12.0)) / 100.0

    def get_account_type(self) -> str:
        return "FixedDeposit"
