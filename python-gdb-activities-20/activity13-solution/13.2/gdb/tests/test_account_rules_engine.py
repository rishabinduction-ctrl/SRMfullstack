# gdb/tests/test_account_rules_engine.py
from gdb.domain.account_rules_engine import AccountRulesEngine

def main():
    print("=== Activity 13.2: Dynamic Account Rules Test ===")
    assert AccountRulesEngine.get_minimum_balance("SAVINGS") == 1000.0
    assert AccountRulesEngine.get_interest_rate("SAVINGS") == 4.0
    assert AccountRulesEngine.get_overdraft_limit("CURRENT") == 10000.0
    assert AccountRulesEngine.get_interest_rate("FIXEDDEPOSIT") == 6.5
    print("Dynamic rule integration verified!")

if __name__ == "__main__":
    main()
