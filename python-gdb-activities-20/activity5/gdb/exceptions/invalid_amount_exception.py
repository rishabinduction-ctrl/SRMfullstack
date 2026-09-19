# gdb/exceptions/invalid_amount_exception.py
from gdb.exceptions.account_exception import AccountException

# TODO (Step 1): Create class InvalidAmountException(AccountException) with an
#   __init__(self, message: str) -> None that passes message on to super().__init__().
#   Raised when an amount is invalid: a deposit/withdrawal <= 0, or a negative opening balance.
