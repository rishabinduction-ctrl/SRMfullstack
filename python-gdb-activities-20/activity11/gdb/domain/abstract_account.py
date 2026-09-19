# gdb/domain/abstract_account.py
from gdb.domain.iaccount import IAccount
from gdb.exceptions import (
    AccountException,
    InvalidAmountException,
    InsufficientBalanceException,
    InactiveAccountException,
    InvalidPinException
)

class AbstractAccount(IAccount):
    """Abstract Base Class implementing IAccount."""
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000") -> None:
        if not account_number or not account_number.strip():
            raise AccountException("Account number cannot be empty")
        if age < 18:
            raise AccountException("Account holder must be at least 18 years old")
        if balance < 0:
            raise InvalidAmountException("Initial balance cannot be negative")
        if not pin or len(pin) != 4 or not pin.isdigit():
            raise InvalidPinException("PIN must be exactly 4 digits")

        self._account_number: str = account_number
        self._name: str = name
        self._age: int = age
        self._balance: float = balance
        self._status: str = status
        self._pin: str = pin

    def deposit(self, amount: float) -> None:
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot deposit to inactive account: {self._account_number}")
        if amount <= 0:
            raise InvalidAmountException(f"Deposit amount must be strictly positive: {amount}")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if self._status.lower() != "active":
            raise InactiveAccountException(f"Cannot withdraw from inactive account: {self._account_number}")
        if amount <= 0:
            raise InvalidAmountException(f"Withdrawal amount must be strictly positive: {amount}")
        if amount > self._balance:
            raise InsufficientBalanceException("Insufficient balance")
        self._balance -= amount

    def validate_pin(self, entered_pin: str) -> bool:
        if entered_pin == self._pin:
            return True
        raise InvalidPinException("Invalid PIN entered")

    def display_account_info(self) -> None:
        print(f"Account Number: {self._account_number}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Balance: Rs {self._balance}")
        print(f"Account Type: {self.get_account_type()}")
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
    def status(self) -> str: return self._status
    @status.setter
    def status(self, status: str) -> None: self._status = status
