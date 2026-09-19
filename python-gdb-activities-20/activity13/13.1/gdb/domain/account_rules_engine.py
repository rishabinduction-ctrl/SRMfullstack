# gdb/domain/account_rules_engine.py

class AccountRulesEngine:
    """Centralized Business Rules Engine for banking policies."""

    @staticmethod
    def _normalize_type(account_type: str) -> str:
        if not account_type or not account_type.strip():
            return ""
        return account_type.strip().upper()

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        norm_type = AccountRulesEngine._normalize_type(account_type)
        if norm_type == "SAVINGS":
            return 1000.0
        return 0.0

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        norm_type = AccountRulesEngine._normalize_type(account_type)
        if norm_type == "SAVINGS":
            return 4.0
        elif norm_type == "FIXEDDEPOSIT":
            return 6.5
        return 0.0

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        norm_type = AccountRulesEngine._normalize_type(account_type)
        if norm_type == "CURRENT":
            return 10000.0
        return 0.0

    @staticmethod
    def validate_withdrawal(account_type: str, current_balance: float, amount: float) -> bool:
        min_balance = AccountRulesEngine.get_minimum_balance(account_type)
        overdraft_limit = AccountRulesEngine.get_overdraft_limit(account_type)
        
        floor = min_balance - overdraft_limit
        return (current_balance - amount) >= floor
