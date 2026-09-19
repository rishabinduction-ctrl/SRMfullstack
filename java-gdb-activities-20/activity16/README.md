# Activity 16: Transaction Model

## Objective
Introduce a structured `Transaction` model and a `TransactionType` enum to capture immutable historical records of banking operations. Students will add overloaded methods to `Account` and `TransferService` that execute money movements and return detailed `Transaction` audit records, while preserving full backward compatibility with existing method signatures.

> **Scope note:** Only money-movement operations (`DEPOSIT`, `WITHDRAW`, `TRANSFER`) are being modeled as Transactions in this activity. The pattern is extensible — future transaction types (`INTEREST_CREDITED`, `ACCOUNT_CLOSED`, `PIN_CHANGED`) can be added later by simply extending `TransactionType` and following the same pattern.

---

## Target Files to Complete
- `src/com/gdb/domain/TransactionType.java`
- `src/com/gdb/domain/Transaction.java`
- `src/com/gdb/domain/Account.java`
- `src/com/gdb/service/TransferService.java`
- `src/com/gdb/tests/TestTransactionModel.java`

---

## Step-by-Step Instructions

Search the code for `📝 STEP` — each step matches one marked placeholder:

### STEP 1 — `domain/TransactionType.java`
Declare the enum constants for supported operations: `DEPOSIT`, `WITHDRAW`, `TRANSFER`.

### STEP 2 — `domain/Transaction.java` → Declare Fields
Declare the following private fields:
- `String transactionId` (unique identifier)
- `LocalDateTime timestamp` (time of execution)
- `int accountNumber` (target account)
- `TransactionType type` (operation type)
- `double amount` (transacted amount)
- `double balanceAfter` (resulting balance)
- `String status` (`"SUCCESS"` or `"FAILED"`)
- `String description` (human-readable summary)
- `int fromAccount` (source account, or 0)
- `int toAccount` (destination account, or 0)

### STEP 3 — `domain/Transaction.java` → All-Args Constructor
Implement constructor initializing all instance variables.

### STEP 4 — `domain/Transaction.java` → Getters & Setters
Provide standard getters and setters for all fields.

### STEP 5 — `domain/Transaction.java` → `toString()`
Format transaction into display format: `[TXN-...] TYPE | Rs. <amount> | Balance After: Rs. <bal> | Status: SUCCESS | <desc>`.

### STEP 6 — `domain/Transaction.java` → `generateId()`
Static generator method returning `"TXN-" + System.currentTimeMillis() + "-" + (++counter)`.

### STEP 7 — `domain/Account.java` → `depositWithTransaction(double amount)`
Call `deposit(amount)`, then build and return a `Transaction` of type `DEPOSIT`.

### STEP 8 — `domain/Account.java` → `withdrawWithTransaction(double amount, int pin)`
Call `withdraw(amount, pin)`, then build and return a `Transaction` of type `WITHDRAW`.

### STEP 9 — `service/TransferService.java` → `transferWithTransaction(...)`
Call existing `transfer(from, to, amount, pin)`, then construct and return a `Transaction` of type `TRANSFER`.

### STEPS 10–13 — `tests/TestTransactionModel.java`
- **STEP 10**: Create account, set PIN, execute `depositWithTransaction(5000)`, print Transaction.
- **STEP 11**: Execute `withdrawWithTransaction(2000, 1234)`, print Transaction.
- **STEP 12**: Execute `transferWithTransaction(acc1, acc2, 1000, 1234)`, print Transaction.
- **STEP 13**: Call legacy `deposit(1000)` and verify backward compatibility.

---

## How to Compile & Run

### Windows (PowerShell)
```powershell
New-Item bin -ItemType Directory -Force | Out-Null
Copy-Item src\main\resources\config bin -Recurse -Force
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java -cp bin com.gdb.tests.TestTransactionModel
```

### Linux & macOS (Terminal / Bash)
```bash
mkdir -p bin && cp -r src/main/resources/config bin/
javac -encoding UTF-8 -d bin $(find src -name "*.java")
java -cp bin com.gdb.tests.TestTransactionModel
```

---

## Expected Output
```text
============================================================
  ACTIVITY 16 — TRANSACTION MODEL TEST
============================================================

📂 Loading account rules from properties files...
--------------------------------------------------
✅ Loaded rules for: SAVINGS (4 tenure buckets)
✅ Loaded rules for: CURRENT (3 tenure buckets)
✅ Loaded rules for: FIXEDDEPOSIT (4 tenure buckets)
✅ Loaded rules for: SALARY (4 tenure buckets)
--------------------------------------------------
✅ All rules loaded successfully!

[STEP 10] Deposit Transaction: [TXN-...] DEPOSIT | Rs. 5000.0 | Balance After: Rs. 55000.0 | Status: SUCCESS | Deposit of Rs. 5000.0
[STEP 11] Withdrawal Transaction: [TXN-...] WITHDRAW | Rs. 2000.0 | Balance After: Rs. 53000.0 | Status: SUCCESS | Withdrawal of Rs. 2000.0
[STEP 12] Transfer Transaction: [TXN-...] TRANSFER | Rs. 1000.0 | Balance After: Rs. 52000.0 | Status: SUCCESS | Transfer of Rs. 1000.0 to Account #1002
[STEP 13] Legacy Deposit +1000: Account #1001 | Rajesh Sharma (30 yrs, Tenure: 0 yrs) | Savings | Rs. 53000.0 | Active
```
