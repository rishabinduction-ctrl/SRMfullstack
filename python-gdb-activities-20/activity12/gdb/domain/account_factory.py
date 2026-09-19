# gdb/domain/account_factory.py
# ACTIVITY 12: Replace this file with your completed Activity 11 version before writing the tests.

from gdb.domain.iaccount import IAccount
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.salary_account import SalaryAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount
from gdb.exceptions import AccountException

class AccountFactory:
    """Factory creating IAccount instances based on type."""

    @staticmethod
    def create_account(account_type: str, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000") -> IAccount:
        if not account_type or not account_type.strip():
            raise AccountException("Account type cannot be empty")

        normalized_type = account_type.strip().upper()

        if normalized_type == "SAVINGS":
            return SavingsAccount(account_number, name, age, balance, status, pin, interest_rate=4.0, minimum_balance=1000.0)
        elif normalized_type == "CURRENT":
            return CurrentAccount(account_number, name, age, balance, status, pin, overdraft_limit=10000.0)
        elif normalized_type == "SALARY":
            return SalaryAccount(account_number, name, age, balance, status, pin)
        elif normalized_type == "FIXEDDEPOSIT":
            return FixedDepositAccount(account_number, name, age, balance, status, pin, tenure_months=12, interest_rate=6.5)
        else:
            raise AccountException(f"Unknown account type: {account_type}")
