package com.gdb.domain;

/**
 * Account - Enhanced bank account with PIN authentication, age validation, and status transitions.
 */
public class Account {
    private String accountNumber;
    private String name;
    private int age;
    private double balance;
    private String accountType;
    private String status;
    private String pin;

    public Account(String accountNumber, String name, int age, double balance, String accountType, String status, String pin) {
        if (age < 18) {
            throw new IllegalArgumentException("Customer age must be 18 or above");
        }
        if (balance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative");
        }
        if (pin == null || !pin.matches("\\d{4}")) {
            throw new IllegalArgumentException("PIN must be 4 digits");
        }
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
        if (!validatePin(oldPin)) {
            return false;
        }
        if (newPin == null || !newPin.matches("\\d{4}")) {
            return false;
        }
        this.pin = newPin;
        return true;
    }

    public boolean deposit(double amount) {
        if (amount > 0) {
            this.balance += amount;
            return true;
        }
        return false;
    }

    public boolean withdraw(double amount, String enteredPin) {
        if (!validatePin(enteredPin)) {
            return false;
        }
        if (!"ACTIVE".equalsIgnoreCase(this.status)) {
            return false;
        }
        if (amount > 0 && amount <= this.balance) {
            this.balance -= amount;
            return true;
        }
        return false;
    }

    public void suspend() { this.status = "SUSPENDED"; }
    public void activate() { this.status = "ACTIVE"; }
    public void close() { this.status = "CLOSED"; }

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
