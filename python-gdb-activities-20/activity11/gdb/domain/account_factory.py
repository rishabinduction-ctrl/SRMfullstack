# gdb/domain/account_factory.py
from gdb.domain.iaccount import IAccount
from gdb.domain.salary_account import SalaryAccount
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount

class AccountFactory:
    @staticmethod
    def create_account(account_type: str, account_number: str, name: str, age: int, balance: float, pin: str = "0000") -> IAccount:
        account_type = account_type.strip().lower()

        if account_type in ["salary", "salaryaccount"]:
            return SalaryAccount(account_number, name, age, balance, pin=pin)
        elif account_type in ["savings", "savingsaccount"]:
            return SavingsAccount(account_number, name, age, balance, pin=pin)
        elif account_type in ["current", "currentaccount"]:
            return CurrentAccount(account_number, name, age, balance, pin=pin)
        elif account_type in ["fixeddeposit", "fixeddepositaccount", "fd"]:
            return FixedDepositAccount(account_number, name, age, balance, pin=pin)
        else:
            raise ValueError(f"Unknown account type: {account_type}")
