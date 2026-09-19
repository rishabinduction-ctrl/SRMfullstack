package com.gdb.domain;

import com.gdb.exceptions.*;

public class SavingsAccount extends Account {
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

    public void applyInterest() {
        double interest = this.balance * (interestRate / 100.0);
        this.balance += interest;
    }

    public double getMinBalance() { return minBalance; }
    public double getInterestRate() { return interestRate; }
}
