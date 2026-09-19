# gdb/command/withdraw_command.py
from typing import Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.transaction import Transaction
from gdb.command.transaction_command import TransactionCommand

class WithdrawCommand(TransactionCommand):
    """Command executing a withdrawal operation."""

    def __init__(self, account: IAccount, amount: float, pin: int) -> None:
        self._account = account
        self._amount = float(amount)
        self._pin = int(pin)
        self._transaction: Optional[Transaction] = None

    def execute(self) -> None:
        if hasattr(self._account, "withdraw_with_transaction"):
            self._transaction = self._account.withdraw_with_transaction(self._amount, self._pin)
        else:
            self._account.withdraw(self._amount, self._pin)

    def get_transaction(self) -> Optional[Transaction]:
        return self._transaction

    def getTransaction(self) -> Optional[Transaction]:
        return self.get_transaction()
