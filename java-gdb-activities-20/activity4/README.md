# Activity 4: Enhanced Account Testing Suite

## Objective
Write comprehensive automated test cases to verify PIN security, status rules, age restrictions, and error handling for the enhanced `Account` class.

---

## Target File to Complete
- `src/com/gdb/tests/TestAccount.java`

---

## Plain English Step-by-Step Instructions

### Step 1: Test Age Validation on Account Creation
1. Attempt to create an account with an age less than 18 (e.g., age 16) inside a try-catch block.
2. Verify that an `IllegalArgumentException` is caught and print `[PASS]`.

### Step 2: Test PIN Verification on Withdrawal
1. Create an account with PIN `"1234"` and balance 5000.0.
2. Attempt to withdraw with a wrong PIN (e.g., `"9999"`). Verify that withdrawal returns `false` and balance remains unchanged.
3. Attempt to withdraw with the correct PIN `"1234"`. Verify that withdrawal returns `true` and balance decreases.

### Step 3: Test PIN Change Functionality
1. Change the PIN from `"1234"` to `"5678"`. Verify the change returns `true`.
2. Try withdrawing with the old PIN `"1234"`. Verify it now fails.
3. Try withdrawing with the new PIN `"5678"`. Verify it succeeds.

### Step 4: Test Account Suspension and Reactivation
1. Suspend the account using `suspend()`.
2. Attempt to withdraw with the correct PIN. Verify that the transaction fails because the account is suspended.
3. Reactivate the account using `activate()`.
4. Attempt withdrawal again. Verify that the transaction now succeeds.

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
=== Activity 4: Enhanced Account Test Suite ===
Test 1 (Underage Customer Rejection): [PASS]
Test 2 (Wrong PIN Rejection): [PASS]
Test 3 (Correct PIN Withdrawal): [PASS]
Test 4 (PIN Change & Old PIN Invalidation): [PASS]
Test 5 (Suspended Account Block): [PASS]
Test 6 (Reactivation & Success): [PASS]
All Enhanced Account tests passed!
```
