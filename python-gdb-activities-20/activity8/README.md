# Activity 8: Polymorphism and Method Overriding

## Objective
Implement runtime polymorphism and method overriding in Python, specializing `withdraw()` rules for `SavingsAccount` (minimum balance constraint) and `CurrentAccount` (overdraft protection).

---

## Target Files to Complete
- `gdb/domain/savings_account.py`
- `gdb/domain/current_account.py`
- `gdb/tests/test_account_subclasses.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Override `withdraw()` in `SavingsAccount`
1. Enforce minimum balance requirement (e.g. Rs 1000).
2. If remaining balance would drop below minimum balance, raise `MinimumBalanceViolationException`.

### Step 2: Override `withdraw()` in `CurrentAccount`
1. Permit balance to go negative up to `self._overdraft_limit`.
2. Raise `InsufficientBalanceException` only if withdrawal exceeds `balance + overdraft_limit`.

---

## How to Run (Multi-OS Guide)
Run these commands from inside this activity folder (the folder that contains `gdb/`).

### Windows (PowerShell)
```powershell
python -m gdb.tests.test_account_subclasses
```

### Windows (Command Prompt - CMD)
```cmd
python -m gdb.tests.test_account_subclasses
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_account_subclasses
```
