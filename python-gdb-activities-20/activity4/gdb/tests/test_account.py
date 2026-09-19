# gdb/tests/test_account.py
from gdb.domain.account import Account

def main():
    print("=== Activity 4: Enhanced Account Test Suite ===")
    acc = Account("ACC3001", "Charlie", 28, 5000.0, "Savings", "Active", "4321")

    # TODO (Step 1): PIN authentication -- assert acc.validate_pin("4321") is True,
    #   and that a wrong PIN (e.g. "0000") and None both return False.

    # TODO (Step 2): Active transactions -- assert deposit() and withdraw() return True while the
    #   status is "Active", and that the balance changes by exactly the expected amount.

    # TODO (Step 3): Inactive invariant -- set acc.status = "Inactive", then assert deposit() and
    #   withdraw() both return False and the balance does not change.

if __name__ == "__main__":
    main()
