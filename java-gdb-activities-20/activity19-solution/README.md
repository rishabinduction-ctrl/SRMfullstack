# Activity 19: AccountService (Service Layer) (Solution)

## Solution Overview
This solution implements the `AccountService` orchestrator managing the in-memory account registry, transaction execution, and audit logging.

---

## Files Included
| File | Description |
|---|---|
| `AccountService.java` | Core service layer orchestrator |
| `TestAccountService.java` | Test driver verifying service layer workflows |
| `Main.java` | Service-driven console bootstrap |

---

## How to Compile & Run

### Windows (PowerShell)
```powershell
New-Item bin -ItemType Directory -Force | Out-Null
Copy-Item src\main\resources\config bin -Recurse -Force
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java -cp bin com.gdb.tests.TestAccountService
```

### Linux & macOS (Terminal / Bash)
```bash
mkdir -p bin && cp -r src/main/resources/config bin/
javac -encoding UTF-8 -d bin $(find src -name "*.java")
java -cp bin com.gdb.tests.TestAccountService
```
