package com.gdb.domain;

import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * Model class representing a financial transaction in the GDB banking system.
 */
public class Transaction implements Serializable {
    private static final long serialVersionUID = 1L;
    private static long counter = 0;

    // ============================================================
    // 📝 STEP 2: Declare Transaction Fields
    //
    // INSTRUCTIONS:
    //   1. transactionId (String) - Unique identifier for the transaction
    //   2. timestamp (LocalDateTime) - Timestamp when transaction occurred
    //   3. accountNumber (int) - Account on which transaction was performed
    //   4. type (TransactionType) - DEPOSIT, WITHDRAW, or TRANSFER
    //   5. amount (double) - Monetary value of the transaction
    //   6. balanceAfter (double) - Account balance after transaction execution
    //   7. status (String) - "SUCCESS" or "FAILED"
    //   8. description (String) - Human-readable summary
    //   9. fromAccount (int) - Source account (0 if not a TRANSFER)
    //   10. toAccount (int) - Destination account (0 if not a TRANSFER)
    // ============================================================
    // TODO: declare all transaction fields

    public Transaction() {
    }

    // ============================================================
    // 📝 STEP 3: Constructor With All Fields
    //
    // INSTRUCTIONS:
    //   Initialize all instance variables from constructor parameters.
    // ============================================================
    // TODO: implement all-arguments constructor
    public Transaction(String transactionId, LocalDateTime timestamp, int accountNumber,
                       TransactionType type, double amount, double balanceAfter,
                       String status, String description, int fromAccount, int toAccount) {
        // TODO: Step 3 - implement all-arguments constructor
    }

    // ============================================================
    // 📝 STEP 4: Getters and Setters
    //
    // INSTRUCTIONS:
    //   Provide standard accessors and mutators for all fields.
    // ============================================================
    // TODO: implement getters and setters
    public String getTransactionId() { return null; }
    public void setTransactionId(String transactionId) { }

    public LocalDateTime getTimestamp() { return null; }
    public void setTimestamp(LocalDateTime timestamp) { }

    public int getAccountNumber() { return 0; }
    public void setAccountNumber(int accountNumber) { }

    public TransactionType getType() { return null; }
    public void setType(TransactionType type) { }

    public double getAmount() { return 0.0; }
    public void setAmount(double amount) { }

    public double getBalanceAfter() { return 0.0; }
    public void setBalanceAfter(double balanceAfter) { }

    public String getStatus() { return null; }
    public void setStatus(String status) { }

    public String getDescription() { return null; }
    public void setDescription(String description) { }

    public int getFromAccount() { return 0; }
    public void setFromAccount(int fromAccount) { }

    public int getToAccount() { return 0; }
    public void setToAccount(int toAccount) { }

    // ============================================================
    // 📝 STEP 5: toString Display Format
    //
    // INSTRUCTIONS:
    //   Format transaction into a readable summary string.
    // ============================================================
    // TODO: implement toString() method
    @Override
    public String toString() {
        // TODO: Step 5 - implement toString() method
        return "";
    }

    // ============================================================
    // 📝 STEP 6: Static Helper generateId()
    //
    // INSTRUCTIONS:
    //   Generate a unique transaction identifier string:
    //   "TXN-" + System.currentTimeMillis() + "-" + (++counter)
    // ============================================================
    // TODO: generate unique transaction ID
    public static synchronized String generateId() {
        // TODO: Step 6 - generate unique transaction ID
        return "";
    }
}
