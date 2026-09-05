"""Domain exception thrown when a customer's age violates regulatory policy."""

from gdb.exceptions.account_exception import AccountException

class InvalidAgeException(AccountException):
    """Exception thrown when customer age is under 18 years or name is empty."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
