# gdb/domain/account.py
from gdb.exceptions import (
    AccountException,
    InvalidAmountException,
    InsufficientBalanceException,
    InactiveAccountException,
    InvalidPinException
)

class Account:
    """Account Entity with strongly typed domain exception handling."""

    def __init__(self, account_number: str, name: str, age: int, balance: float, account_type: str, status: str = "Active", pin: str = "0000") -> None:
        # TODO (Step 2): Replace each ValueError below (your Activity 3 guards) with the matching custom exception:
        #   empty account number / age under 18 -> AccountException
        #   negative opening balance            -> InvalidAmountException
        #   PIN not exactly 4 digits            -> InvalidPinException
        if not account_number or not account_number.strip():
            raise ValueError("Account number cannot be empty")
        if age < 18:
            raise ValueError("Account holder must be at least 18 years old")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        if not pin or len(pin) != 4 or not pin.isdigit():
            raise ValueError("PIN must be exactly 4 digits")

        self._account_number: str = account_number
        self._name: str = name
        self._age: int = age
        self._balance: float = balance
        self._account_type: str = account_type
        self._status: str = status
        self._pin: str = pin

    def deposit(self, amount: float) -> None:
        # TODO (Step 2): This method no longer returns True/False. Replace each `return False` with a raise:
        #   account not active -> InactiveAccountException
        #   amount <= 0        -> InvalidAmountException
        #   On success just add the amount to the balance (no return value).
        if self._status.lower() != "active":
            return False
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> None:
        # TODO (Step 2): This method no longer returns True/False. Replace each `return False` with a raise:
        #   account not active     -> InactiveAccountException
        #   amount <= 0            -> InvalidAmountException
        #   amount > self._balance -> InsufficientBalanceException
        #   On success just subtract the amount from the balance (no return value).
        if self._status.lower() != "active":
            return False
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def validate_pin(self, entered_pin: str) -> bool:
        # TODO (Step 2): Raise InvalidPinException when entered_pin does not match self._pin;
        #   return True when it matches.
        return self._pin == entered_pin

    def display_account_info(self) -> None:
        print(f"Account Number: {self._account_number}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Balance: Rs {self._balance}")
        print(f"Account Type: {self._account_type}")
        print(f"Status: {self._status}")

    @property
    def account_number(self) -> str: return self._account_number
    @property
    def name(self) -> str: return self._name
    @property
    def age(self) -> int: return self._age
    @property
    def balance(self) -> float: return self._balance
    @property
    def account_type(self) -> str: return self._account_type
    @property
    def status(self) -> str: return self._status
    @status.setter
    def status(self, status: str) -> None: self._status = status
