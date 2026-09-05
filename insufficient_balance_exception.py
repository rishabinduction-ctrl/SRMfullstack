"""Domain exception thrown when a withdrawal request exceeds total available funds."""

from gdb.exceptions.account_exception import AccountException

class InsufficientBalanceException(AccountException):
    """Exception thrown when a withdrawal request exceeds available funds."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
