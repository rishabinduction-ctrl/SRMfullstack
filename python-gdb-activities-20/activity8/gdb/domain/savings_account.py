# gdb/domain/savings_account.py
# ACTIVITY 8: Fill the Activity 7 TODOs with your completed Activity 7 code, then complete the Activity 8 TODOs.
from gdb.domain.account import Account
from gdb.exceptions import (
    AccountException,
    InactiveAccountException,
    InvalidAmountException,
    MinimumBalanceViolationException
)

# TODO (Activity 7): Make SavingsAccount inherit from Account.
class SavingsAccount:
    """Savings Account enforcing minimum balance on withdrawal."""
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", interest_rate: float = 4.0, minimum_balance: float = 1000.0) -> None:
        # TODO (Activity 7): Call super().__init__(...) with account_type="Savings" and store self._interest_rate.
        # TODO (Activity 8): Store minimum_balance in self._minimum_balance.
        pass

    def withdraw(self, amount: float) -> None:
        # TODO (Activity 8, Step 1): Override Account.withdraw() to enforce the minimum balance:
        #   - account not active                        -> raise InactiveAccountException
        #   - amount <= 0                               -> raise InvalidAmountException
        #   - balance - amount < self._minimum_balance  -> raise MinimumBalanceViolationException
        #   - otherwise let the parent perform the withdrawal: super().withdraw(amount)
        raise NotImplementedError("TODO: override SavingsAccount.withdraw()")

    def calculate_interest(self) -> float:
        # TODO (Activity 7): Return balance * interest_rate / 100.
        raise NotImplementedError("TODO: implement SavingsAccount.calculate_interest()")

    @property
    def minimum_balance(self) -> float: return self._minimum_balance
