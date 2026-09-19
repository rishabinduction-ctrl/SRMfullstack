package com.gdb.service;

import com.gdb.domain.*;
import com.gdb.exceptions.*;

public class TransferService {

    public TransferService() {
    }

    public void transfer(IAccount from, IAccount to, double amount, int pin)
            throws AccountException {
        // 1. Null check
        if (from == null || to == null) {
            throw new AccountException("Source and destination accounts are required");
        }

        // 2. Active check
        if (!from.isActive() || !to.isActive()) {
            throw new InactiveAccountException("Both accounts must be active to transfer funds");
        }

        // 3. PIN verify
        if (!from.verifyPin(pin)) {
            throw new InvalidPinException("Incorrect PIN");
        }

        // 4. Balance check
        if (!from.canWithdraw(amount)) {
            throw new InsufficientBalanceException("Insufficient balance for transfer of Rs. " + amount);
        }

        // 5. Daily-limit check
        Account source = (Account) from;
        source.resetDailyTransferIfNeeded();
        if (!source.canTransfer(amount)) {
            throw new AccountException("Daily transfer limit exceeded. Remaining today: Rs. " + source.getRemainingDailyTransferLimit());
        }

        // 6. Debit source
        from.withdraw(amount, pin);

        // 7. Credit destination
        to.deposit(amount);

        // 8. Update daily total
        source.updateDailyTransferTotal(amount);
    }
}
