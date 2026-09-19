package com.gdb.domain;

// TODO: Step 2.1 - Make CurrentAccount extend Account.
public class CurrentAccount {
    // TODO: Step 2.2 - Declare a private double field overdraftLimit (default 25000.0).

    public CurrentAccount(String accountNumber, String name, int age, double balance, String status, String pin) {
        // TODO: Step 2.3 - Call super(...) as the FIRST statement, passing "CURRENT" as the account type.
    }

    public CurrentAccount(String accountNumber, String name, int age, double balance, String status, String pin, double overdraftLimit) {
        // TODO: Step 2.3 - Call super(...) with "CURRENT", then store overdraftLimit in the field.
    }

    // TODO: Step 2.4 - Getter and setter for overdraftLimit.
    public double getOverdraftLimit() {
        return 0.0;
    }

    public void setOverdraftLimit(double overdraftLimit) {
    }
}
