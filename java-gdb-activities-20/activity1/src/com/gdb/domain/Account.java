package com.gdb.domain;

public class Account {
    // TODO: Step 1 - Declare the 6 private fields:
    // - accountNumber (String)
    // - name (String)
    // - age (int)
    // - balance (double)
    // - accountType (String)
    // - status (String)

    public Account(String accountNumber, String name, int age, double balance, String accountType, String status) {
        // TODO: Step 2 - Initialize instance variables with parameters
    }

    public boolean deposit(double amount) {
        // TODO: Step 3 - Validate amount > 0, increase balance, and return true; return false otherwise
        return false;
    }

    public boolean withdraw(double amount) {
        // TODO: Step 4 - Validate amount > 0 and balance >= amount, deduct from balance, and return true; return false otherwise
        return false;
    }

    public void displayAccountInfo() {
        // TODO: Step 5 - Print formatted account information (AccountNumber, Name, Age, Balance, AccountType, Status)
    }

    // TODO: Step 6 - Declare public getters and setters for all private fields
}
