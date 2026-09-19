# gdb/domain/account_rules_engine.py
from typing import Dict, Any, Optional
from gdb.domain.account_rules_properties_loader import AccountRulesPropertiesLoader

class AccountRulesEngine:
    """Singleton rules engine managing business rules, minimum balances, interest rates, and daily limits."""

    _instance: Optional["AccountRulesEngine"] = None

    def __init__(self) -> None:
        self._rules: Dict[str, Dict[str, float]] = {}
        self._load_rules()

    @classmethod
    def get_instance(cls) -> "AccountRulesEngine":
        if cls._instance is None:
            cls._instance = AccountRulesEngine()
        return cls._instance

    @classmethod
    def getInstance(cls) -> "AccountRulesEngine":
        return cls.get_instance()

    def _load_rules(self) -> None:
        types = ["SAVINGS", "CURRENT", "FIXEDDEPOSIT", "SALARY"]
        for t in types:
            props = AccountRulesPropertiesLoader.load_rules(t.lower())
            self._rules[t] = {
                "min_balance": float(props.get("min.balance", 0.0)),
                "interest_rate": float(props.get("interest.rate", 0.0)),
                "limit_new": float(props.get("daily.transfer.limit.new", 50000.0)),
                "limit_standard": float(props.get("daily.transfer.limit.standard", 100000.0)),
                "limit_premium": float(props.get("daily.transfer.limit.premium", 200000.0)),
                "limit_privilege": float(props.get("daily.transfer.limit.privilege", 500000.0)),
            }

    def get_tier(self, tenure_years: int) -> str:
        if tenure_years <= 1:
            return "NEW"
        elif tenure_years <= 5:
            return "STANDARD"
        elif tenure_years <= 10:
            return "PREMIUM"
        else:
            return "PRIVILEGE"

    def getTier(self, tenure_years: int) -> str:
        return self.get_tier(tenure_years)

    def get_minimum_balance(self, account_type: str) -> float:
        t = account_type.upper().replace(" ", "").replace("_", "")
        return self._rules.get(t, {}).get("min_balance", 0.0)

    def getMinimumBalance(self, account_type: str) -> float:
        return self.get_minimum_balance(account_type)

    def get_interest_rate(self, account_type: str) -> float:
        t = account_type.upper().replace(" ", "").replace("_", "")
        return self._rules.get(t, {}).get("interest_rate", 0.0)

    def getInterestRate(self, account_type: str) -> float:
        return self.get_interest_rate(account_type)

    def get_daily_transfer_limit(self, account_type: str, tenure_years: int) -> float:
        # ============================================================
        # 📝 STEP 8: Implement get_daily_transfer_limit()
        #
        # INSTRUCTIONS:
        #   1. Normalise account_type the same way get_minimum_balance() does
        #      (upper-case, then remove spaces and underscores).
        #   2. Find the tenure tier with self.get_tier(tenure_years) -> "NEW", "STANDARD", "PREMIUM" or "PRIVILEGE".
        #   3. Build the rule key f"limit_{tier.lower()}" (e.g. "limit_new") -- _load_rules() stores each
        #      daily.transfer.limit.<tier> property under that key.
        #   4. Return self._rules.get(<normalised type>, {}).get(<key>, 0.0) so unknown types give 0.0.
        # ============================================================
        # TODO: look up the daily transfer limit for this account type and tenure tier
        raise NotImplementedError("TODO: Step 8 - implement get_daily_transfer_limit")

    def getDailyTransferLimit(self, account_type: str, tenure_years: int) -> float:
        return self.get_daily_transfer_limit(account_type, tenure_years)
