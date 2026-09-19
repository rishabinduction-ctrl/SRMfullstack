# gdb/exceptions/invalid_pin_exception.py
from gdb.exceptions.account_exception import AccountException

class InvalidPinException(AccountException):
    """Raised when an invalid or incorrect PIN is provided."""
    pass
