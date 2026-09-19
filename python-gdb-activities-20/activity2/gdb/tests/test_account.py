# gdb/tests/test_account.py
from gdb.domain.account import Account

def main():
    print("=== Activity 2: Test Account Suite ===")

    # TODO (Step 1): Create an Account with known values, e.g.
    #   acc = Account("ACC1001", "Alice", 25, 5000.0, "Savings", "Active")
    #   and assert every property (account_number, name, age, balance, account_type, status)
    #   matches the constructor argument.

    # TODO (Step 2): Deposit a positive amount -> assert it returns True and the balance grew by that amount.
    #   Then deposit a negative amount and zero -> assert each returns False and the balance is unchanged.

    # TODO (Step 3): Withdraw an amount within the balance -> assert it returns True and the balance shrank.
    #   Then withdraw more than the balance -> assert it returns False and the balance is unchanged.

if __name__ == "__main__":
    main()
