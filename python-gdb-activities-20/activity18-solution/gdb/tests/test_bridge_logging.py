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
        self.acc = AccountFactory.create_account("SAVINGS", 1001, "Rajesh", 30, 50000.0)
        self.acc.set_pin(1234)

    def test_memory_logging(self):
        dest = MemoryLogDestination()
        logger = TransactionLogger(dest)
        cmd = DepositCommand(self.acc, 5000.0)
        cmd.execute()
        logger.log(cmd.get_transaction())
        self.assertEqual(len(logger.get_transactions()), 1)
        self.assertEqual(logger.get_destination().get_destination_name(), "In-Memory")

    def test_database_logging(self):
        db = SimulatedDatabase()
        dest = DatabaseLogDestination(db)
        logger = TransactionLogger(dest)
        cmd = DepositCommand(self.acc, 2000.0)
        cmd.execute()
        logger.log(cmd.get_transaction())
        self.assertEqual(len(logger.get_transactions()), 1)
        self.assertEqual(logger.get_destination().get_destination_name(), "Database")

    def test_file_logging(self):
        test_file = "bridge_test.log"
        dest = FileLogDestination(test_file)
        logger = TransactionLogger(dest)
        cmd = DepositCommand(self.acc, 1000.0)
        cmd.execute()
        logger.log(cmd.get_transaction())
        self.assertEqual(len(logger.get_transactions()), 1)
        dest.clear()

if __name__ == "__main__":
    unittest.main()
