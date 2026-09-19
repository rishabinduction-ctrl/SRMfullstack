package com.gdb.domain;

import com.gdb.exceptions.*;
import java.time.LocalDateTime;

/**
 * Abstract class Account implementing default behavior for IAccount interface.
 * Encapsulates common state fields, customer tenure, and default validation routines.
 */
public abstract class Account implements IAccount, java.io.Serializable {
    private static final long serialVersionUID = 1L;
    protected int accountNumber;
    protected String accountHolderName;
    protected int age;
    protected double balance;
    protected String status;
    protected Integer pin;
    protected String openingDate;
    protected int tenureYears;

    protected double dailyTransferTotal = 0.0;
    protected LocalDateTime lastTransferDate = LocalDateTime.now();

    public Account(int accountNumber, String name, int age, double initialBalance) throws InvalidAgeException {
        this(accountNumber, name, age, initialBalance, 0);
    }

    public Account(int accountNumber, String name, int age, double initialBalance, int tenureYears) throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("Customer must be at least 18 years old. Provided: " + age);
        }
        if (name == null || name.trim().isEmpty()) {
            throw new InvalidAgeException("Name cannot be empty");
        }

        this.accountNumber = accountNumber;
        this.accountHolderName = name;
        this.age = age;
        this.balance = initialBalance;
        this.status = "Active";
        this.pin = null;
        this.openingDate = "2026-08-28";
        this.tenureYears = Math.max(0, tenureYears);
    }

    @Override
    public void deposit(double amount) throws InactiveAccountException, InvalidAmountException {
        if (!"Active".equals(status)) {
            throw new InactiveAccountException("Account is inactive.");
        }
        if (amount <= 0) {
            throw new InvalidAmountException("Deposit amount must be positive. Provided: Rs. " + amount);
        }
        balance += amount;
    }

    @Override
    public void withdraw(double amount, int pin) throws InactiveAccountException, InvalidPinException, InvalidAmountException, InsufficientBalanceException {
        if (!"Active".equals(status)) {
            throw new InactiveAccountException("Account is inactive.");
        }
        if (this.pin == null) {
            throw new InvalidPinException("PIN not set for this account");
        }
        if (this.pin != pin) {
            throw new InvalidPinException("Incorrect PIN");
        }
        if (amount <= 0) {
            throw new InvalidAmountException("Amount must be positive. Provided: Rs. " + amount);
        }
        if (!canWithdraw(amount)) {
            throw new InsufficientBalanceException("Withdrawal not allowed");
        }
        balance -= amount;
    }

    @Override
    public void closeAccount() throws InactiveAccountException {
        if (!"Active".equals(status)) {
            throw new InactiveAccountException("Account is already closed / inactive.");
        }
        status = "Inactive";
    }

    @Override
    public void reopenAccount() throws InactiveAccountException {
        if ("Active".equals(status)) {
            throw new InactiveAccountException("Account is already active.");
        }
        status = "Active";
    }

    @Override
    public void setPin(int pin) throws InvalidPinException {
        if (pin < 1000 || pin > 9999) {
            throw new InvalidPinException("PIN must be a 4-digit number (1000-9999). Provided: " + pin);
        }
        this.pin = pin;
    }

    @Override public boolean verifyPin(int pin) { return this.pin != null && this.pin == pin; }
    @Override public boolean hasPin() { return pin != null; }
    @Override public boolean isActive() { return "Active".equals(status); }

    @Override
    public String getAccountInfo() {
        return "Account #" + accountNumber + " | " + accountHolderName + " (" + age + " yrs, Tenure: " + tenureYears + " yrs) | " +
               getAccountType() + " | Rs. " + balance + " | " + status;
    }

    @Override public int getAccountNumber() { return accountNumber; }
    @Override public String getAccountHolderName() { return accountHolderName; }
    @Override public double getBalance() { return balance; }
    @Override public String getOpeningDate() { return openingDate; }
    @Override public int getTenureYears() { return tenureYears; }
    @Override public void setTenureYears(int tenureYears) { this.tenureYears = Math.max(0, tenureYears); }

    public double getDailyTransferLimit() {
        return AccountRulesEngine.getInstance().getDailyTransferLimit(getAccountType(), getTenureYears());
    }

    public double getRemainingDailyTransferLimit() {
        resetDailyTransferIfNeeded();
        return Math.max(0.0, getDailyTransferLimit() - dailyTransferTotal);
    }

    public boolean canTransfer(double amount) {
        resetDailyTransferIfNeeded();
        return (dailyTransferTotal + amount) <= getDailyTransferLimit();
    }

    public void updateDailyTransferTotal(double amount) {
        resetDailyTransferIfNeeded();
        dailyTransferTotal += amount;
        lastTransferDate = LocalDateTime.now();
    }

    public void resetDailyTransferIfNeeded() {
        if (lastTransferDate == null || !lastTransferDate.toLocalDate().equals(LocalDateTime.now().toLocalDate())) {
            dailyTransferTotal = 0.0;
            lastTransferDate = LocalDateTime.now();
        }
    }

    public double getDailyTransferTotal() { return dailyTransferTotal; }
    public LocalDateTime getLastTransferDate() { return lastTransferDate; }

    protected Transaction buildTransaction(TransactionType type, double amount, 
                                           int fromAcc, int toAcc, String desc) {
        return new Transaction(
            Transaction.generateId(),
            LocalDateTime.now(),
            this.accountNumber,
            type, amount, this.balance, "SUCCESS",
            desc, fromAcc, toAcc
        );
    }

    public Transaction depositWithTransaction(double amount) throws AccountException {
        deposit(amount);
        return buildTransaction(TransactionType.DEPOSIT, amount, 0, 0, "Deposit of Rs. " + amount);
    }

    public Transaction withdrawWithTransaction(double amount, int pin) throws AccountException {
        withdraw(amount, pin);
        return buildTransaction(TransactionType.WITHDRAW, amount, 0, 0, "Withdrawal of Rs. " + amount);
    }
}
