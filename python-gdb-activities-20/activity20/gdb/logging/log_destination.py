# gdb/logging/log_destination.py
from abc import ABC, abstractmethod
from typing import List
from gdb.domain.transaction import Transaction

class LogDestination(ABC):
    """Implementor Interface in the Bridge Pattern for log persistence destinations."""

    @abstractmethod
    def write(self, transaction: Transaction) -> None:
        """Write a transaction to the storage destination."""
        pass

    @abstractmethod
    def read_all(self) -> List[Transaction]:
        """Read all transactions from the storage destination."""
        pass

    @abstractmethod
    def get_destination_name(self) -> str:
        """Return human-readable destination identifier."""
        pass

    def readAll(self) -> List[Transaction]:
        return self.read_all()

    def getDestinationName(self) -> str:
        return self.get_destination_name()
