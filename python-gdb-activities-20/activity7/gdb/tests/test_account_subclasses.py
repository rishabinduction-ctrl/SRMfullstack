# gdb/tests/test_account_subclasses.py
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount

def main():
    print("=== Activity 7: Account Subclasses Test ===")
    sa = SavingsAccount("SA101", "Alice", 28, 10000.0, "Active", "1234", 4.5)
    print(f"Savings Account Interest on Rs 10000 @ 4.5%: Rs {sa.calculate_interest()}")
    assert sa.calculate_interest() == 450.0
    
    ca = CurrentAccount("CA201", "Bob Corp", 35, 50000.0, "Active", "5678", 20000.0)
    print(f"Current Account Overdraft Limit: Rs {ca.overdraft_limit}")
    assert ca.overdraft_limit == 20000.0
    print("All subclasses instantiated successfully!")

if __name__ == "__main__":
    main()
