# gdb/tests/test_account.py
from gdb.domain.account import Account

def main():
    print("=== Activity 3: Enhanced Account Test ===")
    acc = Account("ACC2001", "Bob", 30, 5000.0, "Savings", "Active", "1234")
    
    print(f"PIN '1234' validation: {acc.validate_pin('1234')}")
    print(f"PIN '9999' validation: {acc.validate_pin('9999')}")
    
    acc.deposit(1000.0)
    print(f"Deposit on active account: Balance = Rs {acc.balance}")
    
    acc.withdraw(3000.0)
    print(f"Withdraw with new PIN: SUCCESS | Balance: Rs {acc.balance}")

if __name__ == "__main__":
    main()
