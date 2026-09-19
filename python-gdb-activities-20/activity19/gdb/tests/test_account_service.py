# gdb/tests/test_account_service.py
import unittest
from gdb.logging.memory_log_destination import MemoryLogDestination
from gdb.logging.transaction_logger import TransactionLogger
from gdb.service.account_service import AccountService
from gdb.exceptions.account_exception import AccountException
from gdb.exceptions.invalid_pin_exception import InvalidPinException

class TestAccountService(unittest.TestCase):
    def setUp(self):
        # ============================================================
        # 📝 STEP 9: Set Up The Service
        #
        # INSTRUCTIONS:
        #   1. self.dest = MemoryLogDestination()
        #   2. self.logger = TransactionLogger(self.dest)
        #   3. self.service = AccountService(self.logger)
        # ============================================================
        # TODO: wire the in-memory log destination, the logger and the service
        raise NotImplementedError("TODO: Step 9 - set up the AccountService")

    def test_open_and_get_account(self):
        # ============================================================
        # 📝 STEP 10: Open And Look Up An Account
        #
        # INSTRUCTIONS:
        #   1. Open a Savings account for "Rajesh Sharma" (30 yrs, Rs. 20,000, tenure 2) with open_account().
        #   2. Assert its account number is 1001 (the first number the service hands out).
        #   3. Fetch it again with get_account(1001) and assert the holder name is "Rajesh Sharma".
        # ============================================================
        # TODO: open an account and assert it can be looked up by number
        raise NotImplementedError("TODO: Step 10 - test open_account and get_account")

    def test_deposit(self):
        # ============================================================
        # 📝 STEP 11: Deposit Through The Service
        #
        # INSTRUCTIONS:
        #   1. Open a Savings account (Rs. 20,000) and set PIN 1234.
        #   2. Deposit Rs. 5,000 with service.deposit(1001, 5000.0).
        #   3. Assert the balance is 25000.0 and the transaction history holds 1 record.
        # ============================================================
        # TODO: deposit through the service and assert balance and history
        raise NotImplementedError("TODO: Step 11 - test deposit")

    def test_withdraw(self):
        # ============================================================
        # 📝 STEP 12: Withdraw Through The Service
        #
        # INSTRUCTIONS:
        #   1. Open a Savings account (Rs. 20,000) and set PIN 1234.
        #   2. Withdraw Rs. 5,000 with service.withdraw(1001, 5000.0, 1234).
        #   3. Assert the balance is 15000.0 and the transaction history holds 1 record.
        # ============================================================
        # TODO: withdraw through the service and assert balance and history
        raise NotImplementedError("TODO: Step 12 - test withdraw")

    def test_transfer(self):
        # ============================================================
        # 📝 STEP 13: Transfer Through The Service
        #
        # INSTRUCTIONS:
        #   1. Open a Savings account #1001 (Rs. 50,000, PIN 1234) and a Current account #1002 (Rs. 30,000, PIN 5678).
        #   2. Transfer Rs. 10,000 from 1001 to 1002 with PIN 1234.
        #   3. Assert both balances are now 40000.0 and the history holds 1 record.
        # ============================================================
        # TODO: transfer through the service and assert both balances and the history
        raise NotImplementedError("TODO: Step 13 - test transfer")

    def test_close_account(self):
        # ============================================================
        # 📝 STEP 14: Close An Account
        #
        # INSTRUCTIONS:
        #   1. Open a Savings account and set PIN 1234.
        #   2. Close it with service.close_account(1001, 1234).
        #   3. Assert the account is no longer active (is_active() is False).
        # ============================================================
        # TODO: close an account through the service and assert it is inactive
        raise NotImplementedError("TODO: Step 14 - test close_account")

    def test_error_cases(self):
        # ============================================================
        # 📝 STEP 15: Error Cases
        #
        # INSTRUCTIONS:
        #   1. Assert that depositing into a non-existent account (9999) raises AccountException.
        #   2. Open a Savings account with PIN 1234 and assert that withdrawing with PIN 9999
        #      raises InvalidPinException.
        #
        # HINT: Use `with self.assertRaises(...):` for each case.
        # ============================================================
        # TODO: assert the service rejects unknown accounts and wrong PINs
        raise NotImplementedError("TODO: Step 15 - test error cases")

if __name__ == "__main__":
    unittest.main()
