# gdb/tests/test_account_subclasses.py
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.exceptions import MinimumBalanceViolationException

def main():
    print("=== Activity 8: Polymorphism Test ===")
    
    # Polymorphic list of accounts
    accounts = [
        SavingsAccount("SA001", "Alice", 25, 5000.0, "Active", "1111", 4.0, 1000.0),
        CurrentAccount("CA001", "Bob", 35, 2000.0, "Active", "2222", 5000.0)
    ]
    
    # Test 1: Savings Min Balance Violation
    try:
        accounts[0].withdraw(4500.0)
        assert False, "Expected MinimumBalanceViolationException"
    except MinimumBalanceViolationException as e:
        print(f"PASS: Caught MinimumBalanceViolationException -> {e}")
        
    # Test 2: Current Account Overdraft
    accounts[1].withdraw(6000.0)
    assert accounts[1].balance == -4000.0
    print(f"PASS: Overdraft withdrawal succeeded! New Balance: Rs {accounts[1].balance}")

    print("All polymorphic behaviors verified!")

if __name__ == "__main__":
    main()
