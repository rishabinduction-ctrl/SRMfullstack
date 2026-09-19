# gdb/exceptions/minimum_balance_violation_exception.py
from gdb.exceptions.account_exception import AccountException
class MinimumBalanceViolationException(AccountException):
    def __init__(self, message: str) -> None: super().__init__(message)
