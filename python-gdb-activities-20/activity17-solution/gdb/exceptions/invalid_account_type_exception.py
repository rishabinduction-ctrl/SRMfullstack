# gdb/exceptions/invalid_account_type_exception.py
from gdb.exceptions.account_exception import AccountException

class InvalidAccountTypeException(AccountException):
    """Raised when an unrecognized account type is requested."""
    pass
