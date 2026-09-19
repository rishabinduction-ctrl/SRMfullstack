# gdb/tests/test_abstract_account.py
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount
from gdb.exceptions import MinimumBalanceViolationException

def main():
    print("=== Activity 10: Banking Operations Suite ===")
    sa = SavingsAccount("SA001", "Alice", 25, 10000.0, "Active", "1234", 4.0, 1000.0)
    ca = CurrentAccount("CA001", "Bob", 35, 50000.0, "Active", "5678", 25000.0)
    fd = FixedDepositAccount("FD001", "Charlie", 40, 100000.0, "Active", "9999", 12, 6.5)

    # TODO (Step 1a): Loop over [sa, ca, fd], treating each one only as a BankAccount, and assert that
    #   calculate_interest() returns the expected value for each product
    #   (Savings: 4% of 10000, Current: 0.0, FixedDeposit: 6.5% for 12 months).

    # TODO (Step 1b): Assert the SavingsAccount minimum balance: a withdrawal that would leave less than
    #   Rs 1000 must raise MinimumBalanceViolationException (try / assert False / except pattern).

if __name__ == "__main__":
    main()
