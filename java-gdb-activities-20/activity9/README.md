# Activity 9: Abstract Classes & Template Method Pattern

## Objective
Refactor the banking hierarchy by creating an abstract base class `AbstractAccount` that enforces common workflows using the Template Method Pattern.

---

## Target Files to Complete
- `src/com/gdb/domain/AbstractAccount.java`
- `src/com/gdb/domain/SavingsAccount.java`
- `src/com/gdb/domain/CurrentAccount.java`
- `src/com/gdb/domain/FixedDepositAccount.java`
- `src/com/gdb/domain/SalaryAccount.java`

---

## Plain English Step-by-Step Instructions

### Step 1: Create `AbstractAccount` Base Class
1. Declare `AbstractAccount` as an abstract class.
2. Move all shared fields (`accountNumber`, `name`, `age`, `balance`, `accountType`, `status`, `pin`) into this class.
3. Implement shared concrete methods: `deposit`, `validatePin`, `changePin`, and `displayAccountInfo`.
4. Declare an abstract method `processDebit(double amount)` that returns void and throws `AccountException`.

### Step 2: Implement the Template Method for Withdrawal
In `AbstractAccount`, write the concrete `withdraw` method that enforces the fixed banking sequence:
1. Validate PIN. If invalid, throw `InvalidPinException`.
2. Validate account status. If not active, throw `InactiveAccountException`.
3. Validate amount. If zero or negative, throw `InvalidAmountException`.
4. Call `processDebit(amount)` so each subclass executes its own debit logic.

### Step 3: Implement `processDebit` in Each Subclass
1. `SavingsAccount`: Check minimum balance rule, then deduct amount.
2. `CurrentAccount`: Check overdraft limit rule, then deduct amount.
3. `SalaryAccount`: Check available balance, then deduct amount.
4. `FixedDepositAccount`: Throw exception blocking premature withdrawal.

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
=== Activity 9: Abstract Account & Template Pattern ===
[Savings] Withdraw 2000: SUCCESS | Balance: Rs 8000.0
[Savings] Withdraw below min balance: Caught MinimumBalanceViolationException [PASS]
[Current] Overdraft debit: SUCCESS | Balance: Rs -3000.0
[FixedDeposit] Premature debit: Caught AccountException [PASS]
Template method pattern executed successfully!
```
