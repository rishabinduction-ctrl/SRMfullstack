package com.gdb.command;

import com.gdb.domain.Transaction;
import java.io.Serializable;

/**
 * Command interface defining common operations for financial transaction commands.
 */
public interface TransactionCommand extends Serializable {
    void execute() throws Exception;
    Transaction getTransaction();
}
