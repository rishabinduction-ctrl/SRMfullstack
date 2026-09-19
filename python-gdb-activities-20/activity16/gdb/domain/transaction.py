# gdb/domain/transaction.py
from datetime import datetime
from typing import Optional
from gdb.domain.transaction_type import TransactionType

class Transaction:
    """Enterprise Transaction Record model."""
    _counter = 100000

    @classmethod
    def generate_id(cls) -> int:
        cls._counter += 1
        return cls._counter

    # ============================================================
    # 📝 STEP 2: Constructor & Fields
    # ============================================================
    def __init__(
        self,
        transaction_id: int,
        timestamp: datetime,
        account_number: int,
        transaction_type: TransactionType,
        amount: float,
        balance_after: float,
        status: str,
        description: str,
        from_account: Optional[int] = None,
        to_account: Optional[int] = None,
    ) -> None:
        # TODO: initialize fields
        pass

    # ============================================================
    # 📝 STEP 3-6: Implement Getters and get_receipt()
    # ============================================================
    def get_receipt(self) -> str:
        # TODO: return formatted receipt string
        return ""
