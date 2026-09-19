# Activity 15: Funds Transfer with Daily Limits

## Objective
Introduce a `TransferService` that moves money between two accounts, protected by a **daily transfer limit** that depends on the sender's account type and tenure tier. You will implement the transfer workflow, the daily-limit tracking on `Account`, the rules-engine lookup, and the unit tests that prove it all works.

---

## Prerequisites
- Activity 14 completed: business rules are read from external `.properties` files by the rules engine.
- You are comfortable with `IAccount`, the abstract `Account` class, `AccountFactory`, and the custom exceptions in `gdb/exceptions/`.

---

## What Is Already Done For You
| File | What is provided |
|------|------------------|
| `config/rules/*.properties` | `min.balance`, `interest.rate` and `daily.transfer.limit.<tier>` for every account type (table below). |
| `gdb/domain/account_rules_properties_loader.py` | Reads the `.properties` files from `config/rules/` in this activity folder. |
| `gdb/domain/account_rules_engine.py` | Singleton `AccountRulesEngine`. `_load_rules()` stores each `daily.transfer.limit.<tier>` value under the key `limit_<tier>`; `get_tier(tenure_years)` returns the tier name. |
| `gdb/domain/account.py` | The tracking fields `_daily_transfer_total` and `_last_transfer_date`, plus `get_daily_transfer_total()` and `get_last_transfer_date()`. |
| `gdb/domain/*_account.py` | `can_withdraw(amount)` on every product -- it enforces that product's minimum balance. |

**Tenure tiers** (`get_tier()`):

| Tenure (years) | 0-1 | 2-5 | 6-10 | 11+ |
|----------------|-----|-----|------|-----|
| Tier | `NEW` | `STANDARD` | `PREMIUM` | `PRIVILEGE` |

**Daily transfer limits** (Rs.):

| Properties file | NEW | STANDARD | PREMIUM | PRIVILEGE |
|-----------------|-----|----------|---------|-----------|
| `savings.properties` | 50,000 | 1,00,000 | 2,00,000 | 5,00,000 |
| `current.properties` | 1,00,000 | 2,50,000 | 5,00,000 | 10,00,000 |
| `fixeddeposit.properties` | 0 | 0 | 0 | 0 |
| `salary.properties` | 75,000 | 1,50,000 | 3,00,000 | 7,50,000 |

---

## Target Files to Complete
- `gdb/service/transfer_service.py`
- `gdb/domain/account.py`
- `gdb/domain/account_rules_engine.py`
- `gdb/tests/test_transfer.py`

---

## Step-by-Step Instructions
Search the code for `📝 STEP` -- each step below matches one marked placeholder. Replace each `raise NotImplementedError(...)` with your implementation.

### STEP 1 -- `service/transfer_service.py` -> `transfer(from_acc, to_acc, amount, pin)`
Implement the eight checks/actions **in this order** -- no money may move until every check has passed:
1. Either account is `None` -> `AccountException("Source and destination accounts are required")`
2. Either account is not active (`is_active()`) -> `InactiveAccountException("Both accounts must be active to transfer funds")`
3. `from_acc.verify_pin(pin)` fails -> `InvalidPinException("Incorrect PIN")`
4. `from_acc.can_withdraw(amount)` fails -> `InsufficientBalanceException(f"Insufficient balance for transfer of Rs. {amount}")`
5. Call `from_acc.reset_daily_transfer_if_needed()`; if `from_acc.can_transfer(amount)` fails -> `AccountException` saying the daily limit was exceeded and showing `get_remaining_daily_transfer_limit()`
6. Debit: `from_acc.withdraw(amount, pin)`
7. Credit: `to_acc.deposit(amount)`
8. Record: `from_acc.update_daily_transfer_total(amount)`

> There is no STEP 2 marker: the daily-tracking fields are already provided in `Account.__init__`. Read them before starting Step 3.

### STEP 3 -- `domain/account.py` -> `get_daily_transfer_limit()`
Ask the rules engine: `AccountRulesEngine.get_instance().get_daily_transfer_limit(self.get_account_type(), self.get_tenure_years())`.

### STEP 4 -- `Account.get_remaining_daily_transfer_limit()`
Reset if needed, then return the limit minus `_daily_transfer_total`, never below `0.0`.

### STEP 5 -- `Account.can_transfer(amount)`
Reset if needed, then return `True` only if `_daily_transfer_total + amount` does not exceed the daily limit.

### STEP 6 -- `Account.update_daily_transfer_total(amount)`
Reset if needed, add `amount` to `_daily_transfer_total`, and set `_last_transfer_date` to `datetime.now()`.

### STEP 7 -- `Account.reset_daily_transfer_if_needed()`
If `_last_transfer_date.date()` is not `date.today()`, set `_daily_transfer_total` back to `0.0` and `_last_transfer_date` to `datetime.now()`.

### STEP 8 -- `domain/account_rules_engine.py` -> `get_daily_transfer_limit(account_type, tenure_years)`
Normalise the account type (as `get_minimum_balance()` does), find the tier with `get_tier()`, and look up `limit_<tier>` in `self._rules`. Unknown types or tiers return `0.0`.

### STEPS 9-13 -- `tests/test_transfer.py`
| Step | Test method | What to write |
|------|-------------|---------------|
| 9 | `setUp` | Create a `TransferService`, `acc1` (Savings #1001, Rs. 1,00,000) and `acc2` (Savings #1002, Rs. 20,000) with `AccountFactory` (tenure 0); set PIN `1234` on `acc1` and `5678` on `acc2`. |
| 10 | `test_successful_transfer` | Transfer Rs. 5,000 and assert the balances are Rs. 95,000 and Rs. 25,000. |
| 11 | `test_insufficient_balance` | Assert that a Rs. 95,000 transfer raises `InsufficientBalanceException`. |
| 12 | `test_daily_transfer_limit_breach` | Two Rs. 20,000 transfers succeed; assert the third raises `AccountException`. |
| 13 | `test_remaining_limit` | After a Rs. 10,000 transfer, assert used = Rs. 10,000 and remaining = Rs. 40,000. |

---

## How to Run
Run these commands from inside the `activity15` folder (the folder that contains `gdb/` and `config/`).

### Windows (PowerShell or Command Prompt)
```powershell
python -m gdb.tests.test_transfer -v
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_transfer -v
```

---

## Expected Output
Before you start, every test errors with `NotImplementedError: TODO: Step 9 ...` -- that is your to-do list. When you have finished:
```text
test_daily_transfer_limit_breach ... ok
test_insufficient_balance ... ok
test_remaining_limit ... ok
test_successful_transfer ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.00Xs

OK
```
(The exact test-name format depends on your Python version.)

---

## Verification Checklist
- [ ] `python -m gdb.tests.test_transfer` reports `Ran 4 tests` and `OK`.
- [ ] A Rs. 5,000 transfer moves money from `acc1` to `acc2`.
- [ ] A transfer larger than the available balance raises `InsufficientBalanceException` and moves nothing.
- [ ] The third Rs. 20,000 transfer is rejected by the daily limit, and no money moves on the rejected attempt.
- [ ] Used + remaining always equals the daily limit (10,000 + 40,000 = 50,000).
- [ ] A Fixed Deposit account can never transfer (its limit is 0).

---

## Understanding Questions
1. Why must every check run **before** `from_acc.withdraw(...)`? What would go wrong if the daily-limit check came after the debit?
2. `reset_daily_transfer_if_needed()` compares `date` values, not `datetime` values. Why?
3. The daily-limit methods live on `Account`, not on `IAccount`. What happens if `TransferService` receives a different `IAccount` implementation? How could you make that contract explicit?
4. The tier boundaries live in `get_tier()`, but the limit amounts live in `.properties` files. Which of the two can the operations team change without a code release?
5. A customer's tenure moves from 5 to 6 years. Which daily limit applies now, and why does no Python code need to change for it?
