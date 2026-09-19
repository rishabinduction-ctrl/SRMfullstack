package com.gdb.domain;

import com.gdb.exceptions.*;

/**
 * Concrete FixedDepositAccount subclass extending Abstract Account and implementing IAccount.
 * Dynamically queries AccountRulesEngine for minimum balance, interest rate, lock-in period, and penalty rate.
 */
public class FixedDepositAccount extends Account {
    private String maturityDate = "2027-08-28";
    private double interestEarned = 0.0;

    public FixedDepositAccount(int accountNumber, String name, int age, double initialBalance)
            throws InvalidAgeException, MinimumBalanceViolationException {
        this(accountNumber, name, age, initialBalance, 0);
    }

    public FixedDepositAccount(int accountNumber, String name, int age, double initialBalance, int tenureYears)
            throws InvalidAgeException, MinimumBalanceViolationException {
        super(accountNumber, name, age, initialBalance, tenureYears);
        double minRequired = getMinimumBalance();
        if (initialBalance < minRequired) {
            throw new MinimumBalanceViolationException("FixedDeposit account requires minimum balance of Rs. " + minRequired + ". Provided: Rs. " + initialBalance);
        }
    }

    @Override
    public double getMinimumBalance() {
        return AccountRulesEngine.getInstance().getMinimumBalance("FIXEDDEPOSIT", tenureYears);
    }

    @Override
    public String getAccountType() {
        return "FixedDeposit";
    }

    @Override
    public double getInterestRate() {
        return AccountRulesEngine.getInstance().getInterestRate("FIXEDDEPOSIT", tenureYears);
    }

    public int getLockinMonths() {
        Object val = AccountRulesEngine.getInstance().getAdditionalFeature("FIXEDDEPOSIT", tenureYears, "lockinMonths");
        if (val instanceof Number) {
            return ((Number) val).intValue();
        }
        return 12;
    }

    public double getPenaltyPercentage() {
        Object val = AccountRulesEngine.getInstance().getAdditionalFeature("FIXEDDEPOSIT", tenureYears, "penaltyPercentage");
        if (val instanceof Number) {
            return ((Number) val).doubleValue();
        }
        return 1.00;
    }

    @Override
    public boolean canWithdraw(double amount) {
        return false;
    }

    @Override
    public void withdraw(double amount, int pin) throws InsufficientBalanceException {
        throw new InsufficientBalanceException("Account not matured. " + getLockinMonths() + " months remaining until maturity date: " + maturityDate);
    }

    public void applyMonthlyInterest() {
        double rate = getInterestRate();
        double monthlyInterest = balance * (rate / 100.0) / 12.0;
        balance += monthlyInterest;
        interestEarned += monthlyInterest;
    }

    public String getMaturityDate() { return maturityDate; }
    public double getInterestEarned() { return interestEarned; }
    public int getDaysToMaturity() { return 365; }
}
