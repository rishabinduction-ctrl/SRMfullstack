# gdb/tests/test_account_exceptions.py
from gdb.domain.account import Account
from gdb.exceptions import (
    AccountException,
    InvalidAmountException,
    InsufficientBalanceException,
    InactiveAccountException
)

def main():
    print("=== Activity 5: Custom Exceptions Test ===")
    acc = Account("ACC101", "Alice", 25, 5000.0, "Savings", "Active", "1234")
    
    # Valid Withdrawal
    acc.withdraw(1000.0)
    print(f"Successful withdrawal completed: Rs 1000.0 | New Balance: Rs {acc.balance}")
    
    # Invalid Amount
    try:
        acc.deposit(-100.0)
    except InvalidAmountException as e:
        print(f"PASS: Caught InvalidAmountException -> {e}")
        
    # Insufficient Balance
    try:
        acc.withdraw(99999.0)
    except InsufficientBalanceException as e:
        print(f"PASS: Caught InsufficientBalanceException -> {e}")

if __name__ == "__main__":
    main()
