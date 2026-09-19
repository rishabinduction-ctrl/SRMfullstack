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

        # Daily transfer tracking -- provided for you. Steps 3-7 read and update these two fields:
        #   _daily_transfer_total : sum of all transfers sent today (starts at 0.0)
        #   _last_transfer_date   : when that total was last updated (starts at now)
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
        # ============================================================
        # 📝 STEP 3: Get Daily Transfer Limit
        #
        # INSTRUCTIONS:
        #   1. Ask the rules engine for this account's limit:
        #      AccountRulesEngine.get_instance().get_daily_transfer_limit(self.get_account_type(), self.get_tenure_years())
        #   2. Return that value.
        #
        # HINT: The limit depends on account type and tenure tier, e.g. a NEW Savings account gets Rs. 50,000.
        # ============================================================
        # TODO: return the daily transfer limit from the rules engine
        raise NotImplementedError("TODO: Step 3 - implement get_daily_transfer_limit")

    def get_remaining_daily_transfer_limit(self) -> float:
        # ============================================================
        # 📝 STEP 4: Get Remaining Daily Limit
        #
        # INSTRUCTIONS:
        #   1. Call self.reset_daily_transfer_if_needed() so yesterday's transfers are not counted.
        #   2. Return self.get_daily_transfer_limit() - self._daily_transfer_total, but never less than 0.
        #
        # HINT: max(0.0, ...) keeps the result from going negative.
        # ============================================================
        # TODO: return how much can still be transferred today
        raise NotImplementedError("TODO: Step 4 - implement get_remaining_daily_transfer_limit")

    def can_transfer(self, amount: float) -> bool:
        # ============================================================
        # 📝 STEP 5: Check Amount Against Daily Limit
        #
        # INSTRUCTIONS:
        #   1. Call self.reset_daily_transfer_if_needed().
        #   2. Return True if self._daily_transfer_total + amount <= self.get_daily_transfer_limit(), otherwise False.
        #
        # HINT: A limit of 0 (Fixed Deposit) must block every transfer.
        # ============================================================
        # TODO: return whether this amount fits within today's limit
        raise NotImplementedError("TODO: Step 5 - implement can_transfer")

    def update_daily_transfer_total(self, amount: float) -> None:
        # ============================================================
        # 📝 STEP 6: Record A Completed Transfer
        #
        # INSTRUCTIONS:
        #   1. Call self.reset_daily_transfer_if_needed().
        #   2. Add amount to self._daily_transfer_total.
        #   3. Set self._last_transfer_date to datetime.now().
        # ============================================================
        # TODO: add the amount to today's running total
        raise NotImplementedError("TODO: Step 6 - implement update_daily_transfer_total")

    def reset_daily_transfer_if_needed(self) -> None:
        # ============================================================
        # 📝 STEP 7: Reset The Total On A New Day
        #
        # INSTRUCTIONS:
        #   1. Compare self._last_transfer_date.date() with date.today().
        #   2. If they differ, set self._daily_transfer_total to 0.0 and self._last_transfer_date to datetime.now().
        #
        # HINT: Compare dates, not date-times -- two transfers an hour apart are still on the same day.
        # ============================================================
        # TODO: reset the daily total when the calendar day has changed
        raise NotImplementedError("TODO: Step 7 - implement reset_daily_transfer_if_needed")

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
