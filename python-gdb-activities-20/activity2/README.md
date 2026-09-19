# Activity 2: Testing Account Class

## Objective
Write automated unit-level verification tests for the `Account` domain class, asserting positive transaction paths and negative boundary conditions.

---

## Target Files to Complete
- `gdb/tests/test_account.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Initial State Verification
In `gdb/tests/test_account.py`:
1. Instantiate an `Account` with known values.
2. Assert that attributes match constructor arguments.

### Step 2: Test Valid and Invalid Deposits
1. Perform a positive deposit and verify balance increases and method returns `True`.
2. Perform negative and zero deposits, asserting rejection (`False`) and state preservation.

### Step 3: Test Valid and Overdraft Withdrawals
1. Perform a withdrawal within available balance and assert success.
2. Attempt a withdrawal exceeding balance, asserting rejection (`False`) and balance preservation.

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
