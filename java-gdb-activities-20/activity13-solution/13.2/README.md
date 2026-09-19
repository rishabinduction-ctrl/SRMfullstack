# Activity 13.2: Rules Engine Integration

This solution demonstrates comprehensive integration and rule validation testing between domain account models and the `AccountRulesEngine`.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Integrate Rules Engine with Domain Workflows** - Query rule engine parameters dynamically during transaction processing.
- **Validate Policy Decision Logic** - Assert combined minimum balance and overdraft limit checks via `validateWithdrawal()`.
- **Test Multi-Product Policy Coverage** - Verify rules across all supported product lines.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `AccountRulesEngine.java` | Central rules engine. |
| `TestAccountRulesEngine.java` | Integration test driver validating policy decisions across all banking products. |

---

## 🔍 Code Walkthrough

### File: `TestAccountRulesEngine.java`

#### Test Scenarios
1. **Savings Policy Verification**: Queries minimum balance ($Rs\ 1000.0$) and interest rate ($4.0\%$).
2. **Current Account Policy Verification**: Queries approved overdraft limit ($Rs\ 10000.0$).
3. **Fixed Deposit Policy Verification**: Queries fixed term interest rate ($6.5\%$).
4. **Withdrawal Policy Assertion**: Validates that withdrawals violating policy thresholds return `false`.

---

## 💡 Key Concepts

### Concept 1: Policy Invariant Enforcement
Centralizing rule execution ensures consistent policy enforcement across web, mobile, and batch banking interfaces.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Composite validation method `validateWithdrawal()` | Consolidates complex balance + overdraft - minBalance calculations in one testable function. |

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
=== Activity 13.2: Account Rules Engine Test ===
Savings Min Balance: 1000.0
Savings Interest Rate: 4.0%
Current Overdraft Limit: 10000.0
Fixed Deposit Interest Rate: 6.5%
=== Rules Engine Verification Completed ===
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to test centralized rules engines across multiple domain products.

### How It Connects
- **Previous**: Activity 13.1 created the rules engine.
- **Next**: Activity 14 externalizes all rules into configuration `.properties` files.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Duplicate rule logic in tests | Query the rules engine directly for expected thresholds. |

---

## 🏁 Next Steps

Proceed to **Activity 14** to externalize business rules into `.properties` files.

---
*End of Activity 13.2 Solution*
