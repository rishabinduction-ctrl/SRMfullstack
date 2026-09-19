# gdb/domain/account_rules_engine.py

class AccountRulesEngine:
    """Centralized Business Rules Engine for banking policies."""

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        if account_type and account_type.strip().upper() == "SAVINGS":
            return 1000.0
        return 0.0

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        if not account_type:
            return 0.0
        t = account_type.strip().upper()
        if t == "SAVINGS":
            return 4.0
        elif t == "FIXEDDEPOSIT":
            return 6.5
        return 0.0

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        if account_type and account_type.strip().upper() == "CURRENT":
            return 10000.0
        return 0.0

    @staticmethod
    def validate_withdrawal(account_type: str, current_balance: float, amount: float) -> bool:
        min_bal = AccountRulesEngine.get_minimum_balance(account_type)
        overdraft = AccountRulesEngine.get_overdraft_limit(account_type)
        return (current_balance - amount) >= (min_bal - overdraft)
