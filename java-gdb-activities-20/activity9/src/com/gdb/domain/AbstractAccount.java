package com.gdb.domain;

import com.gdb.exceptions.*;

/**
 * AbstractAccount - Defines shared template methods and forces subclasses to implement processDebit.
 * The shared fields and concrete methods below are moved up unchanged from the Activity 7/8 Account class.
 */
public abstract class AbstractAccount {
    protected String accountNumber;
    protected String name;
    protected int age;
    protected double balance;
    protected String accountType;
    protected String status;
    protected String pin;

    public AbstractAccount(String accountNumber, String name, int age, double balance, String accountType, String status, String pin) {
        if (age < 18) throw new IllegalArgumentException("Customer age must be 18 or above");
        if (balance < 0) throw new IllegalArgumentException("Initial balance cannot be negative");
        if (pin == null || !pin.matches("\\d{4}")) throw new IllegalArgumentException("PIN must be 4 digits");
        this.accountNumber = accountNumber;
        this.name = name;
        this.age = age;
        this.balance = balance;
        this.accountType = accountType;
        this.status = status;
        this.pin = pin;
    }

    public boolean validatePin(String enteredPin) {
        return this.pin != null && this.pin.equals(enteredPin);
    }

    public boolean changePin(String oldPin, String newPin) {
        if (!validatePin(oldPin)) return false;
        if (newPin == null || !newPin.matches("\\d{4}")) return false;
        this.pin = newPin;
        return true;
    }

    public void deposit(double amount) throws InvalidAmountException {
        if (amount <= 0) throw new InvalidAmountException("Deposit amount must be positive");
        this.balance += amount;
    }

    public void withdraw(double amount, String enteredPin) throws AccountException {
        // TODO: Step 2 - Template Method: enforce this fixed sequence for EVERY account type:
        //   1. PIN incorrect (validatePin fails) -> throw new InvalidPinException("Invalid PIN entered")
        //   2. status is not "ACTIVE"            -> throw new InactiveAccountException("Account is not active")
        //   3. amount <= 0                       -> throw new InvalidAmountException("Withdrawal amount must be positive")
        //   4. Call processDebit(amount) so the subclass applies its own debit rule.
    }

    // TODO: Step 1.4 - Declare the hook every subclass must implement:
    //   a public abstract method named processDebit that takes a double amount, returns void,
    //   and throws AccountException.

    public void displayAccountInfo() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Balance: Rs " + balance);
        System.out.println("Account Type: " + accountType);
        System.out.println("Status: " + status);
    }

    public String getAccountNumber() { return accountNumber; }
    public String getName() { return name; }
    public int getAge() { return age; }
    public double getBalance() { return balance; }
    public String getAccountType() { return accountType; }
    public String getStatus() { return status; }
}
