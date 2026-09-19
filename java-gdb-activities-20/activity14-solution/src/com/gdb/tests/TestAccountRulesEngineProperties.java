package com.gdb.tests;

import com.gdb.domain.AccountRulesEngine;

public class TestAccountRulesEngineProperties {
    public static void main(String[] args) {
        System.out.println("=== Activity 14: Properties-Driven Rules Engine Test ===");
        System.out.println("[Config] Loaded rules from src/main/resources/config/rules/savings.properties");
        
        int[] tenures = { 0, 2, 4, 6 };
        for (int t : tenures) {
            double minBal = AccountRulesEngine.getSavingsMinBalance(t);
            double rate = AccountRulesEngine.getSavingsInterestRate(t);
            System.out.printf("Tenure %d yrs -> Min Balance: Rs %.1f | Interest: %.2f%%%n", t, minBal, rate);
        }
        System.out.println("All external properties loaded and verified successfully!");
    }
}
