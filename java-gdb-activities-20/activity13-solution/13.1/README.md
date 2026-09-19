# Activity 13.1: Rules Engine (If-Else)

This solution demonstrates centralizing business policy thresholds into a dedicated **Business Rules Engine** (`AccountRulesEngine`) using structured conditional evaluation.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Centralize Business Policies** - Extract minimum balance, interest rate, and overdraft threshold rules out of domain classes into a dedicated engine.
- **Implement Policy Evaluation** - Write clean conditional rules for interest rates, minimum balances, and tenure constraints.
- **Decouple Policy from Data** - Allow domain objects to act as pure state models while delegating rule checks to the engine.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `AccountRulesEngine.java` | Central engine providing static policy evaluation methods for all account types. |
| `TestAccountRulesEngine.java` | Test driver verifying policy rules across Savings, Current, Salary, and Fixed Deposit accounts. |

---

## 🔍 Code Walkthrough

### File: `AccountRulesEngine.java`

```java
package com.gdb.domain;

public class AccountRulesEngine {
    public static double getMinimumBalance(String accountType) {
        if ("SAVINGS".equalsIgnoreCase(accountType)) {
            return 1000.0;
        }
        return 0.0;
    }

    public static double getInterestRate(String accountType) {
        if ("SAVINGS".equalsIgnoreCase(accountType)) {
            return 4.0;
        } else if ("FIXEDDEPOSIT".equalsIgnoreCase(accountType)) {
            return 6.5;
        }
        return 0.0;
    }

    public static double getOverdraftLimit(String accountType) {
        if ("CURRENT".equalsIgnoreCase(accountType)) {
            return 10000.0;
        }
        return 0.0;
    }

    public static boolean validateWithdrawal(String accountType, double currentBalance, double amount) {
        double minBal = getMinimumBalance(accountType);
        double overdraft = getOverdraftLimit(accountType);
        return (currentBalance - amount) >= (minBal - overdraft);
    }
}
```

---

## 💡 Key Concepts

### Concept 1: Separation of Rules from Domain Entities
Hardcoding business values (like 4% interest or Rs 1000 min balance) inside entity classes makes system-wide policy updates difficult. A rules engine provides a single source of truth for all business parameters.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Static rule evaluation methods | Allows fast, stateless rule querying without requiring object allocation. |

---

## 🚀 How to Run

### Prerequisites
- Java JDK 17 or higher installed

### Windows (PowerShell)
```powershell
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }
javac -d bin (Get-ChildItem -Recurse -Filter *.java src | ForEach-Object { $_.FullName })
java -cp bin com.gdb.tests.TestAccountRulesEngine
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb\exceptions\*.java src\com\gdb	ests\*.java
java -cp bin com.gdb.tests.TestAccountRulesEngine
```

### Linux / macOS (Terminal)
```bash
mkdir -p bin
find src -name "*.java" -print0 | xargs -0 javac -d bin
java -cp bin com.gdb.tests.TestAccountRulesEngine
```

---

## 📊 Expected Output

```
=== Activity 13.1: Account Rules Engine Test ===
Savings Min Balance: 1000.0
Savings Interest Rate: 4.0%
Current Overdraft Limit: 10000.0
Fixed Deposit Interest Rate: 6.5%
=== Rules Engine Verification Completed ===
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to extract business policy rules into a centralized engine.
- How to perform unified withdrawal validation using policy parameters.

### How It Connects
- **Previous**: Activity 12 tested interface factories.
- **Next**: Activity 13.2 optimizes rule lookups and tests complex rule integrations.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Leaving hardcoded numbers in domain classes | Always query `AccountRulesEngine` for policy constants. |

---

## 🏁 Next Steps

Proceed to **Activity 13.2** for advanced rules engine testing and optimization.

---
*End of Activity 13.1 Solution*
