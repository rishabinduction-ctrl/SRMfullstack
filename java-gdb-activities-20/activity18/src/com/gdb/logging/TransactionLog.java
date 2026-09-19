package com.gdb.logging;

import com.gdb.command.TransactionCommand;
import java.io.*;
import java.util.*;

public class TransactionLog {
    private static final String FILE_PATH = "data/transactions.ser";

    private static class AppendableObjectOutputStream extends ObjectOutputStream {
        public AppendableObjectOutputStream(OutputStream out) throws IOException {
            super(out);
        }
        @Override
        protected void writeStreamHeader() throws IOException {
            // do not write header when appending to an existing stream
        }
    }

    public synchronized void log(TransactionCommand cmd) throws IOException {
        File file = new File(FILE_PATH);
        if (file.getParentFile() != null && !file.getParentFile().exists()) {
            file.getParentFile().mkdirs();
        }
        boolean isNewOrEmpty = !file.exists() || file.length() == 0;
        try (ObjectOutputStream out = isNewOrEmpty
                ? new ObjectOutputStream(new FileOutputStream(file))
                : new AppendableObjectOutputStream(new FileOutputStream(file, true))) {
            out.writeObject(cmd);
            out.flush();
        }
    }

    public synchronized List<TransactionCommand> readAll() throws IOException, ClassNotFoundException {
        List<TransactionCommand> list = new ArrayList<>();
        File file = new File(FILE_PATH);
        if (!file.exists() || file.length() == 0) {
            return list;
        }
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(file))) {
            while (true) {
                try {
                    Object obj = in.readObject();
                    if (obj instanceof TransactionCommand) {
                        list.add((TransactionCommand) obj);
                    }
                } catch (EOFException e) {
                    break;
                }
            }
        }
        return list;
    }

    public synchronized void clear() {
        File file = new File(FILE_PATH);
        if (file.exists()) {
            file.delete();
        }
    }
}
