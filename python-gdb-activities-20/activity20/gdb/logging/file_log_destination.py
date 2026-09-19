# gdb/logging/file_log_destination.py
import pickle
import os
from typing import List
from gdb.domain.transaction import Transaction
from gdb.logging.log_destination import LogDestination

class FileLogDestination(LogDestination):
    """File storage destination implementor."""

    def __init__(self, filename: str = "transactions.log") -> None:
        self._filename = filename

    def write(self, transaction: Transaction) -> None:
        txns = self.read_all()
        txns.append(transaction)
        with open(self._filename, "wb") as f:
            pickle.dump(txns, f)

    def read_all(self) -> List[Transaction]:
        if os.path.exists(self._filename):
            try:
                with open(self._filename, "rb") as f:
                    return pickle.load(f)
            except Exception:
                return []
        return []

    def get_destination_name(self) -> str:
        return f"File: {self._filename}"

    def clear(self) -> None:
        if os.path.exists(self._filename):
            try:
                os.remove(self._filename)
            except OSError:
                pass
