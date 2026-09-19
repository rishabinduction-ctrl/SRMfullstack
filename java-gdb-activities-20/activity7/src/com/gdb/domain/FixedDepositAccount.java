package com.gdb.domain;

// TODO: Step 3.1 - Make FixedDepositAccount extend Account.
public class FixedDepositAccount {
    // TODO: Step 3.2 - Declare private fields tenureMonths (int, default 12) and interestRate (double, default 6.5).

    public FixedDepositAccount(String accountNumber, String name, int age, double balance, String status, String pin) {
        // TODO: Step 3.3 - Call super(...) as the FIRST statement, passing "FIXED_DEPOSIT" as the account type.
    }

    public FixedDepositAccount(String accountNumber, String name, int age, double balance, String status, String pin, int tenureMonths, double interestRate) {
        // TODO: Step 3.3 - Call super(...) with "FIXED_DEPOSIT", then store tenureMonths and interestRate in the fields.
    }

    public double calculateMaturityAmount() {
        // TODO: Step 3.4 - Return the maturity amount using monthly compound interest:
        //   balance * (1 + monthlyRate) ^ tenureMonths, where monthlyRate = (interestRate / 100.0) / 12
        //   Hint: Math.pow(base, exponent).
        return 0.0;
    }

    // TODO: Return the fields (the test program prints them).
    public int getTenureMonths() {
        return 0;
    }

    public double getInterestRate() {
        return 0.0;
    }
}
