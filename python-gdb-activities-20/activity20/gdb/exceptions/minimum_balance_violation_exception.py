# gdb/exceptions/minimum_balance_violation_exception.py
from gdb.exceptions.account_exception import AccountException

class MinimumBalanceViolationException(AccountException):
    """Raised when an operation would violate the minimum balance requirement."""
    pass
