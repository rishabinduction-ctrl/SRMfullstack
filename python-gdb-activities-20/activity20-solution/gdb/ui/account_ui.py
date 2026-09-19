# gdb/ui/account_ui.py
import sys
from gdb.service.account_service import AccountService
from gdb.exceptions.account_exception import AccountException

class AccountUI:
    """Interactive console interface for banking operations."""

    def __init__(self, service: AccountService) -> None:
        self._service = service

    def start(self) -> None:
        while True:
            self.display_main_menu()
            choice = self.read_int("Enter your choice: ")
            try:
                if choice == 1:
                    self.handle_open_account()
                elif choice == 2:
                    self.handle_deposit()
                elif choice == 3:
                    self.handle_withdraw()
                elif choice == 4:
                    self.handle_transfer()
                elif choice == 5:
                    self.handle_close_account()
                elif choice == 6:
                    self.handle_view_account()
                elif choice == 7:
                    self.handle_view_transactions()
                elif choice == 8:
                    print("Thank you! Goodbye.")
                    break
                else:
                    print("Invalid choice. Please enter 1-8.")
            except Exception as e:
                print(f"ERROR: {e}")

    def display_main_menu(self) -> None:
        print("\n" + "=" * 50)
        print("     GLOBAL DIGITAL BANK (GDB) — MAIN MENU")
        print("=" * 50)
        print("1. Open Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Transfer Funds")
        print("5. Close Account")
        print("6. View Account Details")
        print("7. View Transaction History")
        print("8. Exit")
        print("=" * 50)

    def handle_open_account(self) -> None:
        acc_type = self.read_string("Account Type (Savings/Current/FixedDeposit/Salary): ")
        name = self.read_string("Account Holder Name: ")
        age = self.read_int("Age: ")
        initial_balance = self.read_double("Initial Balance: ")
        tenure = self.read_int("Customer Tenure in Years (0 for new): ")
        acc = self._service.open_account(acc_type, name, age, initial_balance, tenure)
        pin = self.read_int("Set 4-digit PIN (1000-9999): ")
        acc.set_pin(pin)
        print(f"SUCCESS: Account #{acc.get_account_number()} created successfully!")
        print(acc.get_account_info())

    def handle_deposit(self) -> None:
        acc_no = self.read_int("Account Number: ")
        amount = self.read_double("Amount to deposit: ")
        txn = self._service.deposit(acc_no, amount)
        print(f"SUCCESS: {txn.get_receipt()}")

    def handle_withdraw(self) -> None:
        acc_no = self.read_int("Account Number: ")
        amount = self.read_double("Amount to withdraw: ")
        pin = self.read_int("4-digit PIN: ")
        txn = self._service.withdraw(acc_no, amount, pin)
        print(f"SUCCESS: {txn.get_receipt()}")

    def handle_transfer(self) -> None:
        from_acc = self.read_int("From Account Number: ")
        to_acc = self.read_int("To Account Number: ")
        amount = self.read_double("Amount to transfer: ")
        pin = self.read_int("Sender 4-digit PIN: ")
        txn = self._service.transfer(from_acc, to_acc, amount, pin)
        print(f"SUCCESS: {txn.get_receipt()}")

    def handle_close_account(self) -> None:
        acc_no = self.read_int("Account Number: ")
        pin = self.read_int("4-digit PIN: ")
        self._service.close_account(acc_no, pin)
        print(f"SUCCESS: Account #{acc_no} closed.")

    def handle_view_account(self) -> None:
        acc_no = self.read_int("Account Number: ")
        acc = self._service.get_account(acc_no)
        if acc is None:
            print(f"Account #{acc_no} not found.")
        else:
            print(acc.get_account_info())

    def handle_view_transactions(self) -> None:
        txns = self._service.get_transaction_history()
        if not txns:
            print("No transactions logged.")
            return
        print("\n--- TRANSACTION HISTORY LOG ---")
        for i, t in enumerate(txns, 1):
            print(f"[{i}] {t.get_receipt()}")

    def read_int(self, prompt: str) -> int:
        while True:
            try:
                val = input(prompt).strip()
                return int(val)
            except ValueError:
                print("Invalid integer. Please try again.")

    def read_double(self, prompt: str) -> float:
        while True:
            try:
                val = input(prompt).strip()
                return float(val)
            except ValueError:
                print("Invalid number. Please try again.")

    def read_string(self, prompt: str) -> str:
        while True:
            val = input(prompt).strip()
            if val:
                return val
            print("Input cannot be empty.")
