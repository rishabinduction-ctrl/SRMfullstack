package com.gdb.domain;

import java.util.HashMap;
import java.util.Map;

public class AccountRulesEngine {
    private static final Map<String, Double> SAVINGS_MIN_BALANCES = new HashMap<>();
    private static final Map<String, Double> SAVINGS_INTEREST_RATES = new HashMap<>();

    static {
        SAVINGS_MIN_BALANCES.put("NEW", 10000.0);
        SAVINGS_MIN_BALANCES.put("STANDARD", 7500.0);
        SAVINGS_MIN_BALANCES.put("PREMIUM", 5000.0);
        SAVINGS_MIN_BALANCES.put("PRIVILEGE", 2500.0);

        SAVINGS_INTEREST_RATES.put("NEW", 2.70);
        SAVINGS_INTEREST_RATES.put("STANDARD", 3.00);
        SAVINGS_INTEREST_RATES.put("PREMIUM", 3.50);
        SAVINGS_INTEREST_RATES.put("PRIVILEGE", 4.00);
    }

    public static String getSavingsBucket(int tenureYears) {
        if (tenureYears >= 5) return "PRIVILEGE";
        if (tenureYears >= 3) return "PREMIUM";
        if (tenureYears >= 1) return "STANDARD";
        return "NEW";
    }

    public static double getSavingsMinBalance(int tenureYears) {
        String bucket = getSavingsBucket(tenureYears);
        return SAVINGS_MIN_BALANCES.getOrDefault(bucket, 10000.0);
    }

    public static double getSavingsInterestRate(int tenureYears) {
        String bucket = getSavingsBucket(tenureYears);
        return SAVINGS_INTEREST_RATES.getOrDefault(bucket, 2.70);
    }

    public static double getCurrentOverdraftLimit(double monthlyTurnover) {
        return Math.max(25000.0, monthlyTurnover * 2.5);
    }

    public static double getFDInterestRate(int months) {
        if (months >= 36) return 7.50;
        if (months >= 12) return 6.50;
        return 5.00;
    }
}
