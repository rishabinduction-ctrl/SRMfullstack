# Activity 5: Custom Exceptions Hierarchy

## Objective
Replace silent boolean error codes with strongly typed custom domain exceptions in Python, modeling banking business errors as expressively handled exception classes.

---

## Target Files to Complete
- `gdb/exceptions/account_exception.py`
- `gdb/exceptions/invalid_amount_exception.py`
- `gdb/exceptions/insufficient_balance_exception.py`
- `gdb/exceptions/inactive_account_exception.py`
- `gdb/exceptions/invalid_pin_exception.py`
- `gdb/exceptions/minimum_balance_violation_exception.py`
- `gdb/domain/account.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Build Custom Exception Hierarchy
1. Create `AccountException(Exception)` as the base class for all domain errors.
2. Specialize subclasses:
   - `InvalidAmountException` for amounts $\le 0$.
   - `InsufficientBalanceException` for withdrawals exceeding balance.
   - `InactiveAccountException` for operations on inactive accounts.
   - `InvalidPinException` for PIN failures.
   - `MinimumBalanceViolationException` for minimum balance breaches.

### Step 2: Update `Account` Class
1. In `__init__`, `deposit()`, `withdraw()`, and `validate_pin()`, replace return `False` with `raise <SpecificException>(...)`.

---

## How to Run (Multi-OS Guide)
Run these commands from inside this activity folder (the folder that contains `gdb/`).

### Windows (PowerShell)
```powershell
python -m gdb.tests.test_account_exceptions
```

### Windows (Command Prompt - CMD)
```cmd
python -m gdb.tests.test_account_exceptions
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_account_exceptions
```
