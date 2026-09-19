# ACTIVITY 20: AccountUI (Interactive Console Application)

## Objective
Build a comprehensive **menu-driven console application** (`AccountUI`) on top of `AccountService`. The UI layer strictly communicates through the service layer, gathering user input, formatting parameters, calling service methods, and rendering friendly feedback.

---

## 🏗️ Architecture Diagram

```text
┌──────────────┐
│    Main      │   ← wires dependencies
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  AccountUI   │   ← collects user input, prints output
└──────┬───────┘
       │ delegates
       ▼
┌──────────────────┐
│  AccountService  │   ← orchestration + logging
└──────┬───────────┘
       │
       ▼
   Domain / Commands / Logger
```

> **Separation of Concerns:** The UI knows nothing about `Transaction`, `Command`, or `AccountRulesEngine`. It only knows `AccountService`. This is why we can swap the console UI for a REST API, web app, or mobile app tomorrow without touching business logic classes.

---

## Target Files to Complete
- `src/com/gdb/ui/AccountUI.java`
- `src/com/gdb/Main.java`

---

## Step-by-Step Instructions

Search the code for `📝 STEP` — each step matches one marked placeholder:

### STEPS 1–2 — `ui/AccountUI.java` → Fields & Constructor
- Declare `AccountService service` and `Scanner scanner`.
- Initialize in constructor.

### STEP 3 — `ui/AccountUI.java` → `start()`
- Run an infinite `while (true)` loop:
  - Display main menu.
  - Read integer choice.
  - Dispatch via switch statement to appropriate handler (1 to 8).
  - Handle exceptions and print clean error messages without crashing.

### STEP 4 — `ui/AccountUI.java` → `displayMainMenu()`
- Render the 8-option ASCII menu.

### STEPS 5–11 — `ui/AccountUI.java` → Action Handlers
- **`handleOpenAccount()`**: collect type, name, age, balance, call `service.openAccount`, then prompt for PIN and call `acc.setPin(pin)`.
- **`handleDeposit()`**: collect account number and amount, call `service.deposit`.
- **`handleWithdraw()`**: collect account number, amount, and PIN, call `service.withdraw`.
- **`handleTransfer()`**: collect source/destination account numbers, amount, and PIN, call `service.transfer`.
- **`handleCloseAccount()`**: collect account number and PIN, call `service.closeAccount`.
- **`handleViewAccount()`**: collect account number and display details.
- **`handleViewTransactions()`**: display all logged commands with indexing.

### STEPS 12–14 — `ui/AccountUI.java` → Robust Input Helpers
- **`readInt(prompt)`**, **`readDouble(prompt)`**, **`readString(prompt)`** with exception handling against non-numeric entries.

### STEP 15 — `Main.java`
- Wire up `FileLogDestination` → `TransactionLogger` → `AccountService` → `AccountUI` → `ui.start()`.

---

## How to Compile & Run

### Interactive Console App
#### Windows (PowerShell)
```powershell
New-Item bin -ItemType Directory -Force | Out-Null
Copy-Item src\main\resources\config bin -Recurse -Force
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java -cp bin com.gdb.Main
```

#### Linux & macOS (Terminal / Bash)
```bash
mkdir -p bin && cp -r src/main/resources/config bin/
javac -encoding UTF-8 -d bin $(find src -name "*.java")
java -cp bin com.gdb.Main
```

### Automated Integration Test
```powershell
java -cp bin com.gdb.tests.TestAccountUI
```

---

## Sample Interactive Session

```text
Booting Global Digital Bank...

========================================
   GLOBAL DIGITAL BANK
========================================
1. Open Account
2. Deposit
3. Withdraw
4. Transfer
5. Close Account
6. View Account Details
7. View Transaction History
8. Exit
========================================
Enter your choice: 1

--- Open Account ---
Account Type (Savings/Current/FixedDeposit/Salary): SAVINGS
Name: John Doe
Age: 25
Initial Balance: 15000
SUCCESS: Account #1001 | John Doe (25 yrs, Tenure: 0 yrs) | Savings | Rs. 15000.0 | Active
Set 4-digit PIN: 1234
PIN set successfully.

========================================
   GLOBAL DIGITAL BANK
========================================
...
Enter your choice: 2

--- Deposit ---
Account Number: 1001
Amount to deposit: 5000
SUCCESS: Deposited Rs. 5000.0 to #1001. New balance: Rs. 20000.0

...

Enter your choice: 8
Thank you! Goodbye.
```
