# Activity 3: Enhanced Account Class

This solution demonstrates defensive programming and security enhancements in the `Account` class. It adds strict input validation, 4-digit security PIN verification, and account status controls to prevent invalid data from entering the domain model.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Implement Defensive Programming** - Validate constructor parameters and reject invalid values upfront.
- **Enforce Business Constraints** - Require account holders to be at least 18 years old and maintain valid PIN formats.
- **Implement Security Controls** - Add PIN authentication for sensitive operations and manage account active/inactive statuses.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `Account.java` | Enhanced account entity with defensive validation, PIN storage, PIN verification, and status validation. |
| `TestAccount.java` | Test driver verifying PIN authentication, inactive account handling, and valid operations. |

---

## 🔍 Code Walkthrough

### File: `Account.java`

#### Fields
| Field | Type | Access | Description |
|---|---|---|---|
| `accountNumber` | `String` | `private` | Unique account identifier (non-empty). |
| `name` | `String` | `private` | Holder name (non-empty). |
| `age` | `int` | `private` | Holder age ($\ge 18$). |
| `balance` | `double` | `private` | Monetary balance ($\ge 0.0$). |
| `accountType` | `String` | `private` | Type of account. |
| `status` | `String` | `private` | Lifecycle status ("Active" / "Inactive"). |
| `pin` | `String` | `private` | 4-digit secret security PIN. |

#### Constructor
Validates that `accountNumber` is not null/empty, `age >= 18`, `balance >= 0`, and `pin` is exactly 4 characters before assigning fields.

#### Key Methods
- `public boolean validatePin(String enteredPin)`: Verifies if `enteredPin` matches stored `pin`.
- `public boolean deposit(double amount)`: Checks that `status` is "Active" and `amount > 0`.
- `public boolean withdraw(double amount)`: Checks that `status` is "Active", `amount > 0`, and `amount <= balance`.

#### Key Code Snippets
```java
// PIN Validation Method
public boolean validatePin(String enteredPin) {
    if (enteredPin != null && enteredPin.equals(this.pin)) {
        return true;
    }
    return false;
}

// Status check in transaction methods
public boolean withdraw(double amount) {
    if (!"Active".equalsIgnoreCase(this.status)) {
        return false; // Reject transactions on inactive accounts
    }
    if (amount > 0 && amount <= this.balance) {
        this.balance -= amount;
        return true;
    }
    return false;
}
```

### File: `TestAccount.java`

#### Test Scenarios
1. **Valid Creation & PIN Check**: Verifies that correct PIN returns `true` and incorrect PIN returns `false`.
2. **Active vs Inactive Transactions**: Verifies transactions work on Active accounts and are blocked on Inactive accounts.

---

## 💡 Key Concepts

### Concept 1: Defensive Programming
Defensive programming ensures that an object protects its own invariants. Constructors and methods validate arguments before executing logic to prevent invalid states.

### Concept 2: Authentication & Access Control
Protecting sensitive account actions with credential checks (`validatePin`) and operational state flags (`status`).

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Store PIN as `String` | Preserves leading zeroes in PINs (e.g., `"0123"` which would lose the leading zero as integer `123`). |
| Case-insensitive status check (`equalsIgnoreCase`) | Provides robust status evaluation regardless of casing (e.g., "active", "Active", "ACTIVE"). |

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
=== Starting Enhanced Account Tests ===
Account created successfully: ACC2001 (Holder: Bob, Age: 30)
PIN Validation (Correct: '1234'): PASS
PIN Validation (Wrong: '9999'): PASS (Correctly rejected)
Deposit on Active Account: PASS (New Balance: 7000.0)
Withdrawal on Inactive Account: PASS (Correctly blocked)
=== Enhanced Account Tests Completed ===
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to implement defensive parameter checks inside constructors.
- How to handle PIN authentication safely using `String` equality.
- How to enforce business lifecycle rules using account status.

### How It Connects
- **Previous**: Activity 2 verified basic state mutations.
- **Next**: Activity 4 builds an exhaustive test suite covering security and validation edge cases.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Comparing Strings with `==` | Always use `.equals()` or `.equalsIgnoreCase()` for string comparisons in Java. |
| Using `int` for PIN storage | Use `String` to support leading zeros (e.g. `"0042"`). |

---

## 🏁 Next Steps

Proceed to **Activity 4** to execute a comprehensive security and validation test harness.

---
*End of Activity 3 Solution*
