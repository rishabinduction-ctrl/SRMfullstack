# ACTIVITY 15: Funds Transfer with Daily Limits

## Objective
Introduce a `TransferService` that moves money between two accounts, protected by a **daily transfer limit** that depends on the sender's account type and tenure (privilege level). You will implement the transfer workflow, the daily-limit tracking on `Account`, the rules-engine lookup, and a test driver that proves it all works.

## Prerequisites
- Activity 14 completed: `AccountRulesEngine` (Singleton) loads rules from `src/main/resources/config/rules/*.properties`.
- You understand `IAccount`, the abstract `Account` class, `AccountFactory`, and the custom exceptions in `com.gdb.exceptions`.
- Tenure buckets: `NEW` (0-1 yr), `STANDARD` (1-3 yrs), `PREMIUM` (3-5 yrs), `PRIVILEGE` (5+ yrs).

## What Is Already Done For You
| File | Change |
|------|--------|
| `src/main/resources/config/rules/*.properties` | `daily.transfer.limit.<bucket>` values added (see table below). |
| `AccountRulesPropertiesLoader.java` | `daily.transfer.limit.*` values are parsed as `Double` and stored under the feature key `dailyTransferLimit` (same pattern as `overdraft.limit`). |
| `Account.java` | Fields `dailyTransferTotal` and `lastTransferDate`, plus the getters `getDailyTransferTotal()` and `getLastTransferDate()`. |

| File | new | standard | premium | privilege |
|------|-----|----------|---------|-----------|
| savings | 50000 | 100000 | 200000 | 500000 |
| current | 100000 | 500000 | 1000000 | 1000000 |
| fixeddeposit | 0 | 0 | 0 | 0 |
| salary | 100000 | 500000 | 1000000 | 2500000 |

> `current.properties` only defines the `new`, `standard` and `premium` tenure buckets, so its `privilege` limit is not loaded (Current accounts with 5+ years fall back to `0.0`, exactly like their minimum balance does today).

## Step-by-Step Instructions
Search the code for `📝 STEP` — each step below matches one marked placeholder.

### STEP 1 — `service/TransferService.java` → `transfer(from, to, amount, pin)`
Replace the `UnsupportedOperationException` with the eight checks/actions, **in this order** (nothing may move until every check passes):
1. Null check → `AccountException("Source and destination accounts are required")`
2. Both accounts active → `InactiveAccountException("Both accounts must be active to transfer funds")`
3. `from.verifyPin(pin)` → `InvalidPinException("Incorrect PIN")`
4. `from.canWithdraw(amount)` → `InsufficientBalanceException("Insufficient balance for transfer of Rs. " + amount)`
5. Cast `from` to `Account`, call `resetDailyTransferIfNeeded()`, then `canTransfer(amount)` → `AccountException("Daily transfer limit exceeded. Remaining today: Rs. " + remaining)`
6. Debit: `from.withdraw(amount, pin)`
7. Credit: `to.deposit(amount)`
8. Record: `source.updateDailyTransferTotal(amount)`

### STEP 2.1 — `domain/Account.java` → daily tracking fields
Read the two provided fields. `dailyTransferTotal` is today's running total; `lastTransferDate` tells you which day that total belongs to.

### STEP 3 — `Account.getDailyTransferLimit()`
Return `AccountRulesEngine.getInstance().getDailyTransferLimit(getAccountType(), getTenureYears())`.

### STEP 4 — `Account.getRemainingDailyTransferLimit()`
Reset if needed, then return `Math.max(0.0, getDailyTransferLimit() - dailyTransferTotal)`.

### STEP 5 — `Account.canTransfer(double amount)`
Reset if needed, then return `dailyTransferTotal + amount <= getDailyTransferLimit()`.

### STEP 6 — `Account.updateDailyTransferTotal(double amount)`
Reset if needed, add `amount` to `dailyTransferTotal`, set `lastTransferDate = LocalDateTime.now()`.

### STEP 7 — `Account.resetDailyTransferIfNeeded()`
If `lastTransferDate.toLocalDate()` is not today's date, set `dailyTransferTotal = 0.0` and `lastTransferDate = LocalDateTime.now()`.

### STEP 8 — `domain/AccountRulesEngine.java` → `getDailyTransferLimit(accountType, tenureYears)`
Call `getAdditionalFeature(accountType, tenureYears, "dailyTransferLimit")`; return `0.0` if it is `null`, otherwise cast it to `Double`.

### STEPS 9-13 — `tests/TestTransfer.java`
| Step | What to write |
|------|---------------|
| 9 | Create `acc1` (Savings #1001, Rs. 1,00,000) and `acc2` (Savings #1002, Rs. 20,000) via `AccountFactory`, cast both to `Account`, set PIN `1234` on `acc1`. |
| 10 | Transfer Rs. 5,000 from `acc1` to `acc2`; print both balances. |
| 11 | Try to transfer Rs. 1,00,000; catch `InsufficientBalanceException`. |
| 12 | Print the daily limit, then transfer Rs. 20,000 in a loop until an `AccountException` is thrown; print it. |
| 13 | Print today's used total and the remaining limit. |

## Compile & Run
The `.properties` files must be copied next to the compiled classes, otherwise the engine silently falls back to default rules.

**Windows (PowerShell)** — run inside `activity15`:
```powershell
New-Item bin -ItemType Directory -Force | Out-Null
Copy-Item src\main\resources\config bin -Recurse -Force
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java "-Dfile.encoding=UTF-8" -cp bin com.gdb.tests.TestTransfer
```

**Linux / macOS / Git Bash** — run inside `activity15`:
```bash
mkdir -p bin && cp -r src/main/resources/config bin/
javac -encoding UTF-8 -d bin $(find src -name "*.java")
java -Dfile.encoding=UTF-8 -cp bin com.gdb.tests.TestTransfer
```

The Activity 14 driver still runs unchanged: `java -Dfile.encoding=UTF-8 -cp bin com.gdb.tests.TestAccountRulesEngineProperties`

## Expected Output
```
============================================================
  ACTIVITY 15 — TRANSFER WITH DAILY LIMITS
============================================================

📂 Loading account rules from properties files...
--------------------------------------------------
✅ Loaded rules for: SAVINGS (4 tenure buckets)
✅ Loaded rules for: CURRENT (3 tenure buckets)
✅ Loaded rules for: FIXEDDEPOSIT (4 tenure buckets)
✅ Loaded rules for: SALARY (4 tenure buckets)
--------------------------------------------------
✅ All rules loaded successfully!
   Loaded at: <timestamp>
   Account types: [SALARY, SAVINGS, FIXEDDEPOSIT, CURRENT]

[STEP 9] Account #1001 | Rajesh Sharma (30 yrs, Tenure: 0 yrs) | Savings | Rs. 100000.0 | Active
[STEP 9] Account #1002 | Priya Patel (28 yrs, Tenure: 0 yrs) | Savings | Rs. 20000.0 | Active

[STEP 10] Transfer Rs. 5,000: SUCCESS | acc1 = Rs. 95000.0 | acc2 = Rs. 25000.0
[STEP 11] Caught InsufficientBalanceException: Insufficient balance for transfer of Rs. 100000.0
[STEP 12] Daily limit for acc1: Rs. 50000.0
  Transfer #1 of Rs. 20,000: SUCCESS | used today = Rs. 25000.0
  Transfer #2 of Rs. 20,000: SUCCESS | used today = Rs. 45000.0
[STEP 12] Caught AccountException: Daily transfer limit exceeded. Remaining today: Rs. 5000.0
[STEP 13] Used today: Rs. 45000.0 | Remaining: Rs. 5000.0
```
Your print statements may be worded differently; the balances, the limit (Rs. 50,000), the exception types and the final remaining amount (Rs. 5,000) must match.

## Verification Checklist
- [ ] The project compiles with no errors.
- [ ] `TestAccountRulesEngineProperties` (Activity 14) still runs; its rules table now also lists `dailyTransferLimit`.
- [ ] A Rs. 5,000 transfer moves money from `acc1` to `acc2`.
- [ ] A transfer larger than the available balance throws `InsufficientBalanceException` and moves nothing.
- [ ] The third Rs. 20,000 transfer is rejected by the daily limit; no money moves on the rejected attempt.
- [ ] Used + remaining always equals the daily limit (45,000 + 5,000 = 50,000).
- [ ] A Fixed Deposit account can never transfer (its limit is 0).

## Understanding Questions
1. Why must every check run **before** `from.withdraw(...)`? What would go wrong if the daily-limit check came after the debit?
2. `resetDailyTransferIfNeeded()` compares `LocalDate`, not `LocalDateTime`. Why?
3. The daily-limit methods live on `Account`, not `IAccount`, so `TransferService` casts `from` to `Account`. What happens if someone passes a different `IAccount` implementation? How could you avoid the cast?
4. Why did the properties loader need a change for `daily.transfer.limit.*` even though its generic loop already picks up any `<prefix>.<bucket>` key?
5. A customer's tenure moves from 2 to 3 years. Which of their daily limits changes, and why does no Java code need to change for it?
