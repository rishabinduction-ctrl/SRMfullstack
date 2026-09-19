# gdb/logging/file_log_destination.py
import pickle
import os
from typing import List
from gdb.domain.transaction import Transaction
from gdb.logging.log_destination import LogDestination

class FileLogDestination(LogDestination):
    """File storage destination implementor using pickle serialization."""

    # ============================================================
    # 📝 STEP 2: Implement FileLogDestination
    #
    # INSTRUCTIONS:
    #   1. __init__: store filename in self._filename.
    #   2. write(transaction): load the existing list with self.read_all(), append the transaction,
    #      then pickle.dump() the whole list back to the file (open it in mode "wb").
    #   3. read_all(): if the file exists, pickle.load() the list from it (mode "rb") and return it;
    #      return [] if the file is missing or cannot be read.
    #   4. clear(): delete the file if it exists (ignore an OSError if the delete fails).
    # ============================================================
    # TODO: store the file name
    def __init__(self, filename: str = "transactions.log") -> None:
        raise NotImplementedError("TODO: Step 2 - implement FileLogDestination constructor")

    def write(self, transaction: Transaction) -> None:
        # TODO: read existing, append transaction, write back
        pass

    def read_all(self) -> List[Transaction]:
        # TODO: read and return transactions from file
        return []

    def get_destination_name(self) -> str:
        return f"File: {self._filename}"

    def clear(self) -> None:
        # TODO: delete the log file if it exists
        pass
