package com.gdb.domain;

import com.gdb.exceptions.*;

public class SavingsAccount extends AbstractAccount {
    private int tenureYears;
    private double minBalance;
    private double interestRate;

    public SavingsAccount(String accountNumber, String name, int age, double balance, String status, String pin, int tenureYears) {
        super(accountNumber, name, age, balance, "SAVINGS", status, pin);
        this.tenureYears = tenureYears;
        this.minBalance = AccountRulesEngine.getSavingsMinBalance(tenureYears);
        this.interestRate = AccountRulesEngine.getSavingsInterestRate(tenureYears);
    }

    public SavingsAccount(String accountNumber, String name, int age, double balance, String status, String pin, double minBalance, double interestRate) {
        super(accountNumber, name, age, balance, "SAVINGS", status, pin);
        this.tenureYears = 0;
        this.minBalance = minBalance;
        this.interestRate = interestRate;
    }

    @Override
    public void processDebit(double amount) throws AccountException {
        if ((this.balance - amount) < this.minBalance) {
            throw new MinimumBalanceViolationException("Cannot breach minimum balance of Rs " + minBalance);
        }
        this.balance -= amount;
    }

    public void applyInterest() {
        double interest = this.balance * (interestRate / 100.0);
        this.balance += interest;
    }

    public int getTenureYears() { return tenureYears; }
    public double getMinBalance() { return minBalance; }
    public double getInterestRate() { return interestRate; }
}
