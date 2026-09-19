# Activity 6: Testing Exceptions

This solution demonstrates structured testing strategies for custom exception handling in Java. It asserts that expected exceptions are thrown under boundary error conditions and validates error message details.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Test Negative Paths** - Structure `try-catch` test blocks to verify that invalid operations trigger the exact expected exception.
- **Verify Fail-Safe Invariants** - Fail the test explicitly if an expected exception is not thrown.
- **Validate Exception Types** - Assert that specific subclasses (e.g. `InvalidAmountException`) are caught rather than unrelated exceptions.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `Account.java` | Domain class with strict validations throwing `AccountException` subclasses. |
| `AccountException.java` & Subclasses | Custom domain checked exceptions. |
| `TestAccountExceptions.java` | Test suite with targeted `try-catch` blocks asserting positive flows and negative error paths. |

---

## 🔍 Code Walkthrough

### File: `TestAccountExceptions.java`

#### Test Scenarios
1. **Positive Path**: Verifies valid account creation, deposit, and withdrawal complete without throwing any exception.
2. **Negative Deposit**: Asserts `deposit(-500.0)` triggers `InvalidAmountException`.
3. **Overdraft Withdrawal**: Asserts withdrawing amount $>$ balance triggers `InsufficientBalanceException`.
4. **Inactive Account Operation**: Asserts transactions on inactive accounts trigger `InactiveAccountException`.

#### Key Code Snippets
```java
// Testing for expected exception
try {
    Account acc = new Account("ACC002", "Jane Roe", 32, 3000.0, "Savings", "Active", "1234");
    acc.deposit(-500.0);
    System.out.println("FAIL: Expected InvalidAmountException was not thrown.");
} catch (InvalidAmountException e) {
    System.out.println("PASS: Caught expected InvalidAmountException -> " + e.getMessage());
} catch (AccountException e) {
    System.out.println("FAIL: Caught unexpected exception type: " + e.getMessage());
}
```

---

## 💡 Key Concepts

### Concept 1: Negative Testing Pattern
To test that a method throws an expected exception:
1. Place the failing method invocation inside a `try` block.
2. Immediately follow it with `FAIL: Exception was not thrown`.
3. In the `catch (ExpectedException e)` block, mark the test as `PASS`.
4. In any broader `catch` block, mark as `FAIL` (wrong exception type).

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Catch specific subclasses before base class | Enforces Java exception handling precedence and verifies accurate exception categorization. |
| Comprehensive error messaging | Validates that exception messages contain actionable diagnostic data (e.g., requested amount vs balance). |

---

## 🚀 How to Run

### Prerequisites
- Java JDK 17 or higher installed

### Windows (PowerShell)
```powershell
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }
javac -d bin (Get-ChildItem -Recurse -Filter *.java src | ForEach-Object { $_.FullName })
java -cp bin com.gdb.tests.TestAccountExceptions
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb\exceptions\*.java src\com\gdb	ests\*.java
java -cp bin com.gdb.tests.TestAccountExceptions
```

### Linux / macOS (Terminal)
```bash
mkdir -p bin
find src -name "*.java" -print0 | xargs -0 javac -d bin
java -cp bin com.gdb.tests.TestAccountExceptions
```

---

## 📊 Expected Output

```
=========================================
   ACTIVITY 6: EXCEPTION TEST SUITE      
=========================================

[TEST 1] Valid Account Lifecycle:
PASS: Balance after transactions: Rs 5500.0

[TEST 2] Negative Deposit Amount (-500.0):
PASS: Caught expected InvalidAmountException -> Deposit amount must be strictly positive: -500.0

[TEST 3] Overdraft Withdrawal (Balance: 1000, Request: 5000):
PASS: Caught expected InsufficientBalanceException -> Insufficient balance. Available: 1000.0, Requested: 5000.0

[TEST 4] Withdrawal from Inactive Account:
PASS: Caught expected InactiveAccountException -> Cannot withdraw from inactive account: ACC004

=========================================
   ALL TEST CASES EXECUTED SUCCESSFULLY   
=========================================
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to test exception paths systematically in Java.
- How to ensure error conditions fail safely without corrupting application state.

### How It Connects
- **Previous**: Activity 5 created custom domain exception classes.
- **Next**: Activity 7 uses inheritance to specialize account types into Savings, Current, Salary, and Fixed Deposit.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Omitting the failure line inside the `try` block | Always include `FAIL` after the failing line so missed exceptions are detected. |
| Catching generic `Throwable` | Catch specific domain exception types. |

---

## 🏁 Next Steps

Proceed to **Activity 7** to implement inheritance with specialized account subclasses.

---
*End of Activity 6 Solution*
