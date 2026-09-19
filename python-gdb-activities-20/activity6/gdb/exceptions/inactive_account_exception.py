# gdb/exceptions/inactive_account_exception.py
# ACTIVITY 6: Replace this file with your completed Activity 5 version before writing the tests.
from gdb.exceptions.account_exception import AccountException

# TODO (Step 1): Create class InactiveAccountException(AccountException) with an
#   __init__(self, message: str) -> None that passes message on to super().__init__().
#   Raised when a deposit/withdrawal is attempted on an account whose status is not "Active".
