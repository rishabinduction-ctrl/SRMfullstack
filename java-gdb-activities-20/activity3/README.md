# Activity 3: Enhanced Account Class (Validation & PIN Security)

## Objective
Upgrade the `Account` class with defensive programming: enforce customer age limits, initial balance rules, 4-digit PIN authentication for withdrawals, and account status management.

---

## Target File to Complete
- `src/com/gdb/domain/Account.java`

---

## Plain English Step-by-Step Instructions

### Step 1: Add Private PIN Field
Add a new private text variable `pin` to `Account.java` to store the customer's 4-digit security PIN.

### Step 2: Add Constructor Validations
Update the constructor to accept the PIN parameter and add input checks:
1. Verify customer age is at least 18. If younger, throw an IllegalArgumentException with a clear message.
2. Verify initial balance is not negative (must be 0 or greater). If negative, throw an IllegalArgumentException.
3. Verify the PIN is exactly 4 numerical digits. If invalid, throw an IllegalArgumentException.
4. Assign all valid arguments to their respective fields.

### Step 3: Implement PIN Validation Method
Create a method `validatePin` that accepts an input PIN string:
- Compare the input PIN with the stored PIN.
- Return `true` if they match, or `false` if they do not match or if the input is empty.

### Step 4: Implement PIN Change Method
Create a method `changePin` that accepts an old PIN and a new PIN:
1. Check if the old PIN is correct using `validatePin`. If incorrect, return `false`.
2. Check if the new PIN is exactly 4 digits. If invalid, return `false`.
3. If both checks pass, update the stored PIN to the new PIN and return `true`.

### Step 5: Implement PIN-Protected Withdrawal
Update the `withdraw` method to accept both the withdrawal amount and the entered PIN:
1. Verify the entered PIN using `validatePin`. If incorrect, reject the transaction and return `false`.
2. Verify the account status is `"ACTIVE"`. If suspended or closed, reject the transaction and return `false`.
3. Verify the amount is positive and does not exceed the current balance.
4. If all checks pass, subtract the amount from the balance and return `true`.

### Step 6: Implement Account Status Management
Add helper methods to change the account status:
1. `suspend()` - Sets status to `"SUSPENDED"`.
2. `activate()` - Sets status to `"ACTIVE"`.
3. `close()` - Sets status to `"CLOSED"`.

---

## How to Compile & Run (Multi-OS Guide)

### Windows (PowerShell)
```powershell
# Create bin folder if not exists
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }

# Compile all source files
javac -d bin (Get-ChildItem -Recurse -Filter *.java src | ForEach-Object { $_.FullName })

# Run the test program
java -cp bin com.gdb.tests.TestAccount
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb\tests\*.java
java -cp bin com.gdb.tests.TestAccount
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
# Create bin directory
mkdir -p bin

# Compile all Java files
find src -name "*.java" -print0 | xargs -0 javac -d bin

# Run the test program
java -cp bin com.gdb.tests.TestAccount
```

---

## Expected Output
```
=== Activity 3: Enhanced Account Test ===
Initial Balance: Rs 5000.0 | Status: ACTIVE
Withdraw with correct PIN: SUCCESS | Balance: Rs 4000.0
Withdraw with wrong PIN: FAILED | Balance: Rs 4000.0
Account Suspended.
Withdraw on SUSPENDED account: FAILED | Balance: Rs 4000.0
Account Re-Activated.
PIN Changed Successfully.
Withdraw with new PIN: SUCCESS | Balance: Rs 3000.0
```
