# Activity 6: Exception Handling & Recovery

## Objective
Learn how to use structured `try-catch` blocks to catch specific banking exceptions, display user-friendly error messages, and safely handle failure scenarios.

---

## Target File to Complete
- `src/com/gdb/tests/TestAccountExceptions.java`

---

## Plain English Step-by-Step Instructions

### Step 1: Handle Invalid PIN Exception
1. Inside a `try` block, attempt to withdraw money using an incorrect PIN.
2. Catch `InvalidPinException`, print the error message, and mark the test as `[PASS]`.

### Step 2: Handle Inactive Account Exception
1. Suspend an account.
2. Inside a `try` block, attempt a withdrawal with the correct PIN.
3. Catch `InactiveAccountException`, print the error message, and mark the test as `[PASS]`.

### Step 3: Handle Invalid Amount Exception
1. Inside a `try` block, attempt to deposit or withdraw a negative amount (e.g., -500.0).
2. Catch `InvalidAmountException`, print the error message, and mark the test as `[PASS]`.

### Step 4: Handle Insufficient Balance Exception
1. Inside a `try` block, attempt to withdraw an amount larger than the balance.
2. Catch `InsufficientBalanceException`, print the error message, and mark the test as `[PASS]`.

### Step 5: Polymorphic Catch with Base Exception
1. Close an account.
2. Inside a `try` block, attempt an operation.
3. Catch the base `AccountException` polymorphically, demonstrating that all custom exceptions can be handled by their parent type.

---

## How to Compile & Run (Multi-OS Guide)

### Windows (PowerShell)
```powershell
# Create bin folder if not exists
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }

# Compile all source files
javac -d bin (Get-ChildItem -Recurse -Filter *.java src | ForEach-Object { $_.FullName })

# Run the test program
java -cp bin com.gdb.tests.TestAccountExceptions
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb\tests\*.java src\com\gdb\exceptions\*.java
java -cp bin com.gdb.tests.TestAccountExceptions
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
# Create bin directory
mkdir -p bin

# Compile all Java files
find src -name "*.java" -print0 | xargs -0 javac -d bin

# Run the test program
java -cp bin com.gdb.tests.TestAccountExceptions
```

---

## Expected Output
```
=== Activity 6: Exception Handling Suite ===
[Test 1] Caught Invalid PIN: Invalid PIN entered [PASS]
[Test 2] Caught Inactive Account: Account is not active [PASS]
[Test 3] Caught Invalid Amount: Deposit amount must be positive [PASS]
[Test 4] Caught Insufficient Funds: Insufficient funds in account [PASS]
[Test 5] Polymorphic Handler caught: Account is closed [PASS]
All exception handling tests completed successfully!
```
