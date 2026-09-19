# gdb/logging/transaction_logger.py
from typing import List
from gdb.domain.transaction import Transaction
from gdb.logging.log_destination import LogDestination

class TransactionLogger:
    """Bridge Abstraction: delegates logging operations to LogDestination implementor."""

    def __init__(self, destination: LogDestination) -> None:
        self._destination = destination

    def log(self, transaction: Transaction) -> None:
        if transaction is not None:
            self._destination.write(transaction)

    def get_transactions(self) -> List[Transaction]:
        return self._destination.read_all()

    def getTransactions(self) -> List[Transaction]:
        return self.get_transactions()

    def get_destination(self) -> LogDestination:
        return self._destination

    def getDestination(self) -> LogDestination:
        return self.get_destination()

    def set_destination(self, destination: LogDestination) -> None:
        self._destination = destination

    def setDestination(self, destination: LogDestination) -> None:
        self.set_destination(destination)
