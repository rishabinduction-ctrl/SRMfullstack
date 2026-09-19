# gdb/tests/test_command_logging.py
import unittest
import os
from gdb.domain.account_factory import AccountFactory
from gdb.command.deposit_command import DepositCommand
from gdb.command.withdraw_command import WithdrawCommand
from gdb.command.transfer_command import TransferCommand
from gdb.service.transfer_service import TransferService
from gdb.logging.transaction_log import TransactionLog

class TestCommandLogging(unittest.TestCase):
    def setUp(self):
        # ============================================================
        # 📝 STEP 15: Create The Log, Accounts And Service
        #
        # INSTRUCTIONS:
        #   1. self.log_file = "test_transactions.log"
        #   2. self.log = TransactionLog(self.log_file), then call self.log.clear() so every test starts empty.
        #   3. self.acc1 = AccountFactory.create_account("SAVINGS", 1001, "Rajesh", 30, 50000.0) with PIN 1234.
        #   4. self.acc2 = AccountFactory.create_account("CURRENT", 1002, "Priya", 28, 50000.0) with PIN 5678.
        #   5. self.transfer_svc = TransferService()
        # ============================================================
        # TODO: create the transaction log, the two accounts and the transfer service
        raise NotImplementedError("TODO: Step 15 - create the log, accounts and transfer service")

    def tearDown(self):
        # Provided: delete the test log file after every test.
        self.log.clear()

    def test_deposit_command(self):
        # ============================================================
        # 📝 STEP 16: Execute And Log A DepositCommand
        #
        # INSTRUCTIONS:
        #   1. Create DepositCommand(self.acc1, 5000.0) and call execute().
        #   2. Assert get_transaction() is not None.
        #   3. Log it with self.log.log_transaction(...) and assert the log now holds exactly 1 transaction.
        # ============================================================
        # TODO: execute a deposit command, log its transaction and assert the log size
        raise NotImplementedError("TODO: Step 16 - test DepositCommand")

    def test_withdraw_command(self):
        # ============================================================
        # 📝 STEP 17: Execute And Log A WithdrawCommand
        #
        # INSTRUCTIONS:
        #   1. Create WithdrawCommand(self.acc1, 10000.0, 1234) and call execute().
        #   2. Assert get_transaction() is not None.
        #   3. Log it and assert the log now holds exactly 1 transaction.
        # ============================================================
        # TODO: execute a withdraw command, log its transaction and assert the log size
        raise NotImplementedError("TODO: Step 17 - test WithdrawCommand")

    def test_transfer_command(self):
        # ============================================================
        # 📝 STEP 18: Execute And Log A TransferCommand
        #
        # INSTRUCTIONS:
        #   1. Create TransferCommand(self.transfer_svc, self.acc1, self.acc2, 5000.0, 1234) and call execute().
        #   2. Assert get_transaction() is not None.
        #   3. Log it and assert the log now holds exactly 1 transaction.
        # ============================================================
        # TODO: execute a transfer command, log its transaction and assert the log size
        raise NotImplementedError("TODO: Step 18 - test TransferCommand")

    def test_file_persistence(self):
        # ============================================================
        # 📝 STEP 19: Verify File Persistence
        #
        # INSTRUCTIONS:
        #   1. Execute a DepositCommand(self.acc1, 3000.0) and log its transaction.
        #   2. Create a brand-new TransactionLog(self.log_file) and call load_from_file().
        #   3. Assert the new log loaded exactly 1 transaction from the file.
        #
        # HINT: The new instance starts empty, so the record can only come from the file on disk.
        # ============================================================
        # TODO: prove the logged transaction survives in the file
        raise NotImplementedError("TODO: Step 19 - test file persistence")

if __name__ == "__main__":
    unittest.main()
