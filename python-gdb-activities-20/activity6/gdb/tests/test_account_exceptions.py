# gdb/tests/test_account_exceptions.py
from gdb.domain.account import Account
from gdb.exceptions import (
    AccountException,
    InvalidAmountException,
    InsufficientBalanceException,
    InactiveAccountException
)

def main():
    print("=== Activity 6: Exception Handling Suite ===")
    acc = Account("ACC001", "John", 28, 5000.0, "Savings", "Active", "1234")

    # TODO (Step 1): Invalid deposit -- call acc.deposit(-500.0) inside a try block, follow it with
    #   assert False, "Expected InvalidAmountException"
    #   and catch InvalidAmountException to print a PASS message.

    # TODO (Step 2a): Overdraft -- withdraw more than the balance and assert that
    #   InsufficientBalanceException is raised (same try / assert False / except pattern).

    # TODO (Step 2b): Inactive account -- create an Account with status "Inactive", withdraw from it
    #   and assert that InactiveAccountException is raised.

if __name__ == "__main__":
    main()
