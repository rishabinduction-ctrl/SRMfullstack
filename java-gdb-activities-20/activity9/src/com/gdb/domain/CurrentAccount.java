package com.gdb.domain;

import com.gdb.exceptions.*;

public class CurrentAccount extends AbstractAccount {
    private double overdraftLimit;

    public CurrentAccount(String accountNumber, String name, int age, double balance, String status, String pin, double overdraftLimit) {
        super(accountNumber, name, age, balance, "CURRENT", status, pin);
        this.overdraftLimit = overdraftLimit;
    }

    // TODO: Step 3.2 - Current debit rule (add @Override once processDebit is declared abstract in AbstractAccount):
    //   1. If amount > (balance + overdraftLimit) -> throw new InsufficientBalanceException("Overdraft limit exceeded")
    //   2. Otherwise subtract amount from balance (the balance may go negative, down to -overdraftLimit).
    public void processDebit(double amount) throws AccountException {
    }

    public double getOverdraftLimit() { return overdraftLimit; }
    public void setOverdraftLimit(double overdraftLimit) { this.overdraftLimit = overdraftLimit; }
}
