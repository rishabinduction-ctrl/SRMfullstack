# gdb/exceptions/inactive_account_exception.py
from gdb.exceptions.account_exception import AccountException

class InactiveAccountException(AccountException):
    """Raised when an operation is performed on an inactive or closed account."""
    pass
