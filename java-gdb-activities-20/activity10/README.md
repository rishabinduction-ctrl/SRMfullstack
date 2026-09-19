# Activity 10: Banking Operations with Abstract Accounts

## Objective
Build a transaction engine to manage collections of abstract accounts, execute secure fund transfers between accounts, and process monthly banking cycles.

---

## Target File to Complete
- `src/com/gdb/tests/TestAbstractAccount.java`

---

## Plain English Step-by-Step Instructions

### Step 1: Create Account Portfolio
Create an array of `AbstractAccount` objects containing different account types (Savings, Current, and Salary accounts).

### Step 2: Implement Fund Transfer Method
Write a method to transfer funds from one account to another:
1. Attempt to withdraw the amount from the source account using the provided PIN.
2. If withdrawal succeeds, deposit the amount into the destination account.
3. If withdrawal throws an exception, ensure the destination account is NOT credited and handle the error gracefully.

### Step 3: Process Monthly Banking Cycle
Loop through the account portfolio and perform monthly account maintenance:
1. If an account is a `SavingsAccount`, apply its monthly interest to the balance.
2. If an account is a `SalaryAccount`, check its salary credit history.

---

## How to Compile & Run (Multi-OS Guide)

### Windows (PowerShell)
```powershell
# Create bin folder if not exists
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }

# Compile all source files
javac -d bin (Get-ChildItem -Recurse -Filter *.java src | ForEach-Object { $_.FullName })

# Run the test program
java -cp bin com.gdb.tests.TestAbstractAccount
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb\tests\*.java src\com\gdb\exceptions\*.java
java -cp bin com.gdb.tests.TestAbstractAccount
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
# Create bin directory
mkdir -p bin

# Compile all Java files
find src -name "*.java" -print0 | xargs -0 javac -d bin

# Run the test program
java -cp bin com.gdb.tests.TestAbstractAccount
```

---

## Expected Output
```
=== Activity 10: Banking Operations Suite ===
Transfer Rs 3000 from Savings to Current: SUCCESS
Savings Balance: Rs 7000.0 | Current Balance: Rs 8000.0
Failed Transfer (Wrong PIN): Exception caught, no balance changed [PASS]
Monthly Interest Cycle processed for all qualifying accounts.
All banking operations passed!
```
