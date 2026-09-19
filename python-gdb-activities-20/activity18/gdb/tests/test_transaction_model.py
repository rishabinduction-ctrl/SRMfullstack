# gdb/tests/test_transaction_model.py
import unittest
from datetime import datetime
from gdb.domain.account_factory import AccountFactory
from gdb.domain.transaction import Transaction
from gdb.domain.transaction_type import TransactionType

class TestTransactionModel(unittest.TestCase):
    def setUp(self):
        self.acc = AccountFactory.create_account("SAVINGS", 1001, "Rajesh Sharma", 30, 50000.0, 3)
        self.acc.set_pin(1234)

    def test_deposit_with_transaction(self):
        txn = self.acc.deposit_with_transaction(5000.0)
        self.assertIsNotNone(txn)
        self.assertEqual(txn.get_type(), TransactionType.DEPOSIT)
        self.assertEqual(txn.get_amount(), 5000.0)
        self.assertEqual(txn.get_balance_after(), 55000.0)
        self.assertEqual(txn.get_status(), "SUCCESS")

    def test_withdraw_with_transaction(self):
        txn = self.acc.withdraw_with_transaction(10000.0, 1234)
        self.assertIsNotNone(txn)
        self.assertEqual(txn.get_type(), TransactionType.WITHDRAW)
        self.assertEqual(txn.get_amount(), 10000.0)
        self.assertEqual(txn.get_balance_after(), 40000.0)

    def test_receipt_formatting(self):
        txn = self.acc.deposit_with_transaction(1000.0)
        receipt = txn.get_receipt()
        self.assertIn("TXN ID:", receipt)
        self.assertIn("DEPOSIT", receipt)
        self.assertIn("Rs. 1,000.00", receipt)

if __name__ == "__main__":
    unittest.main()
