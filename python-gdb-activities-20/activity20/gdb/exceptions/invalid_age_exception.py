# gdb/exceptions/invalid_age_exception.py
from gdb.exceptions.account_exception import AccountException

class InvalidAgeException(AccountException):
    """Raised when an applicant does not meet the age criteria."""
    pass
