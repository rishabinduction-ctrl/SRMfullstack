# gdb/domain/bank_account.py
# ACTIVITY 10: Replace this file with your completed Activity 9 version before writing the tests.
from abc import ABC, abstractmethod
from gdb.exceptions import (
    AccountException,
    InvalidAmountException,
    InsufficientBalanceException,
    InactiveAccountException,
    InvalidPinException
)

class BankAccount(ABC):
    """Abstract Base Class modeling generic Bank Account."""
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

    # TODO (Step 1): Turn the two methods below into abstract contracts by decorating each one with
    #   @abstractmethod (the body can then simply be `pass`). Afterwards BankAccount itself can no longer
    #   be instantiated, and every subclass is forced to override both methods.
    def calculate_interest(self) -> float:
        """Abstract method enforced on all subclasses."""
        raise NotImplementedError("TODO: declare calculate_interest() as an @abstractmethod")

    def get_account_type(self) -> str:
        """Abstract method returning product type string."""
        raise NotImplementedError("TODO: declare get_account_type() as an @abstractmethod")

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
            raise InsufficientBalanceException(f"Insufficient balance")
        self._balance -= amount

    def display_account_info(self) -> None:
        # TODO (Step 1): Make this a template method. BankAccount no longer stores _account_type, so replace
        #   self._account_type below with a call to the abstract hook self.get_account_type().
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
    def status(self) -> str: return self._status
    @status.setter
    def status(self, status: str) -> None: self._status = status
