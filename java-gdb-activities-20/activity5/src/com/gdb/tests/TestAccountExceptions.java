package com.gdb.tests;

import com.gdb.domain.Account;
import com.gdb.exceptions.*;

public class TestAccountExceptions {
    public static void main(String[] args) {
        System.out.println("=== Activity 5: Custom Exceptions Test ===");
        Account acc = new Account("ACC1001", "Rajesh Sharma", 28, 5000.0, "SAVINGS", "ACTIVE", "1234");

        try {
            acc.withdraw(1000.0, "9999");
        } catch (InvalidPinException e) {
            System.out.println("Caught InvalidPinException as expected: " + e.getMessage());
        } catch (AccountException e) {
            System.out.println("Caught unexpected: " + e.getMessage());
        }

        acc.suspend();
        try {
            acc.withdraw(1000.0, "1234");
        } catch (InactiveAccountException e) {
            System.out.println("Caught InactiveAccountException as expected: " + e.getMessage());
        } catch (AccountException e) {
            System.out.println("Caught unexpected: " + e.getMessage());
        }

        acc.activate();
        try {
            acc.withdraw(-500.0, "1234");
        } catch (InvalidAmountException e) {
            System.out.println("Caught InvalidAmountException as expected: " + e.getMessage());
        } catch (AccountException e) {
            System.out.println("Caught unexpected: " + e.getMessage());
        }

        try {
            acc.withdraw(10000.0, "1234");
        } catch (InsufficientBalanceException e) {
            System.out.println("Caught InsufficientBalanceException as expected: " + e.getMessage());
        } catch (AccountException e) {
            System.out.println("Caught unexpected: " + e.getMessage());
        }

        try {
            acc.withdraw(1000.0, "1234");
            System.out.println("Successful withdrawal completed: Rs 1000.0 | New Balance: Rs " + acc.getBalance());
        } catch (AccountException e) {
            System.out.println("Withdrawal failed unexpectedly: " + e.getMessage());
        }
    }
}
