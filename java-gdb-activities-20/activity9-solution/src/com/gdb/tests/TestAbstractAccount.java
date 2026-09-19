package com.gdb.tests;

import com.gdb.domain.*;
import com.gdb.exceptions.*;

public class TestAbstractAccount {
    public static void main(String[] args) {
        System.out.println("=== Activity 9: Abstract Account & Template Pattern ===");

        AbstractAccount sa = new SavingsAccount("SAV1001", "Rajesh Sharma", 28, 10000.0, "ACTIVE", "1234", 1000.0, 4.0);
        try {
            sa.withdraw(2000.0, "1234");
            System.out.println("[Savings] Withdraw 2000: SUCCESS | Balance: Rs " + sa.getBalance());
        } catch (AccountException e) {
            System.out.println("[Savings] [FAIL]");
        }

        try {
            sa.withdraw(8000.0, "1234");
            System.out.println("[Savings] [FAIL]");
        } catch (MinimumBalanceViolationException e) {
            System.out.println("[Savings] Withdraw below min balance: Caught MinimumBalanceViolationException [PASS]");
        } catch (AccountException e) {
            System.out.println("[Savings] [FAIL]");
        }

        AbstractAccount ca = new CurrentAccount("CUR1001", "Priya Patel", 34, 2000.0, "ACTIVE", "5678", 10000.0);
        try {
            ca.withdraw(5000.0, "5678");
            System.out.println("[Current] Overdraft debit: SUCCESS | Balance: Rs " + ca.getBalance());
        } catch (AccountException e) {
            System.out.println("[Current] [FAIL]");
        }

        AbstractAccount fda = new FixedDepositAccount("FD1001", "Amit Kumar", 45, 50000.0, "ACTIVE", "1111", 12, 6.5);
        try {
            fda.withdraw(5000.0, "1111");
            System.out.println("[FixedDeposit] [FAIL]");
        } catch (AccountException e) {
            System.out.println("[FixedDeposit] Premature debit: Caught AccountException [PASS]");
        }

        System.out.println("Template method pattern executed successfully!");
    }
}
