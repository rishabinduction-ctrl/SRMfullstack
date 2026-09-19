# gdb/tests/test_transaction_model.py
import unittest
from datetime import datetime
from gdb.domain.account_factory import AccountFactory
from gdb.domain.transaction import Transaction
from gdb.domain.transaction_type import TransactionType

class TestTransactionModel(unittest.TestCase):
    def setUp(self):
        # ============================================================
        # 📝 STEP 9: Create The Test Account
        #
        # INSTRUCTIONS:
        #   1. self.acc = AccountFactory.create_account("SAVINGS", 1001, "Rajesh Sharma", 30, 50000.0, 3)
        #   2. Set PIN 1234 on the account with set_pin().
        # ============================================================
        # TODO: create the Savings account used by every test and set its PIN
        raise NotImplementedError("TODO: Step 9 - create the test account")

    def test_deposit_with_transaction(self):
        # ============================================================
        # 📝 STEP 10: Deposit With Transaction
        #
        # INSTRUCTIONS:
        #   1. txn = self.acc.deposit_with_transaction(5000.0)
        #   2. Assert txn is not None.
        #   3. Assert its type is TransactionType.DEPOSIT, amount is 5000.0,
        #      balance after is 55000.0 and status is "SUCCESS".
        # ============================================================
        # TODO: deposit with a transaction and assert every field of the returned record
        raise NotImplementedError("TODO: Step 10 - test deposit_with_transaction")

    def test_withdraw_with_transaction(self):
        # ============================================================
        # 📝 STEP 11: Withdraw With Transaction
        #
        # INSTRUCTIONS:
        #   1. txn = self.acc.withdraw_with_transaction(10000.0, 1234)
        #   2. Assert txn is not None.
        #   3. Assert its type is TransactionType.WITHDRAW, amount is 10000.0 and balance after is 40000.0.
        # ============================================================
        # TODO: withdraw with a transaction and assert the returned record
        raise NotImplementedError("TODO: Step 11 - test withdraw_with_transaction")

    def test_receipt_formatting(self):
        # ============================================================
        # 📝 STEP 12: Receipt Formatting
        #
        # INSTRUCTIONS:
        #   1. Deposit Rs. 1,000 with deposit_with_transaction() and call get_receipt() on the result.
        #   2. Assert the receipt contains "TXN ID:", "DEPOSIT" and "Rs. 1,000.00".
        #
        # HINT: Use self.assertIn(expected_text, receipt).
        # ============================================================
        # TODO: assert the receipt text format
        raise NotImplementedError("TODO: Step 12 - test the receipt format")

if __name__ == "__main__":
    unittest.main()
