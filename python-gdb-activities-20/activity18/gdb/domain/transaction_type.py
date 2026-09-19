# gdb/domain/transaction_type.py
from enum import Enum

class TransactionType(Enum):
    """Enumeration of transaction operation types."""
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    TRANSFER_IN = "TRANSFER_IN"
    TRANSFER_OUT = "TRANSFER_OUT"
    TRANSFER = "TRANSFER"
