# gdb/exceptions/account_exception.py
class AccountException(Exception):
    """Base checked domain exception for banking operations."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
