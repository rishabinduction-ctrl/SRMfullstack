# gdb/tests/test_account_ui.py
import unittest
from unittest.mock import patch
from io import StringIO
from gdb.logging.memory_log_destination import MemoryLogDestination
from gdb.logging.transaction_logger import TransactionLogger
from gdb.service.account_service import AccountService
from gdb.ui.account_ui import AccountUI

class TestAccountUI(unittest.TestCase):
    def setUp(self):
        self.dest = MemoryLogDestination()
        self.logger = TransactionLogger(self.dest)
        self.service = AccountService(self.logger)
        self.ui = AccountUI(self.service)

    def test_ui_display_menu(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_main_menu()
            output = fake_out.getvalue()
            self.assertIn("GLOBAL DIGITAL BANK", output)
            self.assertIn("1. Open Account", output)
            self.assertIn("8. Exit", output)

    def test_ui_open_account_and_exit(self):
        # Inputs: 1 (open account), Savings, Rajesh, 30, 20000, 2, 1234 (pin), 8 (exit)
        inputs = ["1", "Savings", "Rajesh Sharma", "30", "20000", "2", "1234", "8"]
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.start()
            acc = self.service.get_account(1001)
            self.assertIsNotNone(acc)
            self.assertEqual(acc.get_account_holder_name(), "Rajesh Sharma")
            self.assertEqual(acc.get_balance(), 20000.0)

if __name__ == "__main__":
    unittest.main()
