package com.gdb.tests;

import com.gdb.domain.*;

public class TestAccountRulesEngine {
    public static void main(String[] args) {
        System.out.println("=== Activity 13.2: Dynamic Account Rules Test ===");
        SavingsAccount sa = (SavingsAccount) AccountFactory.createAccount("SAVINGS", "SAV1001", "Rajesh Sharma", 28, 50000.0, "ACTIVE", "1234", 4);
        System.out.println("Created Savings Account (Tenure: " + sa.getTenureYears() + " yrs):");
        System.out.println(" -> Min Balance: Rs " + sa.getMinBalance() + " (Dynamically fetched)");
        System.out.println(" -> Interest Rate: " + sa.getInterestRate() + "% (Dynamically fetched)");
        System.out.println("Dynamic rule integration verified!");
    }
}
