"""Domain exception thrown when financial operations are attempted on an inactive account."""

from gdb.exceptions.account_exception import AccountException

class InactiveAccountException(AccountException):
    """Exception thrown when operating on a closed or inactive account."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
