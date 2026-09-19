# gdb/domain/transaction.py
from datetime import datetime
from typing import Optional
from gdb.domain.transaction_type import TransactionType

class Transaction:
    """Enterprise Transaction Record model representing a financial operation."""
    _counter = 100000

    @classmethod
    def generate_id(cls) -> int:
        cls._counter += 1
        return cls._counter

    @classmethod
    def generateId(cls) -> int:
        return cls.generate_id()

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
        self.transaction_id = int(transaction_id)
        self.timestamp = timestamp or datetime.now()
        self.account_number = int(account_number)
        self.transaction_type = transaction_type
        self.amount = float(amount)
        self.balance_after = float(balance_after)
        self.status = status
        self.description = description
        self.from_account = int(from_account) if from_account is not None else None
        self.to_account = int(to_account) if to_account is not None else None

    # Getters for Java / PEP 8 compatibility
    def get_id(self) -> int: return self.transaction_id
    def getId(self) -> int: return self.transaction_id
    def get_timestamp(self) -> datetime: return self.timestamp
    def getTimestamp(self) -> datetime: return self.timestamp
    def get_account_number(self) -> int: return self.account_number
    def getAccountNumber(self) -> int: return self.account_number
    def get_type(self) -> TransactionType: return self.transaction_type
    def getType(self) -> TransactionType: return self.transaction_type
    def get_amount(self) -> float: return self.amount
    def getAmount(self) -> float: return self.amount
    def get_balance_after(self) -> float: return self.balance_after
    def getBalanceAfter(self) -> float: return self.balance_after
    def get_status(self) -> str: return self.status
    def getStatus(self) -> str: return self.status
    def get_description(self) -> str: return self.description
    def getDescription(self) -> str: return self.description
    def get_from_account(self) -> Optional[int]: return self.from_account
    def getFromAccount(self) -> Optional[int]: return self.from_account
    def get_to_account(self) -> Optional[int]: return self.to_account
    def getToAccount(self) -> Optional[int]: return self.to_account

    def get_receipt(self) -> str:
        type_str = self.transaction_type.value if hasattr(self.transaction_type, "value") else str(self.transaction_type)
        return (
            f"TXN ID: {self.transaction_id} | Type: {type_str} | Amount: Rs. {self.amount:,.2f} | "
            f"Balance After: Rs. {self.balance_after:,.2f} | Status: {self.status} | {self.description}"
        )

    def getReceipt(self) -> str:
        return self.get_receipt()

    def __str__(self) -> str:
        return self.get_receipt()
