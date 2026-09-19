# gdb/tests/test_bridge_logging.py
import unittest
import os
from gdb.domain.account_factory import AccountFactory
from gdb.command.deposit_command import DepositCommand
from gdb.logging.memory_log_destination import MemoryLogDestination
from gdb.logging.file_log_destination import FileLogDestination
from gdb.logging.database_log_destination import DatabaseLogDestination
from gdb.db.simulated_database import SimulatedDatabase
from gdb.logging.transaction_logger import TransactionLogger

class TestBridgeLogging(unittest.TestCase):
    def setUp(self):
        # ============================================================
        # 📝 STEP 5: Create The Test Account
        #
        # INSTRUCTIONS:
        #   1. self.acc = AccountFactory.create_account("SAVINGS", 1001, "Rajesh", 30, 50000.0)
        #   2. Set PIN 1234 on the account.
        # ============================================================
        # TODO: create the account used by every test
        raise NotImplementedError("TODO: Step 5 - create the test account")

    def test_memory_logging(self):
        # ============================================================
        # 📝 STEP 6: Log To Memory
        #
        # INSTRUCTIONS:
        #   1. Create a TransactionLogger that writes to a MemoryLogDestination().
        #   2. Execute a DepositCommand(self.acc, 5000.0) and log its transaction.
        #   3. Assert the logger returns exactly 1 transaction.
        #   4. Assert logger.get_destination().get_destination_name() == "In-Memory".
        # ============================================================
        # TODO: log a deposit to the in-memory destination and assert the result
        raise NotImplementedError("TODO: Step 6 - test memory logging")

    def test_database_logging(self):
        # ============================================================
        # 📝 STEP 7: Log To The Database
        #
        # INSTRUCTIONS:
        #   1. Create a SimulatedDatabase() and a TransactionLogger that writes to DatabaseLogDestination(db).
        #   2. Execute a DepositCommand(self.acc, 2000.0) and log its transaction.
        #   3. Assert the logger returns exactly 1 transaction and the destination name is "Database".
        # ============================================================
        # TODO: log a deposit to the database destination and assert the result
        raise NotImplementedError("TODO: Step 7 - test database logging")

    def test_file_logging(self):
        # ============================================================
        # 📝 STEP 8: Log To A File
        #
        # INSTRUCTIONS:
        #   1. Create a FileLogDestination("bridge_test.log") and a TransactionLogger that uses it.
        #   2. Execute a DepositCommand(self.acc, 1000.0) and log its transaction.
        #   3. Assert the logger returns exactly 1 transaction.
        #   4. Call clear() on the destination so no test file is left behind.
        # ============================================================
        # TODO: log a deposit to the file destination, assert the result, then clean up
        raise NotImplementedError("TODO: Step 8 - test file logging")

    def test_switch_destination(self):
        # ============================================================
        # 📝 STEP 9: Switch Destination At Runtime
        #
        # INSTRUCTIONS:
        #   1. Create a TransactionLogger with a MemoryLogDestination and log one deposit.
        #   2. Call logger.set_destination(DatabaseLogDestination(SimulatedDatabase())).
        #   3. Assert get_destination().get_destination_name() is now "Database".
        #   4. Assert get_transactions() returns 0 records -- each backend keeps its own data.
        # ============================================================
        # TODO: switch the logger's backend and assert the data stays isolated
        raise NotImplementedError("TODO: Step 9 - test switching destinations")

if __name__ == "__main__":
    unittest.main()
