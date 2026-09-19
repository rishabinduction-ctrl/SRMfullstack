package com.gdb;

import com.gdb.domain.IAccount;
import com.gdb.logging.FileLogDestination;
import com.gdb.logging.LogDestination;
import com.gdb.logging.TransactionLogger;
import com.gdb.service.AccountService;

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Global Digital Bank — Service Demo");
        System.out.println("=".repeat(60));

        // 📝 STEP 20 — Wire up dependencies
        LogDestination dest = new FileLogDestination();
        dest.clear();
        TransactionLogger logger = new TransactionLogger(dest);
        AccountService service = new AccountService(logger);

        // 📝 STEP 21 — Run a demo workflow
        IAccount acc1 = service.openAccount("SAVINGS", "Rajesh Sharma", 30, 25000);
        acc1.setPin(1234);
        IAccount acc2 = service.openAccount("SAVINGS", "Priya Patel", 28, 15000);
        acc2.setPin(5678);

        service.deposit(acc1.getAccountNumber(), 5000);
        service.withdraw(acc1.getAccountNumber(), 2000, 1234);
        service.transfer(acc1.getAccountNumber(), acc2.getAccountNumber(), 3000, 1234);

        System.out.println("Account #1001 balance: Rs. " + acc1.getBalance());
        System.out.println("Account #1002 balance: Rs. " + acc2.getBalance());
        System.out.println("Total logged transactions: " + service.getTransactionHistory().size());
    }
}
