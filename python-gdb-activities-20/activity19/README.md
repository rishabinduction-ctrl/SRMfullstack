# Activity 19: AccountService (Service Layer)

## Objective
Introduce `AccountService` as the **single entry point and orchestrator** for all banking operations. It keeps the in-memory registry of accounts, uses `AccountFactory` to open accounts, runs every money movement as a Command (Activity 17), and records each resulting `Transaction` through the `TransactionLogger` bridge (Activity 18).

---

## Prerequisites
- Activities 15-18 completed: `TransferService`, the `Transaction` model, the three commands and `TransactionLogger` with its destinations all work.

---

## Target Files to Complete
- `gdb/service/account_service.py`
- `gdb/tests/test_account_service.py`

---

## Step-by-Step Instructions
Search the code for `📝 STEP` -- each step below matches one marked placeholder.

### STEP 1 -- Constructor & fields
Create an empty `dict` registry of accounts keyed by account number, keep the `TransactionLogger` you are given, create a `TransferService`, and start `_next_account_number` at `1001`.

### STEP 2 -- `open_account(account_type, name, age, initial_balance, tenure_years=0)`
1. Take the next account number (`_next_account_number`).
2. Create the account with `AccountFactory.create_account(account_type, number, name, age, initial_balance, tenure_years)`.
3. Store it in the registry, increase `_next_account_number` by 1, and return the account.

### STEP 3 -- `get_account(account_number)`
Return the account for that number, or `None` if it does not exist.

### STEPS 4-6 -- `deposit()`, `withdraw()`, `transfer()`
Each operation follows the same four-part recipe:
1. **Look up** the account(s) with `get_account()`. If one is missing, raise `AccountException` (e.g. `"Account #9999 not found"`; for transfers say whether the *source* or *destination* is missing).
2. **Create** the matching command: `DepositCommand(acc, amount)`, `WithdrawCommand(acc, amount, pin)` or `TransferCommand(self._transfer_service, from_acc, to_acc, amount, pin)`.
3. **Execute** it, then take its `Transaction` with `get_transaction()`.
4. **Log** the transaction with `self._logger.log(txn)` (only if it is not `None`) and **return** it.

### STEP 7 -- `close_account(account_number, pin)`
Look up the account (`AccountException` if missing), check `verify_pin(pin)` (`InvalidPinException("Incorrect PIN")` if wrong), then call the account's `close_account()`.

### STEP 8 -- `get_transaction_history()`
Return every logged transaction from the logger.

### STEPS 9-15 -- `tests/test_account_service.py`
| Step | Test method | What to write |
|------|-------------|---------------|
| 9 | `setUp` | Wire `MemoryLogDestination` -> `TransactionLogger` -> `AccountService`. |
| 10 | `test_open_and_get_account` | Open a Savings account; assert it is #1001 and `get_account(1001)` returns it. |
| 11 | `test_deposit` | Deposit Rs. 5,000 into a Rs. 20,000 account; assert balance 25,000 and 1 history record. |
| 12 | `test_withdraw` | Withdraw Rs. 5,000 (PIN 1234); assert balance 15,000 and 1 history record. |
| 13 | `test_transfer` | Transfer Rs. 10,000 from Savings #1001 (Rs. 50,000) to Current #1002 (Rs. 30,000); assert both balances are 40,000 and 1 history record. |
| 14 | `test_close_account` | Close an account with the right PIN; assert it is no longer active. |
| 15 | `test_error_cases` | Assert an unknown account raises `AccountException` and a wrong PIN raises `InvalidPinException`. |

---

## How to Run
Run these commands from inside the `activity19` folder (the folder that contains `gdb/` and `config/`).

### Windows (PowerShell or Command Prompt)
```powershell
# This activity's tests
python -m gdb.tests.test_account_service -v

# Every test in the folder (Activities 15-18 regression tests included)
python -m unittest discover -s gdb/tests -t . -v
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_account_service -v
python3 -m unittest discover -s gdb/tests -t . -v
```

---

## Expected Output
Before you start, every test in `test_account_service.py` errors with `NotImplementedError: TODO: Step 9 ...`. When you have finished:
```text
test_close_account ... ok
test_deposit ... ok
test_error_cases ... ok
test_open_and_get_account ... ok
test_transfer ... ok
test_withdraw ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.0XXs

OK
```

---

## Verification Checklist
- [ ] `python -m gdb.tests.test_account_service` reports `Ran 6 tests` and `OK`.
- [ ] The Activity 15-18 tests still pass.
- [ ] Account numbers are handed out in order: 1001, 1002, 1003 ...
- [ ] Every successful deposit, withdrawal and transfer adds exactly one record to the history.
- [ ] A failed operation (unknown account, wrong PIN) raises an exception and adds nothing to the history.

---

## Understanding Questions
1. Why should the UI (Activity 20) talk only to `AccountService` and never directly to accounts, commands or loggers?
2. `AccountService` receives its `TransactionLogger` from outside instead of creating one. What does this *dependency injection* make easier (hint: look at `setUp`)?
3. Why does the service look up accounts by number instead of taking account objects as arguments?
4. What would need to change to store accounts in a real database instead of a `dict`?
5. Where should a new rule such as "no more than 5 withdrawals per day" live -- in the service, the command or the account? Why?
