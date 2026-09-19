# gdb/exceptions/minimum_balance_violation_exception.py
# ACTIVITY 6: Replace this file with your completed Activity 5 version before writing the tests.
from gdb.exceptions.account_exception import AccountException

# TODO (Step 1): Create class MinimumBalanceViolationException(AccountException) with an
#   __init__(self, message: str) -> None that passes message on to super().__init__().
#   Raised when a withdrawal would take the balance below a required minimum (used from Activity 8).
