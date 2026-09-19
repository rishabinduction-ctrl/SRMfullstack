# gdb/tests/test_account.py
from gdb.domain.account import Account

def main():
    print("=== Activity 2: Test Account Suite ===")
    acc = Account("ACC1001", "Alice", 25, 5000.0, "Savings", "Active")
    
    # Test 1: Initial State
    assert acc.account_number == "ACC1001"
    assert acc.balance == 5000.0
    print(f"Test 1: Initial Account Creation -> PASS [Balance: {acc.balance}]")
    
    # Test 2: Valid Deposit
    res = acc.deposit(1500.0)
    assert res is True and acc.balance == 6500.0
    print(f"Test 2: Valid Deposit (+1500.0) -> PASS [New Balance: {acc.balance}]")
    
    # Test 3: Invalid Deposit
    res = acc.deposit(-500.0)
    assert res is False and acc.balance == 6500.0
    print(f"Test 3: Invalid Deposit (-500.0) -> PASS [Rejected, Balance: {acc.balance}]")
    
    # Test 4: Valid Withdrawal
    res = acc.withdraw(2000.0)
    assert res is True and acc.balance == 4500.0
    print(f"Test 4: Valid Withdrawal (-2000.0) -> PASS [New Balance: {acc.balance}]")
    
    # Test 5: Overdraft
    res = acc.withdraw(10000.0)
    assert res is False and acc.balance == 4500.0
    print(f"Test 5: Overdraft Withdrawal (-10000.0) -> PASS [Rejected, Balance: {acc.balance}]")
    
    print("All Account tests completed successfully!")

if __name__ == "__main__":
    main()
