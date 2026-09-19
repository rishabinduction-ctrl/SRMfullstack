package com.gdb.tests;

import com.gdb.domain.Account;

public class TestAccount {
    public static void main(String[] args) {
        System.out.println("=== Activity 3: Enhanced Account Test ===");
        Account acc = new Account("ACC1001", "Rajesh Sharma", 28, 5000.0, "SAVINGS", "ACTIVE", "1234");
        System.out.println("Initial Balance: Rs " + acc.getBalance() + " | Status: " + acc.getStatus());

        boolean ok = acc.withdraw(1000.0, "1234");
        System.out.println("Withdraw with correct PIN: " + (ok ? "SUCCESS" : "FAILED") + " | Balance: Rs " + acc.getBalance());

        boolean failPin = acc.withdraw(1000.0, "9999");
        System.out.println("Withdraw with wrong PIN: " + (failPin ? "SUCCESS" : "FAILED") + " | Balance: Rs " + acc.getBalance());

        acc.suspend();
        System.out.println("Account Suspended.");
        boolean failSuspended = acc.withdraw(1000.0, "1234");
        System.out.println("Withdraw on SUSPENDED account: " + (failSuspended ? "SUCCESS" : "FAILED") + " | Balance: Rs " + acc.getBalance());

        acc.activate();
        System.out.println("Account Re-Activated.");

        boolean pinChanged = acc.changePin("1234", "5678");
        if (pinChanged) {
            System.out.println("PIN Changed Successfully.");
        }

        boolean newPinOk = acc.withdraw(1000.0, "5678");
        System.out.println("Withdraw with new PIN: " + (newPinOk ? "SUCCESS" : "FAILED") + " | Balance: Rs " + acc.getBalance());
    }
}
