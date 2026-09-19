# ACTIVITY 18: Bridge Pattern (File + DB)

## Objective
Decouple the high-level `TransactionLogger` abstraction from its pluggable `LogDestination` storage backends using the **Bridge Design Pattern**. Support multiple backends — File, In-Memory DB, and Simulated Database — selectable and switchable at runtime.

---

## 🏗️ Architecture Diagram

```text
┌────────────────────────────┐
│   TransactionLogger        │  ← Abstraction
│  (holds a LogDestination)  │
└──────────────┬─────────────┘
               │
               │ bridge
               ▼
┌────────────────────────────┐
│   «interface»              │
│   LogDestination           │  ← Implementor
└──────────────┬─────────────┘
               │
     ┌─────────┼─────────┬─────────────┐
     ▼         ▼         ▼             ▼
  FileLog   MemoryLog  DatabaseLog   (future
  Dest      Dest       Dest           impls)
```

> **Bridge Pattern benefit:** We can add new destinations (e.g., Kafka, S3, CloudWatch, PostgreSQL) without changing `TransactionLogger` or any caller code. This is what makes the architecture production-friendly.

---

## Target Files to Complete
- `src/com/gdb/logging/LogDestination.java`
- `src/com/gdb/logging/FileLogDestination.java`
- `src/com/gdb/logging/DatabaseLogDestination.java`
- `src/com/gdb/logging/TransactionLogger.java`
- `src/com/gdb/tests/TestBridgeLogging.java`

*(Note: `SimulatedDatabase.java` and `MemoryLogDestination.java` are complete reference implementations provided for you.)*

---

## Step-by-Step Instructions

Search the code for `📝 STEP` — each step matches one marked placeholder:

### STEPS 1–4 — `logging/LogDestination.java`
Declare the interface methods:
1. `void write(TransactionCommand cmd);`
2. `List<TransactionCommand> readAll();`
3. `void clear();`
4. `String getDestinationName();`

### STEPS 5–10 — `logging/FileLogDestination.java`
1. Declare `private TransactionLog log;`
2. In constructor, initialize `this.log = new TransactionLog();`
3. Delegate `write`, `readAll`, `clear` to `TransactionLog`.
4. Return `"FILE"` from `getDestinationName()`.

### STEPS 11–16 — `logging/DatabaseLogDestination.java`
1. Declare `private final SimulatedDatabase db;`
2. In constructor, accept and store `SimulatedDatabase`.
3. In `write(cmd)`: call `db.insert("transaction_log", cmd)`.
4. In `readAll()`: call `db.selectAll("transaction_log")` and map to `List<TransactionCommand>`.
5. In `clear()`: call `db.deleteAll("transaction_log")`.
6. Return `"DATABASE"` from `getDestinationName()`.

### STEPS 17–23 — `logging/TransactionLogger.java`
1. Declare `protected LogDestination destination;`
2. Constructor accepting `LogDestination`.
3. Setter `setDestination(LogDestination destination)` for runtime switching.
4. Delegate `log`, `readAll`, `clear`, and `getDestinationName` to current `destination`.

### STEPS 24–29 — `tests/TestBridgeLogging.java`
- Instantiate all log destinations (`FileLogDestination`, `DatabaseLogDestination`, `MemoryLogDestination`).
- Log transactions to each backend via `logger.setDestination(...)`.
- Verify data isolation across all backends.

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

---

## Expected Output
```text
============================================================
  ACTIVITY 18 — BRIDGE PATTERN (FILE + DB)
============================================================

[STEP 25] Logging to FILE destination...
  FILE log count: 3

[STEP 26] Switched to DATABASE destination...
  DATABASE log count: 3

[STEP 27] Switched to MEMORY destination...
  MEMORY log count: 3

[STEP 28] Verifying Data Isolation:
  FILE count: 3 [EXPECTED: 3]
  DATABASE count: 3 [EXPECTED: 3]
  MEMORY count: 3 [EXPECTED: 3]

[STEP 29] All Bridge Pattern log backends verified successfully!
```
