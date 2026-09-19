# gdb/exceptions/account_exception.py
class AccountException(Exception):
    def __init__(self, message: str) -> None: super().__init__(message)
