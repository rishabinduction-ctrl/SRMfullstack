# Activity 5: Custom Exceptions in Account Class

This solution demonstrates replacing silent boolean error codes with a strongly typed **Custom Exception Hierarchy** in Python.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Build Domain Exception Hierarchies** - Create `AccountException(Exception)` and specialize domain subclasses.
- **Apply Fail-Fast Exceptions** - Raise specific exceptions immediately when business rules are breached.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `account_exception.py` | Base domain exception extending `Exception`. |
| `invalid_amount_exception.py` | Raised when amount $\le 0$. |
| `insufficient_balance_exception.py` | Raised when withdrawal exceeds balance. |
| `inactive_account_exception.py` | Raised on inactive account operations. |
| `invalid_pin_exception.py` | Raised on PIN validation failure. |
| `minimum_balance_violation_exception.py` | Raised on minimum balance breach. |
| `account.py` | Domain class raising exceptions on invalid operations. |
| `test_account_exceptions.py` | Test driver verifying exception propagation. |

---

## 🔍 Code Walkthrough

### File: `gdb/domain/account.py`
```python
def deposit(self, amount: float) -> None:
    if self._status.lower() != "active":
        raise InactiveAccountException(f"Cannot deposit to inactive account: {self._account_number}")
    if amount <= 0:
        raise InvalidAmountException(f"Deposit amount must be strictly positive: {amount}")
    self._balance += amount

def withdraw(self, amount: float) -> None:
    if self._status.lower() != "active":
        raise InactiveAccountException(f"Cannot withdraw from inactive account: {self._account_number}")
    if amount <= 0:
        raise InvalidAmountException(f"Withdrawal amount must be strictly positive: {amount}")
    if amount > self._balance:
        raise InsufficientBalanceException(f"Insufficient balance. Available: {self._balance}, Requested: {amount}")
    self._balance -= amount
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
=== Activity 5: Custom Exceptions Test ===
Successful withdrawal completed: Rs 1000.0 | New Balance: Rs 4000.0
PASS: Caught InvalidAmountException -> Deposit amount must be strictly positive: -100.0
PASS: Caught InsufficientBalanceException -> Insufficient balance. Available: 4000.0, Requested: 99999.0
```

---

## 🏁 Next Steps

Proceed to **Activity 6** for exception testing suites.

---
*End of Activity 5 Solution*
