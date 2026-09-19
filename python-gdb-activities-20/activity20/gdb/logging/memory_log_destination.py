# gdb/logging/memory_log_destination.py
from typing import List
from gdb.domain.transaction import Transaction
from gdb.logging.log_destination import LogDestination

class MemoryLogDestination(LogDestination):
    """In-memory storage destination implementor."""

    def __init__(self) -> None:
        self._transactions: List[Transaction] = []

    def write(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)

    def read_all(self) -> List[Transaction]:
        return list(self._transactions)

    def get_destination_name(self) -> str:
        return "In-Memory"

    def clear(self) -> None:
        self._transactions.clear()
