# Activity 18: Bridge Pattern (File + DB) (Solution)

## Solution Overview
This solution implements the Bridge Design Pattern to decouple `TransactionLogger` abstraction from multiple pluggable `LogDestination` implementors (`FileLogDestination`, `DatabaseLogDestination`, and `MemoryLogDestination`).

---

## Files Included
| File | Description |
|---|---|
| `SimulatedDatabase.java` | In-memory key-value database engine |
| `LogDestination.java` | Bridge implementor interface |
| `FileLogDestination.java` | File serialization log destination |
| `MemoryLogDestination.java` | In-memory list destination |
| `DatabaseLogDestination.java` | Simulated database destination |
| `TransactionLogger.java` | Bridge abstraction logger |
| `TestBridgeLogging.java` | Complete multi-backend verification test |

---

## How to Compile & Run

### Windows (PowerShell)
```powershell
New-Item bin -ItemType Directory -Force | Out-Null
Copy-Item src\main\resources\config bin -Recurse -Force
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java -cp bin com.gdb.tests.TestBridgeLogging
```

### Linux & macOS (Terminal / Bash)
```bash
mkdir -p bin && cp -r src/main/resources/config bin/
javac -encoding UTF-8 -d bin $(find src -name "*.java")
java -cp bin com.gdb.tests.TestBridgeLogging
```
