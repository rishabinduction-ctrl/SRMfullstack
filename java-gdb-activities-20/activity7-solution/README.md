# Activity 7: Account Subclasses (Inheritance)

This solution demonstrates Object-Oriented **Inheritance** in Java by extending the base `Account` class into specialized banking products: `SavingsAccount`, `CurrentAccount`, `FixedDepositAccount`, and `SalaryAccount`.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Apply Class Inheritance (`extends`)** - Inherit core attributes and methods from `Account` to avoid code duplication.
- **Master Constructor Chaining (`super`)** - Pass common parameters up to the superclass constructor using `super(...)`.
- **Add Product-Specific Attributes** - Introduce specialized fields (such as `interestRate`, `overdraftLimit`, `tenureMonths`, `employerName`) in child classes.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `Account.java` | Base superclass holding common state and foundational transaction methods. |
| `SavingsAccount.java` | Subclass adding `minBalance`, `interestRate`, and `applyInterest()` logic. |
| `CurrentAccount.java` | Subclass adding `overdraftLimit` for commercial accounts. |
| `FixedDepositAccount.java` | Subclass adding `tenureMonths` and `calculateMaturityAmount()`. |
| `SalaryAccount.java` | Subclass adding `employerName` and `inactiveMonths`. |
| `TestAccountSubclasses.java` | Test driver instantiating and verifying each subclass product. |

---

## 🔍 Code Walkthrough

### File: `SavingsAccount.java`
```java
package com.gdb.domain;

import com.gdb.exceptions.*;

public class SavingsAccount extends Account {
    private double minBalance = 1000.0;
    private double interestRate = 4.0;

    public SavingsAccount(String accountNumber, String name, int age, double balance, String status, String pin) {
        super(accountNumber, name, age, balance, "SAVINGS", status, pin);
    }

    public SavingsAccount(String accountNumber, String name, int age, double balance, String status, String pin, double minBalance, double interestRate) {
        super(accountNumber, name, age, balance, "SAVINGS", status, pin);
        this.minBalance = minBalance;
        this.interestRate = interestRate;
    }

    public void applyInterest() {
        double interest = this.balance * (interestRate / 100.0);
        this.balance += interest;
    }

    public double getMinBalance() { return minBalance; }
    public double getInterestRate() { return interestRate; }
}
```

### File: `CurrentAccount.java`
```java
package com.gdb.domain;

public class CurrentAccount extends Account {
    private double overdraftLimit = 25000.0;

    public CurrentAccount(String accountNumber, String name, int age, double balance, String status, String pin) {
        super(accountNumber, name, age, balance, "CURRENT", status, pin);
    }

    public CurrentAccount(String accountNumber, String name, int age, double balance, String status, String pin, double overdraftLimit) {
        super(accountNumber, name, age, balance, "CURRENT", status, pin);
        this.overdraftLimit = overdraftLimit;
    }

    public double getOverdraftLimit() { return overdraftLimit; }
    public void setOverdraftLimit(double overdraftLimit) { this.overdraftLimit = overdraftLimit; }
}
```

### File: `FixedDepositAccount.java`
```java
package com.gdb.domain;

public class FixedDepositAccount extends Account {
    private int tenureMonths = 12;
    private double interestRate = 6.5;

    public FixedDepositAccount(String accountNumber, String name, int age, double balance, String status, String pin) {
        super(accountNumber, name, age, balance, "FIXED_DEPOSIT", status, pin);
    }

    public FixedDepositAccount(String accountNumber, String name, int age, double balance, String status, String pin, int tenureMonths, double interestRate) {
        super(accountNumber, name, age, balance, "FIXED_DEPOSIT", status, pin);
        this.tenureMonths = tenureMonths;
        this.interestRate = interestRate;
    }

    public double calculateMaturityAmount() {
        return this.balance * Math.pow(1 + (interestRate / 100.0) / 12, 12 * (tenureMonths / 12.0));
    }

    public int getTenureMonths() { return tenureMonths; }
    public double getInterestRate() { return interestRate; }
}
```

### File: `SalaryAccount.java`
```java
package com.gdb.domain;

public class SalaryAccount extends Account {
    private String employerName;
    private int inactiveMonths = 0;

    public SalaryAccount(String accountNumber, String name, int age, double balance, String status, String pin) {
        super(accountNumber, name, age, balance, "SALARY", status, pin);
    }

    public SalaryAccount(String accountNumber, String name, int age, double balance, String status, String pin, String employerName) {
        super(accountNumber, name, age, balance, "SALARY", status, pin);
        this.employerName = employerName;
        this.inactiveMonths = 0;
    }

    public String getEmployerName() { return employerName; }
    public int getInactiveMonths() { return inactiveMonths; }
    public void setInactiveMonths(int inactiveMonths) { this.inactiveMonths = inactiveMonths; }
    public void incrementInactiveMonths() { this.inactiveMonths++; }
}
```

---

## 💡 Key Concepts

### Concept 1: Inheritance & DRY Principle
Inheritance (`extends`) promotes the **Don't Repeat Yourself (DRY)** principle by allowing child classes to automatically inherit all accessible fields and methods of the parent class.

### Concept 2: Constructor Delegation via `super()`
The first statement in a subclass constructor must explicitly call `super(...)` to ensure the parent class fields are properly initialized.

---

## 🚀 How to Run

### Prerequisites
- Java JDK 17 or higher installed

### Windows (PowerShell)
```powershell
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }
javac -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java -cp bin com.gdb.tests.TestAccountSubclasses
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb\exceptions\*.java src\com\gdb\tests\*.java
java -cp bin com.gdb.tests.TestAccountSubclasses
```

### Linux / macOS (Terminal)
```bash
mkdir -p bin
find src -name "*.java" -print0 | xargs -0 javac -d bin
java -cp bin com.gdb.tests.TestAccountSubclasses
```

---

## 📊 Expected Output

```
=== Activity 7: Account Subclasses Test ===
Savings Account Created: Balance Rs 10000.0 | Min Balance: Rs 1000.0
Current Account Created: Overdraft Limit Rs 25000.0
Fixed Deposit Created: Tenure 12 months | Interest: 6.5%
Salary Account Created: Employer Infosys
All subclasses instantiated successfully!
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to structure specialized domain entities using inheritance.
- How to invoke superclass constructors using `super()`.

### How It Connects
- **Previous**: Activity 6 verified exception handling.
- **Next**: Activity 8 adds method overriding (`@Override`) and runtime polymorphism across subclasses.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Placing statements before `super()` in constructor | `super(...)` MUST be the very first statement in a constructor. |
| Re-declaring inherited fields in child classes | Do not re-declare `balance` or `name` in `SavingsAccount`; use inherited accessors. |

---

## 🏁 Next Steps

Proceed to **Activity 8** to implement method overriding and polymorphic withdrawals.

---
*End of Activity 7 Solution*
