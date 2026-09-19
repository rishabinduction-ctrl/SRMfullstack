# gdb/command/withdraw_command.py
from typing import Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.transaction import Transaction
from gdb.command.transaction_command import TransactionCommand

class WithdrawCommand(TransactionCommand):
    """Command executing a withdrawal operation."""

    # ============================================================
    # 📝 STEP 5: Constructor
    #
    # INSTRUCTIONS:
    #   1. Store account in self._account.
    #   2. Store amount (as a float) in self._amount and pin (as an int) in self._pin.
    #   3. Set self._transaction = None -- execute() fills it in later.
    # ============================================================
    # TODO: store the account, amount and PIN, and start with no transaction
    def __init__(self, account: IAccount, amount: float, pin: int) -> None:
        raise NotImplementedError("TODO: Step 5 - implement WithdrawCommand constructor")

    # ============================================================
    # 📝 STEP 6: Implement execute()
    #
    # INSTRUCTIONS:
    #   Call account.withdraw_with_transaction(amount, pin) and store in self._transaction.
    # ============================================================
    # TODO: execute withdrawal
    def execute(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 7: Implement get_transaction()
    #
    # INSTRUCTIONS:
    #   Return self._transaction (it stays None until execute() has run).
    # ============================================================
    # TODO: return _transaction
    def get_transaction(self) -> Optional[Transaction]:
        raise NotImplementedError("TODO: Step 7 - implement get_transaction")
