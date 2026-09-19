# gdb/exceptions/invalid_amount_exception.py
from gdb.exceptions.account_exception import AccountException

class InvalidAmountException(AccountException):
    """Raised when a non-positive or invalid monetary amount is supplied."""
    pass
