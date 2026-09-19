package com.gdb.domain;

import com.gdb.exceptions.*;

public class SavingsAccount extends AbstractAccount {
    private double minBalance = 1000.0;
    private double interestRate = 4.0;

    public SavingsAccount(String accountNumber, String name, int age, double balance, String status, String pin) {
        super(accountNumber, name, age, balance, "SAVINGS", status, pin);
    }

    public SavingsAccount(String accountNumber, String name, int age, double balance, String status, String pin, double minBalance, double interestRate) {
        super(accountNumber, name, age, balance, "SAVINGS", status, pin);
        this.minBalance = minBalance;
        this.interestRate = interestRate;
    }

    // TODO: Step 3.1 - Savings debit rule (add @Override once processDebit is declared abstract in AbstractAccount):
    //   1. If (balance - amount) < minBalance -> throw new MinimumBalanceViolationException("Cannot breach minimum balance of Rs " + minBalance)
    //   2. Otherwise subtract amount from balance.
    public void processDebit(double amount) throws AccountException {
    }

    public void applyInterest() {
        double interest = this.balance * (interestRate / 100.0);
        this.balance += interest;
    }

    public double getMinBalance() { return minBalance; }
    public double getInterestRate() { return interestRate; }
}
