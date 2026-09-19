# ACTIVITY 19: AccountService (Service Layer)

## Objective
Introduce `AccountService` as the **single entry point and orchestrator** for all banking operations. It maintains the in-memory registry of accounts, coordinates with `AccountFactory` and `TransferService`, and uses `TransactionLogger` to log every money movement.

---

## 🏗️ Architecture Diagram

```text
┌──────────────┐
│    Main      │
└──────┬───────┘
       │
       ▼
┌───────────────────────┐
│   AccountService      │  ← Orchestrator
│  - accounts map       │
│  - logger             │
│  - transferService    │
└──┬─────────┬──────────┘
   │         │
   ▼         ▼
┌────────┐ ┌──────────────────┐
│Factory │ │TransactionLogger │
└────────┘ └────────┬─────────┘
                    │
                    ▼
              ┌──────────────┐
              │LogDestination│
              └──────────────┘
```

> **Why a Service Layer?** Without it, every caller would have to remember: (1) create the command, (2) execute, (3) log, (4) build a Transaction. The service hides all of that behind clean, unified method calls.

---

## Target Files to Complete
- `src/com/gdb/service/AccountService.java`
- `src/com/gdb/tests/TestAccountService.java`
- `src/com/gdb/Main.java`

---

## Step-by-Step Instructions

Search the code for `📝 STEP` — each step matches one marked placeholder:

### STEPS 1–2 — `service/AccountService.java` → Fields & Constructor
- Declare `Map<Integer, IAccount> accounts`, `TransactionLogger logger`, `TransferService transferService`, `int nextAccountNumber = 1001`.
- Initialize in constructor.

### STEPS 3–7 — `service/AccountService.java` → Business Methods
- **`openAccount(type, name, age, initialBalance)`**: generate account number, call `AccountFactory`, store in map, return account.
- **`closeAccount(accountNumber, pin)`**: look up account, verify PIN, close account.
- **`deposit(accountNumber, amount)`**: look up account, execute & log `DepositCommand`, return `Transaction`.
- **`withdraw(accountNumber, amount, pin)`**: look up account, execute & log `WithdrawCommand`, return `Transaction`.
- **`transfer(fromAcc, toAcc, amount, pin)`**: look up both accounts, execute & log `TransferCommand`, return `Transaction`.

### STEPS 8–11 — `service/AccountService.java` → Queries
- **`getAccount(accNo)`**, **`getAllAccounts()`**, **`getTransactionHistory()`**, **`getNextAccountNumber()`**.

### STEPS 12–19 — `tests/TestAccountService.java`
- Wire dependencies with `MemoryLogDestination` + `TransactionLogger` + `AccountService`.
- Verify full account lifecycle, transfers, transaction history retrieval, and exception handling.

### STEPS 20–21 — `Main.java`
- Set up service with `FileLogDestination` and execute demo workflow.

---

## How to Compile & Run

### Windows (PowerShell)
```powershell
New-Item bin -ItemType Directory -Force | Out-Null
Copy-Item src\main\resources\config bin -Recurse -Force
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java -cp bin com.gdb.tests.TestAccountService
```

### Linux & macOS (Terminal / Bash)
```bash
mkdir -p bin && cp -r src/main/resources/config bin/
javac -encoding UTF-8 -d bin $(find src -name "*.java")
java -cp bin com.gdb.tests.TestAccountService
```

---

## Expected Output
```text
============================================================
  ACTIVITY 19 — ACCOUNT SERVICE DEMO
============================================================

[STEP 13] Opened: Account #1001 | John Doe (25 yrs, Tenure: 0 yrs) | Savings | Rs. 15000.0 | Active
[STEP 13] Opened: Account #1002 | Jane Smith (30 yrs, Tenure: 0 yrs) | Savings | Rs. 10000.0 | Active

[STEP 14] Deposit: [TXN-...] DEPOSIT | Rs. 5000.0 | Balance After: Rs. 20000.0 | Status: SUCCESS | Deposit of Rs. 5000.0
[STEP 15] Withdrawal: [TXN-...] WITHDRAW | Rs. 2000.0 | Balance After: Rs. 18000.0 | Status: SUCCESS | Withdrawal of Rs. 2000.0
[STEP 16] Transfer: [TXN-...] TRANSFER | Rs. 1000.0 | Balance After: Rs. 17000.0 | Status: SUCCESS | Transfer of Rs. 1000.0 to Account #1002

[STEP 17] Final Balances:
  John (Account #1001): Rs. 17000.0
  Jane (Account #1002): Rs. 11000.0

[STEP 18] Transaction History (3 records):
  [1] [TXN-...] DEPOSIT | Rs. 5000.0 | Balance After: Rs. 20000.0 | Status: SUCCESS | Deposit of Rs. 5000.0
  [2] [TXN-...] WITHDRAW | Rs. 2000.0 | Balance After: Rs. 18000.0 | Status: SUCCESS | Withdrawal of Rs. 2000.0
  [3] [TXN-...] TRANSFER | Rs. 1000.0 | Balance After: Rs. 17000.0 | Status: SUCCESS | Transfer of Rs. 1000.0 to Account #1002

[STEP 19] Error Handling Checks:
  Deposit to missing account caught: Account not found: 9999 [PASS]
  Withdrawal with wrong PIN caught: Incorrect PIN [PASS]
```
