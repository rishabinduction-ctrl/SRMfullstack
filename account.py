"""Abstract base class Account representing generic bank account properties in Global Digital Bank (GDB).

Architectural Role:
Serves as the top-level abstract superclass for concrete account types (SavingsAccount, CurrentAccount, FixedDepositAccount).
Holds shared non-public fields (`_account_number`, `_account_holder_name`, `_age`, `_balance`, `_status`, `_pin`, `_opening_date`)
and declares abstract method contracts (`get_minimum_balance`, `get_account_type`, `get_interest_rate`, `can_withdraw`, `apply_monthly_interest`).
Throws custom domain exceptions exclusively for runtime failures and rule violations.
"""

from abc import ABC, abstractmethod
from gdb.exceptions.invalid_age_exception import InvalidAgeException
from gdb.exceptions.inactive_account_exception import InactiveAccountException
from gdb.exceptions.invalid_amount_exception import InvalidAmountException
from gdb.exceptions.invalid_pin_exception import InvalidPinException
from gdb.exceptions.insufficient_balance_exception import InsufficientBalanceException

class Account(ABC):
    """Abstract Base Class defining shared banking attributes and abstract contract methods."""

    def __init__(self, account_number: int, name: str, age: int, initial_balance: float) -> None:
        """Abstract Account constructor initializing protected state fields with precondition checks.

        Args:
            account_number (int): Unique integer identifying the account.
            name (str): Full customer legal holder name.
            age (int): Customer age in years.
            initial_balance (float): Opening deposit balance in Rs.

        Raises:
            InvalidAgeException: If customer age is under 18 years or name is empty.
        """
        # Precondition Check 1: Enforce legal customer age policy (must be >= 18 years old)
        if age < 18:
            # Raise custom domain exception detailing underage violation
            raise InvalidAgeException(f"Customer must be at least 18 years old. Provided: {age}")
            
        # Precondition Check 2: Enforce non-empty customer legal holder name policy
        if not name or not name.strip():
            # Raise custom domain exception detailing empty name violation
            raise InvalidAgeException("Name cannot be empty")

        # Assign unique account integer identifier to protected field
        self._account_number: int = account_number
        
        # Assign customer legal holder name string to protected field
        self._account_holder_name: str = name
        
        # Assign customer age integer in years to protected field
        self._age: int = age
        
        # Assign current monetary balance float in Indian Rupees (Rs.) to protected field
        self._balance: float = initial_balance
        
        # Invariant default lifecycle status initialization: newly created accounts enter Active status
        self._status: str = "Active"
        
        # Initialize authorization PIN to None (unconfigured state)
        self._pin: int | None = None
        
        # Store opening date timestamp string in ISO format
        self._opening_date: str = "2026-08-28"

    # =========================================================================
    # Abstract Method Contracts (Must be implemented by concrete subclasses)
    # =========================================================================

    @abstractmethod
    def get_minimum_balance(self) -> float:
        """Returns required minimum balance for specific account type in Rs."""
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        """Returns classification category string of account type."""
        pass

    @abstractmethod
    def get_interest_rate(self) -> float:
        """Returns per-annum interest rate percentage assigned to account."""
        pass

    @abstractmethod
    def can_withdraw(self, amount: float) -> bool:
        """Evaluates whether withdrawal amount is permitted under account type rules."""
        pass

    @abstractmethod
    def apply_monthly_interest(self) -> None:
        """Calculates and credits monthly interest to balance."""
        pass

    # =========================================================================
    # Concrete Shared Banking Operations
    # =========================================================================

    def deposit(self, amount: float) -> None:
        """Deposits positive monetary amount into an Active account.

        Args:
            amount (float): Monetary value to credit in Rs.

        Raises:
            InactiveAccountException: If account status is not Active.
            InvalidAmountException: If deposit amount is <= 0.
        """
        # Precondition Check 1: Enforce Active lifecycle status state
        if self._status != "Active":
            # Raise exception indicating inactive account state
            raise InactiveAccountException("Account is inactive.")
            
        # Precondition Check 2: Validate positive deposit monetary amount
        if amount <= 0:
            # Raise exception detailing negative or zero amount error
            raise InvalidAmountException(f"Deposit amount must be positive. Provided: Rs. {amount}")
            
        # State Mutation: Credit positive deposit amount to current account balance
        self._balance += amount

    def withdraw(self, amount: float, pin: int) -> None:
        """Withdraws amount after verifying status, PIN, and delegating checks to can_withdraw().

        Args:
            amount (float): Monetary value to deduct in Rs.
            pin (int): 4-digit authorization PIN integer.

        Raises:
            InactiveAccountException: If account status is not Active.
            InvalidPinException: If PIN is missing or incorrect.
            InvalidAmountException: If amount is <= 0.
            InsufficientBalanceException: If can_withdraw() returns False.
        """
        # Precondition Check 1: Status Lifecycle Active Check
        if self._status != "Active":
            raise InactiveAccountException("Account is inactive.")
            
        # Precondition Check 2: PIN Configuration Check
        if self._pin is None:
            raise InvalidPinException("PIN not set for this account")
            
        # Precondition Check 3: PIN Authorization Check
        if self._pin != pin:
            raise InvalidPinException("Incorrect PIN")
            
        # Precondition Check 4: Positive Monetary Amount Check
        if amount <= 0:
            raise InvalidAmountException(f"Amount must be positive. Provided: Rs. {amount}")
            
        # Precondition Check 5: Delegate liquidity evaluation to concrete subclass implementation
        if not self.can_withdraw(amount):
            raise InsufficientBalanceException(f"Withdrawal not allowed. Available: Rs. {self.get_available_balance()}, Requested: Rs. {amount}")

        # State Mutation: Deduct authorized withdrawal amount from account balance
        self._balance -= amount

    def close_account(self) -> None:
        """Transitions account status state to Inactive.

        Raises:
            InactiveAccountException: If account is already closed.
        """
        # Precondition Check: Reject closure if account is already Inactive
        if self._status != "Active":
            raise InactiveAccountException("Account is already closed")
            
        # State Mutation: Update status property to Inactive
        self._status = "Inactive"

    def reopen_account(self) -> None:
        """Transitions account status state to Active.

        Raises:
            InactiveAccountException: If account is already active.
        """
        # Precondition Check: Reject reopening if account is already Active
        if self._status == "Active":
            raise InactiveAccountException("Account is already active")
            
        # State Mutation: Update status property to Active
        self._status = "Active"

    def set_pin(self, pin: int) -> None:
        """Configures a 4-digit security authorization PIN (1000 to 9999).

        Args:
            pin (int): 4-digit PIN integer.

        Raises:
            InvalidPinException: If PIN is outside 1000-9999 range.
        """
        # Precondition Check: Validate 4-digit integer boundaries (1000 <= pin <= 9999)
        if not (1000 <= pin <= 9999):
            raise InvalidPinException(f"PIN must be a 4-digit number (1000-9999). Provided: {pin}")
            
        # State Mutation: Set private PIN field
        self._pin = pin

    def verify_pin(self, pin: int) -> bool:
        """Verifies supplied PIN integer against configured account PIN."""
        return self._pin is not None and self._pin == pin

    def has_pin(self) -> bool:
        """Checks whether authorization PIN has been configured."""
        return self._pin is not None

    def get_available_balance(self) -> float:
        """Returns total current available balance float."""
        return self._balance

    # Property Accessors
    @property
    def account_number(self) -> int: return self._account_number
    @property
    def account_holder_name(self) -> str: return self._account_holder_name
    @property
    def age(self) -> int: return self._age
    @property
    def balance(self) -> float: return self._balance
    @property
    def status(self) -> str: return self._status
    @property
    def opening_date(self) -> str: return self._opening_date
