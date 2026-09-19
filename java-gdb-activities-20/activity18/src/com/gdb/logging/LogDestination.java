package com.gdb.logging;

import com.gdb.command.TransactionCommand;
import java.util.List;

/**
 * Implementor interface for Bridge Pattern decoupling transaction log storage backends.
 */
public interface LogDestination {
    // ============================================================
    // 📝 STEP 1: Add write(TransactionCommand cmd)
    // ============================================================
    // TODO: declare write method
    void write(TransactionCommand cmd);

    // ============================================================
    // 📝 STEP 2: Add readAll()
    // ============================================================
    // TODO: declare readAll method returning List<TransactionCommand>
    List<TransactionCommand> readAll();

    // ============================================================
    // 📝 STEP 3: Add clear()
    // ============================================================
    // TODO: declare clear method
    void clear();

    // ============================================================
    // 📝 STEP 4: Add getDestinationName()
    // ============================================================
    // TODO: declare getDestinationName method returning String
    String getDestinationName();
}
