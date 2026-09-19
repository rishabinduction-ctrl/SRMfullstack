# gdb/domain/account_rules_properties_loader.py
import os

class AccountRulesPropertiesLoader:
    """Utility loading external .properties files."""

    @staticmethod
    def load_rules(account_type: str) -> dict:
        if not account_type or not account_type.strip():
            return {}

        file_name = f"{account_type.strip().lower()}.properties"
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "..", "resources", "config", "rules", file_name)

        if not os.path.exists(file_path):
            return {}

        properties = {}
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        key, val = line.split("=", 1)
                        properties[key.strip()] = val.strip()
        except OSError:
            return {}

        return properties
