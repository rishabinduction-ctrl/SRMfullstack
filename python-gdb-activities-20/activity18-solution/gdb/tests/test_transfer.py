# gdb/tests/test_transfer.py
import unittest
from gdb.domain.account_factory import AccountFactory
from gdb.domain.account_rules_engine import AccountRulesEngine
from gdb.service.transfer_service import TransferService
from gdb.exceptions.account_exception import AccountException
from gdb.exceptions.insufficient_balance_exception import InsufficientBalanceException

class TestTransfer(unittest.TestCase):
    def setUp(self):
        self.svc = TransferService()
        self.acc1 = AccountFactory.create_account("SAVINGS", 1001, "Rajesh Sharma", 30, 100000.0, 0)
        self.acc2 = AccountFactory.create_account("SAVINGS", 1002, "Priya Patel", 28, 20000.0, 0)
        self.acc1.set_pin(1234)
        self.acc2.set_pin(5678)

    def test_successful_transfer(self):
        self.svc.transfer(self.acc1, self.acc2, 5000.0, 1234)
        self.assertEqual(self.acc1.get_balance(), 95000.0)
        self.assertEqual(self.acc2.get_balance(), 25000.0)

    def test_insufficient_balance(self):
        with self.assertRaises(InsufficientBalanceException):
            self.svc.transfer(self.acc1, self.acc2, 95000.0, 1234)

    def test_daily_transfer_limit_breach(self):
        # Limit for NEW Savings is Rs. 50,000
        self.svc.transfer(self.acc1, self.acc2, 20000.0, 1234)
        self.svc.transfer(self.acc1, self.acc2, 20000.0, 1234)
        with self.assertRaises(AccountException):
            self.svc.transfer(self.acc1, self.acc2, 20000.0, 1234)

    def test_remaining_limit(self):
        self.svc.transfer(self.acc1, self.acc2, 10000.0, 1234)
        self.assertEqual(self.acc1.get_daily_transfer_total(), 10000.0)
        self.assertEqual(self.acc1.get_remaining_daily_transfer_limit(), 40000.0)

if __name__ == "__main__":
    unittest.main()
