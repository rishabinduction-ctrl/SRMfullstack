"""Concrete CurrentAccount class extending abstract Account class.

Architectural Role:
Implements specialized banking behavior for Current Accounts in Global Digital Bank (GDB).
Enforces Rs. 1000.0 minimum balance constraint, 0.0% interest rate, and a Rs. 5000.0 Overdraft credit facility.

Key Invariants:
- Minimum Balance (`MINIMUM_BALANCE`): Rs. 1000.0.
- Overdraft Limit (`OVERDRAFT_LIMIT`): Rs. 5000.0.
- Interest Rate (`INTEREST_RATE`): 0.0% p.a.
- Overdraft Tracking: Tracks drawn credit via `_overdraft_used` attribute.
"""

from gdb.domain.account import Account
from gdb.exceptions.minimum_balance_violation_exception import MinimumBalanceViolationException
from gdb.exceptions.inactive_account_exception import InactiveAccountException
from gdb.exceptions.invalid_pin_exception import InvalidPinException
from gdb.exceptions.invalid_amount_exception import InvalidAmountException
from gdb.exceptions.insufficient_balance_exception import InsufficientBalanceException

class CurrentAccount(Account):
    """Current Account subclass with Rs. 5000.0 overdraft credit facility."""

    # Class-Level Invariant Constants
    MINIMUM_BALANCE: float = 1000.0
    INTEREST_RATE: float = 0.0
    OVERDRAFT_LIMIT: float = 5000.0

    def __init__(self, account_number: int, name: str, age: int, initial_balance: float) -> None:
        """Constructs CurrentAccount verifying initial deposit against Rs. 1000.0 minimum requirement.

        Args:
            account_number (int): Unique integer identifying the account.
            name (str): Full customer legal name.
            age (int): Customer age in years.
            initial_balance (float): Opening deposit balance in Rs.

        Raises:
            MinimumBalanceViolationException: If initial_balance < Rs. 1000.0.
        """
        # Call abstract Account superclass constructor
        super().__init__(account_number, name, age, initial_balance)
        
        # Precondition Check: Enforce Rs. 1000.0 minimum opening deposit requirement
        if initial_balance < self.MINIMUM_BALANCE:
            raise MinimumBalanceViolationException(f"Current account requires minimum balance of Rs. {self.MINIMUM_BALANCE}. Provided: Rs. {initial_balance}")
            
        # Initialize drawn overdraft tracker to zero
        self._overdraft_used: float = 0.0

    def get_minimum_balance(self) -> float:
        """Returns required minimum balance for Current Account (Rs. 1000.0)."""
        return self.MINIMUM_BALANCE

    def get_account_type(self) -> str:
        """Returns classification category string ("Current")."""
        return "Current"

    def get_interest_rate(self) -> float:
        """Returns per-annum interest rate percentage (0.0%)."""
        return self.INTEREST_RATE

    def can_withdraw(self, amount: float) -> bool:
        """Evaluates maximum allowable withdrawal including available overdraft credit.

        Args:
            amount (float): Requested withdrawal amount in Rs.

        Returns:
            bool: True if amount <= (balance - min_bal + overdraft_limit - overdraft_used).
        """
        # Calculate maximum available liquidity including overdraft limit
        max_withdraw = self._balance - self.MINIMUM_BALANCE + self.OVERDRAFT_LIMIT - self._overdraft_used
        # Return True if requested amount is within available liquidity boundary
        return amount <= max_withdraw

    def apply_monthly_interest(self) -> None:
        """No-op method: Current accounts do not earn interest (0.0% p.a.)."""
        pass

    def withdraw(self, amount: float, pin: int) -> None:
        """Overrides withdraw to manage balance deduction and overdraft tracking when balance drops below Rs. 1000.0.

        Args:
            amount (float): Monetary amount to withdraw in Rs.
            pin (int): 4-digit authorization PIN integer.

        Raises:
            InactiveAccountException: If status is not Active.
            InvalidPinException: If PIN is missing or incorrect.
            InvalidAmountException: If amount is <= 0.
            InsufficientBalanceException: If amount exceeds available liquidity + overdraft.
        """
        # Check 1: Status Lifecycle Precondition Check
        if self._status != "Active":
            raise InactiveAccountException("Account is inactive.")
            
        # Check 2: Security PIN Configuration Precondition Check
        if self._pin is None:
            raise InvalidPinException("PIN not set for this account")
            
        # Check 3: Security PIN Match Precondition Check
        if self._pin != pin:
            raise InvalidPinException("Incorrect PIN")
            
        # Check 4: Positive Amount Precondition Check
        if amount <= 0:
            raise InvalidAmountException(f"Amount must be positive. Provided: Rs. {amount}")
            
        # Check 5: Overdraft Liquidity Precondition Check
        if not self.can_withdraw(amount):
            raise InsufficientBalanceException(f"Insufficient funds. Available: Rs. {self.get_available_balance()} (including overdraft), Requested: Rs. {amount}")

        # Compute post-withdrawal balance
        new_balance = self._balance - amount
        
        # Check if withdrawal draws into overdraft credit limit (balance drops below Rs. 1000.0 min)
        if new_balance < self.MINIMUM_BALANCE:
            # Calculate required overdraft draw amount
            overdraft_amt = self.MINIMUM_BALANCE - new_balance
            # Increment drawn overdraft credit tracker
            self._overdraft_used += overdraft_amt
            
        # State Mutation: Update account balance
        self._balance = new_balance

    @property
    def overdraft_limit(self) -> float:
        """Total assigned overdraft credit limit (Rs. 5000.0)."""
        return self.OVERDRAFT_LIMIT

    @property
    def overdraft_used(self) -> float:
        """Total drawn overdraft credit amount in Rs."""
        return self._overdraft_used

    @property
    def available_overdraft(self) -> float:
        """Remaining available overdraft credit in Rs."""
        return self.OVERDRAFT_LIMIT - self._overdraft_used

    def repay_overdraft(self, amount: float) -> None:
        """Repays drawn overdraft credit.

        Args:
            amount (float): Repayment monetary amount in Rs.

        Raises:
            InvalidAmountException: If repayment amount is <= 0.
            InsufficientBalanceException: If repayment amount exceeds drawn overdraft balance.
        """
        # Precondition Check 1: Validate positive repayment amount
        if amount <= 0:
            raise InvalidAmountException("Repayment amount must be positive")
            
        # Precondition Check 2: Validate repayment does not exceed drawn overdraft balance
        if amount > self._overdraft_used:
            raise InsufficientBalanceException("Repayment amount exceeds overdraft used")
            
        # State Mutation: Deduct repaid amount from drawn overdraft balance
        self._overdraft_used -= amount
        
        # State Mutation: Restore account balance
        self._balance += amount

    def get_available_balance(self) -> float:
        """Returns total available funds including remaining overdraft credit."""
        return self._balance - self.MINIMUM_BALANCE + self.OVERDRAFT_LIMIT - self._overdraft_used
