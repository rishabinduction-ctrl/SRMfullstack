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
        self.log_file = "test_transactions.log"
        self.log = TransactionLog(self.log_file)
        self.log.clear()
        self.acc1 = AccountFactory.create_account("SAVINGS", 1001, "Rajesh", 30, 50000.0)
        self.acc2 = AccountFactory.create_account("CURRENT", 1002, "Priya", 28, 50000.0)
        self.acc1.set_pin(1234)
        self.acc2.set_pin(5678)
        self.transfer_svc = TransferService()

    def tearDown(self):
        self.log.clear()

    def test_deposit_command(self):
        cmd = DepositCommand(self.acc1, 5000.0)
        cmd.execute()
        txn = cmd.get_transaction()
        self.assertIsNotNone(txn)
        self.log.log_transaction(txn)
        self.assertEqual(len(self.log.get_transactions()), 1)

    def test_withdraw_command(self):
        cmd = WithdrawCommand(self.acc1, 10000.0, 1234)
        cmd.execute()
        txn = cmd.get_transaction()
        self.assertIsNotNone(txn)
        self.log.log_transaction(txn)
        self.assertEqual(len(self.log.get_transactions()), 1)

    def test_transfer_command(self):
        cmd = TransferCommand(self.transfer_svc, self.acc1, self.acc2, 5000.0, 1234)
        cmd.execute()
        txn = cmd.get_transaction()
        self.assertIsNotNone(txn)
        self.log.log_transaction(txn)
        self.assertEqual(len(self.log.get_transactions()), 1)

    def test_file_persistence(self):
        cmd = DepositCommand(self.acc1, 3000.0)
        cmd.execute()
        self.log.log_transaction(cmd.get_transaction())
        
        new_log = TransactionLog(self.log_file)
        txns = new_log.load_from_file()
        self.assertEqual(len(txns), 1)

if __name__ == "__main__":
    unittest.main()
