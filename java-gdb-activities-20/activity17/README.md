# Activity 17: Command Pattern + File Logging

## Objective
Encapsulate each financial money-movement operation (`DEPOSIT`, `WITHDRAW`, `TRANSFER`) as an executable and serializable **Command** object. Log executed commands to a binary file using Java native Object Serialization. This decouples transaction execution from audit logging and enables repeatable command replay.

> **Scope note:** Only `DEPOSIT`, `WITHDRAW`, and `TRANSFER` are modeled as commands here. New operation types (`INTEREST_CREDITED`, `PIN_CHANGED`) can be added later by creating new `XxxCommand` classes — no changes to `TransactionLog` needed. This is the power of the Command Pattern.

---

## Target Files to Complete
- `src/com/gdb/command/TransactionCommand.java`
- `src/com/gdb/command/DepositCommand.java`
- `src/com/gdb/command/WithdrawCommand.java`
- `src/com/gdb/command/TransferCommand.java`
- `src/com/gdb/logging/TransactionLog.java`
- `src/com/gdb/tests/TestCommandLogging.java`

---

## Step-by-Step Instructions

Search the code for `📝 STEP` — each step matches one marked placeholder:

### STEP 1 & 2 — `command/TransactionCommand.java`
1. Declare `void execute() throws Exception;`
2. Declare `Transaction getTransaction();`

### STEP 3 to 6 — `DepositCommand`, `WithdrawCommand`, `TransferCommand`
- **Fields**: store required account references, amounts, pins, and resulting `Transaction`.
- **Constructor**: store all execution arguments.
- **`execute()`**: call the corresponding method (`depositWithTransaction`, `withdrawWithTransaction`, or `transferWithTransaction`) and store the returned `Transaction`.
- **`getTransaction()`**: return stored `Transaction`.

### STEP 7 — `logging/TransactionLog.java` → `log(TransactionCommand cmd)`
- Ensure `data/` directory exists.
- If file doesn't exist, open `ObjectOutputStream`.
- If file already exists, open `AppendableObjectOutputStream` (avoids duplicate stream headers).
- Write `cmd`, flush, and close.

### STEP 8 — `logging/TransactionLog.java` → `readAll()`
- Open `ObjectInputStream` on `data/transactions.ser`.
- Loop `readObject()` until `EOFException` is caught.
- Return `List<TransactionCommand>`.

### STEP 9 — `logging/TransactionLog.java` → `clear()`
- Delete `data/transactions.ser` if it exists.

### STEPS 10–15 — `tests/TestCommandLogging.java`
- Create accounts, execute and log `DepositCommand`, `WithdrawCommand`, `TransferCommand`.
- Read history back and verify count.
- Open new `TransactionLog` instance and verify file persistence.

---

## How to Compile & Run

### Windows (PowerShell)
```powershell
New-Item bin -ItemType Directory -Force | Out-Null
Copy-Item src\main\resources\config bin -Recurse -Force
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java -cp bin com.gdb.tests.TestCommandLogging
```

### Linux & macOS (Terminal / Bash)
```bash
mkdir -p bin && cp -r src/main/resources/config bin/
javac -encoding UTF-8 -d bin $(find src -name "*.java")
java -cp bin com.gdb.tests.TestCommandLogging
```

---

## Expected Output
```text
============================================================
  ACTIVITY 17 — COMMAND PATTERN + FILE LOGGING
============================================================

[STEP 11] Logged: [TXN-...] DEPOSIT | Rs. 5000.0 | Balance After: Rs. 20000.0 | Status: SUCCESS | Deposit of Rs. 5000.0
[STEP 12] Logged: [TXN-...] WITHDRAW | Rs. 2000.0 | Balance After: Rs. 18000.0 | Status: SUCCESS | Withdrawal of Rs. 2000.0
[STEP 13] Logged: [TXN-...] TRANSFER | Rs. 3000.0 | Balance After: Rs. 15000.0 | Status: SUCCESS | Transfer of Rs. 3000.0 to Account #1002

[STEP 14] Read 3 commands from transaction log:
  [1] [TXN-...] DEPOSIT | Rs. 5000.0 | Balance After: Rs. 20000.0 | Status: SUCCESS | Deposit of Rs. 5000.0
  [2] [TXN-...] WITHDRAW | Rs. 2000.0 | Balance After: Rs. 18000.0 | Status: SUCCESS | Withdrawal of Rs. 2000.0
  [3] [TXN-...] TRANSFER | Rs. 3000.0 | Balance After: Rs. 15000.0 | Status: SUCCESS | Transfer of Rs. 3000.0 to Account #1002

[STEP 15] Fresh reader verified 3 persisted commands [PASS]
```
