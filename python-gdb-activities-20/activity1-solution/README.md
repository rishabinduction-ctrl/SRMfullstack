# Activity 1: Basic Account Class

This solution demonstrates the foundational implementation of an `Account` class in Python using Object-Oriented Programming (OOP) principles. It showcases proper data encapsulation, state initialization via `__init__`, safe transaction methods for depositing and withdrawing funds, and formatted account reporting.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Understand Encapsulation in Python** - Protect object state using private/protected attributes (`_attribute`) and `@property` decorators.
- **Implement State Initialization** - Construct valid objects using `__init__` constructor methods with explicit type annotations.
- **Enforce Business Invariants** - Implement safe mathematical validations for deposit and withdrawal operations.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `account.py` | Core domain model encapsulating account state (account number, holder name, age, balance, account type, status) and business operations. |
| `test_account.py` | Test driver verifying account creation, successful deposits, withdrawals, and formatted information display. |

---

## 🔍 Code Walkthrough

### File: `gdb/domain/account.py`

#### Fields
| Field | Type | Access | Description |
|---|---|---|---|
| `_account_number` | `str` | Protected | Unique identifier for the bank account. |
| `_name` | `str` | Protected | Full name of the account holder. |
| `_age` | `int` | Protected | Age of the account holder. |
| `_balance` | `float` | Protected | Current monetary balance in Rupees. |
| `_account_type` | `str` | Protected | Type of account (e.g., "Savings", "Current"). |
| `_status` | `str` | Protected | Operational status (e.g., "Active", "Inactive"). |

#### Constructor
```python
def __init__(self, account_number: str, name: str, age: int, balance: float, account_type: str, status: str = "Active") -> None:
    self._account_number: str = account_number
    self._name: str = name
    self._age: int = age
    self._balance: float = balance
    self._account_type: str = account_type
    self._status: str = status
```
Initializes all 6 instance variables when an `Account` object is created.

#### Key Methods
- `deposit(self, amount: float) -> bool`: Validates `amount > 0`. If valid, adds amount to `_balance` and returns `True`; otherwise `False`.
- `withdraw(self, amount: float) -> bool`: Validates `0 < amount <= self._balance`. If valid, deducts amount and returns `True`; otherwise `False`.
- `display_account_info(self) -> None`: Formats and prints all account attributes to standard output.

#### Key Code Snippets
```python
def deposit(self, amount: float) -> bool:
    if amount > 0:
        self._balance += amount
        return True
    return False

def withdraw(self, amount: float) -> bool:
    if 0 < amount <= self._balance:
        self._balance -= amount
        return True
    return False
```

### File: `gdb/tests/test_account.py`

#### Test Scenarios
1. **Creation**: Instantiates an `Account` with ID `"ACC1001"`, Name `"Alice"`, Age `25`, Balance `5000.0`, Type `"Savings"`.
2. **Deposit Verification**: Performs a deposit of `1500.0` and asserts that balance updates to `6500.0`.
3. **Withdrawal Verification**: Performs a withdrawal of `2000.0` and asserts that balance updates to `4500.0`.

---

## 💡 Key Concepts

### Concept 1: Encapsulation & Properties in Python
Python uses leading underscores (`_name`) by convention to mark attributes as non-public, exposing them safely through `@property` getters and `@name.setter` methods.

### Concept 2: Safe Mutators & State Integrity
Instead of mutating `_balance` directly, all balance changes occur through `deposit()` and `withdraw()` with boundary checks.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Protected `_` fields with `@property` | Idiomatic Python encapsulation allowing future validation inside setters without breaking existing code. |
| `bool` return types | Clear operational signal indicating success or failure of financial transactions. |

---

## 🚀 How to Run

### Prerequisites
- Python 3.10 or higher installed

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
=== Activity 1: Basic Account Test ===
Account Number: ACC1001
Name: Alice
Age: 25
Balance: Rs 5000.0
Account Type: Savings
Status: Active

Depositing Rs 1500.0...
Deposit Successful! Current Balance: Rs 6500.0

Withdrawing Rs 2000.0...
Withdrawal Successful! Current Balance: Rs 4500.0

Withdrawing Rs 10000.0 (exceeds balance)...
Withdraw 10000 (exceeds balance): FAILED | Balance: Rs 4500.0
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to structure a clean Python domain class.
- How to implement constructor initialization and property decorators.

### How It Connects
- **Previous**: None (Starting Activity).
- **Next**: Activity 2 introduces automated test assertions and verification suites.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Directly mutating `acc._balance` | Always call `acc.deposit()` or `acc.withdraw()`. |
| Allowing negative deposits or withdrawals | Check `amount > 0` before mutating `_balance`. |

---

## 🏁 Next Steps

Proceed to **Activity 2** to write unit test assertions.

---
*End of Activity 1 Solution*
