# gdb/tests/test_account.py
from gdb.domain.account import Account

def main():
    print("=== Activity 4: Enhanced Account Test Suite ===")
    acc = Account("ACC3001", "Charlie", 28, 5000.0, "Savings", "Active", "4321")
    
    # PIN Tests
    assert acc.validate_pin("4321") is True
    assert acc.validate_pin("0000") is False
    assert acc.validate_pin(None) is False
    print("Test 1: PIN Validation Suite -> PASS")
    
    # Active Transactions
    assert acc.deposit(1000.0) is True
    assert acc.balance == 6000.0
    print("Test 2: Active Account Transactions -> PASS")
    
    # Inactive Blocking
    acc.status = "Inactive"
    assert acc.withdraw(500.0) is False
    assert acc.deposit(500.0) is False
    print("Test 3: Inactive Protection -> PASS")
    
    print("All Enhanced Account tests passed!")

if __name__ == "__main__":
    main()
