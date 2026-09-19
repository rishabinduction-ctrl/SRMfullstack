package com.gdb.domain;

import com.gdb.exceptions.*;

public class FixedDepositAccount extends AbstractAccount {
    private int tenureMonths;
    private double interestRate;

    public FixedDepositAccount(String accountNumber, String name, int age, double balance, String status, String pin, int tenureMonths, double interestRate) {
        super(accountNumber, name, age, balance, "FIXED_DEPOSIT", status, pin);
        this.tenureMonths = tenureMonths;
        this.interestRate = interestRate;
    }

    // TODO: Step 3.4 - Fixed Deposit debit rule (add @Override once processDebit is declared abstract in AbstractAccount):
    //   Premature withdrawals are never allowed, so always
    //   throw new AccountException("Premature withdrawal not allowed on Fixed Deposit")
    public void processDebit(double amount) throws AccountException {
    }

    public double calculateMaturityAmount() {
        return this.balance * Math.pow(1 + (interestRate / 100.0) / 12, 12 * (tenureMonths / 12.0));
    }

    public int getTenureMonths() { return tenureMonths; }
    public double getInterestRate() { return interestRate; }
}
