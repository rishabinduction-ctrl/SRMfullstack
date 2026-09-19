package com.gdb.domain;

import com.gdb.exceptions.*;

// TODO: Step 1.1 - Make SavingsAccount extend Account.
public class SavingsAccount {
    // TODO: Step 1.2 - Declare private double fields minBalance (default 1000.0) and interestRate (default 4.0).

    public SavingsAccount(String accountNumber, String name, int age, double balance, String status, String pin) {
        // TODO: Step 1.3 - Call super(...) as the FIRST statement, passing "SAVINGS" as the account type
        //   (check Account's constructor for the parameter order).
    }

    public SavingsAccount(String accountNumber, String name, int age, double balance, String status, String pin, double minBalance, double interestRate) {
        // TODO: Step 1.3 - Call super(...) with "SAVINGS", then store minBalance and interestRate in the fields.
    }

    public void applyInterest() {
        // TODO: Step 1.4 - Calculate interest = balance * (interestRate / 100.0) and add it to the balance.
        //   Tip: Account's fields are protected, so subclasses can use this.balance directly.
    }

    // TODO: Return the fields (the test program prints them).
    public double getMinBalance() {
        return 0.0;
    }

    public double getInterestRate() {
        return 0.0;
    }
}
