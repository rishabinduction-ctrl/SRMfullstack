# Activity 7: Account Subclasses (Inheritance)

## Objective
Apply Object-Oriented inheritance in Python to extend the `Account` base class into specialized banking product classes (`SavingsAccount`, `CurrentAccount`).

---

## Target Files to Complete
- `gdb/domain/savings_account.py`
- `gdb/domain/current_account.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Implement `SavingsAccount`
1. Inherit from `Account`.
2. In `__init__`, invoke `super().__init__(..., account_type="Savings", ...)` and store `_interest_rate`.
3. Implement `calculate_interest(self) -> float`.

### Step 2: Implement `CurrentAccount`
1. Inherit from `Account`.
2. In `__init__`, invoke `super().__init__(..., account_type="Current", ...)` and store `_overdraft_limit`.

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
