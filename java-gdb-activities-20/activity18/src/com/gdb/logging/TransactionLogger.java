package com.gdb.logging;

import com.gdb.command.TransactionCommand;
import java.util.ArrayList;
import java.util.List;

/**
 * Bridge abstraction class decoupling high-level logger API from pluggable storage backends.
 */
public class TransactionLogger {
    // ============================================================
    // 📝 STEP 17: Declare Field
    // ============================================================
    // TODO: declare protected LogDestination destination;

    // ============================================================
    // 📝 STEP 18: Constructor
    // ============================================================
    // TODO: implement constructor accepting LogDestination
    public TransactionLogger(LogDestination destination) {
        // TODO: Step 18 - implement constructor
    }

    // ============================================================
    // 📝 STEP 19: setDestination
    // ============================================================
    // TODO: implement setter for hot-swapping destination
    public void setDestination(LogDestination destination) {
        // TODO: Step 19 - implement setter
    }

    // ============================================================
    // 📝 STEP 20: log(TransactionCommand cmd)
    // ============================================================
    // TODO: delegate to destination.write(cmd)
    public void log(TransactionCommand cmd) {
        // TODO: Step 20 - delegate to destination.write(cmd)
    }

    // ============================================================
    // 📝 STEP 21: readAll()
    // ============================================================
    // TODO: delegate to destination.readAll()
    public List<TransactionCommand> readAll() {
        // TODO: Step 21 - delegate to destination.readAll()
        return new ArrayList<>();
    }

    // ============================================================
    // 📝 STEP 22: clear()
    // ============================================================
    // TODO: delegate to destination.clear()
    public void clear() {
        // TODO: Step 22 - delegate to destination.clear()
    }

    // ============================================================
    // 📝 STEP 23: getDestinationName()
    // ============================================================
    // TODO: delegate to destination.getDestinationName()
    public String getDestinationName() {
        // TODO: Step 23 - delegate to destination.getDestinationName()
        return "";
    }
}
