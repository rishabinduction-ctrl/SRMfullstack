# gdb/domain/account_rules_engine.py
from gdb.domain.account_rules_properties_loader import AccountRulesPropertiesLoader

class AccountRulesEngine:
    """Properties-Driven Rules Engine."""

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        props = AccountRulesPropertiesLoader.load_rules(account_type)
        return float(props.get("minBalance", 0.0))

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        props = AccountRulesPropertiesLoader.load_rules(account_type)
        return float(props.get("interestRate", 0.0))

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        props = AccountRulesPropertiesLoader.load_rules(account_type)
        return float(props.get("overdraftLimit", 0.0))
