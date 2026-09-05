"""Concrete SavingsAccount class extending abstract Account class.

Architectural Role:
Implements specialized banking behavior for Savings Accounts in Global Digital Bank (GDB).
Enforces Rs. 500.0 minimum balance constraint and 4.0% per-annum monthly compounding interest.

Key Invariants:
- Minimum Balance (`MINIMUM_BALANCE`): Rs. 500.0.
- Interest Rate (`INTEREST_RATE`): 4.0% p.a.
- Monthly Interest Accrual: `balance += balance * (4.0 / 100.0) / 12.0`.
"""

from gdb.domain.account import Account
from gdb.exceptions.minimum_balance_violation_exception import MinimumBalanceViolationException

class SavingsAccount(Account):
    """Savings Account subclass with 4.0% p.a. interest and Rs. 500.0 minimum balance."""

    # Class-Level Invariant Constants
    MINIMUM_BALANCE: float = 500.0
    INTEREST_RATE: float = 4.0

    def __init__(self, account_number: int, name: str, age: int, initial_balance: float) -> None:
        """Constructs SavingsAccount verifying opening balance against Rs. 500.0 minimum requirement.

        Args:
            account_number (int): Unique integer identifying the account.
            name (str): Full customer legal name.
            age (int): Customer age in years.
            initial_balance (float): Opening deposit balance in Rs.

        Raises:
            MinimumBalanceViolationException: If initial_balance < Rs. 500.0.
        """
        # Call abstract Account superclass constructor
        super().__init__(account_number, name, age, initial_balance)
        
        # Precondition Check: Enforce Rs. 500.0 minimum opening deposit requirement
        if initial_balance < self.MINIMUM_BALANCE:
            raise MinimumBalanceViolationException(f"Savings account requires minimum balance of Rs. {self.MINIMUM_BALANCE}. Provided: Rs. {initial_balance}")

    def get_minimum_balance(self) -> float:
        """Returns required minimum balance for Savings Account (Rs. 500.0)."""
        return self.MINIMUM_BALANCE

    def get_account_type(self) -> str:
        """Returns classification category string ("Savings")."""
        return "Savings"

    def get_interest_rate(self) -> float:
        """Returns per-annum interest rate percentage (4.0%)."""
        return self.INTEREST_RATE

    def can_withdraw(self, amount: float) -> bool:
        """Evaluates whether withdrawal amount leaves balance >= Rs. 500.0 minimum threshold.

        Args:
            amount (float): Requested withdrawal amount in Rs.

        Returns:
            bool: True if (balance - amount) >= Rs. 500.0; False otherwise.
        """
        # Evaluate post-withdrawal balance against Rs. 500.0 minimum limit boundary
        return (self._balance - amount) >= self.MINIMUM_BALANCE

    def apply_monthly_interest(self) -> None:
        """Calculates and credits monthly interest (4.0% p.a. / 12 months) directly to balance."""
        # Calculate monthly compounding interest amount: balance * (4.0 / 100) / 12
        monthly_interest = self._balance * (self.INTEREST_RATE / 100.0) / 12.0
        
        # State Mutation: Credit monthly interest to account balance
        self._balance += monthly_interest
