"""Domain exception thrown when a zero or negative monetary amount is supplied."""

from gdb.exceptions.account_exception import AccountException

class InvalidAmountException(AccountException):
    """Exception thrown when transaction amount is less than or equal to zero."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
