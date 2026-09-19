package com.gdb.domain;

/**
 * Account - Enhanced bank account with PIN authentication, age validation, and status transitions.
 * Starts from the completed Activity 1 Account; the TODOs below are the Activity 3 upgrades.
 */
public class Account {
    private String accountNumber;
    private String name;
    private int age;
    private double balance;
    private String accountType;
    private String status;
    // TODO: Step 1 - Declare a private String field named pin (the customer's 4-digit security PIN).

    public Account(String accountNumber, String name, int age, double balance, String accountType, String status, String pin) {
        // TODO: Step 2 - Validate the inputs BEFORE assigning any field:
        //   1. age < 18                            -> throw new IllegalArgumentException("Customer age must be 18 or above")
        //   2. balance < 0                         -> throw new IllegalArgumentException("Initial balance cannot be negative")
        //   3. pin is null or not exactly 4 digits -> throw new IllegalArgumentException("PIN must be 4 digits")
        //      Hint: pin.matches("\\d{4}") is true only for exactly 4 digits.
        //   4. After the assignments below, also store the pin parameter in the pin field.
        this.accountNumber = accountNumber;
        this.name = name;
        this.age = age;
        this.balance = balance;
        this.accountType = accountType;
        this.status = status;
    }

    public boolean validatePin(String enteredPin) {
        // TODO: Step 3 - Return true only if enteredPin equals the stored pin.
        //   Return false if it does not match, or if enteredPin is null/empty.
        return false;
    }

    public boolean changePin(String oldPin, String newPin) {
        // TODO: Step 4 - Change the PIN:
        //   1. If validatePin(oldPin) is false, return false.
        //   2. If newPin is null or not exactly 4 digits, return false.
        //   3. Otherwise store newPin in the pin field and return true.
        return false;
    }

    public boolean deposit(double amount) {
        if (amount > 0) {
            this.balance += amount;
            return true;
        }
        return false;
    }

    public boolean withdraw(double amount, String enteredPin) {
        // TODO: Step 5 - PIN-protected withdrawal (replaces the Activity 1 withdraw):
        //   1. If validatePin(enteredPin) is false, return false.
        //   2. If the status is not "ACTIVE" (hint: "ACTIVE".equalsIgnoreCase(status)), return false.
        //   3. If amount > 0 and amount <= balance, subtract amount from balance and return true.
        //   4. Otherwise return false.
        return false;
    }

    public void suspend() {
        // TODO: Step 6.1 - Set status to "SUSPENDED".
    }

    public void activate() {
        // TODO: Step 6.2 - Set status to "ACTIVE".
    }

    public void close() {
        // TODO: Step 6.3 - Set status to "CLOSED".
    }

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
