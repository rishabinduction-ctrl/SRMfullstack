# Activity 4: Testing Enhanced Account

## Objective
Build an automated verification and security test harness for the enhanced `Account` class, testing PIN authentication, lifecycle states, and boundary guards.

---

## Target Files to Complete
- `gdb/tests/test_account.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Test PIN Authentication
In `gdb/tests/test_account.py`:
1. Test valid 4-digit PIN against `validate_pin` (assert `True`).
2. Test wrong PIN and `None` (assert `False`).

### Step 2: Test Active Transactions
1. Verify deposits and withdrawals succeed when status is `"Active"`.

### Step 3: Test Inactive Status Invariant
1. Set status to `"Inactive"` and assert that deposits and withdrawals are blocked.

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
