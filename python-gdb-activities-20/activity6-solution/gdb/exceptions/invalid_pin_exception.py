# gdb/exceptions/invalid_pin_exception.py
from gdb.exceptions.account_exception import AccountException

class InvalidPinException(AccountException):
    def __init__(self, message: str) -> None:
        super().__init__(message)
