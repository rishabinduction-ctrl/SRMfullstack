# Activity 17: Command Pattern + File Logging

## Objective
Encapsulate each money-movement operation (`DEPOSIT`, `WITHDRAW`, `TRANSFER`) as an executable **Command** object, and persist the resulting `Transaction` records to a file using Python's `pickle` serialization. This decouples *executing* an operation from *auditing* it.

> **Scope note:** Only deposit, withdraw and transfer are modelled as commands here. New operations (`INTEREST_CREDITED`, `PIN_CHANGED`) can be added later by writing new `XxxCommand` classes -- `TransactionLog` does not need to change. That is the power of the Command Pattern.

---

## Prerequisites
- Activity 16 completed: `deposit_with_transaction()` / `withdraw_with_transaction()` return `Transaction` records, and `TransferService.transfer()` works.

---

## Target Files to Complete
- `gdb/command/transaction_command.py`
- `gdb/command/deposit_command.py`
- `gdb/command/withdraw_command.py`
- `gdb/command/transfer_command.py`
- `gdb/logging/transaction_log.py`
- `gdb/tests/test_command_logging.py`

---

## Step-by-Step Instructions
Search the code for `📝 STEP` -- each step below matches one marked placeholder.

### STEP 1 -- `command/transaction_command.py` -> `TransactionCommand` interface
Declare two abstract methods on the `ABC`:
1. `execute(self) -> None`
2. `get_transaction(self) -> Optional[Transaction]`

### STEPS 2-4 -- `command/deposit_command.py`
- **STEP 2 (constructor):** store `account` and `amount`, and set `self._transaction = None`.
- **STEP 3 (`execute()`):** call `account.deposit_with_transaction(amount)` and keep the returned `Transaction`.
- **STEP 4 (`get_transaction()`):** return the stored `Transaction`.

### STEPS 5-7 -- `command/withdraw_command.py`
Same shape as `DepositCommand`, but also store the `pin`, and `execute()` calls `account.withdraw_with_transaction(amount, pin)`.

### STEPS 8-10 -- `command/transfer_command.py`
- **STEP 8 (constructor):** store the `TransferService`, both accounts, the amount and the PIN; set `self._transaction = None`.
- **STEP 9 (`execute()`):** call `transfer_service.transfer(from_account, to_account, amount, pin)`, then build a `Transaction` describing the money leaving the sender:
  - `transaction_id=Transaction.generate_id()`, `timestamp=datetime.now()`
  - `account_number` = the sender's number, `transaction_type=TransactionType.TRANSFER_OUT`
  - `amount` = the transferred amount, `balance_after` = the sender's balance after the transfer
  - `status="SUCCESS"`, a description such as `"Transfer to #1002"`, plus `from_account` / `to_account` numbers
- **STEP 10 (`get_transaction()`):** return the stored `Transaction`.

### STEPS 11-14 -- `logging/transaction_log.py`
- **STEP 11 (constructor):** remember the log file path and start with an empty in-memory list.
- **STEP 12 (`log_transaction(txn)`):** append the transaction to the list, then call `save_to_file()`.
- **STEP 13 (`save_to_file()` / `load_from_file()`):**
  - `save_to_file()` writes the whole list to the file with `pickle.dump()` (open the file in binary mode `"wb"`).
  - `load_from_file()` reads the list back with `pickle.load()` (mode `"rb"`) if the file exists, falling back to an empty list if the file is missing or unreadable, and returns a copy of the list.
- **STEP 14 (`clear()`):** empty the list and delete the log file if it exists.

> **Python note:** the Java version appends one object at a time with a special `AppendableObjectOutputStream`. With `pickle`, it is simpler to rewrite the whole list on every save.

### STEPS 15-19 -- `tests/test_command_logging.py`
| Step | Test method | What to write |
|------|-------------|---------------|
| 15 | `setUp` | Create `TransactionLog("test_transactions.log")` and clear it; create a Savings account (#1001, Rs. 50,000, PIN 1234), a Current account (#1002, Rs. 50,000, PIN 5678) and a `TransferService`. |
| 16 | `test_deposit_command` | Execute a Rs. 5,000 `DepositCommand`, log its transaction, assert the log holds 1 record. |
| 17 | `test_withdraw_command` | Execute a Rs. 10,000 `WithdrawCommand` (PIN 1234), log it, assert 1 record. |
| 18 | `test_transfer_command` | Execute a Rs. 5,000 `TransferCommand` from #1001 to #1002, log it, assert 1 record. |
| 19 | `test_file_persistence` | Log one deposit, then prove a brand-new `TransactionLog` loads that 1 record from the file. |

`tearDown` is provided -- it clears the test log file after each test.

---

## How to Run
Run these commands from inside the `activity17` folder (the folder that contains `gdb/` and `config/`).

### Windows (PowerShell or Command Prompt)
```powershell
# This activity's tests
python -m gdb.tests.test_command_logging -v

# Every test in the folder (Activities 15-16 regression tests included)
python -m unittest discover -s gdb/tests -t . -v
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_command_logging -v
python3 -m unittest discover -s gdb/tests -t . -v
```

---

## Expected Output
Before you start, every test in `test_command_logging.py` errors with `NotImplementedError: TODO: Step 15 ...`. When you have finished:
```text
test_deposit_command ... ok
test_file_persistence ... ok
test_transfer_command ... ok
test_withdraw_command ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.0XXs

OK
```

---

## Verification Checklist
- [ ] `python -m gdb.tests.test_command_logging` reports `Ran 4 tests` and `OK`.
- [ ] The Activity 15 and 16 tests still pass.
- [ ] `get_transaction()` returns `None` before `execute()` and a `Transaction` after it.
- [ ] A fresh `TransactionLog` pointed at the same file sees every previously logged transaction.
- [ ] `clear()` removes the log file, so no `test_transactions.log` is left behind after the tests.

---

## Understanding Questions
1. The caller of a command only ever calls `execute()` and `get_transaction()`. Why does that make it easy to add new operation types later?
2. Why does `TransferCommand` receive a `TransferService` instead of moving the money itself?
3. `pickle` can load arbitrary Python objects. Why should you never `pickle.load()` a file you did not create yourself?
4. `save_to_file()` rewrites the whole list every time. When would that become a problem, and what could you do instead?
5. How could you use the stored commands to *replay* or *undo* operations?
