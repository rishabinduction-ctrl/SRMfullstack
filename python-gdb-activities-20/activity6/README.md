# Activity 6: Testing Exceptions

## Objective
Write automated unit-level exception assertion tests in Python, using `try-except` blocks to ensure boundary conditions trigger the exact expected custom exceptions.

---

## Target Files to Complete
- `gdb/tests/test_account_exceptions.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Test Invalid Deposit Exceptions
In `gdb/tests/test_account_exceptions.py`:
1. Call `acc.deposit(-500.0)` inside a `try` block.
2. Follow with a failure assertion if no exception was raised.
3. Catch `InvalidAmountException` and mark as PASS.

### Step 2: Test Overdraft & Inactive Exceptions
1. Attempt withdrawal exceeding balance and assert `InsufficientBalanceException`.
2. Attempt withdrawal on inactive account and assert `InactiveAccountException`.

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
