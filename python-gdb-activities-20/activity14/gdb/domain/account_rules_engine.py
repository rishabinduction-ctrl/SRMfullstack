# gdb/domain/account_rules_engine.py
from gdb.domain.account_rules_properties_loader import AccountRulesPropertiesLoader

class AccountRulesEngine:
    """Properties-Driven Rules Engine."""

    @staticmethod
    def _get_property(account_type: str, key: str) -> float:
        props = AccountRulesPropertiesLoader.load_rules(account_type)
        value = props.get(key)
        if value is None or value == "":
            return 0.0
        try:
            return float(value)
        except (ValueError, TypeError):
            return 0.0

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        return AccountRulesEngine._get_property(account_type, "minBalance")

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        return AccountRulesEngine._get_property(account_type, "interestRate")

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        return AccountRulesEngine._get_property(account_type, "overdraftLimit")

    @staticmethod
    def validate_withdrawal(account_type: str, current_balance: float, amount: float) -> bool:
        min_balance = AccountRulesEngine.get_minimum_balance(account_type)
        overdraft_limit = AccountRulesEngine.get_overdraft_limit(account_type)
        floor = min_balance - overdraft_limit
        return (current_balance - amount) >= floor
