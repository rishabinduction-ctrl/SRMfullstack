# Activity 9: Abstract Classes and Template Methods

This solution demonstrates **Abstract Base Classes (ABC)** and the **Template Method Pattern** in Python using the `abc` module.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Define Abstract Base Classes** - Inherit from `abc.ABC` and decorate abstract methods with `@abstractmethod`.
- **Implement Template Method Pattern** - Combine shared concrete workflows (`display_account_info()`) with abstract hooks (`get_account_type()`).

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `bank_account.py` | Abstract base class defining abstract contracts and template methods. |
| `savings_account.py` | Concrete savings account implementation. |
| `current_account.py` | Concrete current account implementation. |
| `fixed_deposit_account.py` | Concrete fixed deposit account implementation. |
| `test_abstract_account.py` | Test driver verifying template pattern execution. |

---

## 🔍 Code Walkthrough

### File: `gdb/domain/bank_account.py`
```python
from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self) -> float: pass

    @abstractmethod
    def get_account_type(self) -> str: pass

    def display_account_info(self) -> None:
        print(f"Account Number: {self._account_number}")
        print(f"Account Type: {self.get_account_type()}")
        print(f"Balance: Rs {self._balance}")
```

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
=== Activity 9: Abstract Account & Template Pattern ===
Account Number: SA901
Account Type: Savings
Balance: Rs 10000.0
Account Number: CA902
Account Type: Current
Balance: Rs 50000.0
Account Number: FD903
Account Type: FixedDeposit
Balance: Rs 100000.0
Template method pattern executed successfully!
```

---

## 🏁 Next Steps

Proceed to **Activity 10** for abstract account testing.

---
*End of Activity 9 Solution*
