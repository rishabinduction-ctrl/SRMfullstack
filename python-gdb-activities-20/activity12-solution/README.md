# Activity 12: Testing Interface and Factory

This solution demonstrates end-to-end integration testing of client applications interacting exclusively via `IAccount` and `AccountFactory`.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Verify Complete Interface Decoupling** - Write client code referencing only interface contracts.
- **Assert Factory Completeness** - Verify creation across Savings, Current, Salary, and Fixed Deposit accounts.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `iaccount.py` | Interface contract. |
| `account_factory.py` | Factory class. |
| `test_interface_factory.py` | Test driver verifying interface operations. |

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
=== Activity 12: Factory-Driven System Suite ===
Factory-driven architecture successfully verified!
```

---

## 🏁 Next Steps

Proceed to **Activity 13.1** to extract business rules into a centralized engine.

---
*End of Activity 12 Solution*
