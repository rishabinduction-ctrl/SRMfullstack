# gdb/domain/fixed_deposit_account.py
from gdb.domain.account import Account
from gdb.domain.account_rules_engine import AccountRulesEngine

class FixedDepositAccount(Account):
    """Fixed deposit account with higher interest rates and lock-in withdrawals."""

    def __init__(self, account_number: int, name: str, age: int, initial_balance: float, tenure_years: int = 0) -> None:
        super().__init__(account_number, name, age, initial_balance, tenure_years)

    def get_account_type(self) -> str:
        return "FixedDeposit"

    def get_minimum_balance(self) -> float:
        return AccountRulesEngine.get_instance().get_minimum_balance("FIXEDDEPOSIT")

    def get_interest_rate(self) -> float:
        return AccountRulesEngine.get_instance().get_interest_rate("FIXEDDEPOSIT")

    def can_withdraw(self, amount: float) -> bool:
        return False
