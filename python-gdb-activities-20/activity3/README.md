# Activity 3: Enhanced Account Class

## Objective
Enhance the `Account` class with defensive input validation, 4-digit security PIN verification, minimum age constraints ($\ge 18$), and lifecycle status management.

---

## Target Files to Complete
- `gdb/domain/account.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Constructor Defensive Guards
In `gdb/domain/account.py`:
1. Reject empty or null account numbers.
2. Require age $\ge 18$; raise `ValueError` if younger.
3. Require non-negative initial balance; raise `ValueError` if $< 0$.
4. Validate 4-digit PIN format.

### Step 2: Implement PIN Validation
1. In `validate_pin(self, entered_pin: str) -> bool`:
   - Compare `entered_pin` to `self._pin` and return `True` on match, `False` otherwise.

### Step 3: Enforce Status Checks
1. In `deposit` and `withdraw`, check that `self._status.lower() == "active"` before allowing transactions.

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
