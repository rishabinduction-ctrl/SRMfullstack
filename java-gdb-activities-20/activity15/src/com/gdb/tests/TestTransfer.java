package com.gdb.tests;

import com.gdb.domain.*;
import com.gdb.service.TransferService;
import com.gdb.exceptions.*;

public class TestTransfer {
    public static void main(String[] args) throws Exception {
        System.out.println("=".repeat(60));
        System.out.println("  ACTIVITY 15 — TRANSFER WITH DAILY LIMITS");
        System.out.println("=".repeat(60));

        TransferService svc = new TransferService();
        AccountRulesEngine engine = AccountRulesEngine.getInstance();

        // ============================================================
        // 📝 STEP 9: Create Two Accounts And Set PIN
        //
        // INSTRUCTIONS:
        //   1. Create acc1 = (Account) AccountFactory.createAccount("SAVINGS", 1001, "Rajesh Sharma", 30, 100000).
        //   2. Create acc2 = (Account) AccountFactory.createAccount("SAVINGS", 1002, "Priya Patel", 28, 20000).
        //   3. Call acc1.setPin(1234).
        //
        // HINT: Declare both as Account (not IAccount) so you can call the daily-limit methods later.
        // ============================================================
        // TODO: create acc1 and acc2 with AccountFactory and set PIN 1234 on acc1

        // ============================================================
        // 📝 STEP 10: Successful Transfer
        //
        // INSTRUCTIONS:
        //   1. Call svc.transfer(acc1, acc2, 5000, 1234).
        //   2. Print both balances, e.g. "Transfer Rs. 5,000: SUCCESS | acc1 = Rs. 95000.0 | acc2 = Rs. 25000.0".
        // ============================================================
        // TODO: transfer Rs. 5,000 from acc1 to acc2 and print both balances

        // ============================================================
        // 📝 STEP 11: Insufficient Balance
        //
        // INSTRUCTIONS:
        //   1. Inside a try block, transfer 1_00_000 from acc1 to acc2.
        //   2. Catch InsufficientBalanceException and print its message.
        //
        // HINT: acc1 must keep its Rs. 10,000 minimum balance, so only Rs. 85,000 can leave it.
        // ============================================================
        // TODO: attempt a Rs. 1,00,000 transfer and catch InsufficientBalanceException

        // ============================================================
        // 📝 STEP 12: Daily Limit Breach
        //
        // INSTRUCTIONS:
        //   1. Print acc1.getDailyTransferLimit() (Rs. 50,000 for a NEW Savings account).
        //   2. In a loop, transfer Rs. 20,000 from acc1 to acc2 and print each success.
        //   3. Stop when an AccountException is thrown; print its message.
        //
        // HINT: Rs. 5,000 is already used today, so the third Rs. 20,000 transfer crosses the limit.
        // ============================================================
        // TODO: transfer repeatedly until the daily limit is breached, then catch and print the exception

        // ============================================================
        // 📝 STEP 13: Print Remaining Limit
        //
        // INSTRUCTIONS:
        //   1. Print acc1.getDailyTransferTotal() and acc1.getRemainingDailyTransferLimit().
        //
        // HINT: Total used + remaining should add up to the daily limit.
        // ============================================================
        // TODO: print acc1.getRemainingDailyTransferLimit()
    }
}
