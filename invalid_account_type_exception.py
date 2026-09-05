"""Domain exception thrown when an unrecognized account category string is supplied."""

from gdb.exceptions.account_exception import AccountException

class InvalidAccountTypeException(AccountException):
    """Exception thrown when an unrecognized account type string is passed."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
