# Activity 11: IAccount Interface and Factory Pattern

This solution demonstrates pure **Interface Contracts (`IAccount`)** and the **Factory Design Pattern (`AccountFactory`)** in Python.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Design Interface Contracts (`IAccount`)** - Define purely abstract interfaces using `abc.ABC`.
- **Implement Factory Pattern (`AccountFactory`)** - Centralize object creation logic behind `AccountFactory.create_account()`.
- **Achieve Loose Coupling** - Decouple client code from concrete class constructors.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `iaccount.py` | Pure interface declaring all banking operations. |
| `abstract_account.py` | Base class implementing `IAccount`. |
| `account_factory.py` | Central factory creating account instances. |
| `test_interface_factory.py` | Test driver verifying factory creation. |

---

## 🔍 Code Walkthrough

### File: `gdb/domain/account_factory.py`
```python
class AccountFactory:
    @staticmethod
    def create_account(account_type: str, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000") -> IAccount:
        t = account_type.strip().upper()
        if t == "SAVINGS":
            return SavingsAccount(account_number, name, age, balance, status, pin, 4.0, 1000.0)
        elif t == "CURRENT":
            return CurrentAccount(account_number, name, age, balance, status, pin, 10000.0)
        elif t == "SALARY":
            return SalaryAccount(account_number, name, age, balance, status, pin)
        elif t == "FIXEDDEPOSIT":
            return FixedDepositAccount(account_number, name, age, balance, status, pin, 12, 6.5)
        raise AccountException(f"Unknown account type: {account_type}")
```

---

## 🚀 How to Run

### Windows (PowerShell)
```powershell
python gdb/tests/test_interface_factory.py
```

### Linux / macOS (Terminal)
```bash
python3 gdb/tests/test_interface_factory.py
```

---

## 📊 Expected Output

```
=== Activity 11: Interface & Factory Pattern Test ===
All accounts successfully created through AccountFactory!
```

---

## 🏁 Next Steps

Proceed to **Activity 12** for factory-driven system testing.

---
*End of Activity 11 Solution*
