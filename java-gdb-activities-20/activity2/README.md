# Activity 2: Testing Account Class

## Objective
Write automated unit test cases in Java to verify that the `Account` class works reliably for both normal operations and edge cases.

---

## Target File to Complete
- `src/com/gdb/tests/TestAccount.java`

---

## Plain English Step-by-Step Instructions

### Step 1: Test Account Creation & Initial Balance
1. Create a new `Account` object with an initial balance of 5000.0.
2. Check if the balance returned by `getBalance()` equals 5000.0.
3. Print `[PASS]` if it matches, or `[FAIL]` if it does not.

### Step 2: Test Valid Deposit
1. Deposit an amount of 2000.0 into the account.
2. Verify that the method returns `true` and the new balance becomes 7000.0.
3. Print `[PASS]` if both conditions are met, otherwise print `[FAIL]`.

### Step 3: Test Negative Deposit (Edge Case)
1. Attempt to deposit a negative amount (e.g., -500.0).
2. Verify that the method returns `false` and the balance remains unchanged at 7000.0.
3. Print `[PASS]` or `[FAIL]`.

### Step 4: Test Valid Withdrawal
1. Withdraw 3000.0 from the account.
2. Verify that the method returns `true` and the balance decreases to 4000.0.
3. Print `[PASS]` or `[FAIL]`.

### Step 5: Test Withdrawal Exceeding Balance (Edge Case)
1. Attempt to withdraw 10000.0 (which is greater than the available 4000.0).
2. Verify that the method returns `false` and the balance remains 4000.0.
3. Print `[PASS]` or `[FAIL]`.

### Step 6: Test Negative Withdrawal (Edge Case)
1. Attempt to withdraw a negative amount (e.g., -100.0).
2. Verify that the method returns `false` and the balance remains 4000.0.
3. Print `[PASS]` or `[FAIL]`.

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
=== Activity 2: Test Account Suite ===
Test 1 (Initial Balance 5000.0): [PASS]
Test 2 (Deposit 2000.0 -> Balance 7000.0): [PASS]
Test 3 (Negative Deposit -> Rejected): [PASS]
Test 4 (Withdraw 3000.0 -> Balance 4000.0): [PASS]
Test 5 (Exceeding Withdrawal -> Rejected): [PASS]
Test 6 (Negative Withdrawal -> Rejected): [PASS]
All Account tests completed successfully!
```
