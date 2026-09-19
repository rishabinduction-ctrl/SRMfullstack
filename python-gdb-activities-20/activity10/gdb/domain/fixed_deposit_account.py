# gdb/domain/fixed_deposit_account.py
# ACTIVITY 10: Replace this file with your completed Activity 9 version before writing the tests.
from gdb.domain.bank_account import BankAccount

class FixedDepositAccount(BankAccount):
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", tenure_months: int = 12, interest_rate: float = 6.5) -> None:
        super().__init__(account_number, name, age, balance, status, pin)
        self._tenure_months = tenure_months
        self._interest_rate = interest_rate

    def calculate_interest(self) -> float:
        # TODO (Step 2): Return simple interest for the full tenure:
        #   balance * interest_rate / 100, scaled by (tenure_months / 12).
        raise NotImplementedError("TODO: implement FixedDepositAccount.calculate_interest()")

    def get_account_type(self) -> str:
        # TODO (Step 2): Fulfil the abstract contract -- return the product type name "FixedDeposit".
        raise NotImplementedError("TODO: implement FixedDepositAccount.get_account_type()")
