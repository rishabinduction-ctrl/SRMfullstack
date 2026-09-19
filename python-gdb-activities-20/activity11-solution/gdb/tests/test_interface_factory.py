# gdb/tests/test_interface_factory.py
from gdb.domain.account_factory import AccountFactory

def main():
    print("=== Activity 11: Interface & Factory Pattern Test ===")
    sa = AccountFactory.create_account("SAVINGS", "SA100", "Alice", 25, 5000.0, "Active", "1234")
    ca = AccountFactory.create_account("CURRENT", "CA200", "Bob", 35, 10000.0, "Active", "5678")
    sal = AccountFactory.create_account("SALARY", "SAL300", "Charlie", 28, 0.0, "Active", "9999")
    fd = AccountFactory.create_account("FIXEDDEPOSIT", "FD400", "Diana", 45, 50000.0, "Active", "0000")
    
    assert sa.get_account_type() == "Savings"
    assert ca.get_account_type() == "Current"
    assert sal.get_account_type() == "Salary"
    assert fd.get_account_type() == "FixedDeposit"
    print("All accounts successfully created through AccountFactory!")

if __name__ == "__main__":
    main()
