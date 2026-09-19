# Activity 7: Account Subclasses (Inheritance)

This solution demonstrates Object-Oriented **Inheritance** in Python by extending the `Account` base class into specialized subclasses: `SavingsAccount` and `CurrentAccount`.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Apply Class Inheritance (`class Sub(Parent):`)** - Inherit core attributes and methods to avoid duplication.
- **Master Constructor Delegation (`super().__init__()`)** - Pass shared attributes to parent class.
- **Add Product-Specific Attributes** - Introduce `interest_rate` and `overdraft_limit`.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `account.py` | Base class with core attributes and transactions. |
| `savings_account.py` | Subclass adding `interest_rate` and `calculate_interest()`. |
| `current_account.py` | Subclass adding `overdraft_limit`. |
| `test_account_subclasses.py` | Test driver instantiating each subclass product. |

---

## 🔍 Code Walkthrough

### File: `gdb/domain/savings_account.py`
```python
from gdb.domain.account import Account

class SavingsAccount(Account):
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000", interest_rate: float = 4.0) -> None:
        super().__init__(account_number, name, age, balance, "Savings", status, pin)
        self._interest_rate = interest_rate

    def calculate_interest(self) -> float:
        return (self._balance * self._interest_rate) / 100.0
```

---

## 🚀 How to Run

### Windows (PowerShell)
```powershell
python gdb/tests/test_account_subclasses.py
```

### Linux / macOS (Terminal)
```bash
python3 gdb/tests/test_account_subclasses.py
```

---

## 📊 Expected Output

```
=== Activity 7: Account Subclasses Test ===
Savings Account Interest on Rs 10000 @ 4.5%: Rs 450.0
Current Account Overdraft Limit: Rs 20000.0
All subclasses instantiated successfully!
```

---

## 🏁 Next Steps

Proceed to **Activity 8** for method overriding and polymorphism.

---
*End of Activity 7 Solution*
