package com.gdb.service;

import com.gdb.domain.*;
import com.gdb.exceptions.*;

public class TransferService {

    public TransferService() {
    }

    public void transfer(IAccount from, IAccount to, double amount, int pin)
            throws AccountException {
        if (from == null || to == null) {
            throw new AccountException("Source and destination accounts are required");
        }
        if (!from.isActive() || !to.isActive()) {
            throw new InactiveAccountException("Both accounts must be active to transfer funds");
        }
        if (!from.verifyPin(pin)) {
            throw new InvalidPinException("Incorrect PIN");
        }
        if (!from.canWithdraw(amount)) {
            throw new InsufficientBalanceException("Insufficient balance for transfer of Rs. " + amount);
        }
        Account source = (Account) from;
        source.resetDailyTransferIfNeeded();
        if (!source.canTransfer(amount)) {
            throw new AccountException("Daily transfer limit exceeded. Remaining today: Rs. " + source.getRemainingDailyTransferLimit());
        }
        from.withdraw(amount, pin);
        to.deposit(amount);
        source.updateDailyTransferTotal(amount);
    }

    // ============================================================
    // 📝 STEP 9: Return Transaction From transfer
    //
    // INSTRUCTIONS:
    //   1. Call existing transfer(from, to, amount, pin).
    //   2. Build and return a Transaction with:
    //      - ID: Transaction.generateId()
    //      - timestamp: LocalDateTime.now()
    //      - accountNumber: from.getAccountNumber()
    //      - type: TransactionType.TRANSFER
    //      - amount: amount
    //      - balanceAfter: from.getBalance()
    //      - status: "SUCCESS"
    //      - description: "Transfer of Rs. " + amount + " to Account #" + to.getAccountNumber()
    //      - fromAccount: from.getAccountNumber()
    //      - toAccount: to.getAccountNumber()
    // ============================================================
    // TODO: perform transfer and return Transaction record
    public Transaction transferWithTransaction(IAccount from, IAccount to, 
                                               double amount, int pin) throws AccountException {
        // Trainee: call transfer(from, to, amount, pin), then build and return Transaction
        return null;
    }
}
