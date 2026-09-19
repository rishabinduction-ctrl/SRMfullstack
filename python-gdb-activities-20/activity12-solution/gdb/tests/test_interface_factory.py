# gdb/tests/test_interface_factory.py
from gdb.domain.account_factory import AccountFactory

def main():
    print("=== Activity 12: Factory-Driven System Suite ===")
    sa = AccountFactory.create_account("SAVINGS", "SA100", "Alice", 25, 5000.0, "Active", "1234")
    ca = AccountFactory.create_account("CURRENT", "CA200", "Bob", 35, 10000.0, "Active", "5678")
    sal = AccountFactory.create_account("SALARY", "SAL300", "Charlie", 28, 0.0, "Active", "9999")
    fd = AccountFactory.create_account("FIXEDDEPOSIT", "FD400", "Diana", 45, 50000.0, "Active", "0000")
    
    assert sa.balance == 5000.0
    assert ca.balance == 10000.0
    assert sal.balance == 0.0
    assert fd.balance == 50000.0
    
    print("Factory-driven architecture successfully verified!")

if __name__ == "__main__":
    main()
