# gdb/tests/test_account.py
from gdb.domain.account import Account

def main():
    print("=== Activity 1: Basic Account Test ===")
    acc = Account("ACC1001", "Alice", 25, 5000.0, "Savings", "Active")
    acc.display_account_info()
    
    print("\nDepositing Rs 1500.0...")
    if acc.deposit(1500.0):
        print(f"Deposit Successful! Current Balance: Rs {acc.balance}")
        
    print("\nWithdrawing Rs 2000.0...")
    if acc.withdraw(2000.0):
        print(f"Withdrawal Successful! Current Balance: Rs {acc.balance}")
        
    print("\nWithdrawing Rs 10000.0 (exceeds balance)...")
    if not acc.withdraw(10000.0):
        print(f"Withdraw 10000 (exceeds balance): FAILED | Balance: Rs {acc.balance}")

if __name__ == "__main__":
    main()
