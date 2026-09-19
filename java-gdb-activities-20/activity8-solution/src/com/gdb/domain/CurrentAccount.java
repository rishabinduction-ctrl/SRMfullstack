package com.gdb.domain;

import com.gdb.exceptions.*;

public class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount(String accountNumber, String name, int age, double balance, String status, String pin, double overdraftLimit) {
        super(accountNumber, name, age, balance, "CURRENT", status, pin);
        this.overdraftLimit = overdraftLimit;
    }

    @Override
    public void withdraw(double amount, String enteredPin) throws AccountException {
        if (!validatePin(enteredPin)) throw new InvalidPinException("Invalid PIN entered");
        if (!"ACTIVE".equalsIgnoreCase(this.status)) throw new InactiveAccountException("Account is not active");
        if (amount <= 0) throw new InvalidAmountException("Withdrawal amount must be positive");
        if (amount > (this.balance + this.overdraftLimit)) {
            throw new InsufficientBalanceException("Overdraft limit exceeded");
        }
        this.balance -= amount;
    }

    public double getOverdraftLimit() { return overdraftLimit; }
    public void setOverdraftLimit(double overdraftLimit) { this.overdraftLimit = overdraftLimit; }
}
