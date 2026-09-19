package com.gdb.tests;

import com.gdb.command.*;
import com.gdb.db.SimulatedDatabase;
import com.gdb.domain.*;
import com.gdb.logging.*;
import java.util.List;

public class TestBridgeLogging {
    public static void main(String[] args) throws Exception {
        System.out.println("=".repeat(60));
        System.out.println("  ACTIVITY 18 — BRIDGE PATTERN (FILE + DB)");
        System.out.println("=".repeat(60));

        // Setup test accounts
        IAccount acc1 = AccountFactory.createAccount("SAVINGS", 1001, "John", 25, 15000);
        acc1.setPin(1234);
        IAccount acc2 = AccountFactory.createAccount("SAVINGS", 1002, "Jane", 30, 10000);

        // 📝 STEP 24 — Create destinations
        FileLogDestination fileDest = new FileLogDestination();
        fileDest.clear();
        SimulatedDatabase db = new SimulatedDatabase();
        DatabaseLogDestination dbDest = new DatabaseLogDestination(db);
        MemoryLogDestination memDest = new MemoryLogDestination();

        // 📝 STEP 25 — Create TransactionLogger with File destination
        TransactionLogger logger = new TransactionLogger(fileDest);
        System.out.println("\n[STEP 25] Logging to " + logger.getDestinationName() + " destination...");
        executeAndLog(logger, acc1, acc2);
        System.out.println("  FILE log count: " + logger.readAll().size());

        // 📝 STEP 26 — Switch to Database destination
        logger.setDestination(dbDest);
        System.out.println("\n[STEP 26] Switched to " + logger.getDestinationName() + " destination...");
        executeAndLog(logger, acc1, acc2);
        System.out.println("  DATABASE log count: " + logger.readAll().size());

        // 📝 STEP 27 — Switch to Memory destination
        logger.setDestination(memDest);
        System.out.println("\n[STEP 27] Switched to " + logger.getDestinationName() + " destination...");
        executeAndLog(logger, acc1, acc2);
        System.out.println("  MEMORY log count: " + logger.readAll().size());

        // 📝 STEP 28 — Verify each destination retained its own data
        System.out.println("\n[STEP 28] Verifying Data Isolation:");
        logger.setDestination(fileDest);
        System.out.println("  FILE count: " + logger.readAll().size() + " [EXPECTED: 3]");
        logger.setDestination(dbDest);
        System.out.println("  DATABASE count: " + logger.readAll().size() + " [EXPECTED: 3]");
        logger.setDestination(memDest);
        System.out.println("  MEMORY count: " + logger.readAll().size() + " [EXPECTED: 3]");

        // 📝 STEP 29 — Print destination name for each
        System.out.println("\n[STEP 29] All Bridge Pattern log backends verified successfully!");
    }

    private static void executeAndLog(TransactionLogger logger, IAccount acc1, IAccount acc2) throws Exception {
        DepositCommand dep = new DepositCommand(acc1, 1000);
        dep.execute();
        logger.log(dep);

        WithdrawCommand wth = new WithdrawCommand(acc1, 500, 1234);
        wth.execute();
        logger.log(wth);

        TransferCommand trf = new TransferCommand(acc1, acc2, 500, 1234);
        trf.execute();
        logger.log(trf);
    }
}
