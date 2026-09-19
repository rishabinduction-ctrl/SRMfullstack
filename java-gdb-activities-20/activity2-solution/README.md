# Activity 2: Testing Account Class

This solution demonstrates writing structured, comprehensive unit-level test scenarios in Java to verify the correctness of the `Account` class under normal and boundary conditions.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Structure Automated Verification** - Write systematic test cases that programmatically check expected values.
- **Test Boundary Conditions** - Verify edge cases including zero deposits, negative withdrawals, and overdraft attempts.
- **Inspect State Transitions** - Track balance mutations across sequential banking transactions.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `Account.java` | Domain class representing bank account entity with deposit, withdraw, and display methods. |
| `TestAccount.java` | Test driver asserting state changes across positive, negative, and zero transaction amounts. |

---

## 🔍 Code Walkthrough

### File: `Account.java`
Implements the core entity with `accountNumber`, `name`, `age`, `balance`, `accountType`, and `status`.

### File: `TestAccount.java`

#### Test Scenarios
1. **Initial State Verification**: Asserts that fields match values supplied in the constructor.
2. **Valid Deposit Test**: Depositing positive amounts increases balance and returns `true`.
3. **Invalid Deposit Test**: Depositing zero or negative amounts is rejected, returning `false` and leaving balance unchanged.
4. **Valid Withdrawal Test**: Withdrawing amounts $\le$ balance succeeds, deducting from balance and returning `true`.
5. **Overdraft Prevention Test**: Withdrawing amount $>$ balance is rejected, returning `false` and preserving balance.

#### Key Code Snippets
```java
// Testing overdraft protection
double initialBalance = acc.getBalance();
boolean withdrawResult = acc.withdraw(100000.0); // Exceeds balance
if (!withdrawResult && acc.getBalance() == initialBalance) {
    System.out.println("PASS: Overdraft correctly prevented.");
} else {
    System.out.println("FAIL: Overdraft protection failed.");
}
```

---

## 💡 Key Concepts

### Concept 1: Test Assertions & Expected vs Actual
A test compares the *Actual Value* produced by code against the *Expected Value* mandated by business specifications. If `actual == expected`, the test passes; otherwise it fails.

### Concept 2: Boundary Value Analysis
Testing values at the edges of equivalence partitions (e.g., amount = 0, amount = balance, amount = balance + 0.01) to catch subtle logical bugs.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Verification without external frameworks (JUnit) | Focuses student attention on raw Java control flow, boolean assertions, and debugging before introducing test frameworks. |
| Clear PASS/FAIL console reporting | Enables immediate visual verification of test outcomes. |

---

## 🚀 How to Run

### Prerequisites
- Java JDK 17 or higher installed

### Windows (PowerShell)
```powershell
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }
javac -d bin (Get-ChildItem -Recurse -Filter *.java src | ForEach-Object { $_.FullName })
java -cp bin com.gdb.tests.TestAccount
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb	ests\*.java
java -cp bin com.gdb.tests.TestAccount
```

### Linux / macOS (Terminal)
```bash
mkdir -p bin
find src -name "*.java" -print0 | xargs -0 javac -d bin
java -cp bin com.gdb.tests.TestAccount
```

---

## 📊 Expected Output

```
=== Starting Account Test Suite ===
Test 1: Initial Account Creation -> PASS
Test 2: Valid Deposit (+1500.0) -> PASS [New Balance: 6500.0]
Test 3: Invalid Deposit (-500.0) -> PASS [Rejected, Balance: 6500.0]
Test 4: Valid Withdrawal (-2000.0) -> PASS [New Balance: 4500.0]
Test 5: Overdraft Withdrawal (-10000.0) -> PASS [Rejected, Balance: 4500.0]
=== All Tests Completed Successfully ===
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to systematically test all logical branches of domain methods.
- How to verify that failed operations do not corrupt or alter object state.

### How It Connects
- **Previous**: Activity 1 built the basic `Account` class.
- **Next**: Activity 3 introduces defensive validation, security PINs, and lifecycle status checks.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Only testing happy paths (positive amounts) | Always write negative test cases (negative amounts, zero, overdrafts). |
| Not verifying balance after a rejected transaction | Assert that balance remains strictly unchanged when `withdraw()` returns `false`. |

---

## 🏁 Next Steps

Proceed to **Activity 3** to enhance `Account` with defensive parameter validation and PIN authentication.

---
*End of Activity 2 Solution*
