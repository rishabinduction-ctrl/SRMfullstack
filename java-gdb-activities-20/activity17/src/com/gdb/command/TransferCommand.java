package com.gdb.command;

import com.gdb.domain.IAccount;
import com.gdb.domain.Transaction;
import com.gdb.service.TransferService;

public class TransferCommand implements TransactionCommand {
    private static final long serialVersionUID = 1L;

    // ============================================================
    // 📝 STEP 3: Declare Fields
    //
    // INSTRUCTIONS:
    //   1. private IAccount fromAccount;
    //   2. private IAccount toAccount;
    //   3. private double amount;
    //   4. private int pin;
    //   5. private Transaction transaction;
    // ============================================================
    // TODO: declare fromAccount, toAccount, amount, pin, and transaction fields

    // ============================================================
    // 📝 STEP 4: Write Constructor
    //
    // INSTRUCTIONS:
    //   Accept (IAccount from, IAccount to, double amount, int pin); store all.
    // ============================================================
    // TODO: implement constructor
    public TransferCommand(IAccount from, IAccount to, double amount, int pin) {
        // TODO: Step 4 - implement constructor
    }

    // ============================================================
    // 📝 STEP 5: Implement execute()
    //
    // INSTRUCTIONS:
    //   1. Call new TransferService().transferWithTransaction(fromAccount, toAccount, amount, pin).
    //   2. Store returned Transaction in this.transaction.
    // ============================================================
    // TODO: implement execute() method
    @Override
    public void execute() throws Exception {
        // TODO: Step 5 - implement execute()
    }

    // ============================================================
    // 📝 STEP 6: Implement getTransaction()
    //
    // INSTRUCTIONS:
    //   Return this.transaction.
    // ============================================================
    // TODO: return this.transaction
    @Override
    public Transaction getTransaction() {
        // TODO: Step 6 - return this.transaction
        return null;
    }
}
