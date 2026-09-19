# gdb/logging/database_log_destination.py
from typing import List
from gdb.domain.transaction import Transaction
from gdb.logging.log_destination import LogDestination
from gdb.db.simulated_database import SimulatedDatabase

class DatabaseLogDestination(LogDestination):
    """Database storage destination implementor backed by SimulatedDatabase."""

    # ============================================================
    # 📝 STEP 3: Implement DatabaseLogDestination
    #
    # INSTRUCTIONS:
    #   1. __init__(db): store the SimulatedDatabase in self._db.
    #   2. write(transaction): insert the transaction into the database.
    #   3. read_all(): return every transaction stored in the database.
    #   4. get_destination_name(): return "Database".
    #
    # HINT: SimulatedDatabase (gdb/db/simulated_database.py) is complete -- read its insert()
    #       and query_all() methods first.
    # ============================================================
    # TODO: keep a reference to the database
    def __init__(self, db: SimulatedDatabase) -> None:
        raise NotImplementedError("TODO: Step 3 - implement DatabaseLogDestination constructor")

    def write(self, transaction: Transaction) -> None:
        # TODO: insert the transaction into the database
        raise NotImplementedError("TODO: Step 3 - implement write")

    def read_all(self) -> List[Transaction]:
        # TODO: return all transactions stored in the database
        raise NotImplementedError("TODO: Step 3 - implement read_all")

    def get_destination_name(self) -> str:
        # TODO: return "Database"
        raise NotImplementedError("TODO: Step 3 - implement get_destination_name")
