from abc import ABC, abstractmethod

class IAccount(ABC):
    """Pure Interface defining the contract for all bank accounts."""

    @property
    @abstractmethod
    def account_number() -> str:
        pass

    @property
    @abstractmethod
    def name() -> str:
        pass

    @property
    @abstractmethod
    def age() -> int:
        pass

    @property
    @abstractmethod
    def balance() -> float:
        pass

    @property
    @abstractmethod
    def status() -> str:
        pass

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    @abstractmethod
    def calculate_interest(self) -> float:
        pass

    @abstractmethod
    def display_account_info(self) -> None:
        pass

    @abstractmethod
    def validate_pin(self, entered_pin: str) -> bool:
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        pass
