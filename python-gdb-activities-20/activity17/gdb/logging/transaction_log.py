# gdb/logging/transaction_log.py
import pickle
import os
from typing import List
from gdb.domain.transaction import Transaction

class TransactionLog:
    """File persistence logger for Transaction records using pickle serialization."""

    # ============================================================
    # 📝 STEP 11: Constructor & Fields
    #
    # INSTRUCTIONS:
    #   1. Store log_file (the path of the pickle file) in self._log_file.
    #   2. Start with an empty list in self._transactions.
    # ============================================================
    # TODO: store the log file path and create the in-memory transaction list
    def __init__(self, log_file: str = "transactions.log") -> None:
        raise NotImplementedError("TODO: Step 11 - implement TransactionLog constructor")

    # ============================================================
    # 📝 STEP 12: Implement log_transaction(transaction)
    # ============================================================
    # TODO: append transaction and save to file
    def log_transaction(self, transaction: Transaction) -> None:
        pass

    # ============================================================
    # 📝 STEP 13: Implement save_to_file() & load_from_file()
    # ============================================================
    # TODO: serialize and deserialize transactions
    def save_to_file(self) -> None:
        pass

    def load_from_file(self) -> List[Transaction]:
        return []

    def get_transactions(self) -> List[Transaction]:
        return self._transactions

    # ============================================================
    # 📝 STEP 14: Implement clear()
    #
    # INSTRUCTIONS:
    #   1. Empty self._transactions.
    #   2. If the log file exists, delete it with os.remove() (ignore an OSError if the delete fails).
    # ============================================================
    # TODO: forget every transaction and delete the log file
    def clear(self) -> None:
        raise NotImplementedError("TODO: Step 14 - implement clear")
