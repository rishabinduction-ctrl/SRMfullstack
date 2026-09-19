# gdb/domain/account.py
# ACTIVITY 4: Replace this file with your completed Activity 3 version before writing the tests.

class Account:
    """Enhanced Account Entity with defensive validation, PIN authentication, and status checks."""

    def __init__(self, account_number: str, name: str, age: int, balance: float, account_type: str, status: str = "Active", pin: str = "0000") -> None:
        # TODO (Step 1): Add defensive guards here, BEFORE any attribute is stored. Raise ValueError when:
        #   - account_number is None, empty, or only whitespace
        #   - age is below 18
        #   - balance is negative
        #   - pin is not exactly 4 digits (hint: len(pin) and pin.isdigit())

        self._account_number: str = account_number
        self._name: str = name
        self._age: int = age
        self._balance: float = balance
        self._account_type: str = account_type
        self._status: str = status
        self._pin: str = pin

    def validate_pin(self, entered_pin: str) -> bool:
        # TODO (Step 2): Return True if entered_pin matches self._pin, otherwise False
        #   (a wrong PIN and None must both return False).
        raise NotImplementedError("TODO: implement Account.validate_pin()")

    def deposit(self, amount: float) -> bool:
        # TODO (Step 3): Before anything else, return False if the account is not active
        #   (check self._status.lower() == "active"). The logic below is your Activity 1 code.
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        # TODO (Step 3): Before anything else, return False if the account is not active
        #   (check self._status.lower() == "active"). The logic below is your Activity 1 code.
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
