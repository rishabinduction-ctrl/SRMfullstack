# Activity 12: Testing Interface and Factory

This solution demonstrates writing comprehensive integration tests for client applications interacting exclusively through the `IAccount` interface and `AccountFactory`.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Verify Complete Interface Decoupling** - Write client code that never references concrete class constructors.
- **Validate Factory Product Creation** - Verify that all supported account type strings instantiate the correct underlying product with proper defaults.
- **Test Error Paths in Factory** - Assert that null or unrecognized account types throw meaningful exceptions.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `IAccount.java` | Interface contract. |
| `AccountFactory.java` | Factory class. |
| `TestInterfaceFactory.java` | Test harness asserting factory product creation and interface method execution. |

---

## 🔍 Code Walkthrough

### File: `TestInterfaceFactory.java`

#### Test Scenarios
1. **Savings Creation via Factory**: Verifies creation, interest calculation (4.0%), and info display.
2. **Current Creation via Factory**: Verifies overdraft limit setup and display.
3. **Salary Creation via Factory**: Verifies zero-balance payroll account creation.
4. **Fixed Deposit Creation via Factory**: Verifies tenure setup and interest calculation (6.5%).
5. **Invalid Type Handling**: Asserts `AccountFactory.createAccount("UNKNOWN", ...)` throws `AccountException`.

#### Key Code Snippets
```java
// Testing Factory instantiation
IAccount savings = AccountFactory.createAccount("SAVINGS", "SA100", "Alice", 25, 5000.0, "Active", "1234");
savings.displayAccountInfo();
System.out.println("Savings Interest: Rs " + savings.calculateInterest());

IAccount fd = AccountFactory.createAccount("FIXEDDEPOSIT", "FD400", "Diana", 45, 50000.0, "Active", "0000");
fd.displayAccountInfo();
System.out.println("FD Interest: Rs " + fd.calculateInterest());
```

---

## 💡 Key Concepts

### Concept 1: Dependency Inversion Principle (DIP)
High-level modules (the test driver/client) should not depend on low-level modules (concrete classes). Both should depend on abstractions (`IAccount`).

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Strictly use `IAccount` variable references | Confirms complete decoupling of client code from concrete implementations. |

---

## 🚀 How to Run

### Prerequisites
- Java JDK 17 or higher installed

### Windows (PowerShell)
```powershell
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }
javac -d bin (Get-ChildItem -Recurse -Filter *.java src | ForEach-Object { $_.FullName })
java -cp bin com.gdb.tests.TestInterfaceFactory
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb\exceptions\*.java src\com\gdb	ests\*.java
java -cp bin com.gdb.tests.TestInterfaceFactory
```

### Linux / macOS (Terminal)
```bash
mkdir -p bin
find src -name "*.java" -print0 | xargs -0 javac -d bin
java -cp bin com.gdb.tests.TestInterfaceFactory
```

---

## 📊 Expected Output

```
=========================================
   ACTIVITY 12: FACTORY PATTERN TESTS    
=========================================

--- Testing Savings Account Created via Factory ---
Account Number: SA100
Name: Alice
Age: 25
Balance: Rs 5000.0
Account Type: Savings
Status: Active
Savings Interest: Rs 200.0

--- Testing Current Account Created via Factory ---
Account Number: CA200
Name: Bob
Age: 35
Balance: Rs 10000.0
Account Type: Current
Status: Active

--- Testing Salary Account Created via Factory ---
Account Number: SAL300
Name: Charlie
Age: 28
Balance: Rs 0.0
Account Type: Salary
Status: Active

--- Testing Fixed Deposit Account Created via Factory ---
Account Number: FD400
Name: Diana
Age: 45
Balance: Rs 50000.0
Account Type: FixedDeposit
Status: Active
FD Interest: Rs 3250.0

=========================================
   FACTORY TESTS COMPLETED SUCCESSFULLY  
=========================================
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to write pure interface-based client applications.
- How to test Factory implementations for completeness and error safety.

### How It Connects
- **Previous**: Activity 11 introduced `IAccount` and `AccountFactory`.
- **Next**: Activity 13.1 extracts business policy rules into an `AccountRulesEngine`.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Importing concrete subclasses into client test file | When testing factory decoupling, only import `IAccount` and `AccountFactory`. |

---

## 🏁 Next Steps

Proceed to **Activity 13.1** to build a centralized Business Rules Engine.

---
*End of Activity 12 Solution*
