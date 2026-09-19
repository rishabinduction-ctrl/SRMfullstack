# gdb/domain/iaccount.py
from abc import ABC, abstractmethod

class IAccount(ABC):
    """Pure Interface defining the contract for all bank accounts."""
    @abstractmethod
    def deposit(self, amount: float) -> None: pass
    @abstractmethod
    def withdraw(self, amount: float) -> None: pass
    @abstractmethod
    def calculate_interest(self) -> float: pass
    @abstractmethod
    def display_account_info(self) -> None: pass
    @abstractmethod
    def validate_pin(self, entered_pin: str) -> bool: pass
    @property
    @abstractmethod
    def account_number(self) -> str: pass
    @property
    @abstractmethod
    def name(self) -> str: pass
    @property
    @abstractmethod
    def age(self) -> int: pass
    @property
    @abstractmethod
    def balance(self) -> float: pass
    @property
    @abstractmethod
    def status(self) -> str: pass
    @abstractmethod
    def get_account_type(self) -> str: pass
