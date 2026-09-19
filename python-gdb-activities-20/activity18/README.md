# Activity 18: Bridge Pattern (File + DB)

## Objective
Decouple the high-level `TransactionLogger` abstraction from its pluggable `LogDestination` storage backends using the **Bridge Design Pattern**. Support multiple backends -- File, In-Memory and a Simulated Database -- that can be selected and switched at runtime.

---

## Architecture Diagram
```text
┌────────────────────────────┐
│   TransactionLogger        │  <- Abstraction
│  (holds a LogDestination)  │
└──────────────┬─────────────┘
               │
               │ bridge
               ▼
┌────────────────────────────┐
│   «interface»              │
│   LogDestination           │  <- Implementor
└──────────────┬─────────────┘
               │
     ┌─────────┼──────────┬──────────────┐
     ▼         ▼          ▼              ▼
  FileLog   MemoryLog  DatabaseLog    (future
  Dest      Dest       Dest            impls)
```

> **Bridge Pattern benefit:** new destinations (Kafka, S3, CloudWatch, PostgreSQL ...) can be added without changing `TransactionLogger` or any code that calls it.

---

## Prerequisites
- Activity 17 completed: commands produce `Transaction` records and `TransactionLog` persists them with `pickle`.

---

## What Is Already Done For You
| File | What is provided |
|------|------------------|
| `gdb/db/simulated_database.py` | `SimulatedDatabase` -- an in-memory "table" with `insert()`, `query_all()`, `query_by_account()` and `clear()`. |
| `gdb/logging/memory_log_destination.py` | `MemoryLogDestination` -- a complete reference implementor. Read it before you start. |

---

## Target Files to Complete
- `gdb/logging/log_destination.py`
- `gdb/logging/file_log_destination.py`
- `gdb/logging/database_log_destination.py`
- `gdb/logging/transaction_logger.py`
- `gdb/tests/test_bridge_logging.py`

---

## Step-by-Step Instructions
Search the code for `📝 STEP` -- each step below matches one marked placeholder.

### STEP 1 -- `logging/log_destination.py` -> `LogDestination` interface
Declare three abstract methods on the `ABC`:
1. `write(self, transaction: Transaction) -> None`
2. `read_all(self) -> List[Transaction]`
3. `get_destination_name(self) -> str`

### STEP 2 -- `logging/file_log_destination.py` -> `FileLogDestination`
1. `__init__`: store the file name.
2. `write(transaction)`: load the existing list with `read_all()`, append the transaction, and `pickle.dump()` the whole list back (mode `"wb"`).
3. `read_all()`: return the list loaded with `pickle.load()` (mode `"rb"`), or `[]` if the file is missing or unreadable.
4. `clear()`: delete the file if it exists.

`get_destination_name()` is provided (it returns `"File: <filename>"`).

### STEP 3 -- `logging/database_log_destination.py` -> `DatabaseLogDestination`
1. `__init__(db)`: store the `SimulatedDatabase`.
2. `write(transaction)`: insert it into the database.
3. `read_all()`: return every stored transaction.
4. `get_destination_name()`: return `"Database"`.

### STEP 4 -- `logging/transaction_logger.py` -> `TransactionLogger` (the bridge)
1. `__init__(destination)`: store the `LogDestination`.
2. `log(transaction)`: if the transaction is not `None`, write it to the current destination.
3. `get_transactions()`: return `read_all()` from the current destination.
4. `get_destination()`: return the current destination.
5. `set_destination(destination)`: replace the current destination (runtime switching).

### STEPS 5-9 -- `tests/test_bridge_logging.py`
| Step | Test method | What to write |
|------|-------------|---------------|
| 5 | `setUp` | Create a Savings account (#1001, "Rajesh", 30, Rs. 50,000) and set PIN `1234`. |
| 6 | `test_memory_logging` | Log a Rs. 5,000 deposit through a logger using `MemoryLogDestination`; assert 1 record and name `"In-Memory"`. |
| 7 | `test_database_logging` | Log a Rs. 2,000 deposit through `DatabaseLogDestination(SimulatedDatabase())`; assert 1 record and name `"Database"`. |
| 8 | `test_file_logging` | Log a Rs. 1,000 deposit through `FileLogDestination("bridge_test.log")`; assert 1 record, then `clear()` the file. |
| 9 | `test_switch_destination` | Log to memory, switch the logger to a database destination with `set_destination()`, and assert the new backend has its own (empty) data. |

---

## How to Run
Run these commands from inside the `activity18` folder (the folder that contains `gdb/` and `config/`).

### Windows (PowerShell or Command Prompt)
```powershell
# This activity's tests
python -m gdb.tests.test_bridge_logging -v

# Every test in the folder (Activities 15-17 regression tests included)
python -m unittest discover -s gdb/tests -t . -v
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_bridge_logging -v
python3 -m unittest discover -s gdb/tests -t . -v
```

---

## Expected Output
Before you start, every test in `test_bridge_logging.py` errors with `NotImplementedError: TODO: Step 5 ...`. When you have finished:
```text
test_database_logging ... ok
test_file_logging ... ok
test_memory_logging ... ok
test_switch_destination ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.0XXs

OK
```

---

## Verification Checklist
- [ ] `python -m gdb.tests.test_bridge_logging` reports `Ran 4 tests` and `OK`.
- [ ] The Activity 15-17 tests still pass.
- [ ] `TransactionLogger` never mentions a concrete destination class -- it only talks to `LogDestination`.
- [ ] Switching the destination at runtime works without creating a new logger.
- [ ] No `bridge_test.log` file is left behind after the tests.

---

## Understanding Questions
1. Which class is the *abstraction* and which is the *implementor* in this Bridge? Why keep them separate?
2. How is the Bridge Pattern different from simply subclassing `TransactionLogger` once per destination?
3. What would you need to add to support a new `KafkaLogDestination`? Which existing files would change?
4. Why is it useful for each backend to keep its own data when you switch destinations?
5. `MemoryLogDestination` loses its data when the program ends. When is that still the right choice?
