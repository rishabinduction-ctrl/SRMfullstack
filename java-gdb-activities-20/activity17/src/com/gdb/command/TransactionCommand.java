package com.gdb.command;

import com.gdb.domain.Transaction;
import java.io.Serializable;

/**
 * Command interface defining common operations for financial transaction commands.
 */
public interface TransactionCommand extends Serializable {
    // ============================================================
    // 📝 STEP 1: Add execute() Method Signature
    //
    // INSTRUCTIONS:
    //   Declare void execute() throws Exception
    // ============================================================
    // TODO: declare execute() method
    void execute() throws Exception;
    
    // ============================================================
    // 📝 STEP 2: Add getTransaction() Method Signature
    //
    // INSTRUCTIONS:
    //   Declare Transaction getTransaction()
    // ============================================================
    // TODO: declare getTransaction() method
    Transaction getTransaction();
}
