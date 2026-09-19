# gdb/command/transfer_command.py
from typing import Optional
from datetime import datetime
from gdb.domain.iaccount import IAccount
from gdb.domain.transaction import Transaction
from gdb.domain.transaction_type import TransactionType
from gdb.command.transaction_command import TransactionCommand
from gdb.service.transfer_service import TransferService

class TransferCommand(TransactionCommand):
    """Command executing a funds transfer operation."""

    # ============================================================
    # 📝 STEP 8: Constructor
    #
    # INSTRUCTIONS:
    #   1. Store transfer_service, from_account and to_account in self._transfer_service,
    #      self._from_account and self._to_account.
    #   2. Store amount (as a float) in self._amount and pin (as an int) in self._pin.
    #   3. Set self._transaction = None -- execute() fills it in later.
    # ============================================================
    # TODO: store the service, both accounts, amount and PIN, and start with no transaction
    def __init__(self, transfer_service: TransferService, from_account: IAccount, to_account: IAccount, amount: float, pin: int) -> None:
        raise NotImplementedError("TODO: Step 8 - implement TransferCommand constructor")

    # ============================================================
    # 📝 STEP 9: Implement execute()
    #
    # INSTRUCTIONS:
    #   1. Call transfer_service.transfer(from_account, to_account, amount, pin).
    #   2. Build and store Transaction with type TRANSFER_OUT in self._transaction.
    # ============================================================
    # TODO: execute transfer
    def execute(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 10: Implement get_transaction()
    #
    # INSTRUCTIONS:
    #   Return self._transaction (it stays None until execute() has run).
    # ============================================================
    # TODO: return _transaction
    def get_transaction(self) -> Optional[Transaction]:
        raise NotImplementedError("TODO: Step 10 - implement get_transaction")
