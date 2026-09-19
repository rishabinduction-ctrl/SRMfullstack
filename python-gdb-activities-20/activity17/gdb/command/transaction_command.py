# gdb/command/transaction_command.py
from abc import ABC, abstractmethod
from typing import Optional
from gdb.domain.transaction import Transaction

# ============================================================
# 📝 STEP 1: Define TransactionCommand Interface
#
# INSTRUCTIONS:
#   1. Declare abstract method execute() -> None
#   2. Declare abstract method get_transaction() -> Optional[Transaction]
#
# HINT: Decorate each method with @abstractmethod; the body can simply be `pass`.
# ============================================================
class TransactionCommand(ABC):
    """Command Interface for financial operations."""

    # TODO: declare the two abstract methods listed in STEP 1
    pass
