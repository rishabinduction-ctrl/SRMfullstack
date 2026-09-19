# Activity 13.1: Rules Engine (If-Else)

This solution demonstrates centralizing business policy thresholds into a dedicated **Business Rules Engine** (`AccountRulesEngine`) using structured conditional evaluations.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Centralize Business Policies** - Extract minimum balance, interest rate, and overdraft threshold rules out of domain classes.
- **Implement Policy Evaluation** - Write clean conditional rules for all account products.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `account_rules_engine.py` | Central rules engine. |
| `test_account_rules_engine.py` | Test driver verifying policy lookups. |

---

## 🔍 Code Walkthrough

```python
class AccountRulesEngine:
    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        if account_type and account_type.strip().upper() == "SAVINGS":
            return 1000.0
        return 0.0

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        t = account_type.strip().upper() if account_type else ""
        if t == "SAVINGS": return 4.0
        elif t == "FIXEDDEPOSIT": return 6.5
        return 0.0
```

---

## 🚀 How to Run

### Windows (PowerShell)
```powershell
python gdb/tests/test_account_rules_engine.py
```

### Linux / macOS (Terminal)
```bash
python3 gdb/tests/test_account_rules_engine.py
```

---

## 📊 Expected Output

```
=== Activity 13.1: Hardcoded Rules Engine Test ===
Rules Engine lookup completed successfully!
```

---

## 🏁 Next Steps

Proceed to **Activity 13.2** for dynamic dictionary-based rules lookup.

---
*End of Activity 13.1 Solution*
