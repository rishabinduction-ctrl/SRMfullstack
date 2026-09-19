# Activity 14: Properties File Migration

This solution demonstrates externalizing all banking business rules into external `.properties` configuration files loaded dynamically via `AccountRulesPropertiesLoader` without requiring Java code recompilation.

---

## 🎯 Learning Objectives

By completing this activity, students will:
- **Externalize Application Configuration** - Move business parameters (interest rates, minimum balances, overdraft limits) into `.properties` files.
- **Load Classpath Resources** - Use `ClassLoader.getResourceAsStream()` to reliably load config files across platforms.
- **Enable Zero-Recompile Rule Updates** - Modify banking rules dynamically by altering configuration files without recompiling code.

---

## 📂 Solution Overview

| File | Purpose |
|------|---------|
| `savings.properties` | Config file defining `minBalance=1000.0` and `interestRate=4.0`. |
| `current.properties` | Config file defining `overdraftLimit=10000.0`. |
| `fixeddeposit.properties` | Config file defining `interestRate=6.5` and `minTenureMonths=6`. |
| `salary.properties` | Config file defining `minBalance=0.0`. |
| `AccountRulesPropertiesLoader.java` | Utility loading configuration properties from the classpath. |
| `AccountRulesEngine.java` | Rules engine reading policy thresholds from properties files. |
| `TestAccountRulesEngineProperties.java` | Test driver verifying dynamic configuration loading. |

---

## 🔍 Code Walkthrough

### File: `AccountRulesPropertiesLoader.java`

```java
package com.gdb.domain;

import java.io.InputStream;
import java.util.Properties;

public class AccountRulesPropertiesLoader {
    public static Properties loadRules(String accountType) {
        Properties props = new Properties();
        String filename = "/config/rules/" + accountType.toLowerCase() + ".properties";
        try (InputStream in = AccountRulesPropertiesLoader.class.getResourceAsStream(filename)) {
            if (in != null) {
                props.load(in);
            } else {
                System.err.println("Warning: Config file not found on classpath: " + filename);
            }
        } catch (Exception e) {
            System.err.println("Error loading config for " + accountType + ": " + e.getMessage());
        }
        return props;
    }
}
```

### Configuration Files (`src/main/resources/config/rules/`)
- **`savings.properties`**:
  ```properties
  minBalance=1000.0
  interestRate=4.0
  ```
- **`current.properties`**:
  ```properties
  overdraftLimit=10000.0
  ```

---

## 💡 Key Concepts

### Concept 1: External Configuration & 12-Factor App
Separating configuration from source code is an industry standard (12-Factor App methodology). Business administrators can update interest rates in production without initiating a full software rebuild and deployment cycle.

### Concept 2: Classpath Resource Resolution
`getResourceAsStream()` loads files bundled within the application JAR or output directory regardless of operating system directory paths.

---

## 🏗️ Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Try-with-resources for `InputStream` | Automatically closes file streams to prevent file descriptor leaks. |
| Default fallback values | Protects system from crashing if a properties file is temporarily missing or corrupted. |

---

## 🚀 How to Run

### Prerequisites
- Java JDK 17 or higher installed

### Windows (PowerShell)
```powershell
if (!(Test-Path bin)) { New-Item -ItemType Directory -Path bin }
javac -d bin (Get-ChildItem -Recurse -Filter *.java src | ForEach-Object { $_.FullName })
Copy-Item -Recurse -Path src/main/resources/* -Destination bin/
java -cp bin com.gdb.tests.TestAccountRulesEngineProperties
```

### Windows (Command Prompt - CMD)
```cmd
if not exist bin mkdir bin
javac -d bin src\com\gdb\domain\*.java src\com\gdb\exceptions\*.java src\com\gdb	ests\*.java
xcopy /E /I /Y src\mainesources\* binjava -cp bin com.gdb.tests.TestAccountRulesEngineProperties
```

### Linux / macOS (Terminal)
```bash
mkdir -p bin
find src -name "*.java" -print0 | xargs -0 javac -d bin
cp -r src/main/resources/* bin/
java -cp bin com.gdb.tests.TestAccountRulesEngineProperties
```

---

## 📊 Expected Output

```
=== Activity 14: Dynamic Rules Configuration Test ===
Loading configuration from classpath: /config/rules/savings.properties
[SAVINGS] Min Balance: 1000.0, Interest Rate: 4.0%
Loading configuration from classpath: /config/rules/current.properties
[CURRENT] Overdraft Limit: 10000.0
Loading configuration from classpath: /config/rules/fixeddeposit.properties
[FIXED DEPOSIT] Interest Rate: 6.5%, Min Tenure: 6 months
=== Dynamic Properties Configuration Verified ===
```

---

## 💡 Key Takeaways

### What This Activity Teaches
- How to externalize application configuration into standard Java `.properties` files.
- How to load and parse classpath resources safely using `java.util.Properties`.
- How enterprise architectures decouple business rules from compiled application bytecode.

### How It Connects
- **Previous**: Activity 13.2 implemented in-code rule engine lookups.
- **Course Capstone**: Concludes the 14-activity Java Banking Architecture curriculum!

---

## ⚠️ Common Mistakes

| Mistake | Solution |
|---------|----------|
| Forgetting to copy resources to the output `bin/` directory | Always copy `src/main/resources/*` into `bin/` before running Java. |
| Hardcoding absolute file paths (e.g. `C:/config.properties`) | Always load via classpath (`getResourceAsStream`) for cross-platform portability. |

---

## 🏁 Course Complete!

Congratulations on mastering Core Java, Object-Oriented Programming, Exception Handling, Design Patterns, and Enterprise Configuration Management!

---
*End of Activity 14 Solution*
