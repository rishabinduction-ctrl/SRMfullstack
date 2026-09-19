# gdb/domain/account_rules_engine.py

class AccountRulesEngine:
    """Dynamic Dictionary-based Rules Engine."""

    _RULES: dict = {
        "SAVINGS": {
            "min_balance": 1000.0,
            "interest_rate": 4.0,
            "overdraft_limit": 0.0,
        },
        "CURRENT": {
            "min_balance": 0.0,
            "interest_rate": 0.0,
            "overdraft_limit": 10000.0,
        },
        "SALARY": {
            "min_balance": 0.0,
            "interest_rate": 0.0,
            "overdraft_limit": 0.0,
        },
        "FIXEDDEPOSIT": {
            "min_balance": 0.0,
            "interest_rate": 6.5,
            "overdraft_limit": 0.0,
        },
    }

    @classmethod
    def get_minimum_balance(cls, account_type: str) -> float:
        if not account_type or not account_type.strip():
            return 0.0
        rules = cls._RULES.get(account_type.strip().upper(), {})
        return rules.get("min_balance", 0.0)

    @classmethod
    def get_interest_rate(cls, account_type: str) -> float:
        if not account_type or not account_type.strip():
            return 0.0
        rules = cls._RULES.get(account_type.strip().upper(), {})
        return rules.get("interest_rate", 0.0)

    @classmethod
    def get_overdraft_limit(cls, account_type: str) -> float:
        if not account_type or not account_type.strip():
            return 0.0
        rules = cls._RULES.get(account_type.strip().upper(), {})
        return rules.get("overdraft_limit", 0.0)

    @classmethod
    def validate_withdrawal(cls, account_type: str, current_balance: float, amount: float) -> bool:
        min_bal = cls.get_minimum_balance(account_type)
        overdraft = cls.get_overdraft_limit(account_type)
        return (current_balance - amount) >= (min_bal - overdraft)

    @classmethod
    def validate_withdrawal(cls, account_type: str, current_balance: float, amount: float) -> bool:
        min_bal = cls.get_minimum_balance(account_type)
        overdraft = cls.get_overdraft_limit(account_type)
        return (current_balance - amount) >= (min_bal - overdraft)
