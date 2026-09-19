# Activity 20: AccountUI (Interactive Console Application)

## Objective
Build a **menu-driven console application** (`AccountUI`) on top of `AccountService`. The UI layer talks to the bank *only* through the service: it collects user input, calls the right service method, and prints friendly feedback -- without ever crashing on bad input or a failed operation.

---

## Architecture Diagram
```text
┌──────────────┐
│   main.py    │   <- wires the dependencies
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  AccountUI   │   <- collects user input, prints output
└──────┬───────┘
       │ delegates
       ▼
┌──────────────────┐
│  AccountService  │   <- orchestration + logging (Activity 19)
└──────┬───────────┘
       │
       ▼
   Domain / Commands / Logger
```

> **Separation of concerns:** the UI knows nothing about `Transaction` internals, commands or the rules engine -- it only knows `AccountService`. That is why the console UI could be swapped for a web app or REST API without touching any business logic.

---

## Prerequisites
- Activity 19 completed: `AccountService` opens accounts, moves money and returns the transaction history.

---

## Target Files to Complete
- `gdb/ui/account_ui.py`
- `main.py`
- `gdb/tests/test_account_ui.py`

---

## Step-by-Step Instructions
Search the code for `📝 STEP` -- each step below matches one marked placeholder.

### STEP 1 -- `ui/account_ui.py` -> constructor
Store the `AccountService` in `self._service`.

### STEP 2 -- `start()` (main menu loop)
Loop until the user chooses **8**:
1. Show the menu with `display_main_menu()`.
2. Read the choice with `read_int("Enter your choice: ")`.
3. Dispatch: 1 open account, 2 deposit, 3 withdraw, 4 transfer, 5 close account, 6 view account, 7 view transactions, 8 print `"Thank you! Goodbye."` and leave the loop. Any other number prints `"Invalid choice. Please enter 1-8."`
4. Wrap the dispatch in `try` / `except Exception as e:` and print `f"ERROR: {e}"` -- a failed operation must never crash the app.

### STEP 3 -- `display_main_menu()`
Print a banner containing `GLOBAL DIGITAL BANK` and these eight options, one per line:
```text
1. Open Account
2. Deposit Funds
3. Withdraw Funds
4. Transfer Funds
5. Close Account
6. View Account Details
7. View Transaction History
8. Exit
```

### STEPS 4-10 -- action handlers
Each handler reads its inputs with the helpers from Steps 11-13, calls **one** service method, and prints the result.

| Step | Handler | Prompts (in this order) | Service call / output |
|------|---------|-------------------------|-----------------------|
| 4 | `handle_open_account()` | account type, holder name, age, initial balance, tenure in years, then a 4-digit PIN | `open_account(type, name, age, balance, tenure)`, then `acc.set_pin(pin)`; print the new account number and `get_account_info()` |
| 5 | `handle_deposit()` | account number, amount | `deposit(...)`; print `"SUCCESS: "` + the transaction receipt |
| 6 | `handle_withdraw()` | account number, amount, PIN | `withdraw(...)`; print the receipt |
| 7 | `handle_transfer()` | from account, to account, amount, sender PIN | `transfer(...)`; print the receipt |
| 8 | `handle_close_account()` | account number, PIN | `close_account(...)`; confirm the account was closed |
| 9 | `handle_view_account()` | account number | `get_account(...)`; print `get_account_info()`, or a "not found" message |
| 10 | `handle_view_transactions()` | -- | `get_transaction_history()`; print `"No transactions logged."` or each receipt numbered `[1]`, `[2]` ... |

> The prompt order in Step 4 matters: the automated test in Step 17 answers the prompts in exactly this order.

### STEPS 11-13 -- robust input helpers
- **`read_int(prompt)`**: keep asking with `input(prompt)` until the (stripped) answer converts with `int()`; on a `ValueError` print `"Invalid integer. Please try again."`.
- **`read_double(prompt)`**: the same with `float()` and `"Invalid number. Please try again."`.
- **`read_string(prompt)`**: keep asking until the stripped answer is not empty; otherwise print `"Input cannot be empty."`.

### STEP 14 -- `main.py`
Print a welcome banner, then wire the application together and start it:
`SimulatedDatabase` -> `DatabaseLogDestination` -> `TransactionLogger` -> `AccountService` -> `AccountUI` -> `ui.start()`.

### STEPS 15-17 -- `tests/test_account_ui.py`
| Step | Test method | What to write |
|------|-------------|---------------|
| 15 | `setUp` | Wire `MemoryLogDestination` -> `TransactionLogger` -> `AccountService` -> `AccountUI`. |
| 16 | `test_ui_display_menu` | Capture `sys.stdout` with `unittest.mock.patch` and assert the menu shows `GLOBAL DIGITAL BANK`, `1. Open Account` and `8. Exit`. |
| 17 | `test_ui_open_account_and_exit` | Patch `builtins.input` with the answers `["1", "Savings", "Rajesh Sharma", "30", "20000", "2", "1234", "8"]`, run `start()`, and assert account #1001 exists with the right name and a balance of 20000.0. |

---

## How to Run
Run these commands from inside the `activity20` folder (the folder that contains `main.py`, `gdb/` and `config/`).

### Windows (PowerShell or Command Prompt)
```powershell
# This activity's tests
python -m gdb.tests.test_account_ui -v

# Every test in the folder (Activities 15-19 regression tests included)
python -m unittest discover -s gdb/tests -t . -v

# The interactive console application
python main.py
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_account_ui -v
python3 -m unittest discover -s gdb/tests -t . -v
python3 main.py
```

---

## Expected Output
Before you start, both tests error with `NotImplementedError: TODO: Step 15 ...`, and `python main.py` stops with `NotImplementedError: TODO: Step 14 ...`. When you have finished, the tests report:
```text
test_ui_display_menu ... ok
test_ui_open_account_and_exit ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.0XXs

OK
```

A sample interactive session (your wording may differ):
```text
============================================================
       GLOBAL DIGITAL BANK (GDB) APPLICATION
============================================================

==================================================
     GLOBAL DIGITAL BANK (GDB) — MAIN MENU
==================================================
1. Open Account
...
8. Exit
==================================================
Enter your choice: 1
Account Type (Savings/Current/FixedDeposit/Salary): Savings
Account Holder Name: John Doe
Age: 25
Initial Balance: 15000
Customer Tenure in Years (0 for new): 0
Set 4-digit PIN (1000-9999): 1234
SUCCESS: Account #1001 created successfully!
Account #1001 | John Doe (25 yrs, Tenure: 0 yrs) | Savings | Rs. 15000.0 | Active
...
Enter your choice: 8
Thank you! Goodbye.
```

---

## Verification Checklist
- [ ] `python -m gdb.tests.test_account_ui` reports `Ran 2 tests` and `OK`.
- [ ] The Activity 15-19 tests still pass.
- [ ] Typing letters where a number is expected shows an error and asks again instead of crashing.
- [ ] A failed operation (wrong PIN, unknown account, insufficient balance) prints `ERROR: ...` and returns to the menu.
- [ ] `AccountUI` imports nothing from `gdb.domain`, `gdb.command` or `gdb.logging` -- only the service.

---

## Understanding Questions
1. Why does `AccountUI` call `AccountService` instead of calling accounts and commands directly?
2. Why is it useful to put all input parsing in `read_int()` / `read_double()` / `read_string()` instead of calling `int(input(...))` in every handler?
3. How does patching `builtins.input` let you test an interactive program automatically?
4. Where should the `try` / `except` live -- in each handler or once in `start()`? What are the trade-offs?
5. What would you change to turn this console UI into a web API that uses the same `AccountService`?
