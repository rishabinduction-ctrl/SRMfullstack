# gdb/domain/account.py


class Account:
    """Pure Domain Entity representing a basic Bank Account in Global Digital Bank (GDB)."""

    def __init__(
        self,
        account_number: str,
        name: str,
        age: int,
        balance: float,
        account_type: str,
        status: str = "Active",
    ) -> None:
        # TODO (Step 1): Store every constructor argument in a protected instance attribute:
        #   self._account_number, self._name, self._age, self._balance, self._account_type, self._status
        self._account_number = account_number
        self._name = name
        self._age = age
        self._balance = balance
        self._account_type = account_type
        self._status = status

    def deposit(self, amount: float) -> bool:
        # TODO (Step 2): If amount > 0, add it to self._balance and return True.
        #   Otherwise (amount <= 0) return False and leave the balance unchanged.
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False

        raise NotImplementedError("TODO: implement Account.deposit()")

    def withdraw(self, amount: float) -> bool:
        # TODO (Step 3): If amount > 0 and amount <= self._balance, subtract it from self._balance and return True.
        #   Otherwise (zero, negative, or more than the balance) return False and leave the balance unchanged.
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

        raise NotImplementedError("TODO: implement Account.withdraw()")

    def display_account_info(self) -> None:
        # TODO (Step 4): Print every account detail on its own line, in this format:
        #   Account Number: ACC1001
        #   Name: Alice
        #   Age: 25
        #   Balance: Rs 5000.0
        #   Account Type: Savings
        #   Status: Active
        print(f"Account Number: {self._account_number}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Balance: {self._balance}")
        print(f"Account Type: {self._account_type}")
        print(f"Status: {self._status}")
        raise NotImplementedError("TODO: implement Account.display_account_info()")

    # Example read-only property -- follow this pattern for the remaining attributes.
    @property
    def account_number(self) -> str:
        return self._account_number

    # TODO (Step 4): Add @property getters for name, age, balance, account_type and status,
    #   and @<attribute>.setter setters for name, age and status.
    #   balance and account_type stay read-only: balance must only change through deposit()/withdraw().
    @property
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        return self._name

    @property
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age
        return self._age

    @property
    def get_balance(self):
        return self._balance

    @property
    def get_account_type(self):
        return self._account_type

    @property
    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status
        return self._status
