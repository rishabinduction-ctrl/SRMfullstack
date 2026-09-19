# gdb/exceptions/invalid_amount_exception.py
from gdb.exceptions.account_exception import AccountException

class InvalidAmountException(AccountException):
    def __init__(self, message: str) -> None:
        super().__init__(message)
