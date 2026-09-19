# Activity 1: Basic Account Class

This solution demonstrates the foundational implementation of an `Account` class in Java using Object-Oriented Programming (OOP) principles. It showcases proper data encapsulation, state initialization via a constructor, safe transaction methods for depositing and withdrawing funds, and account detail reporting.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Understand Data Encapsulation** - Protect class state using `private` access modifiers and control access through public methods.
- **Implement State Initialization** - Construct valid objects using parameterized constructors with the `this` keyword.
- **Enforce Business Invariants** - Implement safe mathematical validations for deposit and withdrawal operations.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `Account.java` | Core domain model encapsulating account state (account number, holder name, age, balance, account type, status) and business operations. |
| `TestAccount.java` | Test driver verifying account creation, successful deposits, withdrawals, and formatted information display. |

---

## 🔍 Code Walkthrough

### File: `Account.java`

#### Fields
| Field | Type | Access | Description |
|---|---|---|---|
| `accountNumber` | `String` | `private` | Unique identifier for the bank account. |
| `name` | `String` | `private` | Full name of the account holder. |
| `age` | `int` | `private` | Age of the account holder. |
| `balance` | `double` | `private` | Current monetary balance in Rupees. |
| `accountType` | `String` | `private` | Type of account (e.g., "Savings", "Current"). |
| `status` | `String` | `private` | Operational status (e.g., "Active", "Inactive"). |

#### Constructor
```java
public Account(String accountNumber, String name, int age, double balance, String accountType, String status) {
    this.accountNumber = accountNumber;
    this.name = name;
    this.age = age;
    this.balance = balance;
    this.accountType = accountType;
    this.status = status;
}
```
Initializes all 6 instance variables when an `Account` object is created. Uses `this` to resolve variable shadowing between parameter names and instance field names.

#### Key Methods
- `public boolean deposit(double amount)`: Validates that `amount > 0`. If valid, adds amount to `balance` and returns `true`; otherwise returns `false`.
- `public boolean withdraw(double amount)`: Validates that `amount > 0` and `amount <= this.balance`. If valid, deducts amount from `balance` and returns `true`; otherwise returns `false`.
- `public void displayAccountInfo()`: Formats and prints all account attributes to standard output.
- Getters (`getAccountNumber`, `getName`, `getBalance`, etc.): Provide read access to encapsulated fields.

#### Key Code Snippets
```java
// Safe deposit operation
public boolean deposit(double amount) {
    if (amount > 0) {
        this.balance += amount;
        return true;
    }
    return false;
}

// Safe withdrawal preventing overdraft
public boolean withdraw(double amount) {
    if (amount > 0 && amount <= this.balance) {
        this.balance -= amount;
        return true;
    }
    return false;
}
```

### File: `TestAccount.java`

#### Test Scenarios
1. **Creation**: Instantiates an `Account` with ID `"ACC1001"`, Name `"Alice"`, Age `25`, Balance `5000.0`, Type `"Savings"`, Status `"Active"`.
2. **Deposit Verification**: Performs a deposit of `1500.0` and asserts that balance updates to `6500.0`.
3. **Withdrawal Verification**: Performs a withdrawal of `2000.0` and asserts that balance updates to `4500.0`.
4. **Information Display**: Calls `displayAccountInfo()` to output formatted state.

---

## 💡 Key Concepts

### Concept 1: Encapsulation
Encapsulation is the bundling of data and the methods that operate on that data into a single unit (class), while restricting direct access to internal state using the `private` modifier. This prevents unauthorized direct mutation (e.g., `acc.balance = -999999;`).

### Concept 2: Safe Mutators & State Integrity
Instead of directly modifying variables, all mutations occur through methods (`deposit`, `withdraw`) that validate incoming parameters to ensure the object never enters an illegal state.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| `private` instance fields | Guarantees data hiding and integrity, forcing all access through validated methods. |
| `boolean` return types for transactions | Allows caller to determine whether the transaction succeeded without throwing exceptions at this initial stage. |
| Parameterized constructor | Ensures an `Account` object is always created in a fully initialized state. |

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
=== Account Management System ===
Account Details:
Account Number: ACC1001
Name: Alice
Age: 25
Balance: Rs 5000.0
Account Type: Savings
Status: Active

Depositing Rs 1500.0...
Deposit Successful! Current Balance: Rs 6500.0

Withdrawing Rs 2000.0...
Withdrawal Successful! Current Balance: Rs 4500.0
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to structure a domain entity class in Java with encapsulated fields.
- How to write constructor initialization and validation logic.
- How to test basic class behaviors via a main test driver.

### How It Connects
- **Previous**: None (Starting Activity).
- **Next**: Activity 2 deepens testing by adding explicit assertions and edge case verifications.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Leaving fields `public` | Always declare instance fields `private`. |
| Omitting `this.` when parameter names match field names | Use `this.field = field;` to explicitly assign parameters to instance fields. |
| Allowing negative withdrawals or deposits | Include strict boundary check `if (amount > 0)` before modifying balance. |

---

## 🏁 Next Steps

Proceed to **Activity 2** to implement advanced test assertions and verification suites.

---
*End of Activity 1 Solution*
