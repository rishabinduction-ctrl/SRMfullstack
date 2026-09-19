# Activity 5: Custom Exceptions Hierarchy

## Objective
Design and implement a structured hierarchy of custom checked exceptions in Java to replace generic error codes and booleans in banking operations.

---

## Target Files to Complete
- `src/com/gdb/exceptions/AccountException.java`
- `src/com/gdb/exceptions/InvalidAmountException.java`
- `src/com/gdb/exceptions/InsufficientBalanceException.java`
- `src/com/gdb/exceptions/MinimumBalanceViolationException.java`
- `src/com/gdb/exceptions/InactiveAccountException.java`
- `src/com/gdb/exceptions/InvalidPinException.java`
- `src/com/gdb/domain/Account.java`

---

## Plain English Step-by-Step Instructions

### Step 1: Create Base Exception Class
Create `AccountException` extending Java's `Exception` class. It should have a constructor that passes the error message to the parent class.

### Step 2: Create Specific Subclass Exceptions
Create each specialized exception class extending `AccountException`:
1. `InvalidAmountException` - For zero or negative deposit/withdrawal amounts.
2. `InsufficientBalanceException` - When an account does not have enough balance.
3. `MinimumBalanceViolationException` - When a withdrawal would breach minimum balance requirements.
4. `InactiveAccountException` - When an operation is attempted on a suspended or closed account.
5. `InvalidPinException` - When an incorrect PIN is entered.

### Step 3: Update `Account.java` to Throw Custom Exceptions
Update the `withdraw` method to declare that it throws these custom exceptions:
1. If the PIN is incorrect, throw `InvalidPinException`.
2. If the account status is not active, throw `InactiveAccountException`.
3. If the withdrawal amount is zero or negative, throw `InvalidAmountException`.
4. If the amount exceeds the available balance, throw `InsufficientBalanceException`.
5. If all checks pass, subtract the amount from the balance.

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
=== Activity 5: Custom Exceptions Test ===
Caught InvalidPinException as expected: Invalid PIN entered
Caught InactiveAccountException as expected: Account is not active
Caught InvalidAmountException as expected: Withdrawal amount must be positive
Caught InsufficientBalanceException as expected: Insufficient funds in account
Successful withdrawal completed: Rs 1000.0 | New Balance: Rs 4000.0
```
