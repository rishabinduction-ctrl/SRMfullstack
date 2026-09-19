# gdb/tests/test_account_service.py
import unittest
from gdb.logging.memory_log_destination import MemoryLogDestination
from gdb.logging.transaction_logger import TransactionLogger
from gdb.service.account_service import AccountService
from gdb.exceptions.account_exception import AccountException
from gdb.exceptions.invalid_pin_exception import InvalidPinException

class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.dest = MemoryLogDestination()
        self.logger = TransactionLogger(self.dest)
        self.service = AccountService(self.logger)

    def test_open_and_get_account(self):
        acc = self.service.open_account("SAVINGS", "Rajesh Sharma", 30, 20000.0, 2)
        self.assertEqual(acc.get_account_number(), 1001)
        retrieved = self.service.get_account(1001)
        self.assertEqual(retrieved.get_account_holder_name(), "Rajesh Sharma")

    def test_deposit(self):
        acc = self.service.open_account("SAVINGS", "Rajesh", 30, 20000.0)
        acc.set_pin(1234)
        txn = self.service.deposit(1001, 5000.0)
        self.assertEqual(acc.get_balance(), 25000.0)
        self.assertEqual(len(self.service.get_transaction_history()), 1)

    def test_withdraw(self):
        acc = self.service.open_account("SAVINGS", "Rajesh", 30, 20000.0)
        acc.set_pin(1234)
        txn = self.service.withdraw(1001, 5000.0, 1234)
        self.assertEqual(acc.get_balance(), 15000.0)
        self.assertEqual(len(self.service.get_transaction_history()), 1)

    def test_transfer(self):
        acc1 = self.service.open_account("SAVINGS", "Rajesh", 30, 50000.0)
        acc2 = self.service.open_account("CURRENT", "Priya", 28, 30000.0)
        acc1.set_pin(1234)
        acc2.set_pin(5678)
        txn = self.service.transfer(1001, 1002, 10000.0, 1234)
        self.assertEqual(acc1.get_balance(), 40000.0)
        self.assertEqual(acc2.get_balance(), 40000.0)
        self.assertEqual(len(self.service.get_transaction_history()), 1)

    def test_close_account(self):
        acc = self.service.open_account("SAVINGS", "Rajesh", 30, 20000.0)
        acc.set_pin(1234)
        self.service.close_account(1001, 1234)
        self.assertFalse(acc.is_active())

if __name__ == "__main__":
    unittest.main()
