# Activity 2: Testing Account Class

This solution demonstrates writing structured, automated unit test assertions in Python to verify the `Account` class under positive, negative, and boundary transaction conditions.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Write Automated Assertions** - Use Python `assert` statements to verify expected vs actual state.
- **Verify Boundary Conditions** - Assert behavior on negative deposits, zero amounts, and overdraft withdrawals.
- **Verify State Integrity** - Confirm that failed transactions leave balance completely unchanged.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `account.py` | Domain class representing bank account entity. |
| `test_account.py` | Test driver asserting state changes across positive and negative transaction paths. |

---

## 🔍 Code Walkthrough

### File: `gdb/tests/test_account.py`

#### Test Scenarios
1. **Initial State Verification**: Asserts constructor arguments match attributes.
2. **Valid Deposit Test**: Depositing positive amount increases balance and returns `True`.
3. **Invalid Deposit Test**: Depositing negative amount returns `False` and preserves balance.
4. **Valid Withdrawal Test**: Withdrawing amount $\le$ balance succeeds and deducts funds.
5. **Overdraft Prevention Test**: Withdrawing amount $>$ balance returns `False` and preserves balance.

#### Key Code Snippets
```python
# Testing overdraft prevention
res = acc.withdraw(10000.0)
assert res is False and acc.balance == 4500.0
print(f"Test 5: Overdraft Withdrawal (-10000.0) -> PASS [Rejected, Balance: {acc.balance}]")
```

---

## 💡 Key Concepts

### Concept 1: Automated Assertions (`assert`)
The `assert` keyword evaluates a condition. If the condition is `False`, Python raises an `AssertionError`, immediately alerting the developer to regression failures.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Native assertions | Keeps testing simple and readable without external framework overhead. |

---

## 🚀 How to Run

### Windows (PowerShell)
```powershell
python gdb/tests/test_account.py
```

### Windows (Command Prompt - CMD)
```cmd
python gdb	ests	est_account.py
```

### Linux / macOS (Terminal)
```bash
python3 gdb/tests/test_account.py
```

---

## 📊 Expected Output

```
=== Activity 2: Test Account Suite ===
Test 1: Initial Account Creation -> PASS [Balance: 5000.0]
Test 2: Valid Deposit (+1500.0) -> PASS [New Balance: 6500.0]
Test 3: Invalid Deposit (-500.0) -> PASS [Rejected, Balance: 6500.0]
Test 4: Valid Withdrawal (-2000.0) -> PASS [New Balance: 4500.0]
Test 5: Overdraft Withdrawal (-10000.0) -> PASS [Rejected, Balance: 4500.0]
All Account tests completed successfully!
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to structure automated test suites in Python.

### How It Connects
- **Previous**: Activity 1 implemented `Account`.
- **Next**: Activity 3 enhances `Account` with defensive validation, PIN authentication, and status controls.

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Missing balance verification after failed transactions | Always assert `acc.balance == expected_balance` after testing rejected operations. |

---

## 🏁 Next Steps

Proceed to **Activity 3** for defensive input validation and PIN security.

---
*End of Activity 2 Solution*
