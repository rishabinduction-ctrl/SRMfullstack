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

        // ============================================================
        // 📝 STEP 24: Create Destinations
        //
        // INSTRUCTIONS:
        //   1. fileDest = new FileLogDestination(); fileDest.clear();
        //   2. db = new SimulatedDatabase();
        //   3. dbDest = new DatabaseLogDestination(db);
        //   4. memDest = new MemoryLogDestination();
        // ============================================================
        // TODO: instantiate all log destinations

        // ============================================================
        // 📝 STEP 25: Create TransactionLogger with File Destination
        //
        // INSTRUCTIONS:
        //   1. logger = new TransactionLogger(fileDest);
        //   2. Execute and log 3 commands (Deposit, Withdraw, Transfer).
        //   3. Print count from logger.readAll().
        // ============================================================
        // TODO: log transactions to FILE destination

        // ============================================================
        // 📝 STEP 26: Switch to Database Destination
        //
        // INSTRUCTIONS:
        //   1. logger.setDestination(dbDest);
        //   2. Execute and log 3 commands.
        //   3. Print count from logger.readAll().
        // ============================================================
        // TODO: log transactions to DATABASE destination

        // ============================================================
        // 📝 STEP 27: Switch to Memory Destination
        //
        // INSTRUCTIONS:
        //   1. logger.setDestination(memDest);
        //   2. Execute and log 3 commands.
        //   3. Print count from logger.readAll().
        // ============================================================
        // TODO: log transactions to MEMORY destination

        // ============================================================
        // 📝 STEP 28: Verify Data Isolation Across Backends
        //
        // INSTRUCTIONS:
        //   1. logger.setDestination(fileDest); print count (should be 3).
        //   2. logger.setDestination(dbDest); print count (should be 3).
        //   3. logger.setDestination(memDest); print count (should be 3).
        // ============================================================
        // TODO: verify each backend maintained its independent data store

        // ============================================================
        // 📝 STEP 29: Print Destination Names
        //
        // INSTRUCTIONS:
        //   Print getDestinationName() for each backend.
        // ============================================================
        // TODO: display active backend names
    }
}
