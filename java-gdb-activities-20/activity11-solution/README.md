# Activity 11: IAccount Interface and Factory Pattern

This solution demonstrates the **Interface Segregation Principle** and the **Factory Design Pattern** to achieve loose coupling between client code and concrete banking product classes.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Design Interface Contracts (`IAccount`)** - Expose pure behavioral capabilities without dictating inheritance or storage details.
- **Implement the Factory Design Pattern (`AccountFactory`)** - Encapsulate complex object instantiation logic behind a centralized factory method.
- **Achieve Loose Coupling** - Ensure client code depends solely on interfaces rather than concrete constructors.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `IAccount.java` | Pure contract interface declaring all public banking operations. |
| `AbstractAccount.java` | Abstract base class implementing `IAccount`. |
| Concrete Subclasses | `SavingsAccount`, `CurrentAccount`, `SalaryAccount`, `FixedDepositAccount`. |
| `AccountFactory.java` | Centralized factory class providing `createAccount()` method. |
| `TestInterfaceFactory.java` | Test driver creating accounts via the factory. |

---

## 🔍 Code Walkthrough

### File: `IAccount.java`
```java
package com.gdb.domain;
import com.gdb.exceptions.*;

public interface IAccount {
    void deposit(double amount) throws AccountException;
    void withdraw(double amount) throws AccountException;
    double calculateInterest();
    void displayAccountInfo();
    boolean validatePin(String enteredPin) throws InvalidPinException;
    String getAccountNumber();
    String getName();
    int getAge();
    double getBalance();
    String getAccountType();
    String getStatus();
}
```

### File: `AccountFactory.java`
```java
package com.gdb.domain;
import com.gdb.exceptions.AccountException;

public class AccountFactory {
    public static IAccount createAccount(String type, String accNum, String name, int age, double balance, String status, String pin) throws AccountException {
        if (type == null) {
            throw new AccountException("Account type cannot be null");
        }
        switch (type.trim().toUpperCase()) {
            case "SAVINGS":
                return new SavingsAccount(accNum, name, age, balance, status, pin, 4.0, 1000.0);
            case "CURRENT":
                return new CurrentAccount(accNum, name, age, balance, status, pin, 10000.0);
            case "SALARY":
                return new SalaryAccount(accNum, name, age, balance, status, pin);
            case "FIXEDDEPOSIT":
                return new FixedDepositAccount(accNum, name, age, balance, status, pin, 12, 6.5);
            default:
                throw new AccountException("Unknown account type: " + type);
        }
    }
}
```

---

## 💡 Key Concepts

### Concept 1: Interface-Driven Design
Interfaces define *what* an object can do, not *how* it does it. This allows multiple completely different implementations to be used interchangeably.

### Concept 2: Factory Design Pattern
The Factory Pattern centralizes object creation in one place. If constructor signatures change or default parameters are updated, only the factory needs modification, protecting client code.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Return `IAccount` from `createAccount()` | Hides concrete implementation classes from callers. |
| Case-insensitive type matching in Factory | Prevents bugs caused by capitalization differences in account type strings. |

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
=== Activity 11: Interface & Factory Pattern ===
Created: SavingsAccount [SA100] via AccountFactory
Created: CurrentAccount [CA200] via AccountFactory
Created: SalaryAccount [SAL300] via AccountFactory
Created: FixedDepositAccount [FD400] via AccountFactory
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How interfaces provide complete abstraction.
- How the Factory Pattern centralizes creation logic and promotes loose coupling.

### How It Connects
- **Previous**: Activity 10 tested abstract classes.
- **Next**: Activity 12 performs comprehensive integration testing of interface-driven factories.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Declaring fields inside an interface | Interfaces should only declare public abstract methods (or constants). |
| Directly instantiating concrete classes in client code | Always use `AccountFactory.createAccount(...)` when using the Factory pattern. |

---

## 🏁 Next Steps

Proceed to **Activity 12** to build an integration test suite for the factory pattern.

---
*End of Activity 11 Solution*
