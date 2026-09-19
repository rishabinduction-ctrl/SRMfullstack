package com.gdb.logging;

import com.gdb.command.TransactionCommand;
import java.util.List;

/**
 * Implementor interface for Bridge Pattern decoupling transaction log storage backends.
 */
public interface LogDestination {
    void write(TransactionCommand cmd);
    List<TransactionCommand> readAll();
    void clear();
    String getDestinationName();
}
