# Activity 3: Enhanced Account Class

This solution demonstrates defensive programming, 4-digit security PIN verification, minimum age constraints ($\ge 18$), and lifecycle status management in Python.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Implement Defensive Input Validation** - Reject invalid parameters upfront in `__init__`.
- **Enforce Business Constraints** - Ensure account holders are at least 18 years old and balance is non-negative.
- **Implement PIN Security** - Add PIN authentication for sensitive account operations.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `account.py` | Enhanced account entity with validation guards, PIN storage, and status verification. |
| `test_account.py` | Test driver verifying authentication, status transitions, and transactions. |

---

## 🔍 Code Walkthrough

### File: `gdb/domain/account.py`

#### Constructor Validation
```python
def __init__(self, account_number: str, name: str, age: int, balance: float, account_type: str, status: str = "Active", pin: str = "0000") -> None:
    if not account_number or not account_number.strip():
        raise ValueError("Account number cannot be empty")
    if age < 18:
        raise ValueError("Account holder must be at least 18 years old")
    if balance < 0:
        raise ValueError("Initial balance cannot be negative")
    if not pin or len(pin) != 4 or not pin.isdigit():
        raise ValueError("PIN must be exactly 4 digits")

    self._account_number = account_number
    self._name = name
    self._age = age
    self._balance = balance
    self._account_type = account_type
    self._status = status
    self._pin = pin
```

#### Key Methods
- `validate_pin(self, entered_pin: str) -> bool`: Checks if `entered_pin` matches `self._pin`.
- `deposit` & `withdraw`: Check `self._status.lower() == "active"` before allowing transactions.

---

## 💡 Key Concepts

### Concept 1: Defensive Programming
An entity must protect its internal invariants so it can never be instantiated in an illegal or corrupted state.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Store PIN as `str` | Preserves leading zeroes (e.g. `"0123"`). |
| Case-insensitive status checks | `.lower() == "active"` handles all casing variations gracefully. |

---

## 🚀 How to Run

### Windows (PowerShell)
```powershell
python gdb/tests/test_account.py
```

### Windows (Command Prompt - CMD)
```cmd
python gdb	ests	est_account.py
```

### Linux / macOS (Terminal)
```bash
python3 gdb/tests/test_account.py
```

---

## 📊 Expected Output

```
=== Activity 3: Enhanced Account Test ===
PIN '1234' validation: True
PIN '9999' validation: False
Deposit on active account: Balance = Rs 6000.0
Withdraw with new PIN: SUCCESS | Balance: Rs 3000.0
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to implement parameter guards and authentication logic in Python.

### How It Connects
- **Previous**: Activity 2 tested basic mutations.
- **Next**: Activity 4 builds an exhaustive security test suite.

---

## 🏁 Next Steps

Proceed to **Activity 4** for comprehensive security testing.

---
*End of Activity 3 Solution*
