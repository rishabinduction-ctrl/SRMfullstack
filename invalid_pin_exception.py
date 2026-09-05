"""Domain exception thrown when withdrawal authorization fails due to incorrect or unconfigured PIN."""

from gdb.exceptions.account_exception import AccountException

class InvalidPinException(AccountException):
    """Exception thrown when PIN setup is invalid or PIN authorization fails."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
