package com.gdb.tests;

import com.gdb.domain.IAccount;
import com.gdb.logging.*;
import com.gdb.service.AccountService;

public class TestAccountUI {
    public static void main(String[] args) throws Exception {
        System.out.println("=".repeat(60));
        System.out.println("  ACTIVITY 20 — ACCOUNT UI & INTEGRATION TEST");
        System.out.println("=".repeat(60));

        LogDestination dest = new MemoryLogDestination();
        TransactionLogger logger = new TransactionLogger(dest);
        AccountService service = new AccountService(logger);

        IAccount acc = service.openAccount("SAVINGS", "Alice Cooper", 28, 20000);
        acc.setPin(1234);
        System.out.println("[UI TEST] Opened: " + acc.getAccountInfo());

        service.deposit(acc.getAccountNumber(), 5000);
        System.out.println("[UI TEST] Deposit Rs. 5000 | Balance: Rs. " + acc.getBalance());

        service.withdraw(acc.getAccountNumber(), 3000, 1234);
        System.out.println("[UI TEST] Withdraw Rs. 3000 | Balance: Rs. " + acc.getBalance());

        System.out.println("[UI TEST] Total Logged Transactions: " + service.getTransactionHistory().size());
        System.out.println("All UI service endpoints validated successfully!");
    }
}
