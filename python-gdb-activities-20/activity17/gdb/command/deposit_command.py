# gdb/command/deposit_command.py
from typing import Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.transaction import Transaction
from gdb.command.transaction_command import TransactionCommand

class DepositCommand(TransactionCommand):
    """Command executing a deposit operation."""

    # ============================================================
    # 📝 STEP 2: Constructor
    #
    # INSTRUCTIONS:
    #   1. Store account in self._account.
    #   2. Store amount (as a float) in self._amount.
    #   3. Set self._transaction = None -- execute() fills it in later.
    # ============================================================
    # TODO: store the account and amount, and start with no transaction
    def __init__(self, account: IAccount, amount: float) -> None:
        raise NotImplementedError("TODO: Step 2 - implement DepositCommand constructor")

    # ============================================================
    # 📝 STEP 3: Implement execute()
    #
    # INSTRUCTIONS:
    #   Call account.deposit_with_transaction(amount) and store in self._transaction.
    # ============================================================
    # TODO: execute deposit
    def execute(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 4: Implement get_transaction()
    #
    # INSTRUCTIONS:
    #   Return self._transaction (it stays None until execute() has run).
    # ============================================================
    # TODO: return _transaction
    def get_transaction(self) -> Optional[Transaction]:
        raise NotImplementedError("TODO: Step 4 - implement get_transaction")
