package com.gdb;

import com.gdb.logging.FileLogDestination;
import com.gdb.logging.LogDestination;
import com.gdb.logging.TransactionLogger;
import com.gdb.service.AccountService;
import com.gdb.ui.AccountUI;

public class Main {
    public static void main(String[] args) {
        System.out.println("Booting Global Digital Bank...");

        // ============================================================
        // 📝 STEP 15: Wire Up Dependencies and Start UI
        //
        // INSTRUCTIONS:
        //   1. LogDestination destination = new FileLogDestination();
        //   2. TransactionLogger logger = new TransactionLogger(destination);
        //   3. AccountService service = new AccountService(logger);
        //   4. AccountUI ui = new AccountUI(service);
        //   5. ui.start();
        // ============================================================
        // TODO: initialize dependencies and launch AccountUI console app
    }
}
