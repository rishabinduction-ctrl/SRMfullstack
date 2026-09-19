package com.gdb.db;

import java.util.*;

/**
 * In-memory simulated database table engine for logging and persistence testing.
 */
public class SimulatedDatabase {
    private final Map<String, List<Object>> tables = new HashMap<>();

    public void insert(String table, Object obj) {
        tables.computeIfAbsent(table, k -> new ArrayList<>()).add(obj);
    }

    public List<Object> selectAll(String table) {
        return new ArrayList<>(tables.getOrDefault(table, Collections.emptyList()));
    }

    public void deleteAll(String table) {
        tables.put(table, new ArrayList<>());
    }

    public int count(String table) {
        return tables.getOrDefault(table, Collections.emptyList()).size();
    }
}
