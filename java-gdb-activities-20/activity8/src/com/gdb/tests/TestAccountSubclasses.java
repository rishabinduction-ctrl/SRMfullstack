package com.gdb.tests;

import com.gdb.domain.*;
import com.gdb.exceptions.*;

public class TestAccountSubclasses {
    public static void main(String[] args) {
        System.out.println("=== Activity 8: Polymorphism Test ===");

        // NOTE: The domain classes in src/com/gdb/domain are provided complete (the Activity 7 subclasses plus
        // their overridden withdraw() methods). Declare each account with the parent type Account so that the
        // overridden withdraw() is chosen at runtime (dynamic method dispatch).

        // TODO: Step 1 - Test SavingsAccount minimum balance breach
        //   Create a SavingsAccount (balance 10000.0, minBalance 1000.0), withdraw 9500.0 with the correct PIN,
        //   catch MinimumBalanceViolationException and print [PASS]; print [FAIL] for any other outcome.

        // TODO: Step 2 - Test CurrentAccount valid withdrawal utilizing overdraft facility
        //   Create a CurrentAccount (balance 5000.0, overdraftLimit 25000.0), withdraw 10000.0 with the correct PIN,
        //   verify it succeeds (balance goes to -5000.0) and print [PASS].

        // TODO: Step 3 - Test CurrentAccount exceeding overdraft limit
        //   On the same account, withdraw 30000.0, catch InsufficientBalanceException and print [PASS].

        // TODO: Step 4 - Test FixedDepositAccount premature withdrawal block
        //   Create a FixedDepositAccount, attempt any withdrawal, catch AccountException and print [PASS].

        System.out.println("=== Complete Activity 8 polymorphism tests and verify output ===");
    }
}
