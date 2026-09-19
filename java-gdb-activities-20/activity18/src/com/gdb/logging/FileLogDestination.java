package com.gdb.logging;

import com.gdb.command.TransactionCommand;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class FileLogDestination implements LogDestination {
    // ============================================================
    // 📝 STEP 5: Declare Field
    // ============================================================
    // TODO: declare private TransactionLog log;

    // ============================================================
    // 📝 STEP 6: Constructor
    // ============================================================
    // TODO: initialize log = new TransactionLog()
    public FileLogDestination() {
        // TODO: Step 6 - initialize log = new TransactionLog()
    }

    // ============================================================
    // 📝 STEP 7: write(cmd)
    // ============================================================
    // TODO: delegate to log.log(cmd)
    @Override
    public void write(TransactionCommand cmd) {
        // TODO: Step 7 - delegate to log.log(cmd)
    }

    // ============================================================
    // 📝 STEP 8: readAll()
    // ============================================================
    // TODO: delegate to log.readAll()
    @Override
    public List<TransactionCommand> readAll() {
        // TODO: Step 8 - delegate to log.readAll()
        return new ArrayList<>();
    }

    // ============================================================
    // 📝 STEP 9: clear()
    // ============================================================
    // TODO: delegate to log.clear()
    @Override
    public void clear() {
        // TODO: Step 9 - delegate to log.clear()
    }

    // ============================================================
    // 📝 STEP 10: getDestinationName()
    // ============================================================
    // TODO: return "FILE"
    @Override
    public String getDestinationName() {
        // TODO: Step 10 - return "FILE"
        return "";
    }
}
