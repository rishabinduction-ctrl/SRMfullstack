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

        // ============================================================
        // 📝 STEP 10: Deposit with Transaction
        //
        // INSTRUCTIONS:
        //   1. Create acc1 (Savings, 1001, "Rajesh Sharma", 30, 50000) and set PIN 1234.
        //   2. Call acc1.depositWithTransaction(5000).
        //   3. Print the returned Transaction object.
        // ============================================================
        // TODO: perform depositWithTransaction and print the returned Transaction

        // ============================================================
        // 📝 STEP 11: Withdraw with Transaction
        //
        // INSTRUCTIONS:
        //   1. Call acc1.withdrawWithTransaction(2000, 1234).
        //   2. Print the returned Transaction object.
        // ============================================================
        // TODO: perform withdrawWithTransaction and print the returned Transaction

        // ============================================================
        // 📝 STEP 12: Transfer with Transaction
        //
        // INSTRUCTIONS:
        //   1. Create acc2 (Savings, 1002, "Priya Patel", 28, 20000).
        //   2. Call svc.transferWithTransaction(acc1, acc2, 1000, 1234).
        //   3. Print the returned Transaction object.
        // ============================================================
        // TODO: perform transferWithTransaction and print the returned Transaction

        // ============================================================
        // 📝 STEP 13: Backward Compatibility Check
        //
        // INSTRUCTIONS:
        //   1. Call acc1.deposit(1000) using the legacy void method.
        //   2. Print acc1.getAccountInfo() showing updated balance.
        // ============================================================
        // TODO: call legacy deposit(1000) and verify account balance
    }
}
