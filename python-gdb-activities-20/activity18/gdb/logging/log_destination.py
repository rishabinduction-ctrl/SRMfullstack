# gdb/logging/log_destination.py
from abc import ABC, abstractmethod
from typing import List
from gdb.domain.transaction import Transaction

# ============================================================
# 📝 STEP 1: Define LogDestination Implementor Interface
#
# INSTRUCTIONS:
#   1. abstractmethod write(transaction: Transaction) -> None
#   2. abstractmethod read_all() -> List[Transaction]
#   3. abstractmethod get_destination_name() -> str
#
# HINT: Decorate each method with @abstractmethod; the body can simply be `pass`.
#       MemoryLogDestination (provided) shows a finished implementor of this interface.
# ============================================================
class LogDestination(ABC):
    """Implementor Interface in the Bridge Pattern for logging storage destinations."""

    # TODO: declare the three abstract methods listed in STEP 1
    pass
