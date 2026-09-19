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

    def __init__(self, transfer_service: TransferService, from_account: IAccount, to_account: IAccount, amount: float, pin: int) -> None:
        self._transfer_service = transfer_service
        self._from_account = from_account
        self._to_account = to_account
        self._amount = float(amount)
        self._pin = int(pin)
        self._transaction: Optional[Transaction] = None

    def execute(self) -> None:
        self._transfer_service.transfer(self._from_account, self._to_account, self._amount, self._pin)
        self._transaction = Transaction(
            transaction_id=Transaction.generate_id(),
            timestamp=datetime.now(),
            account_number=self._from_account.get_account_number(),
            transaction_type=TransactionType.TRANSFER_OUT,
            amount=self._amount,
            balance_after=self._from_account.get_balance(),
            status="SUCCESS",
            description=f"Transfer to #{self._to_account.get_account_number()}",
            from_account=self._from_account.get_account_number(),
            to_account=self._to_account.get_account_number(),
        )

    def get_transaction(self) -> Optional[Transaction]:
        return self._transaction

    def getTransaction(self) -> Optional[Transaction]:
        return self.get_transaction()
