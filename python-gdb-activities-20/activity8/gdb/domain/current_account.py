# gdb/domain/current_account.py
# ACTIVITY 8: Fill the Activity 7 TODOs with your completed Activity 7 code, then complete the Activity 8 TODOs.
from gdb.domain.account import Account
from gdb.exceptions import (
    AccountException,
    InactiveAccountException,
    InvalidAmountException,
    InsufficientBalanceException
)

# TODO (Activity 7): Make CurrentAccount inherit from Account.
class CurrentAccount:
    """Current Account allowing overdraft up to overdraft_limit."""
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", overdraft_limit: float = 10000.0) -> None:
        # TODO (Activity 7): Call super().__init__(...) with account_type="Current" and store self._overdraft_limit.
        pass

    def withdraw(self, amount: float) -> None:
        # TODO (Activity 8, Step 2): Override Account.withdraw() to allow an overdraft:
        #   - account not active                         -> raise InactiveAccountException
        #   - amount <= 0                                -> raise InvalidAmountException
        #   - amount > balance + self._overdraft_limit   -> raise InsufficientBalanceException
        #   - otherwise subtract amount from self._balance (the balance may go negative)
        raise NotImplementedError("TODO: override CurrentAccount.withdraw()")

    @property
    def overdraft_limit(self) -> float: return self._overdraft_limit
