"""Domain exception thrown when a transaction would cause balance to fall below minimum."""

from gdb.exceptions.account_exception import AccountException

class MinimumBalanceViolationException(AccountException):
    """Exception thrown when post-transaction balance drops below required minimum limit."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
