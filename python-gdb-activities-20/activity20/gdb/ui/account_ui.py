# gdb/ui/account_ui.py
import sys
from gdb.service.account_service import AccountService
from gdb.exceptions.account_exception import AccountException

class AccountUI:
    """Interactive console interface for banking operations."""

    # ============================================================
    # 📝 STEP 1: Fields & Constructor
    #
    # INSTRUCTIONS:
    #   Store the AccountService in self._service -- every handler talks to the bank only through it.
    # ============================================================
    # TODO: keep a reference to the AccountService
    def __init__(self, service: AccountService) -> None:
        raise NotImplementedError("TODO: Step 1 - implement AccountUI constructor")

    # ============================================================
    # 📝 STEP 2: Implement start() (Main Menu Loop)
    #
    # INSTRUCTIONS:
    #   Loop until choice 8 (Exit) is selected:
    #   1. display_main_menu()
    #   2. choice = read_int("Enter your choice: ")
    #   3. Dispatch to handler methods
    # ============================================================
    # TODO: implement start() menu loop
    def start(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 3: Implement display_main_menu()
    # ============================================================
    # TODO: print menu banner and options 1-8
    def display_main_menu(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 4: Implement handle_open_account()
    # ============================================================
    # TODO: prompt type, name, age, balance, pin; open account
    def handle_open_account(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 5: Implement handle_deposit()
    # ============================================================
    # TODO: prompt account number, amount; execute deposit
    def handle_deposit(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 6: Implement handle_withdraw()
    # ============================================================
    # TODO: prompt account number, amount, pin; execute withdraw
    def handle_withdraw(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 7: Implement handle_transfer()
    # ============================================================
    # TODO: prompt from, to, amount, pin; execute transfer
    def handle_transfer(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 8: Implement handle_close_account()
    # ============================================================
    # TODO: prompt account number, pin; close account
    def handle_close_account(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 9: Implement handle_view_account()
    # ============================================================
    # TODO: prompt account number; display details
    def handle_view_account(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 10: Implement handle_view_transactions()
    # ============================================================
    # TODO: print transaction history log
    def handle_view_transactions(self) -> None:
        pass

    # ============================================================
    # 📝 STEP 11-13: Robust Input Helpers (read_int, read_double, read_string)
    # ============================================================
    def read_int(self, prompt: str) -> int:
        return 0

    def read_double(self, prompt: str) -> float:
        return 0.0

    def read_string(self, prompt: str) -> str:
        return ""
