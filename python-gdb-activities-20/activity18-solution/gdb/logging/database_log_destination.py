# gdb/logging/database_log_destination.py
from typing import List
from gdb.domain.transaction import Transaction
from gdb.logging.log_destination import LogDestination
from gdb.db.simulated_database import SimulatedDatabase

class DatabaseLogDestination(LogDestination):
    """Database storage destination implementor backed by SimulatedDatabase."""

    def __init__(self, db: SimulatedDatabase) -> None:
        self._db = db

    def write(self, transaction: Transaction) -> None:
        self._db.insert(transaction)

    def read_all(self) -> List[Transaction]:
        return self._db.query_all()

    def get_destination_name(self) -> str:
        return "Database"
