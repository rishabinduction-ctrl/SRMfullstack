# gdb/tests/test_account_exceptions.py
from gdb.domain.account import Account
from gdb.exceptions import (
    AccountException,
    InvalidAmountException,
    InsufficientBalanceException,
    InactiveAccountException
)

def main():
    print("=== Activity 6: Exception Handling Suite ===")
    
    # Test 1: Valid Lifecycle
    acc1 = Account("ACC001", "John", 28, 5000.0, "Savings", "Active", "1234")
    acc1.deposit(2000.0)
    acc1.withdraw(1500.0)
    assert acc1.balance == 5500.0
    print(f"PASS: Valid lifecycle balance: Rs {acc1.balance}")
    
    # Test 2: Negative Deposit
    try:
        acc2 = Account("ACC002", "Jane", 32, 3000.0, "Savings", "Active", "1234")
        acc2.deposit(-500.0)
        assert False, "Expected InvalidAmountException"
    except InvalidAmountException as e:
        print(f"PASS: Caught InvalidAmountException -> {e}")
        
    # Test 3: Insufficient Balance
    try:
        acc3 = Account("ACC003", "Alice", 22, 1000.0, "Savings", "Active", "1234")
        acc3.withdraw(5000.0)
        assert False, "Expected InsufficientBalanceException"
    except InsufficientBalanceException as e:
        print(f"PASS: Caught InsufficientBalanceException -> {e}")

    # Test 4: Inactive Account
    try:
        acc4 = Account("ACC004", "Bob", 45, 10000.0, "Savings", "Inactive", "1234")
        acc4.withdraw(500.0)
        assert False, "Expected InactiveAccountException"
    except InactiveAccountException as e:
        print(f"PASS: Caught InactiveAccountException -> {e}")

    print("All exception handling tests completed successfully!")

if __name__ == "__main__":
    main()
