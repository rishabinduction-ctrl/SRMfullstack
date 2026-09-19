# Activity 9: Abstract Classes and Template Methods

## Objective
Implement abstract base classes in Python using the `abc` module (`ABC`, `@abstractmethod`), establishing contracts for `calculate_interest()` and `get_account_type()` while sharing template methods.

---

## Target Files to Complete
- `gdb/domain/bank_account.py`
- `gdb/domain/savings_account.py`
- `gdb/domain/current_account.py`
- `gdb/domain/fixed_deposit_account.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Create `BankAccount(ABC)`
1. Declare abstract methods: `@abstractmethod def calculate_interest(self) -> float` and `@abstractmethod def get_account_type(self) -> str`.
2. Implement template method `display_account_info()`.

### Step 2: Implement Subclasses
1. Implement `SavingsAccount`, `CurrentAccount`, and `FixedDepositAccount` fulfilling all abstract contracts.

---

## How to Run (Multi-OS Guide)
Run these commands from inside this activity folder (the folder that contains `gdb/`).

### Windows (PowerShell)
```powershell
python -m gdb.tests.test_abstract_account
```

### Windows (Command Prompt - CMD)
```cmd
python -m gdb.tests.test_abstract_account
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_abstract_account
```
