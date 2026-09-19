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
        # ============================================================
        # 📝 STEP 15: Set Up The Service And UI
        #
        # INSTRUCTIONS:
        #   1. self.dest = MemoryLogDestination()
        #   2. self.logger = TransactionLogger(self.dest)
        #   3. self.service = AccountService(self.logger)
        #   4. self.ui = AccountUI(self.service)
        # ============================================================
        # TODO: wire the log destination, logger, service and UI used by every test
        raise NotImplementedError("TODO: Step 15 - set up the service and UI")

    def test_ui_display_menu(self):
        # ============================================================
        # 📝 STEP 16: Test The Main Menu
        #
        # INSTRUCTIONS:
        #   1. Capture printed output: `with patch("sys.stdout", new=StringIO()) as fake_out:`
        #   2. Inside the block call self.ui.display_main_menu() and read fake_out.getvalue().
        #   3. Assert the output contains "GLOBAL DIGITAL BANK", "1. Open Account" and "8. Exit".
        # ============================================================
        # TODO: capture the menu output and assert its key lines
        raise NotImplementedError("TODO: Step 16 - test display_main_menu")

    def test_ui_open_account_and_exit(self):
        # ============================================================
        # 📝 STEP 17: Drive The UI With Scripted Input
        #
        # INSTRUCTIONS:
        #   1. Build the list of answers a user would type, in prompt order:
        #      ["1", "Savings", "Rajesh Sharma", "30", "20000", "2", "1234", "8"]
        #      (menu choice, type, name, age, balance, tenure, PIN, then 8 to exit).
        #   2. Patch both input and output:
        #      `with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new=StringIO()):`
        #   3. Inside the block call self.ui.start().
        #   4. Assert self.service.get_account(1001) is not None, its holder name is "Rajesh Sharma"
        #      and its balance is 20000.0.
        #
        # HINT: side_effect hands out one list item per input() call -- if your prompts ask in a
        #       different order, the answers land in the wrong fields.
        # ============================================================
        # TODO: script a user session that opens an account and exits, then assert the account exists
        raise NotImplementedError("TODO: Step 17 - test opening an account through the UI")

if __name__ == "__main__":
    unittest.main()
