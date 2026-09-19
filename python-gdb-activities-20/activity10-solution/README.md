# Activity 10: Testing Abstract Account

This solution demonstrates testing abstract account hierarchies polymorphically in Python.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Test Abstract Polymorphic References** - Verify interest calculation and boundary enforcement across subclasses.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `bank_account.py` & Subclasses | Abstract domain model. |
| `test_abstract_account.py` | Integration test suite. |

---

## 🚀 How to Run

### Windows (PowerShell)
```powershell
python gdb/tests/test_abstract_account.py
```

### Linux / macOS (Terminal)
```bash
python3 gdb/tests/test_abstract_account.py
```

---

## 📊 Expected Output

```
=== Activity 10: Banking Operations Suite ===
PASS: Caught expected MinimumBalanceViolationException -> Withdrawal would violate minimum balance requirement of Rs 1000.0
All banking operations passed!
```

---

## 🏁 Next Steps

Proceed to **Activity 11** for interfaces and the Factory Pattern.

---
*End of Activity 10 Solution*
