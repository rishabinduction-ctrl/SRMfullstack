# Activity 16: Transaction Model

## Objective
Introduce a structured `Transaction` model and a `TransactionType` enum to capture historical records of banking operations. You will add new methods to `Account` that perform a money movement **and** return a detailed `Transaction` audit record, while keeping the existing `deposit()` / `withdraw()` methods working exactly as before (backward compatibility).

> **Scope note:** Only money-movement operations are modelled as transactions in this activity. The pattern is extensible -- future types (`INTEREST_CREDITED`, `ACCOUNT_CLOSED`, `PIN_CHANGED`) can be added later simply by extending `TransactionType` and following the same pattern.

---

## Prerequisites
- Activity 15 completed: `TransferService.transfer()` and the daily transfer limits work.

---

## What Is Already Done For You
| File | What is provided |
|------|------------------|
| `gdb/domain/transaction.py` | `Transaction.generate_id()` -- a class-level counter that returns a new unique id on every call. |
| `gdb/domain/account.py` | `build_transaction(txn_type, amount, from_acc, to_acc, desc)` -- creates a `Transaction` with a new id, the current time, this account's number and current balance, and status `"SUCCESS"`. |
| Activity 15 code | `TransferService`, the daily-limit methods and the rules engine are complete. |

---

## Target Files to Complete
- `gdb/domain/transaction_type.py`
- `gdb/domain/transaction.py`
- `gdb/domain/account.py`
- `gdb/tests/test_transaction_model.py`

---

## Step-by-Step Instructions
Search the code for `📝 STEP` -- each step below matches one marked placeholder.

### STEP 1 -- `domain/transaction_type.py` -> `TransactionType` enum
Declare the members `DEPOSIT`, `WITHDRAW`, `TRANSFER_IN`, `TRANSFER_OUT` and `TRANSFER`. Give each member a string value equal to its name (for example `DEPOSIT = "DEPOSIT"`) -- the receipt prints this value.

### STEP 2 -- `domain/transaction.py` -> `__init__`
Store every constructor argument in an attribute with the same name: `transaction_id`, `timestamp`, `account_number`, `transaction_type`, `amount`, `balance_after`, `status`, `description`, `from_account`, `to_account`.
*Hint:* convert ids to `int` and money values to `float`; if no `timestamp` is given, use `datetime.now()`.

### STEPS 3-6 -- `domain/transaction.py` -> getters and `get_receipt()`
1. Add a getter for every field: `get_id()`, `get_timestamp()`, `get_account_number()`, `get_type()`, `get_amount()`, `get_balance_after()`, `get_status()`, `get_description()`, `get_from_account()`, `get_to_account()`.
2. Implement `get_receipt()` so it returns one line in this format:
   ```text
   TXN ID: <id> | Type: <TYPE> | Amount: Rs. <amount> | Balance After: Rs. <balance> | Status: <status> | <description>
   ```
   Money values use a thousands separator and two decimals, e.g. `Rs. 1,000.00` (hint: `f"{value:,.2f}"`).
3. *(Optional)* Make `__str__()` return the receipt so `print(txn)` shows it.

### STEP 7 -- `domain/account.py` -> `deposit_with_transaction(amount)`
Call the existing `self.deposit(amount)` (it does all the validation), then return `self.build_transaction(...)` with `TransactionType.DEPOSIT`, this account's number as both from/to account, and a description such as `"Deposit of Rs. 5,000.00"`.

### STEP 8 -- `domain/account.py` -> `withdraw_with_transaction(amount, pin)`
Call the existing `self.withdraw(amount, pin)`, then return a `Transaction` of type `TransactionType.WITHDRAW` built the same way (description such as `"Withdrawal of Rs. 2,000.00"`).

### STEPS 9-12 -- `tests/test_transaction_model.py`
| Step | Test method | What to write |
|------|-------------|---------------|
| 9 | `setUp` | Create a Savings account (#1001, "Rajesh Sharma", 30, Rs. 50,000, tenure 3) with `AccountFactory` and set PIN `1234`. |
| 10 | `test_deposit_with_transaction` | Deposit Rs. 5,000 with a transaction; assert type `DEPOSIT`, amount 5000.0, balance after 55000.0 and status `"SUCCESS"`. |
| 11 | `test_withdraw_with_transaction` | Withdraw Rs. 10,000 with PIN 1234; assert type `WITHDRAW`, amount 10000.0 and balance after 40000.0. |
| 12 | `test_receipt_formatting` | Deposit Rs. 1,000; assert the receipt contains `"TXN ID:"`, `"DEPOSIT"` and `"Rs. 1,000.00"`. |

---

## How to Run
Run these commands from inside the `activity16` folder (the folder that contains `gdb/` and `config/`).

### Windows (PowerShell or Command Prompt)
```powershell
# This activity's tests
python -m gdb.tests.test_transaction_model -v

# Every test in the folder (Activity 15 regression tests included)
python -m unittest discover -s gdb/tests -t . -v
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_transaction_model -v
python3 -m unittest discover -s gdb/tests -t . -v
```

---

## Expected Output
Before you start, every test in `test_transaction_model.py` errors with `NotImplementedError: TODO: Step 9 ...`. When you have finished:
```text
test_deposit_with_transaction ... ok
test_receipt_formatting ... ok
test_withdraw_with_transaction ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.00Xs

OK
```

---

## Verification Checklist
- [ ] `python -m gdb.tests.test_transaction_model` reports `Ran 3 tests` and `OK`.
- [ ] The Activity 15 tests (`test_transfer.py`) still pass -- nothing you added broke the old behaviour.
- [ ] Every `Transaction` gets a different id.
- [ ] `balance_after` is the balance **after** the operation, not before.
- [ ] Plain `deposit()` / `withdraw()` still work and still return nothing.

---

## Understanding Questions
1. Why add *new* methods (`deposit_with_transaction`) instead of changing `deposit()` to return a `Transaction`?
2. Why does `deposit_with_transaction()` call `self.deposit()` instead of repeating the validation code?
3. Why is `TransactionType` an `Enum` rather than plain strings such as `"deposit"`?
4. What would you need to change to record a failed withdrawal as a `Transaction` with status `"FAILED"`?
5. `generate_id()` uses a class-level counter. What problem would this cause if two separate programs wrote to the same transaction history?
