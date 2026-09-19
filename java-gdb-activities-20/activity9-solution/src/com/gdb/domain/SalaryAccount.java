package com.gdb.domain;

import com.gdb.exceptions.*;

public class SalaryAccount extends AbstractAccount {
    private int inactiveMonths;
    private String employerName;

    public SalaryAccount(String accountNumber, String name, int age, double balance, String status, String pin, String employerName) {
        super(accountNumber, name, age, balance, "SALARY", status, pin);
        this.employerName = employerName;
        this.inactiveMonths = 0;
    }

    @Override
    public void processDebit(double amount) throws AccountException {
        if (amount > this.balance) {
            throw new InsufficientBalanceException("Insufficient funds in Salary account");
        }
        this.balance -= amount;
    }

    public String getEmployerName() { return employerName; }
    public int getInactiveMonths() { return inactiveMonths; }
    public void incrementInactiveMonths() { this.inactiveMonths++; }
}
