package com.gdb.tests;

import com.gdb.domain.AccountRulesEngine;

public class TestAccountRulesEngine {
    public static void main(String[] args) {
        System.out.println("=== Activity 13.1: Hardcoded Rules Engine Test ===");
        int[] tenures = { 0, 2, 4, 6 };
        for (int t : tenures) {
            double minBal = AccountRulesEngine.getSavingsMinBalance(t);
            double rate = AccountRulesEngine.getSavingsInterestRate(t);
            System.out.println("Tenure " + t + " yrs -> Min Balance: Rs " + minBal + " | Interest: " + rate + "%");
        }
        System.out.println("Rules Engine lookup completed successfully!");
    }
}
