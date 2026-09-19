# gdb/domain/account.py

class Account:
    """Pure Domain Entity representing a basic Bank Account in Global Digital Bank (GDB)."""

    def __init__(self, account_number: str, name: str, age: int, balance: float, account_type: str, status: str = "Active") -> None:
        self._account_number: str = account_number
        self._name: str = name
        self._age: int = age
        self._balance: float = balance
        self._account_type: str = account_type
        self._status: str = status

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def display_account_info(self) -> None:
        print(f"Account Number: {self._account_number}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Balance: Rs {self._balance}")
        print(f"Account Type: {self._account_type}")
        print(f"Status: {self._status}")

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def account_type(self) -> str:
        return self._account_type

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        self._status = status
