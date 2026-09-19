# gdb/exceptions/insufficient_balance_exception.py
from gdb.exceptions.account_exception import AccountException

class InsufficientBalanceException(AccountException):
    """Raised when account balance is insufficient for withdrawal or transfer."""
    pass
