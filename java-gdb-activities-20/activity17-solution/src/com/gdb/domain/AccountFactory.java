package com.gdb.domain;

import com.gdb.exceptions.*;

/**
 * AccountFactory Creational Pattern supporting SAVINGS, CURRENT, and FIXEDDEPOSIT creation with dynamic rules.
 */
public class AccountFactory {

    public static IAccount createAccount(String accountType, int accountNumber, String name, int age, double initialBalance)
            throws AccountException {
        return createAccount(accountType, accountNumber, name, age, initialBalance, 0);
    }

    public static IAccount createAccount(String accountType, int accountNumber, String name, int age, double initialBalance, int tenureYears)
            throws AccountException {
        if (accountType == null || accountType.trim().isEmpty()) {
            throw new InvalidAccountTypeException("Unknown account type: " + accountType);
        }
        
        String typeUpper = accountType.trim().toUpperCase();
        
        switch (typeUpper) {
            case "SAVINGS":
                return new SavingsAccount(accountNumber, name, age, initialBalance, tenureYears);
            case "CURRENT":
                return new CurrentAccount(accountNumber, name, age, initialBalance, tenureYears);
            case "FIXEDDEPOSIT":
                return new FixedDepositAccount(accountNumber, name, age, initialBalance, tenureYears);
            default:
                throw new InvalidAccountTypeException("Unknown account type: " + accountType);
        }
    }
}
