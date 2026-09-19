# gdb/exceptions/insufficient_balance_exception.py
from gdb.exceptions.account_exception import AccountException
class InsufficientBalanceException(AccountException):
    def __init__(self, message: str) -> None: super().__init__(message)
