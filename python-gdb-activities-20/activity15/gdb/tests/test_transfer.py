# gdb/tests/test_transfer.py
import unittest
from gdb.domain.account_factory import AccountFactory
from gdb.domain.account_rules_engine import AccountRulesEngine
from gdb.service.transfer_service import TransferService
from gdb.exceptions.account_exception import AccountException
from gdb.exceptions.insufficient_balance_exception import InsufficientBalanceException

class TestTransfer(unittest.TestCase):
    def setUp(self):
        # ============================================================
        # 📝 STEP 9: Create The Service And Two Accounts
        #
        # INSTRUCTIONS:
        #   1. self.svc = TransferService()
        #   2. self.acc1 = AccountFactory.create_account("SAVINGS", 1001, "Rajesh Sharma", 30, 100000.0, 0)
        #   3. self.acc2 = AccountFactory.create_account("SAVINGS", 1002, "Priya Patel", 28, 20000.0, 0)
        #   4. Set PIN 1234 on acc1 and PIN 5678 on acc2 with set_pin().
        #
        # HINT: The last factory argument is tenure in years -- 0 puts both accounts in the NEW tier.
        # ============================================================
        # TODO: create the TransferService and the two accounts used by every test
        raise NotImplementedError("TODO: Step 9 - create the service and test accounts")

    def test_successful_transfer(self):
        # ============================================================
        # 📝 STEP 10: Successful Transfer
        #
        # INSTRUCTIONS:
        #   1. Transfer Rs. 5,000 from acc1 to acc2 using PIN 1234.
        #   2. Assert acc1's balance is now 95000.0 and acc2's balance is 25000.0.
        # ============================================================
        # TODO: transfer Rs. 5,000 and assert both balances
        raise NotImplementedError("TODO: Step 10 - test a successful transfer")

    def test_insufficient_balance(self):
        # ============================================================
        # 📝 STEP 11: Insufficient Balance
        #
        # INSTRUCTIONS:
        #   1. Inside `with self.assertRaises(InsufficientBalanceException):`, transfer Rs. 95,000 from acc1.
        #   2. (Optional) After the block, assert that neither balance changed.
        #
        # HINT: A Savings account must keep its minimum balance, so acc1 cannot send almost all of its Rs. 1,00,000.
        # ============================================================
        # TODO: assert that an over-large transfer raises InsufficientBalanceException
        raise NotImplementedError("TODO: Step 11 - test the insufficient balance rule")

    def test_daily_transfer_limit_breach(self):
        # ============================================================
        # 📝 STEP 12: Daily Limit Breach
        #
        # INSTRUCTIONS:
        #   1. Transfer Rs. 20,000 from acc1 to acc2 twice -- both transfers must succeed.
        #   2. Assert that a third Rs. 20,000 transfer raises AccountException.
        #
        # HINT: A NEW Savings account may send Rs. 50,000 per day (acc1.get_daily_transfer_limit()).
        #       40,000 already used + 20,000 would cross that limit.
        # ============================================================
        # TODO: transfer until the daily limit is breached and assert the AccountException
        raise NotImplementedError("TODO: Step 12 - test the daily limit breach")

    def test_remaining_limit(self):
        # ============================================================
        # 📝 STEP 13: Remaining Limit
        #
        # INSTRUCTIONS:
        #   1. Transfer Rs. 10,000 from acc1 to acc2.
        #   2. Assert acc1.get_daily_transfer_total() == 10000.0.
        #   3. Assert acc1.get_remaining_daily_transfer_limit() == 40000.0.
        #
        # HINT: Used today + remaining always adds up to the daily limit.
        # ============================================================
        # TODO: assert the used total and the remaining daily limit
        raise NotImplementedError("TODO: Step 13 - test the remaining daily limit")

if __name__ == "__main__":
    unittest.main()
