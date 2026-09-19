package com.gdb.logging;

import com.gdb.command.TransactionCommand;
import java.util.Collections;
import java.util.List;

/**
 * Bridge abstraction class decoupling high-level logger API from pluggable storage backends.
 */
public class TransactionLogger {
    protected LogDestination destination;

    public TransactionLogger(LogDestination destination) {
        this.destination = destination;
    }

    public void setDestination(LogDestination destination) {
        this.destination = destination;
    }

    public void log(TransactionCommand cmd) {
        if (destination != null) {
            destination.write(cmd);
        }
    }

    public List<TransactionCommand> readAll() {
        if (destination != null) {
            return destination.readAll();
        }
        return Collections.emptyList();
    }

    public void clear() {
        if (destination != null) {
            destination.clear();
        }
    }

    public String getDestinationName() {
        return destination != null ? destination.getDestinationName() : "UNKNOWN";
    }
}
