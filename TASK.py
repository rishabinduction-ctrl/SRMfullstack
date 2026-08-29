
"""
Activity 3: Enhanced Account Model
===================================

In Activity 2, we implemented a basic `Account` class with core
account operations such as deposits, withdrawals, and balance tracking.

Today, we shall enhance the Account model to make it more robust, secure, and
closer to a real-world banking system.

Your Task
---------
Enhance the existing `Account` class by implementing the following:

1. Minimum Balance Rules
   - Savings accounts must maintain a minimum balance of Rs. 500.
   - Current accounts must maintain a minimum balance of Rs. 1000.
   - A withdrawal must be rejected if it causes the balance to fall
     below the applicable minimum balance.

2. Defensive Account Creation
   When creating an account:
   - If the customer's age is below 18, get a guardian's name & age and create account for customer
   - If the account type is invalid, default it to "Savings".
   - If the initial balance is below the minimum balance requirement,
     automatically set the balance to the applicable minimum balance.

3. Account Status
   Every account should have one of two states:
       - "Active"
       - "Inactive"

   Implement:
       - close_account()
       - reopen_account()

   Rules:
   - A closed account must not allow deposits or withdrawals.
   - Closing an already inactive account should fail.
   - Reopening an already active account should fail.

4. PIN Security
   Add support for an optional 4-digit PIN.

   Implement:
       - set_pin(pin)
       - verify_pin(pin)
       - has_pin()

   Rules:
   - Only PINs from 1000 to 9999 are valid.
   - If a PIN has been configured, withdrawals must provide
     the correct PIN.
   - If no PIN has been configured, withdrawals should continue
     to work without requiring a PIN.

5. Properties
   Continue exposing account information using read-only properties:
       - account_number
       - name
       - age
       - balance
       - account_type
       - status

Think About
-----------
- Why should minimum balances be stored as class constants?
- How can defensive programming prevent invalid account states?
- How should account status control financial operations?
- How can `None` be used to represent an unconfigured PIN?
- How can short-circuit boolean logic make PIN verification safe?

Example
-------
    account = Account(101, "Ravi", 17, 200, "Savings")

    # Age -> 18
    # Account Type -> Savings
    # Balance -> Rs. 500

    account.deposit(1000)
    account.set_pin(1234)

    account.withdraw(200, 1234)   # Allowed
    account.withdraw(200)         # Rejected - PIN required

    account.close_account()

    account.deposit(500)          # Rejected - account is inactive

    account.reopen_account()

Goal
----
Transform the basic Account model from Activity 2 into a more
defensive, state-aware, and secure banking domain model.

"""

# repo name
# rishabinduction-ctrl/SRMfullstack

# gdb/domain/account.py

class Account:
    MIN_BALANCE_SAVINGS: float = 500.0
    MIN_BALANCE_CURRENT: float = 1000.0

    def __init__(self, account_number: int, name: str, age: int, initial_balance: float, account_type: str) -> None:
        self._account_number = account_number
        self._name = name
        self._pin: int | None = None
        self._status = "Active"

        if age < 18:
            print(f"Creating account with age {age}")
            self.guardian = input("Enter guardian's name: ")
            self.guardian_age = int(input("Enter guardian's age: "))
            self._age = age
        else: self._age = age

        if account_type not in ("Savings", "Current"):
            print(f'Creating account with type "{account_type}"')
            print("Account type defaulted to: Savings")
            self._account_type = "Savings"
        else: self._account_type = account_type

        min_bal = self.get_minimum_balance()
        if initial_balance < min_bal:
            if self._account_type in ("Savings", "Current"):
                print(f"Creating {self._account_type} account with Rs. {initial_balance} (below minimum)")
                print(f"Balance auto-corrected to minimum: Rs. {min_bal}")
            self._balance = min_bal
        else: self._balance = initial_balance

    def get_minimum_balance(self) -> float:
        return self.MIN_BALANCE_SAVINGS if self._account_type == "Savings" else self.MIN_BALANCE_CURRENT

    def deposit(self, amount: float) -> bool:
        '''
        Enter the amount to be deposited.\n
        Make sure it is a positive float value\n
        The amount will add to the bank balance
        '''
        if self._status != "Active" or amount <= 0: return False
        self._balance += amount
        return True

    def withdraw(self, amount: float, pin: int | None = None) -> bool:
        if self._status != "Active": return False
        if self._pin is not None and (pin is None or self._pin != pin): return False
        if amount <= 0: return False
        if (self._balance - amount) < self.get_minimum_balance(): return False
        self._balance -= amount
        return True

    def close_account(self) -> bool:
        if self._status == "Inactive": return False
        self._status = "Inactive"
        return True

    def reopen_account(self) -> bool:
        if self._status == "Active": return False
        self._status = "Active"
        return True

    def set_pin(self, pin: int) -> bool:
        if 1000 <= pin <= 9999:
            self._pin = pin
            return True
        return False

    def verify_pin(self, pin: int) -> bool: return self._pin is not None and self._pin == pin
    def has_pin(self) -> bool: return self._pin is not None

    # @property
    # def account_number(self) -> int: return self._account_number
    # @property
    # def name(self) -> str: return self._name
    # @property
    # def age(self) -> int: return self._age
    # @property
    # def balance(self) -> float: return self._balance
    # @property
    # def account_type(self) -> str: return self._account_type
    # @property
    # def status(self) -> str: return self._status

