package com.gdb.domain;

import com.gdb.exceptions.*;

/**
 * Concrete SavingsAccount subclass extending Abstract Account and implementing IAccount.
 * Dynamically queries AccountRulesEngine for minimum balance and interest rates based on tenure.
 */
public class SavingsAccount extends Account {

    public SavingsAccount(int accountNumber, String name, int age, double initialBalance)
            throws InvalidAgeException, MinimumBalanceViolationException {
        this(accountNumber, name, age, initialBalance, 0);
    }

    public SavingsAccount(int accountNumber, String name, int age, double initialBalance, int tenureYears)
            throws InvalidAgeException, MinimumBalanceViolationException {
        super(accountNumber, name, age, initialBalance, tenureYears);
        double minRequired = getMinimumBalance();
        if (initialBalance < minRequired) {
            throw new MinimumBalanceViolationException("Savings account requires minimum balance of Rs. " + minRequired + ". Provided: Rs. " + initialBalance);
        }
    }

    @Override
    public double getMinimumBalance() {
        return AccountRulesEngine.getInstance().getMinimumBalance("SAVINGS", tenureYears);
    }

    @Override
    public String getAccountType() {
        return "Savings";
    }

    @Override
    public double getInterestRate() {
        return AccountRulesEngine.getInstance().getInterestRate("SAVINGS", tenureYears);
    }

    @Override
    public boolean canWithdraw(double amount) {
        return (balance - amount) >= getMinimumBalance();
    }

    public void applyMonthlyInterest() {
        double rate = getInterestRate();
        double monthlyInterest = balance * (rate / 100.0) / 12.0;
        balance += monthlyInterest;
    }
}
