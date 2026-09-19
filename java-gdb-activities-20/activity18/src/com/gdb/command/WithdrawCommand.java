package com.gdb.command;

import com.gdb.domain.Account;
import com.gdb.domain.IAccount;
import com.gdb.domain.Transaction;

public class WithdrawCommand implements TransactionCommand {
    private static final long serialVersionUID = 1L;

    private IAccount account;
    private double amount;
    private int pin;
    private Transaction transaction;

    public WithdrawCommand(IAccount account, double amount, int pin) {
        this.account = account;
        this.amount = amount;
        this.pin = pin;
    }

    @Override
    public void execute() throws Exception {
        if (account instanceof Account) {
            this.transaction = ((Account) account).withdrawWithTransaction(amount, pin);
        } else {
            account.withdraw(amount, pin);
        }
    }

    @Override
    public Transaction getTransaction() {
        return this.transaction;
    }
}
