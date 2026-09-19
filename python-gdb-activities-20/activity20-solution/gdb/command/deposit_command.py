# gdb/command/deposit_command.py
from typing import Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.transaction import Transaction
from gdb.command.transaction_command import TransactionCommand

class DepositCommand(TransactionCommand):
    """Command executing a deposit operation."""

    def __init__(self, account: IAccount, amount: float) -> None:
        self._account = account
        self._amount = float(amount)
        self._transaction: Optional[Transaction] = None

    def execute(self) -> None:
        if hasattr(self._account, "deposit_with_transaction"):
            self._transaction = self._account.deposit_with_transaction(self._amount)
        else:
            self._account.deposit(self._amount)

    def get_transaction(self) -> Optional[Transaction]:
        return self._transaction

    def getTransaction(self) -> Optional[Transaction]:
        return self.get_transaction()
