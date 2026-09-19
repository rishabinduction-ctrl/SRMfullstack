# Activity 14: Properties File Migration

This solution demonstrates externalizing all banking policy thresholds into external `.properties` configuration files loaded dynamically in Python via `AccountRulesPropertiesLoader`.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Externalize Application Configuration** - Move business parameters (interest rates, minimum balances, overdraft limits) into `.properties` files.
- **Implement Properties File Parser** - Read and parse `key=value` configuration files dynamically into Python dictionaries.
- **Enable Zero-Recompile Rule Updates** - Modify banking rules at runtime by altering configuration files.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `savings.properties` | Defines `minBalance=1000.0` and `interestRate=4.0`. |
| `current.properties` | Defines `overdraftLimit=10000.0`. |
| `fixeddeposit.properties` | Defines `interestRate=6.5` and `minTenureMonths=6`. |
| `salary.properties` | Defines `minBalance=0.0`. |
| `account_rules_properties_loader.py` | Dynamic loader reading configuration files. |
| `account_rules_engine.py` | Properties-driven rules engine. |
| `test_account_rules_engine_properties.py` | Test driver verifying dynamic configuration loading. |

---

## 🔍 Code Walkthrough

### File: `gdb/domain/account_rules_properties_loader.py`
```python
class AccountRulesPropertiesLoader:
    @staticmethod
    def load_rules(account_type: str) -> dict:
        props = {}
        config_path = f"gdb/resources/config/rules/{account_type.lower()}.properties"
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        props[k.strip()] = v.strip()
        return props
```

---

## 🚀 How to Run

### Windows (PowerShell)
```powershell
python gdb/tests/test_account_rules_engine_properties.py
```

### Windows (Command Prompt - CMD)
```cmd
python gdb	ests	est_account_rules_engine_properties.py
```

### Linux / macOS (Terminal)
```bash
python3 gdb/tests/test_account_rules_engine_properties.py
```

---

## 📊 Expected Output

```
=== Activity 14: Properties-Driven Rules Engine Test ===
All external properties loaded and verified successfully!
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to decouple business configuration from application code.
- How to parse and manage external properties files dynamically in Python.

### How It Connects
- **Previous**: Activity 13.2 implemented in-code dictionary rules.
- **Course Capstone**: Concludes the 14-activity Python Banking Architecture curriculum!

---

## 🏁 Course Complete!

Congratulations on mastering Core Python, Object-Oriented Programming, Custom Exceptions, Design Patterns, and Dynamic Configuration Management!

---
*End of Activity 14 Solution*
