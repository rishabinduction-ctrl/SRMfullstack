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

    # ============================================================
    # 📝 STEP 1: Constructor & Fields
    #
    # INSTRUCTIONS:
    #   1. self._accounts: Dict[int, IAccount] -- an empty registry of accounts keyed by account number.
    #   2. self._logger -- the TransactionLogger passed in.
    #   3. self._transfer_service -- a new TransferService().
    #   4. self._next_account_number -- the next number to hand out, starting at 1001.
    # ============================================================
    # TODO: create the account registry, keep the logger, create the transfer service and set the first account number
    def __init__(self, logger: TransactionLogger) -> None:
        raise NotImplementedError("TODO: Step 1 - implement AccountService constructor")

    # ============================================================
    # 📝 STEP 2: Implement open_account()
    # ============================================================
    # TODO: create account via AccountFactory, store in dict, increment next_account_number, return account
    def open_account(self, account_type: str, name: str, age: int, initial_balance: float, tenure_years: int = 0) -> IAccount:
        raise NotImplementedError("TODO: Step 2 - implement open_account")

    # ============================================================
    # 📝 STEP 3: Implement get_account()
    #
    # INSTRUCTIONS:
    #   Return the account stored under account_number (convert it to int first), or None if there is none.
    #
    # HINT: dict.get() returns None for a missing key.
    # ============================================================
    # TODO: return account from dict or None
    def get_account(self, account_number: int) -> Optional[IAccount]:
        raise NotImplementedError("TODO: Step 3 - implement get_account")

    # ============================================================
    # 📝 STEP 4: Implement deposit()
    # ============================================================
    # TODO: execute DepositCommand, log transaction, return transaction
    def deposit(self, account_number: int, amount: float) -> Transaction:
        raise NotImplementedError("TODO: Step 4 - implement deposit")

    # ============================================================
    # 📝 STEP 5: Implement withdraw()
    # ============================================================
    # TODO: execute WithdrawCommand, log transaction, return transaction
    def withdraw(self, account_number: int, amount: float, pin: int) -> Transaction:
        raise NotImplementedError("TODO: Step 5 - implement withdraw")

    # ============================================================
    # 📝 STEP 6: Implement transfer()
    # ============================================================
    # TODO: execute TransferCommand, log transaction, return transaction
    def transfer(self, from_acc_no: int, to_acc_no: int, amount: float, pin: int) -> Transaction:
        raise NotImplementedError("TODO: Step 6 - implement transfer")

    # ============================================================
    # 📝 STEP 7: Implement close_account()
    # ============================================================
    # TODO: verify pin, close account
    def close_account(self, account_number: int, pin: int) -> None:
        raise NotImplementedError("TODO: Step 7 - implement close_account")

    # ============================================================
    # 📝 STEP 8: Implement get_transaction_history()
    #
    # INSTRUCTIONS:
    #   Return every logged transaction by asking the logger (self._logger.get_transactions()).
    # ============================================================
    # TODO: return list of transactions from logger
    def get_transaction_history(self) -> List[Transaction]:
        raise NotImplementedError("TODO: Step 8 - implement get_transaction_history")
