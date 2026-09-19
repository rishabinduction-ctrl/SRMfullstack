# Activity 1: Basic Account Class

## Objective
Create a foundational `Account` domain class modeling a bank account in Python using Object-Oriented Programming (OOP), encapsulation, properties, constructor initialization, and safe transaction methods.

---

## Target Files to Complete
- `gdb/domain/account.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Declare Constructor and Attributes
In `gdb/domain/account.py`:
1. In `__init__`, accept `account_number`, `name`, `age`, `balance`, `account_type`, and optional `status` (default `"Active"`).
2. Store each argument in protected instance variables (e.g., `self._account_number`, `self._name`, `self._age`, `self._balance`, `self._account_type`, `self._status`).

### Step 2: Implement Deposit Method
1. In `deposit(self, amount: float) -> bool`:
   - Validate that `amount > 0`.
   - If valid, increase `self._balance` by `amount` and return `True`.
   - If invalid ($\le 0$), return `False` without changing balance.

### Step 3: Implement Withdraw Method
1. In `withdraw(self, amount: float) -> bool`:
   - Validate that `amount > 0` and `amount <= self._balance`.
   - If valid, deduct `amount` from `self._balance` and return `True`.
   - If invalid (negative, zero, or exceeding balance), return `False`.

### Step 4: Implement Display Account Info & Properties
1. In `display_account_info(self) -> None`:
   - Print all account details in a clear format.
2. Ensure `@property` getters and setters are defined for all attributes.

---

## How to Run (Multi-OS Guide)
Run these commands from inside this activity folder (the folder that contains `gdb/`).

### Windows (PowerShell)
```powershell
python -m gdb.tests.test_account
```

### Windows (Command Prompt - CMD)
```cmd
python -m gdb.tests.test_account
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_account
```
