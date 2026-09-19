# Activity 8: Polymorphism and Method Overriding

This solution demonstrates **Runtime Polymorphism** and **Method Overriding** in Python to customize withdrawal behaviors per product type.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Override Methods** - Customize `withdraw()` per account subclass.
- **Enforce Product Constraints** - Enforce minimum balance in `SavingsAccount` and overdraft allowance in `CurrentAccount`.
- **Apply Polymorphic Iteration** - Iterate through lists of accounts executing subclass-specific logic dynamically.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `savings_account.py` | Overrides `withdraw()` enforcing minimum balance. |
| `current_account.py` | Overrides `withdraw()` permitting overdrafts. |
| `test_account_subclasses.py` | Polymorphic test driver. |

---

## 🔍 Code Walkthrough

### `SavingsAccount.withdraw()`
```python
def withdraw(self, amount: float) -> None:
    if self._status.lower() != "active":
        raise InactiveAccountException(f"Cannot withdraw from inactive account: {self._account_number}")
    if amount <= 0:
        raise InvalidAmountException(f"Withdrawal amount must be strictly positive: {amount}")
    if (self._balance - amount) < self._minimum_balance:
        raise MinimumBalanceViolationException(f"Withdrawal would violate minimum balance requirement of Rs {self._minimum_balance}")
    super().withdraw(amount)
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
=== Activity 8: Polymorphism Test ===
PASS: Caught MinimumBalanceViolationException -> Withdrawal would violate minimum balance requirement of Rs 1000.0
PASS: Overdraft withdrawal succeeded! New Balance: Rs -4000.0
All polymorphic behaviors verified!
```

---

## 🏁 Next Steps

Proceed to **Activity 9** for Abstract Base Classes.

---
*End of Activity 8 Solution*
