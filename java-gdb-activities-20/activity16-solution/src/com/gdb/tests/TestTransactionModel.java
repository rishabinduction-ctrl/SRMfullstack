package com.gdb.tests;

import com.gdb.domain.*;
import com.gdb.service.TransferService;
import com.gdb.exceptions.*;

public class TestTransactionModel {
    public static void main(String[] args) throws Exception {
        System.out.println("=".repeat(60));
        System.out.println("  ACTIVITY 16 — TRANSACTION MODEL TEST");
        System.out.println("=".repeat(60));

        TransferService svc = new TransferService();

        // 📝 STEP 10: Deposit with Transaction
        Account acc1 = (Account) AccountFactory.createAccount("SAVINGS", 1001, "Rajesh Sharma", 30, 50000);
        acc1.setPin(1234);
        Transaction t1 = acc1.depositWithTransaction(5000);
        System.out.println("[STEP 10] Deposit Transaction: " + t1);

        // 📝 STEP 11: Withdraw with Transaction
        Transaction t2 = acc1.withdrawWithTransaction(2000, 1234);
        System.out.println("[STEP 11] Withdrawal Transaction: " + t2);

        // 📝 STEP 12: Transfer with Transaction
        Account acc2 = (Account) AccountFactory.createAccount("SAVINGS", 1002, "Priya Patel", 28, 20000);
        Transaction t3 = svc.transferWithTransaction(acc1, acc2, 1000, 1234);
        System.out.println("[STEP 12] Transfer Transaction: " + t3);

        // 📝 STEP 13: Backward Compatibility Check
        acc1.deposit(1000);
        System.out.println("[STEP 13] Legacy Deposit +1000: " + acc1.getAccountInfo());
    }
}
