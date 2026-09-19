# Activity 10: Testing Abstract Account

This solution demonstrates building a comprehensive test suite for abstract account hierarchies, asserting polymorphic method resolution and boundary validation across all concrete subclasses.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Test Abstract Type Abstractions** - Reference instances purely via `AbstractAccount` variable types.
- **Verify Template Method Behavior** - Confirm that template methods (`displayAccountInfo()`) invoke the appropriate subclass hooks.
- **Assert Subclass Boundary Enforcements** - Verify minimum balances, interest calculations, and overdraft boundaries.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `AbstractAccount.java` | Abstract base class. |
| Concrete Subclasses | `SavingsAccount`, `CurrentAccount`, `FixedDepositAccount`, `SalaryAccount`. |
| `TestAbstractAccount.java` | Test harness validating polymorphic operations against `AbstractAccount`. |

---

## 🔍 Code Walkthrough

### File: `TestAbstractAccount.java`

#### Test Scenarios
1. **Savings Account Abstract Verification**: Asserts `calculateInterest()` computes interest accurately and `displayAccountInfo()` renders `"Savings"`.
2. **Current Account Abstract Verification**: Asserts `calculateInterest()` returns `0.0` and `displayAccountInfo()` renders `"Current"`.
3. **Minimum Balance Violation**: Asserts withdrawal dropping below minimum balance throws `MinimumBalanceViolationException`.

#### Key Code Snippets
```java
// Testing polymorphically through AbstractAccount
AbstractAccount sa = new SavingsAccount("SA001", "Alice", 25, 10000.0, "Active", "1234", 4.0, 1000.0);
AbstractAccount ca = new CurrentAccount("CA001", "Bob", 35, 50000.0, "Active", "5678", 25000.0);

sa.displayAccountInfo(); // Dynamically invokes SavingsAccount.getAccountType()
ca.displayAccountInfo(); // Dynamically invokes CurrentAccount.getAccountType()
```

---

## 💡 Key Concepts

### Concept 1: Polymorphism with Abstract Types
Using abstract types as references (`AbstractAccount acc`) decouples the test driver from concrete subclass constructors, allowing interchangeable use of any account product.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Program to Abstract Superclass | Ensures the test harness tests the contract rather than internal subclass details. |

---

## 🚀 How to Run

### Prerequisites
- Java JDK 17 or higher installed

### Windows (PowerShell)
```powershell
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }
javac -d bin (Get-ChildItem -Recurse -Filter *.java src | ForEach-Object { $_.FullName })
java -cp bin com.gdb.tests.TestAbstractAccount
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb\exceptions\*.java src\com\gdb	ests\*.java
java -cp bin com.gdb.tests.TestAbstractAccount
```

### Linux / macOS (Terminal)
```bash
mkdir -p bin
find src -name "*.java" -print0 | xargs -0 javac -d bin
java -cp bin com.gdb.tests.TestAbstractAccount
```

---

## 📊 Expected Output

```
=========================================
   ACTIVITY 10: ABSTRACT ACCOUNT TESTS   
=========================================

--- Displaying Savings Account Info ---
Account Number: SA001
Name: Alice
Age: 25
Balance: Rs 10000.0
Account Type: Savings
Status: Active
Calculated Interest: Rs 400.0

--- Displaying Current Account Info ---
Account Number: CA001
Name: Bob
Age: 35
Balance: Rs 50000.0
Account Type: Current
Status: Active
Calculated Interest: Rs 0.0

--- Testing Savings Minimum Balance Enforcement ---
PASS: Caught expected MinimumBalanceViolationException -> Withdrawal would violate minimum balance requirement of Rs 1000.0

=========================================
   ACTIVITY 10 TESTS COMPLETED           
=========================================
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to test abstract class contracts and verify dynamic method dispatch.

### How It Connects
- **Previous**: Activity 9 introduced `AbstractAccount`.
- **Next**: Activity 11 introduces interfaces (`IAccount`) and the Factory Design Pattern (`AccountFactory`).

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Casting down to concrete types unnecessarily | Avoid explicit casts unless testing subclass-specific methods not present in the base class. |

---

## 🏁 Next Steps

Proceed to **Activity 11** to implement interfaces and the Factory Pattern.

---
*End of Activity 10 Solution*
