# gdb/domain/account.py
from datetime import datetime, date
from typing import Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.account_rules_engine import AccountRulesEngine
from gdb.exceptions.invalid_age_exception import InvalidAgeException
from gdb.exceptions.invalid_amount_exception import InvalidAmountException
from gdb.exceptions.invalid_pin_exception import InvalidPinException
from gdb.exceptions.inactive_account_exception import InactiveAccountException
from gdb.exceptions.insufficient_balance_exception import InsufficientBalanceException

try:
    from gdb.domain.transaction import Transaction
    from gdb.domain.transaction_type import TransactionType
except ImportError:
    Transaction = None
    TransactionType = None

class Account(IAccount):
    """Abstract Base Class Account implementing core state, validations, and daily limit tracking."""

    def __init__(self, account_number: int, name: str, age: int, initial_balance: float, tenure_years: int = 0) -> None:
        if age < 18:
            raise InvalidAgeException(f"Customer must be at least 18 years old. Provided: {age}")
        if not name or not name.strip():
            raise InvalidAgeException("Name cannot be empty")

        self._account_number = int(account_number)
        self._name = name.strip()
        self._age = age
        self._balance = float(initial_balance)
        self._status = "Active"
        self._pin: Optional[int] = None
        self._opening_date = "2026-08-28"
        self._tenure_years = max(0, tenure_years)
        self._daily_transfer_total = 0.0
        self._last_transfer_date = datetime.now()

    def deposit(self, amount: float) -> None:
        if self._status != "Active":
            raise InactiveAccountException("Account is inactive.")
        if amount <= 0:
            raise InvalidAmountException(f"Deposit amount must be positive. Provided: Rs. {amount}")
        self._balance += amount

    def withdraw(self, amount: float, pin: int) -> None:
        if self._status != "Active":
            raise InactiveAccountException("Account is inactive.")
        if self._pin is None:
            raise InvalidPinException("PIN not set for this account")
        if self._pin != pin:
            raise InvalidPinException("Incorrect PIN")
        if amount <= 0:
            raise InvalidAmountException(f"Amount must be positive. Provided: Rs. {amount}")
        if not self.can_withdraw(amount):
            raise InsufficientBalanceException("Withdrawal not allowed")
        self._balance -= amount

    def close_account(self) -> None:
        if self._status != "Active":
            raise InactiveAccountException("Account is already closed / inactive.")
        self._status = "Inactive"

    def reopen_account(self) -> None:
        if self._status == "Active":
            raise InactiveAccountException("Account is already active.")
        self._status = "Active"

    def set_pin(self, pin: int) -> None:
        pin_int = int(pin)
        if pin_int < 1000 or pin_int > 9999:
            raise InvalidPinException(f"PIN must be a 4-digit number (1000-9999). Provided: {pin}")
        self._pin = pin_int

    def verify_pin(self, pin: int) -> bool:
        return self._pin is not None and self._pin == int(pin)

    def has_pin(self) -> bool:
        return self._pin is not None

    def is_active(self) -> bool:
        return self._status == "Active"

    def get_account_info(self) -> str:
        return f"Account #{self._account_number} | {self._name} ({self._age} yrs, Tenure: {self._tenure_years} yrs) | {self.get_account_type()} | Rs. {self._balance:.1f} | {self._status}"

    def get_account_number(self) -> int: return self._account_number
    def get_account_holder_name(self) -> str: return self._name
    def get_balance(self) -> float: return self._balance
    def get_opening_date(self) -> str: return self._opening_date
    def get_tenure_years(self) -> int: return self._tenure_years
    def set_tenure_years(self, tenure_years: int) -> None: self._tenure_years = max(0, tenure_years)

    def get_daily_transfer_limit(self) -> float:
        return AccountRulesEngine.get_instance().get_daily_transfer_limit(self.get_account_type(), self.get_tenure_years())

    def reset_daily_transfer_if_needed(self) -> None:
        if self._last_transfer_date is None or self._last_transfer_date.date() != date.today():
            self._daily_transfer_total = 0.0
            self._last_transfer_date = datetime.now()

    def get_remaining_daily_transfer_limit(self) -> float:
        self.reset_daily_transfer_if_needed()
        return max(0.0, self.get_daily_transfer_limit() - self._daily_transfer_total)

    def can_transfer(self, amount: float) -> bool:
        self.reset_daily_transfer_if_needed()
        return (self._daily_transfer_total + amount) <= self.get_daily_transfer_limit()

    def update_daily_transfer_total(self, amount: float) -> None:
        self.reset_daily_transfer_if_needed()
        self._daily_transfer_total += amount
        self._last_transfer_date = datetime.now()

    def get_daily_transfer_total(self) -> float:
        return self._daily_transfer_total

    def get_last_transfer_date(self) -> datetime:
        return self._last_transfer_date

    # CamelCase aliases
    def getDailyTransferLimit(self) -> float: return self.get_daily_transfer_limit()
    def getRemainingDailyTransferLimit(self) -> float: return self.get_remaining_daily_transfer_limit()
    def canTransfer(self, amount: float) -> bool: return self.can_transfer(amount)
    def updateDailyTransferTotal(self, amount: float) -> None: self.update_daily_transfer_total(amount)
    def resetDailyTransferIfNeeded(self) -> None: self.reset_daily_transfer_if_needed()
    def getDailyTransferTotal(self) -> float: return self.get_daily_transfer_total()
    def getLastTransferDate(self) -> datetime: return self.get_last_transfer_date()
    def depositWithTransaction(self, amount: float): return self.deposit_with_transaction(amount)
    def withdrawWithTransaction(self, amount: float, pin: int): return self.withdraw_with_transaction(amount, pin)

    def build_transaction(self, txn_type, amount: float, from_acc: int, to_acc: int, desc: str):
        if Transaction is None:
            return None
        return Transaction(
            transaction_id=Transaction.generate_id(),
            timestamp=datetime.now(),
            account_number=self._account_number,
            transaction_type=txn_type,
            amount=amount,
            balance_after=self._balance,
            status="SUCCESS",
            description=desc,
            from_account=from_acc,
            to_account=to_acc,
        )

    # ============================================================
    # 📝 STEP 7: Add deposit_with_transaction
    #
    # INSTRUCTIONS:
    #   1. Call self.deposit(amount) to perform standard deposit logic and validation.
    #   2. Build and return a Transaction object with type TransactionType.DEPOSIT using build_transaction().
    # ============================================================
    # TODO: perform deposit and return Transaction record
    def deposit_with_transaction(self, amount: float) -> Optional[Transaction]:
        return None

    # ============================================================
    # 📝 STEP 8: Add withdraw_with_transaction
    #
    # INSTRUCTIONS:
    #   1. Call self.withdraw(amount, pin) to perform standard withdrawal logic and validation.
    #   2. Build and return a Transaction object with type TransactionType.WITHDRAW using build_transaction().
    # ============================================================
    # TODO: perform withdraw and return Transaction record
    def withdraw_with_transaction(self, amount: float, pin: int) -> Optional[Transaction]:
        return None

