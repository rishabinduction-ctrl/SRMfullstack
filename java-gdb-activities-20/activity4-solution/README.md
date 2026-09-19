# Activity 4: Testing Enhanced Account

This solution demonstrates an exhaustive validation and security test harness for the enhanced `Account` class, asserting constructor guards, PIN authentication flows, and lifecycle status transitions.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Build Security Test Suites** - Systematically test authentication mechanisms against valid and fraudulent credentials.
- **Verify Lifecycle Invariants** - Test account operations across Active, Suspended, and Inactive states.
- **Assert Boundary Guards** - Verify minimum age, non-null requirements, and PIN length constraints.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `Account.java` | Enhanced domain model with validation guards, PIN security, and lifecycle management. |
| `TestAccount.java` | Test harness asserting authentication security, state transitions, and defensive constraints. |

---

## 🔍 Code Walkthrough

### File: `TestAccount.java`

#### Test Scenarios
1. **PIN Authentication Matrix**:
   - Correct PIN (`"1234"`) -> Returns `true`.
   - Incorrect PIN (`"0000"`) -> Returns `false`.
   - Null or empty PIN -> Returns `false`.
2. **Lifecycle State Transition Matrix**:
   - Status `"Active"` -> Deposits and withdrawals allowed.
   - Status `"Inactive"` -> Deposits and withdrawals rejected.
   - Transitioning status from `"Active"` to `"Inactive"` immediately disables transactions.

#### Key Code Snippets
```java
// Testing status transition
Account acc = new Account("ACC3001", "Charlie", 28, 5000.0, "Savings", "Active", "4321");
acc.deposit(1000.0); // Succeeded

// Deactivating account
acc.setStatus("Inactive");
boolean blockedWithdraw = acc.withdraw(500.0);
if (!blockedWithdraw) {
    System.out.println("PASS: Inactive account blocked withdrawal.");
}
```

---

## 💡 Key Concepts

### Concept 1: State-Dependent Behavior
Objects change their operational behavior based on their internal state (e.g., an account in `"Inactive"` state behaves differently than in `"Active"` state).

### Concept 2: Security Regression Testing
Ensuring that changes to business features do not compromise core authentication or authorization checks.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Modular test methods | Grouping test assertions into distinct named scenarios simplifies defect identification. |
| Setter for `status` with validation | Allows controlled lifecycle transitions (e.g., closing or freezing an account). |

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
=== Starting Activity 4 Security & Lifecycle Tests ===
[TEST 1] PIN Verification:
  - Correct PIN: PASS
  - Incorrect PIN: PASS (Rejected)
  - Null PIN: PASS (Rejected)
[TEST 2] Active Account Transactions: PASS
[TEST 3] Inactive Account Protection: PASS (Transactions Blocked)
[TEST 4] Status Transition: PASS (Active -> Inactive Enforced)
=== All Activity 4 Tests Completed Successfully ===
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to construct multi-scenario security verification suites.
- How to test state transitions and lifecycle mutation effects.

### How It Connects
- **Previous**: Activity 3 added PIN and status defenses.
- **Next**: Activity 5 replaces silent boolean return failures with strongly typed custom domain exceptions.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Forgetting to test `null` inputs | Always pass `null` to `validatePin()` to ensure `NullPointerException` is avoided. |
| Hardcoding test credentials globally | Instantiate fresh `Account` fixtures for each independent test scenario. |

---

## 🏁 Next Steps

Proceed to **Activity 5** to introduce custom domain exceptions.

---
*End of Activity 4 Solution*
