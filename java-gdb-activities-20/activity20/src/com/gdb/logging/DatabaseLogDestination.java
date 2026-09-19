package com.gdb.logging;

import com.gdb.command.TransactionCommand;
import com.gdb.db.SimulatedDatabase;
import java.util.*;
import java.util.stream.Collectors;

public class DatabaseLogDestination implements LogDestination {
    private static final String TABLE = "transaction_log";

    private final SimulatedDatabase db;

    public DatabaseLogDestination(SimulatedDatabase db) {
        this.db = db;
    }

    @Override
    public void write(TransactionCommand cmd) {
        if (db != null) {
            db.insert(TABLE, cmd);
        }
    }

    @Override
    public List<TransactionCommand> readAll() {
        if (db == null) return Collections.emptyList();
        return db.selectAll(TABLE).stream()
                .map(o -> (TransactionCommand) o)
                .collect(Collectors.toList());
    }

    @Override
    public void clear() {
        if (db != null) {
            db.deleteAll(TABLE);
        }
    }

    @Override
    public String getDestinationName() {
        return "DATABASE";
    }
}
