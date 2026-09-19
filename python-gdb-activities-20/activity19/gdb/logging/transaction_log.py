# gdb/logging/transaction_log.py
import pickle
import os
from typing import List
from gdb.domain.transaction import Transaction

class TransactionLog:
    """File persistence logger for Transaction records using serialization."""

    def __init__(self, log_file: str = "transactions.log") -> None:
        self._log_file = log_file
        self._transactions: List[Transaction] = []

    def log_transaction(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)
        self.save_to_file()

    def logTransaction(self, transaction: Transaction) -> None:
        self.log_transaction(transaction)

    def get_transactions(self) -> List[Transaction]:
        return list(self._transactions)

    def getTransactions(self) -> List[Transaction]:
        return self.get_transactions()

    def save_to_file(self) -> None:
        with open(self._log_file, "wb") as f:
            pickle.dump(self._transactions, f)

    def saveToFile(self) -> None:
        self.save_to_file()

    def load_from_file(self) -> List[Transaction]:
        if os.path.exists(self._log_file):
            try:
                with open(self._log_file, "rb") as f:
                    self._transactions = pickle.load(f)
            except Exception:
                self._transactions = []
        return self.get_transactions()

    def loadFromFile(self) -> List[Transaction]:
        return self.load_from_file()

    def clear(self) -> None:
        self._transactions.clear()
        if os.path.exists(self._log_file):
            try:
                os.remove(self._log_file)
            except OSError:
                pass
