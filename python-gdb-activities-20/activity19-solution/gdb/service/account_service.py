# gdb/service/account_service.py
from typing import Dict, List, Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.account_factory import AccountFactory
from gdb.domain.transaction import Transaction
from gdb.service.transfer_service import TransferService
from gdb.logging.transaction_logger import TransactionLogger
from gdb.command.deposit_command import DepositCommand
from gdb.command.withdraw_command import WithdrawCommand
from gdb.command.transfer_command import TransferCommand
from gdb.exceptions.account_exception import AccountException
from gdb.exceptions.invalid_pin_exception import InvalidPinException

class AccountService:
    """Service facade providing high-level bank operations, account lifecycle, and transactions."""

    def __init__(self, logger: TransactionLogger) -> None:
        self._accounts: Dict[int, IAccount] = {}
        self._logger = logger
        self._transfer_service = TransferService()
        self._next_account_number = 1001

    def open_account(self, account_type: str, name: str, age: int, initial_balance: float, tenure_years: int = 0) -> IAccount:
        acc_no = self._next_account_number
        acc = AccountFactory.create_account(account_type, acc_no, name, age, initial_balance, tenure_years)
        self._accounts[acc_no] = acc
        self._next_account_number += 1
        return acc

    def openAccount(self, account_type: str, name: str, age: int, initial_balance: float, tenure_years: int = 0) -> IAccount:
        return self.open_account(account_type, name, age, initial_balance, tenure_years)

    def get_account(self, account_number: int) -> Optional[IAccount]:
        return self._accounts.get(int(account_number))

    def getAccount(self, account_number: int) -> Optional[IAccount]:
        return self.get_account(account_number)

    def deposit(self, account_number: int, amount: float) -> Transaction:
        acc = self.get_account(account_number)
        if acc is None:
            raise AccountException(f"Account #{account_number} not found")
        cmd = DepositCommand(acc, amount)
        cmd.execute()
        txn = cmd.get_transaction()
        if txn is not None:
            self._logger.log(txn)
        return txn

    def withdraw(self, account_number: int, amount: float, pin: int) -> Transaction:
        acc = self.get_account(account_number)
        if acc is None:
            raise AccountException(f"Account #{account_number} not found")
        cmd = WithdrawCommand(acc, amount, pin)
        cmd.execute()
        txn = cmd.get_transaction()
        if txn is not None:
            self._logger.log(txn)
        return txn

    def transfer(self, from_acc_no: int, to_acc_no: int, amount: float, pin: int) -> Transaction:
        from_acc = self.get_account(from_acc_no)
        to_acc = self.get_account(to_acc_no)
        if from_acc is None:
            raise AccountException(f"Source account #{from_acc_no} not found")
        if to_acc is None:
            raise AccountException(f"Destination account #{to_acc_no} not found")

        cmd = TransferCommand(self._transfer_service, from_acc, to_acc, amount, pin)
        cmd.execute()
        txn = cmd.get_transaction()
        if txn is not None:
            self._logger.log(txn)
        return txn

    def close_account(self, account_number: int, pin: int) -> None:
        acc = self.get_account(account_number)
        if acc is None:
            raise AccountException(f"Account #{account_number} not found")
        if not acc.verify_pin(pin):
            raise InvalidPinException("Incorrect PIN")
        acc.close_account()

    def closeAccount(self, account_number: int, pin: int) -> None:
        self.close_account(account_number, pin)

    def get_transaction_history(self) -> List[Transaction]:
        return self._logger.get_transactions()

    def getTransactionHistory(self) -> List[Transaction]:
        return self.get_transaction_history()

    def get_all_accounts(self) -> Dict[int, IAccount]:
        return dict(self._accounts)

    def getAllAccounts(self) -> Dict[int, IAccount]:
        return self.get_all_accounts()
