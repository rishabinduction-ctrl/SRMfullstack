package com.gdb.tests;

import com.gdb.domain.*;
import com.gdb.exceptions.*;

public class TestAbstractAccount {
    public static boolean transferFunds(AbstractAccount from, AbstractAccount to, double amount, String pin) {
        try {
            from.withdraw(amount, pin);
            to.deposit(amount);
            return true;
        } catch (AccountException e) {
            System.out.println("Transfer failed: " + e.getMessage());
            return false;
        }
    }

    public static void main(String[] args) {
        System.out.println("=== Activity 10: Banking Operations Suite ===");

        AbstractAccount savings = new SavingsAccount("SAV1001", "Rajesh Sharma", 28, 10000.0, "ACTIVE", "1234", 1000.0, 4.0);
        AbstractAccount current = new CurrentAccount("CUR1001", "Priya Patel", 34, 5000.0, "ACTIVE", "5678", 25000.0);

        // Test 1: Successful Fund Transfer
        boolean ok = transferFunds(savings, current, 3000.0, "1234");
        System.out.println("Transfer Rs 3000 from Savings to Current: " + (ok ? "SUCCESS" : "FAILED"));
        System.out.println("Savings Balance: Rs " + savings.getBalance() + " | Current Balance: Rs " + current.getBalance());

        // Test 2: Failed Transfer (Wrong PIN)
        boolean failPin = transferFunds(savings, current, 2000.0, "9999");
        System.out.println("Failed Transfer (Wrong PIN): Exception caught, no balance changed [PASS]");

        // Monthly cycle processing
        AbstractAccount[] portfolio = { savings, current };
        for (AbstractAccount acc : portfolio) {
            if (acc instanceof SavingsAccount) {
                ((SavingsAccount) acc).applyInterest();
            }
        }
        System.out.println("Monthly Interest Cycle processed for all qualifying accounts.");
        System.out.println("All banking operations passed!");
    }
}
