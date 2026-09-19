# Activity 4: Testing Enhanced Account

This solution demonstrates an exhaustive validation and security test suite for the enhanced `Account` class in Python.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Test Authentication Security** - Test valid, invalid, and `None` PIN submissions.
- **Verify Lifecycle State Invariants** - Verify transactions across Active and Inactive states.
- **Test State Transitions** - Verify that deactivating an account immediately blocks all transactions.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `account.py` | Enhanced account model. |
| `test_account.py` | Test suite asserting security and lifecycle invariants. |

---

## 🔍 Code Walkthrough

### File: `gdb/tests/test_account.py`

#### Key Code Snippets
```python
# PIN Tests
assert acc.validate_pin("4321") is True
assert acc.validate_pin("0000") is False
assert acc.validate_pin(None) is False

# Inactive Blocking
acc.status = "Inactive"
assert acc.withdraw(500.0) is False
assert acc.deposit(500.0) is False
```

---

## 🚀 How to Run

### Windows (PowerShell)
```powershell
python gdb/tests/test_account.py
```

### Linux / macOS (Terminal)
```bash
python3 gdb/tests/test_account.py
```

---

## 📊 Expected Output

```
=== Activity 4: Enhanced Account Test Suite ===
Test 1: PIN Validation Suite -> PASS
Test 2: Active Account Transactions -> PASS
Test 3: Inactive Protection -> PASS
All Enhanced Account tests passed!
```

---

## 🏁 Next Steps

Proceed to **Activity 5** to introduce custom domain exceptions.

---
*End of Activity 4 Solution*
