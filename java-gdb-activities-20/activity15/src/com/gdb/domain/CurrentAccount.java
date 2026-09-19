package com.gdb.domain;

import com.gdb.exceptions.*;

/**
 * Concrete CurrentAccount subclass extending Abstract Account and implementing IAccount.
 * Dynamically queries AccountRulesEngine for minimum balance, interest rate, and overdraft facility.
 */
public class CurrentAccount extends Account {
    private double overdraftUsed = 0.0;

    public CurrentAccount(int accountNumber, String name, int age, double initialBalance)
            throws InvalidAgeException, MinimumBalanceViolationException {
        this(accountNumber, name, age, initialBalance, 0);
    }

    public CurrentAccount(int accountNumber, String name, int age, double initialBalance, int tenureYears)
            throws InvalidAgeException, MinimumBalanceViolationException {
        super(accountNumber, name, age, initialBalance, tenureYears);
        double minRequired = getMinimumBalance();
        if (initialBalance < minRequired) {
            throw new MinimumBalanceViolationException("Current account requires minimum balance of Rs. " + minRequired + ". Provided: Rs. " + initialBalance);
        }
    }

    @Override
    public double getMinimumBalance() {
        return AccountRulesEngine.getInstance().getMinimumBalance("CURRENT", tenureYears);
    }

    @Override
    public String getAccountType() {
        return "Current";
    }

    @Override
    public double getInterestRate() {
        return AccountRulesEngine.getInstance().getInterestRate("CURRENT", tenureYears);
    }

    public double getOverdraftLimit() {
        Object val = AccountRulesEngine.getInstance().getAdditionalFeature("CURRENT", tenureYears, "overdraftLimit");
        if (val instanceof Number) {
            return ((Number) val).doubleValue();
        }
        return 5000.0;
    }

    @Override
    public boolean canWithdraw(double amount) {
        double maxWithdraw = balance - getMinimumBalance() + getOverdraftLimit() - overdraftUsed;
        return amount <= maxWithdraw;
    }

    @Override
    public void withdraw(double amount, int pin) throws InactiveAccountException, InvalidPinException, InvalidAmountException, InsufficientBalanceException {
        if (!"Active".equals(status)) throw new InactiveAccountException("Account is inactive.");
        if (this.pin == null) throw new InvalidPinException("PIN not set for this account");
        if (this.pin != pin) throw new InvalidPinException("Incorrect PIN");
        if (amount <= 0) throw new InvalidAmountException("Amount must be positive. Provided: Rs. " + amount);
        if (!canWithdraw(amount)) throw new InsufficientBalanceException("Withdrawal not allowed");

        double minBal = getMinimumBalance();
        double newBalance = balance - amount;
        if (newBalance < minBal) {
            double overdraftAmt = minBal - newBalance;
            overdraftUsed += overdraftAmt;
        }
        balance = newBalance;
    }

    public double getOverdraftUsed() { return overdraftUsed; }
    public double getAvailableOverdraft() { return getOverdraftLimit() - overdraftUsed; }

    public void repayOverdraft(double amount) throws InvalidAmountException, InsufficientBalanceException {
        if (amount <= 0) throw new InvalidAmountException("Repayment amount must be positive");
        if (amount > overdraftUsed) throw new InsufficientBalanceException("Repayment amount exceeds overdraft used");
        overdraftUsed -= amount;
        balance += amount;
    }

    public double getAvailableBalance() {
        return balance - getMinimumBalance() + getOverdraftLimit() - overdraftUsed;
    }
}
