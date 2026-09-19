package com.gdb.domain;

import com.gdb.exceptions.*;
import java.time.LocalDateTime;

/**
 * Abstract class Account implementing default behavior for IAccount interface.
 * Encapsulates common state fields, customer tenure, and default validation routines.
 */
public abstract class Account implements IAccount {
    protected int accountNumber;
    protected String accountHolderName;
    protected int age;
    protected double balance;
    protected String status;
    protected Integer pin;
    protected String openingDate;
    protected int tenureYears;

    // ============================================================
    // 📝 STEP 2.1: Daily Transfer Tracking Fields
    //
    // INSTRUCTIONS:
    //   1. dailyTransferTotal holds the sum of all transfers sent today (starts at 0.0).
    //   2. lastTransferDate records when that total was last updated (starts at now).
    //
    // HINT: These are declared for you because the getters below need them to compile; Steps 4-7 read and update them.
    // ============================================================
    // TODO: study these two fields — every daily-limit method in Steps 4-7 works with them
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
        // ============================================================
        // 📝 STEP 3: Get Daily Transfer Limit
        //
        // INSTRUCTIONS:
        //   1. Ask the rules engine for this account's limit:
        //      AccountRulesEngine.getInstance().getDailyTransferLimit(getAccountType(), getTenureYears()).
        //   2. Return that value.
        //
        // HINT: The limit depends on account type and tenure bucket, e.g. a NEW Savings account gets Rs. 50,000.
        // ============================================================
        // TODO: return the daily transfer limit from the rules engine
        return 0.0;
    }

    public double getRemainingDailyTransferLimit() {
        // ============================================================
        // 📝 STEP 4: Get Remaining Daily Limit
        //
        // INSTRUCTIONS:
        //   1. Call resetDailyTransferIfNeeded() so yesterday's transfers are not counted.
        //   2. Return getDailyTransferLimit() - dailyTransferTotal, but never less than 0.
        //
        // HINT: Math.max(0.0, ...) keeps the result from going negative.
        // ============================================================
        // TODO: return how much can still be transferred today
        return 0.0;
    }

    public boolean canTransfer(double amount) {
        // ============================================================
        // 📝 STEP 5: Check Amount Against Daily Limit
        //
        // INSTRUCTIONS:
        //   1. Call resetDailyTransferIfNeeded().
        //   2. Return true if dailyTransferTotal + amount <= getDailyTransferLimit(), otherwise false.
        //
        // HINT: A limit of 0 (Fixed Deposit) must block every transfer.
        // ============================================================
        // TODO: return whether this amount fits within today's limit
        return false;
    }

    public void updateDailyTransferTotal(double amount) {
        // ============================================================
        // 📝 STEP 6: Record A Completed Transfer
        //
        // INSTRUCTIONS:
        //   1. Call resetDailyTransferIfNeeded().
        //   2. Add amount to dailyTransferTotal.
        //   3. Set lastTransferDate to LocalDateTime.now().
        // ============================================================
        // TODO: add the amount to today's running total
    }

    public void resetDailyTransferIfNeeded() {
        // ============================================================
        // 📝 STEP 7: Reset The Total On A New Day
        //
        // INSTRUCTIONS:
        //   1. Compare lastTransferDate.toLocalDate() with LocalDateTime.now().toLocalDate().
        //   2. If they differ, set dailyTransferTotal to 0.0 and lastTransferDate to LocalDateTime.now().
        //
        // HINT: Compare dates, not date-times — two transfers an hour apart are still on the same day.
        // ============================================================
        // TODO: reset the daily total when the calendar day has changed
    }

    public double getDailyTransferTotal() { return dailyTransferTotal; }
    public LocalDateTime getLastTransferDate() { return lastTransferDate; }
}
