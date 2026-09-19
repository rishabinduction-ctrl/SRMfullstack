# gdb/tests/test_account_subclasses.py
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.exceptions import MinimumBalanceViolationException

def main():
    print("=== Activity 8: Polymorphism Test ===")

    # Polymorphic list of accounts
    accounts = [
        SavingsAccount("SA001", "Alice", 25, 5000.0, "Active", "1111", 4.0, 1000.0),
        CurrentAccount("CA001", "Bob", 35, 2000.0, "Active", "2222", 5000.0)
    ]

    # TODO (Test 1): Withdraw from the SavingsAccount an amount that would leave less than its
    #   Rs 1000 minimum balance, and assert MinimumBalanceViolationException is raised
    #   (try / assert False / except pattern).

    # TODO (Test 2): Withdraw from the CurrentAccount more than its balance but within
    #   balance + overdraft limit. Assert it succeeds and the balance is negative by the expected amount.

if __name__ == "__main__":
    main()
