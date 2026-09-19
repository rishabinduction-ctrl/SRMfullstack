# gdb/domain/account_factory.py
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
        if not account_type:
            raise AccountException("Account type cannot be empty")
        
        t = account_type.strip().upper()
        if t == "SAVINGS":
            return SavingsAccount(account_number, name, age, balance, status, pin, 4.0, 1000.0)
        elif t == "CURRENT":
            return CurrentAccount(account_number, name, age, balance, status, pin, 10000.0)
        elif t == "SALARY":
            return SalaryAccount(account_number, name, age, balance, status, pin)
        elif t == "FIXEDDEPOSIT":
            return FixedDepositAccount(account_number, name, age, balance, status, pin, 12, 6.5)
        else:
            raise AccountException(f"Unknown account type: {account_type}")
