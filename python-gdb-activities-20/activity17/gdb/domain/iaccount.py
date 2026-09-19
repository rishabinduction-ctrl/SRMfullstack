# gdb/domain/iaccount.py
from abc import ABC, abstractmethod
from typing import Optional, Any

class IAccount(ABC):
    """Enterprise Interface Contract defining standard public capabilities for all bank accounts."""

    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Deposit funds into account."""
        pass

    @abstractmethod
    def withdraw(self, amount: float, pin: int) -> None:
        """Withdraw funds using PIN verification."""
        pass

    @abstractmethod
    def get_balance(self) -> float:
        """Return current balance."""
        pass

    @abstractmethod
    def get_account_number(self) -> int:
        """Return account number."""
        pass

    @abstractmethod
    def get_account_holder_name(self) -> str:
        """Return holder name."""
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        """Return account type string."""
        pass

    @abstractmethod
    def get_opening_date(self) -> str:
        """Return account opening date."""
        pass

    @abstractmethod
    def is_active(self) -> bool:
        """Check if account is active."""
        pass

    @abstractmethod
    def get_minimum_balance(self) -> float:
        """Return required minimum balance."""
        pass

    @abstractmethod
    def get_interest_rate(self) -> float:
        """Return annual interest rate."""
        pass

    @abstractmethod
    def can_withdraw(self, amount: float) -> bool:
        """Check if withdrawal of amount is permissible."""
        pass

    @abstractmethod
    def set_pin(self, pin: int) -> None:
        """Set a 4-digit PIN."""
        pass

    @abstractmethod
    def verify_pin(self, pin: int) -> bool:
        """Verify entered PIN."""
        pass

    @abstractmethod
    def has_pin(self) -> bool:
        """Check if PIN has been configured."""
        pass

    @abstractmethod
    def close_account(self) -> None:
        """Close this account."""
        pass

    @abstractmethod
    def reopen_account(self) -> None:
        """Reopen a closed account."""
        pass

    @abstractmethod
    def get_account_info(self) -> str:
        """Return formatted summary info."""
        pass

    @abstractmethod
    def get_tenure_years(self) -> int:
        """Return customer tenure in years."""
        pass

    @abstractmethod
    def set_tenure_years(self, tenure_years: int) -> None:
        """Update customer tenure in years."""
        pass

    # Aliases for camelCase and property interop
    def getBalance(self) -> float: return self.get_balance()
    def getAccountNumber(self) -> int: return self.get_account_number()
    def getAccountHolderName(self) -> str: return self.get_account_holder_name()
    def getName(self) -> str: return self.get_account_holder_name()
    def getAccountType(self) -> str: return self.get_account_type()
    def getOpeningDate(self) -> str: return self.get_opening_date()
    def isActive(self) -> bool: return self.is_active()
    def getMinimumBalance(self) -> float: return self.get_minimum_balance()
    def getInterestRate(self) -> float: return self.get_interest_rate()
    def canWithdraw(self, amount: float) -> bool: return self.can_withdraw(amount)
    def setPin(self, pin: int) -> None: self.set_pin(pin)
    def verifyPin(self, pin: int) -> bool: return self.verify_pin(pin)
    def hasPin(self) -> bool: return self.has_pin()
    def closeAccount(self) -> None: self.close_account()
    def reopenAccount(self) -> None: self.reopen_account()
    def getAccountInfo(self) -> str: return self.get_account_info()
    def getTenureYears(self) -> int: return self.get_tenure_years()
    def setTenureYears(self, tenure_years: int) -> None: self.set_tenure_years(tenure_years)

    @property
    def balance(self) -> float: return self.get_balance()
    @property
    def account_number(self) -> int: return self.get_account_number()
    @property
    def name(self) -> str: return self.get_account_holder_name()
    @property
    def account_type(self) -> str: return self.get_account_type()
    @property
    def status(self) -> str: return "Active" if self.is_active() else "Inactive"
