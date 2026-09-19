# Activity 17: Command Pattern + File Logging (Solution)

## Solution Overview
This solution encapsulates banking transactions into executable `TransactionCommand` objects and provides durable audit logging to file using Java object serialization.

---

## Files Included
| File | Description |
|---|---|
| `TransactionCommand.java` | Interface with `execute()` and `getTransaction()` |
| `DepositCommand.java` | Encapsulates deposit operation |
| `WithdrawCommand.java` | Encapsulates withdrawal operation |
| `TransferCommand.java` | Encapsulates transfer operation |
| `TransactionLog.java` | Durable binary log manager |
| `TestCommandLogging.java` | Complete verification test driver |

---

## How to Compile & Run

### Windows (PowerShell)
```powershell
New-Item bin -ItemType Directory -Force | Out-Null
Copy-Item src\main\resources\config bin -Recurse -Force
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java -cp bin com.gdb.tests.TestCommandLogging
```

### Linux & macOS (Terminal / Bash)
```bash
mkdir -p bin && cp -r src/main/resources/config bin/
javac -encoding UTF-8 -d bin $(find src -name "*.java")
java -cp bin com.gdb.tests.TestCommandLogging
```
