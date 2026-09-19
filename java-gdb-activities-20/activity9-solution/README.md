# Activity 9: Abstract Classes and Template Methods

This solution demonstrates **Abstract Classes** (`abstract class AbstractAccount`) and the **Template Method Pattern** to create rigid behavioral contracts while preventing direct instantiation of generic accounts.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Declare Abstract Classes & Methods** - Define non-instantiable base models with abstract contracts (`calculateInterest()`, `getAccountType()`).
- **Implement the Template Method Pattern** - Combine concrete workflow methods (`displayAccountInfo()`, `deposit()`) with abstract hooks in the base class.
- **Enforce Complete Subclass Implementation** - Require every child class to fulfill all abstract method contracts.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `AbstractAccount.java` | Abstract base class encapsulating common state, concrete methods, and abstract hooks. |
| `SavingsAccount.java` | Implements `calculateInterest()` and `getAccountType()` ("Savings"). |
| `CurrentAccount.java` | Implements `calculateInterest()` ($0.0$) and `getAccountType()` ("Current"). |
| `FixedDepositAccount.java` | Implements `calculateInterest()` and `getAccountType()` ("FixedDeposit"). |
| `TestAbstractAccount.java` | Test driver verifying polymorphic invocation on abstract references. |

---

## 🔍 Code Walkthrough

### File: `AbstractAccount.java`

#### Abstract Method Declarations
```java
package com.gdb.domain;
import com.gdb.exceptions.*;

public abstract class AbstractAccount {
    // Encapsulated Fields
    private String accountNumber;
    private String name;
    private int age;
    private double balance;
    private String status;
    private String pin;

    // Abstract methods: Subclasses MUST implement these
    public abstract double calculateInterest();
    public abstract String getAccountType();

    // Template method using getAccountType() polymorphically
    public void displayAccountInfo() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Balance: Rs " + balance);
        System.out.println("Account Type: " + getAccountType());
        System.out.println("Status: " + status);
    }
}
```

---

## 💡 Key Concepts

### Concept 1: Abstract Classes
An abstract class cannot be instantiated using `new`. It acts as an architectural blueprint that provides shared code while mandating specific method implementations in child classes.

### Concept 2: Template Method Pattern
A template method (e.g., `displayAccountInfo()`) defines the invariant skeleton of an algorithm in the abstract superclass, delegating variable steps (e.g., `getAccountType()`) to abstract methods implemented by subclasses.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Make base class `abstract` | In a bank, an account must always be a concrete product type (Savings, Current, etc.); a generic "Account" has no real-world meaning. |
| Abstract `calculateInterest()` | Each product has a radically different interest calculation formula. |

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
=== Activity 9: Abstract Account Implementation ===
Savings Account: ACC901 (Holder: Alice)
Account Type: Savings
Calculated Interest: Rs 400.0

Current Account: ACC902 (Holder: Bob)
Account Type: Current
Calculated Interest: Rs 0.0
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How abstract classes combine concrete shared implementations with enforced abstract contracts.
- How the template method pattern coordinates base class and subclass execution.

### How It Connects
- **Previous**: Activity 8 used concrete `Account` with overriding.
- **Next**: Activity 10 expands testing across all abstract account implementations.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Attempting `new AbstractAccount(...)` | Abstract classes cannot be instantiated directly; instantiate concrete subclasses instead. |
| Forgetting to implement an abstract method in a subclass | All abstract methods must be implemented unless the subclass is also marked `abstract`. |

---

## 🏁 Next Steps

Proceed to **Activity 10** for complete test suite verification of abstract classes.

---
*End of Activity 9 Solution*
