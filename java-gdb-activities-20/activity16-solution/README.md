# Activity 16: Transaction Model (Solution)

## Solution Overview
This solution implements the `Transaction` class and `TransactionType` enum to capture complete audit trails of banking transactions.

---

## Files Included
| File | Description |
|---|---|
| `TransactionType.java` | Enum containing `DEPOSIT`, `WITHDRAW`, `TRANSFER` |
| `Transaction.java` | Full `Serializable` transaction model with ID generation |
| `Account.java` | Base account with `depositWithTransaction` and `withdrawWithTransaction` |
| `TransferService.java` | Transfer service with `transferWithTransaction` |
| `TestTransactionModel.java` | Full test verifying transaction operations and backward compatibility |

---

## How to Compile & Run

### Windows (PowerShell)
```powershell
New-Item bin -ItemType Directory -Force | Out-Null
Copy-Item src\main\resources\config bin -Recurse -Force
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java -cp bin com.gdb.tests.TestTransactionModel
```

### Linux & macOS (Terminal / Bash)
```bash
mkdir -p bin && cp -r src/main/resources/config bin/
javac -encoding UTF-8 -d bin $(find src -name "*.java")
java -cp bin com.gdb.tests.TestTransactionModel
```
