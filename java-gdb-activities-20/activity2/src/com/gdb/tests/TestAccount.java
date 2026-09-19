package com.gdb.tests;

import com.gdb.domain.Account;

public class TestAccount {
    public static void main(String[] args) {
        System.out.println("=== Activity 2: Test Account Suite ===");

        // NOTE: If you completed Activity 1 successfully, paste your working Account.java code into com.gdb.domain.

        Account acc = new Account("ACC1001", "Rajesh Sharma", 28, 5000.0, "SAVINGS", "ACTIVE");

        // TODO: Step 1 - Test Initial Balance (Assert balance == 5000.0)

        // TODO: Step 2 - Test Valid Deposit (Deposit 2000.0 -> Assert balance == 7000.0)

        // TODO: Step 3 - Test Negative Deposit (Deposit -500.0 -> Assert returns false and balance stays 7000.0)

        // TODO: Step 4 - Test Valid Withdrawal (Withdraw 3000.0 -> Assert balance == 4000.0)

        // TODO: Step 5 - Test Exceeding Withdrawal (Withdraw 10000.0 -> Assert returns false and balance stays 4000.0)

        // TODO: Step 6 - Test Negative Withdrawal (Withdraw -100.0 -> Assert returns false and balance stays 4000.0)

        System.out.println("=== Complete Activity 2 unit tests and verify output ===");
    }
}
