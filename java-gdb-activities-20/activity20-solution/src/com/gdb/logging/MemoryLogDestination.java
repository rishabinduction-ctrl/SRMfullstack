package com.gdb.logging;

import com.gdb.command.TransactionCommand;
import java.util.*;

public class MemoryLogDestination implements LogDestination {
    private final List<TransactionCommand> commands = new ArrayList<>();

    @Override
    public void write(TransactionCommand cmd) {
        commands.add(cmd);
    }

    @Override
    public List<TransactionCommand> readAll() {
        return new ArrayList<>(commands);
    }

    @Override
    public void clear() {
        commands.clear();
    }

    @Override
    public String getDestinationName() {
        return "MEMORY";
    }
}
