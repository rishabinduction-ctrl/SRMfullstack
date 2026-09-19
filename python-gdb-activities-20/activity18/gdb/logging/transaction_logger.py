# gdb/logging/transaction_logger.py
from typing import List
from gdb.domain.transaction import Transaction
from gdb.logging.log_destination import LogDestination

class TransactionLogger:
    """Bridge Abstraction: delegates logging operations to LogDestination implementor."""

    # ============================================================
    # 📝 STEP 4: Implement Bridge Constructor & Methods
    #
    # INSTRUCTIONS:
    #   1. __init__: store destination (a LogDestination) in self._destination.
    #   2. log(transaction): if transaction is not None, call self._destination.write(transaction).
    #   3. get_transactions(): return self._destination.read_all().
    #   4. get_destination(): return the current destination.
    #   5. set_destination(destination): replace self._destination -- this is how the backend is switched at runtime.
    # ============================================================
    # TODO: store the destination
    def __init__(self, destination: LogDestination) -> None:
        raise NotImplementedError("TODO: Step 4 - implement TransactionLogger constructor")

    # TODO: implement log, get_transactions, get_destination and set_destination
    def log(self, transaction: Transaction) -> None:
        pass

    def get_transactions(self) -> List[Transaction]:
        return []

    def get_destination(self) -> LogDestination:
        raise NotImplementedError("TODO: Step 4 - implement get_destination")

    def set_destination(self, destination: LogDestination) -> None:
        raise NotImplementedError("TODO: Step 4 - implement set_destination")
