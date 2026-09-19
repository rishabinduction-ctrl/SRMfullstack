# Activity 20: AccountUI (Interactive Console Application)

## Overview
This activity introduces `AccountUI`, a menu-driven interactive console user interface built on top of `AccountService`.

---

## Files Included
| File | Description |
|---|---|
| `AccountUI.java` | Interactive menu-driven console UI |
| `TestAccountUI.java` | Test driver validating UI integration and service endpoints |
| `Main.java` | Application bootstrapper launching `AccountUI` |
| `docs/ACTIVITY_20.md` | Complete activity guide with instructions and architecture |

---

## How to Compile & Run

### Windows (PowerShell)
```powershell
New-Item bin -ItemType Directory -Force | Out-Null
Copy-Item src\main\resources\config bin -Recurse -Force
javac -encoding UTF-8 -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
java -cp bin com.gdb.tests.TestAccountUI
```

To run the interactive console app:
```powershell
java -cp bin com.gdb.Main
```

### Linux & macOS (Terminal / Bash)
```bash
mkdir -p bin && cp -r src/main/resources/config bin/
javac -encoding UTF-8 -d bin $(find src -name "*.java")
java -cp bin com.gdb.tests.TestAccountUI
```

To run the interactive console app:
```bash
java -cp bin com.gdb.Main
```
