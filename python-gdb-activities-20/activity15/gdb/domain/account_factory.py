# gdb/domain/account_factory.py
from gdb.domain.iaccount import IAccount
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount
from gdb.domain.salary_account import SalaryAccount
from gdb.exceptions.invalid_account_type_exception import InvalidAccountTypeException
from gdb.exceptions.minimum_balance_violation_exception import MinimumBalanceViolationException

class AccountFactory:
    """Factory creating appropriate IAccount instances."""

    @staticmethod
    def create_account(account_type: str, account_number: int, name: str, age: int, initial_balance: float, tenure_years: int = 0) -> IAccount:
        t = account_type.upper().replace(" ", "").replace("_", "")
        acc: IAccount
        if t == "SAVINGS":
            acc = SavingsAccount(account_number, name, age, initial_balance, tenure_years)
        elif t == "CURRENT":
            acc = CurrentAccount(account_number, name, age, initial_balance, tenure_years)
        elif t in ("FIXEDDEPOSIT", "FD"):
            acc = FixedDepositAccount(account_number, name, age, initial_balance, tenure_years)
        elif t == "SALARY":
            acc = SalaryAccount(account_number, name, age, initial_balance, tenure_years)
        else:
            raise InvalidAccountTypeException(f"Unsupported account type: {account_type}")

        if initial_balance < acc.get_minimum_balance():
            raise MinimumBalanceViolationException(
                f"Initial balance Rs. {initial_balance:,.2f} is below minimum required Rs. {acc.get_minimum_balance():,.2f}"
            )
        return acc

    @staticmethod
    def createAccount(account_type: str, account_number: int, name: str, age: int, initial_balance: float, tenure_years: int = 0) -> IAccount:
        return AccountFactory.create_account(account_type, account_number, name, age, initial_balance, tenure_years)
