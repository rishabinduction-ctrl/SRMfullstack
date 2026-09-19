package com.gdb.logging;

import com.gdb.command.TransactionCommand;
import com.gdb.db.SimulatedDatabase;
import java.util.*;

public class DatabaseLogDestination implements LogDestination {
    private static final String TABLE = "transaction_log";

    // ============================================================
    // 📝 STEP 11: Declare Field
    // ============================================================
    // TODO: declare private final SimulatedDatabase db;

    // ============================================================
    // 📝 STEP 12: Constructor
    // ============================================================
    // TODO: implement constructor accepting SimulatedDatabase
    public DatabaseLogDestination(SimulatedDatabase db) {
        // TODO: Step 12 - implement constructor
    }

    // ============================================================
    // 📝 STEP 13: write(cmd)
    // ============================================================
    // TODO: insert command into database table
    @Override
    public void write(TransactionCommand cmd) {
        // TODO: Step 13 - insert command into database table
    }

    // ============================================================
    // 📝 STEP 14: readAll()
    //
    // INSTRUCTIONS:
    //   1. Call db.selectAll(TABLE).
    //   2. Map/cast each Object to TransactionCommand.
    //   3. Collect and return List<TransactionCommand>.
    // ============================================================
    // TODO: retrieve and return all commands from database
    @Override
    public List<TransactionCommand> readAll() {
        // TODO: Step 14 - retrieve and return all commands from database
        return new ArrayList<>();
    }

    // ============================================================
    // 📝 STEP 15: clear()
    // ============================================================
    // TODO: delete all records from database table
    @Override
    public void clear() {
        // TODO: Step 15 - delete all records from database table
    }

    // ============================================================
    // 📝 STEP 16: getDestinationName()
    // ============================================================
    // TODO: return "DATABASE"
    @Override
    public String getDestinationName() {
        // TODO: Step 16 - return "DATABASE"
        return "";
    }
}
