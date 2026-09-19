# Activity 5: Custom Exceptions in Account Class

This solution demonstrates replacing silent boolean error flags with an enterprise-grade **Custom Exception Hierarchy**. It models real-world banking domain errors as strongly typed, checked Java exceptions.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Design Domain Exception Hierarchies** - Create a base `AccountException` extending `Exception` and specialize it into specific domain subclasses.
- **Apply Checked Exceptions** - Declare `throws AccountException` on method signatures to enforce explicit error handling.
- **Enforce Fail-Fast Invariants** - Throw descriptive exceptions immediately when input parameters or business invariants fail.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `AccountException.java` | Base checked exception for all banking domain errors. |
| `InvalidAmountException.java` | Thrown when transaction amount is $\le 0$ or negative. |
| `InsufficientBalanceException.java` | Thrown when a withdrawal exceeds available balance. |
| `InactiveAccountException.java` | Thrown when an operation is attempted on an inactive account. |
| `InvalidPinException.java` | Thrown when PIN validation fails or PIN format is invalid. |
| `MinimumBalanceViolationException.java` | Thrown when withdrawal would breach required minimum balance. |
| `Account.java` | Domain class throwing specific domain exceptions on rule violations. |
| `TestAccountExceptions.java` | Test driver asserting exception propagation. |

---

## 🔍 Code Walkthrough

### Exception Hierarchy

```java
// Base Checked Exception
package com.gdb.exceptions;
public class AccountException extends Exception {
    public AccountException(String message) {
        super(message);
    }
}

// Specialized Subclasses
public class InvalidAmountException extends AccountException {
    public InvalidAmountException(String message) { super(message); }
}

public class InsufficientBalanceException extends AccountException {
    public InsufficientBalanceException(String message) { super(message); }
}

public class InactiveAccountException extends AccountException {
    public InactiveAccountException(String message) { super(message); }
}

public class InvalidPinException extends AccountException {
    public InvalidPinException(String message) { super(message); }
}
```

### File: `Account.java`

#### Key Methods with `throws` Declarations
```java
public void deposit(double amount) throws AccountException {
    if (!"Active".equalsIgnoreCase(this.status)) {
        throw new InactiveAccountException("Cannot deposit to inactive account: " + accountNumber);
    }
    if (amount <= 0) {
        throw new InvalidAmountException("Deposit amount must be strictly positive: " + amount);
    }
    this.balance += amount;
}

public void withdraw(double amount) throws AccountException {
    if (!"Active".equalsIgnoreCase(this.status)) {
        throw new InactiveAccountException("Cannot withdraw from inactive account: " + accountNumber);
    }
    if (amount <= 0) {
        throw new InvalidAmountException("Withdrawal amount must be strictly positive: " + amount);
    }
    if (amount > this.balance) {
        throw new InsufficientBalanceException("Insufficient balance. Available: " + this.balance + ", Requested: " + amount);
    }
    this.balance -= amount;
}
```

---

## 💡 Key Concepts

### Concept 1: Custom Exception Hierarchy
Inheriting from `java.lang.Exception` creates checked exceptions that the Java compiler forces callers to handle via `try-catch` or `throws`. Specialized subclasses enable callers to handle specific error types differently.

### Concept 2: Fail-Fast Pattern
Validating preconditions and immediately throwing an exception before performing any state modification guarantees data consistency.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Base class `AccountException` | Allows callers to catch all banking domain errors using a single polymorphic catch block if desired. |
| Checked vs Unchecked exceptions | Banking operations have recoverable errors that calling code must explicitly acknowledge and handle. |

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
=== Starting Activity 5 Exception Tests ===
--- Test 1: Successful Account Creation & Deposit ---
PASS: Balance after deposit = 6500.0

--- Test 2: Invalid Deposit Amount ---
PASS: Caught expected InvalidAmountException: Deposit amount must be strictly positive: -500.0

--- Test 3: Insufficient Balance Withdrawal ---
PASS: Caught expected InsufficientBalanceException: Insufficient balance. Available: 1000.0, Requested: 5000.0

--- Test 4: Inactive Account Withdrawal ---
PASS: Caught expected InactiveAccountException: Cannot withdraw from inactive account: ACC104
=== All Activity 5 Exception Tests Completed ===
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to create and structure custom checked exception classes in Java.
- How to declare `throws` on method signatures and throw exceptions with informative error messages.

### How It Connects
- **Previous**: Activity 4 used boolean return flags.
- **Next**: Activity 6 focuses on advanced exception testing techniques with targeted `try-catch` assertions.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Catching generic `Exception` everywhere | Catch specific subclasses (`InvalidAmountException`, etc.) first before catching base types. |
| Swallowing exceptions with empty catch blocks | Always log the error or rethrow; never leave `catch (Exception e) {}` empty. |

---

## 🏁 Next Steps

Proceed to **Activity 6** to write comprehensive unit test suites for exception handling.

---
*End of Activity 5 Solution*
