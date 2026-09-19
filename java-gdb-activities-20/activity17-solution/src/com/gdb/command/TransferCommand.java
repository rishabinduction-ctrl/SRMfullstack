package com.gdb.command;

import com.gdb.domain.IAccount;
import com.gdb.domain.Transaction;
import com.gdb.service.TransferService;

public class TransferCommand implements TransactionCommand {
    private static final long serialVersionUID = 1L;

    private IAccount fromAccount;
    private IAccount toAccount;
    private double amount;
    private int pin;
    private Transaction transaction;

    public TransferCommand(IAccount from, IAccount to, double amount, int pin) {
        this.fromAccount = from;
        this.toAccount = to;
        this.amount = amount;
        this.pin = pin;
    }

    @Override
    public void execute() throws Exception {
        this.transaction = new TransferService().transferWithTransaction(fromAccount, toAccount, amount, pin);
    }

    @Override
    public Transaction getTransaction() {
        return this.transaction;
    }
}
