package com.gdb.tests;

import com.gdb.domain.Account;

public class TestAccount {
    public static void main(String[] args) {
        System.out.println("=== Activity 1: Basic Account Test ===");
        Account acc = new Account("ACC1001", "Rajesh Sharma", 28, 5000.0, "SAVINGS", "ACTIVE");
        acc.displayAccountInfo();

        boolean depOk = acc.deposit(2000.0);
        System.out.println("Deposit 2000: " + (depOk ? "SUCCESS" : "FAILED") + " | Balance: Rs " + acc.getBalance());

        boolean withOk = acc.withdraw(3000.0);
        System.out.println("Withdraw 3000: " + (withOk ? "SUCCESS" : "FAILED") + " | Balance: Rs " + acc.getBalance());

        boolean failWith = acc.withdraw(10000.0);
        System.out.println("Withdraw 10000 (exceeds balance): " + (failWith ? "SUCCESS" : "FAILED") + " | Balance: Rs " + acc.getBalance());
    }
}
