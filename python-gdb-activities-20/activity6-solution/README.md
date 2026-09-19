# Activity 6: Testing Exceptions

This solution demonstrates writing structured negative test assertions in Python using `try-except` blocks.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Test Negative Paths** - Ensure boundary errors raise expected custom exceptions.
- **Validate Error Information** - Assert exception types and descriptive messages.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `account.py` | Domain model raising custom exceptions. |
| `test_account_exceptions.py` | Test harness asserting exception propagation. |

---

## 🔍 Code Walkthrough

```python
# Testing for expected exception
try:
    acc2 = Account("ACC002", "Jane", 32, 3000.0, "Savings", "Active", "1234")
    acc2.deposit(-500.0)
    assert False, "Expected InvalidAmountException"
except InvalidAmountException as e:
    print(f"PASS: Caught InvalidAmountException -> {e}")
```

---

## 🚀 How to Run

### Windows (PowerShell)
```powershell
python gdb/tests/test_account_exceptions.py
```

### Linux / macOS (Terminal)
```bash
python3 gdb/tests/test_account_exceptions.py
```

---

## 📊 Expected Output

```
=== Activity 6: Exception Handling Suite ===
PASS: Valid lifecycle balance: Rs 5500.0
PASS: Caught InvalidAmountException -> Deposit amount must be strictly positive: -500.0
PASS: Caught InsufficientBalanceException -> Insufficient balance. Available: 1000.0, Requested: 5000.0
PASS: Caught InactiveAccountException -> Cannot withdraw from inactive account: ACC004
All exception handling tests completed successfully!
```

---

## 🏁 Next Steps

Proceed to **Activity 7** for class inheritance.

---
*End of Activity 6 Solution*
