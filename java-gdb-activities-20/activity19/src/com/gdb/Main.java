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

        // ============================================================
        // 📝 STEP 20: Wire Up Dependencies
        //
        // INSTRUCTIONS:
        //   1. LogDestination dest = new FileLogDestination();
        //   2. TransactionLogger logger = new TransactionLogger(dest);
        //   3. AccountService service = new AccountService(logger);
        // ============================================================
        // TODO: instantiate FileLogDestination, TransactionLogger, and AccountService

        // ============================================================
        // 📝 STEP 21: Run A Demo Workflow
        //
        // INSTRUCTIONS:
        //   1. Open accounts, set PINs, perform deposit, withdraw, transfer.
        //   2. Print balances and transaction history.
        // ============================================================
        // TODO: execute demo workflow through AccountService
    }
}
