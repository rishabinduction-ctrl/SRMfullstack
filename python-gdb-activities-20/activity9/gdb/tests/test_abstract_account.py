# gdb/tests/test_abstract_account.py
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount

def main():
    print("=== Activity 9: Abstract Account & Template Pattern ===")
    sa = SavingsAccount("SA901", "Alice", 25, 10000.0, "Active", "1234", 4.0, 1000.0)
    ca = CurrentAccount("CA902", "Bob", 35, 50000.0, "Active", "5678", 25000.0)
    fd = FixedDepositAccount("FD903", "Charlie", 40, 100000.0, "Active", "9999", 12, 6.5)
    
    sa.display_account_info()
    assert sa.calculate_interest() == 400.0
    
    ca.display_account_info()
    assert ca.calculate_interest() == 0.0
    
    fd.display_account_info()
    assert fd.calculate_interest() == 6500.0
    
    print("Template method pattern executed successfully!")

if __name__ == "__main__":
    main()
