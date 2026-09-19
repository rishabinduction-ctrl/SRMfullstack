# Activity 8: Polymorphism and Method Overriding

This solution demonstrates **Runtime Polymorphism** and **Method Overriding** (`@Override`) in Java to implement customized withdrawal rules across different account types.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Implement Method Overriding (`@Override`)** - Specialize superclass method behavior in subclasses.
- **Enforce Product-Specific Constraints** - Implement minimum balance checks for `SavingsAccount` and overdraft thresholds for `CurrentAccount`.
- **Apply Dynamic Method Dispatch** - Invoke overridden methods polymorphically through superclass references.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `Account.java` | Base superclass providing standard withdrawal behavior. |
| `SavingsAccount.java` | Overrides `withdraw()` to enforce mandatory minimum balance ($Rs\ 1000$). |
| `CurrentAccount.java` | Overrides `withdraw()` to permit overdrafts up to `overdraftLimit`. |
| `TestAccountSubclasses.java` | Polymorphic test suite invoking methods through `Account[]` arrays. |

---

## 🔍 Code Walkthrough

### File: `SavingsAccount.java`
```java
@Override
public void withdraw(double amount) throws AccountException {
    if (!"Active".equalsIgnoreCase(getStatus())) {
        throw new InactiveAccountException("Cannot withdraw from inactive account: " + getAccountNumber());
    }
    if (amount <= 0) {
        throw new InvalidAmountException("Withdrawal amount must be strictly positive: " + amount);
    }
    // Enforce minimum balance rule
    if ((getBalance() - amount) < minimumBalance) {
        throw new MinimumBalanceViolationException("Withdrawal violates minimum balance requirement of Rs " + minimumBalance);
    }
    super.withdraw(amount);
}
```

### File: `CurrentAccount.java`
```java
@Override
public void withdraw(double amount) throws AccountException {
    if (!"Active".equalsIgnoreCase(getStatus())) {
        throw new InactiveAccountException("Cannot withdraw from inactive account: " + getAccountNumber());
    }
    if (amount <= 0) {
        throw new InvalidAmountException("Withdrawal amount must be strictly positive: " + amount);
    }
    // Allow balance to dip into overdraft
    if (amount > (getBalance() + overdraftLimit)) {
        throw new InsufficientBalanceException("Withdrawal exceeds balance + overdraft limit of Rs " + (getBalance() + overdraftLimit));
    }
    super.withdraw(amount);
}
```

---

## 💡 Key Concepts

### Concept 1: Dynamic Method Dispatch (Runtime Polymorphism)
When a method is called on a superclass reference (`Account acc = new SavingsAccount(...)`), Java inspects the actual object type at runtime and executes the overridden subclass method.

### Concept 2: Method Overriding Rules
- The method name, return type, and parameters must match the parent signature.
- Access level cannot be more restrictive.
- Checked exceptions thrown cannot be broader than those declared in the parent method.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Delegate to `super.withdraw(amount)` | Reuses balance mutation and audit logic from base class after validating subclass-specific preconditions. |
| Polymorphic test fixtures (`Account[]`) | Verifies that client code can manage diverse account types transparently. |

---

## 🚀 How to Run

### Prerequisites
- Java JDK 17 or higher installed

### Windows (PowerShell)
```powershell
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }
javac -d bin (Get-ChildItem -Recurse -Filter *.java src | ForEach-Object { $_.FullName })
java -cp bin com.gdb.tests.TestAccountSubclasses
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb\exceptions\*.java src\com\gdb	ests\*.java
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
=========================================
   ACTIVITY 8: POLYMORPHISM TEST SUITE   
=========================================

--- Test 1: SavingsAccount Minimum Balance Rule ---
Attempting withdrawal of Rs 4500 from SA001 (Balance: 5000, Min: 1000)...
PASS: Caught expected MinimumBalanceViolationException -> Withdrawal violates minimum balance requirement of Rs 1000.0

--- Test 2: CurrentAccount Overdraft Support ---
Attempting withdrawal of Rs 6000 from CA001 (Balance: 2000, Overdraft: 5000)...
PASS: Overdraft withdrawal succeeded! New Balance: Rs -4000.0

=========================================
   POLYMORPHISM TESTS COMPLETED          
=========================================
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to override methods to specialize behavior per business domain product.
- How Java handles polymorphic method dispatch at runtime.

### How It Connects
- **Previous**: Activity 7 introduced the subclass hierarchy.
- **Next**: Activity 9 abstracts common behavior into an `AbstractAccount` base class.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Omitting `@Override` annotation | Always use `@Override` so the compiler catches accidental method signature typos. |
| Forgetting to check minimum balance before balance mutation | Perform boundary check before mutating instance state. |

---

## 🏁 Next Steps

Proceed to **Activity 9** to convert `Account` into an abstract class (`AbstractAccount`).

---
*End of Activity 8 Solution*
