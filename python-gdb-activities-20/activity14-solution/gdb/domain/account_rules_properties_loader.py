# gdb/domain/account_rules_properties_loader.py
import os

class AccountRulesPropertiesLoader:
    """Utility loading external .properties files."""

    @staticmethod
    def load_rules(account_type: str) -> dict:
        props = {}
        # Try local resources directory relative to domain or root
        base_dir = os.path.dirname(os.path.abspath(__file__))
        possible_paths = [
            os.path.join(base_dir, "..", "resources", "config", "rules", f"{account_type.lower()}.properties"),
            os.path.join(base_dir, "resources", "config", "rules", f"{account_type.lower()}.properties"),
            os.path.join("resources", "config", "rules", f"{account_type.lower()}.properties"),
            os.path.join("gdb", "resources", "config", "rules", f"{account_type.lower()}.properties")
        ]
        
        found_path = None
        for p in possible_paths:
            if os.path.exists(p):
                found_path = p
                break
                
        if found_path:
            with open(found_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        props[k.strip()] = v.strip()
        return props
