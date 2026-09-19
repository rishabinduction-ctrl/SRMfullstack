# gdb/exceptions/inactive_account_exception.py
from gdb.exceptions.account_exception import AccountException

class InactiveAccountException(AccountException):
    def __init__(self, message: str) -> None:
        super().__init__(message)
