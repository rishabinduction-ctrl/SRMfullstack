# gdb/domain/account_rules_properties_loader.py
import os
from typing import Dict

class AccountRulesPropertiesLoader:
    """Loads configuration properties from config/rules properties files."""

    @staticmethod
    def load_rules(account_type: str) -> Dict[str, str]:
        filename = f"{account_type.lower()}.properties"
        paths = [
            os.path.join(os.getcwd(), "config", "rules", filename),
            os.path.join(os.path.dirname(__file__), "..", "..", "config", "rules", filename),
            os.path.join(os.getcwd(), "src", "main", "resources", "config", "rules", filename),
        ]
        
        props: Dict[str, str] = {}
        target_path = None
        for p in paths:
            if os.path.exists(p):
                target_path = p
                break

        if target_path and os.path.exists(target_path):
            with open(target_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        props[k.strip()] = v.strip()
        else:
            # Fallback default configuration
            defaults = {
                "savings": {"min.balance": "10000.0", "interest.rate": "4.0", "daily.transfer.limit.new": "50000.0", "daily.transfer.limit.standard": "100000.0", "daily.transfer.limit.premium": "200000.0", "daily.transfer.limit.privilege": "500000.0"},
                "current": {"min.balance": "25000.0", "interest.rate": "0.0", "daily.transfer.limit.new": "100000.0", "daily.transfer.limit.standard": "250000.0", "daily.transfer.limit.premium": "500000.0", "daily.transfer.limit.privilege": "1000000.0"},
                "fixeddeposit": {"min.balance": "50000.0", "interest.rate": "6.5", "daily.transfer.limit.new": "0.0", "daily.transfer.limit.standard": "0.0", "daily.transfer.limit.premium": "0.0", "daily.transfer.limit.privilege": "0.0"},
                "salary": {"min.balance": "0.0", "interest.rate": "3.5", "daily.transfer.limit.new": "75000.0", "daily.transfer.limit.standard": "150000.0", "daily.transfer.limit.premium": "300000.0", "daily.transfer.limit.privilege": "750000.0"},
            }
            props = defaults.get(account_type.lower(), {})
        return props
