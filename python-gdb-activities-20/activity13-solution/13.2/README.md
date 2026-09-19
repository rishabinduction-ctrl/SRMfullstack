# Activity 13.2: Rules Engine Integration

This solution demonstrates dynamic dictionary-based rule lookups and multi-product policy validation.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Optimize Rule Lookups** - Implement fast dictionary mapping for policy thresholds.
- **Assert Combined Policy Rules** - Validate `validate_withdrawal()` combining balance, overdraft, and minimum balance.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `account_rules_engine.py` | Dynamic dictionary-based rules engine. |
| `test_account_rules_engine.py` | Integration test suite. |

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
=== Activity 13.2: Dynamic Account Rules Test ===
Dynamic rule integration verified!
```

---

## 🏁 Next Steps

Proceed to **Activity 14** to externalize rules into `.properties` files.

---
*End of Activity 13.2 Solution*
