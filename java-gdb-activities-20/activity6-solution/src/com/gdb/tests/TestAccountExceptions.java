package com.gdb.tests;

import com.gdb.domain.Account;
import com.gdb.exceptions.*;

public class TestAccountExceptions {
    public static void main(String[] args) {
        System.out.println("=== Activity 6: Exception Handling Suite ===");
        Account acc = new Account("ACC1001", "Rajesh Sharma", 28, 5000.0, "SAVINGS", "ACTIVE", "1234");

        // Test 1: Invalid PIN handling
        try {
            acc.withdraw(1000.0, "9999");
            System.out.println("[Test 1] [FAIL]");
        } catch (InvalidPinException e) {
            System.out.println("[Test 1] Caught Invalid PIN: " + e.getMessage() + " [PASS]");
        } catch (AccountException e) {
            System.out.println("[Test 1] [FAIL]");
        }

        // Test 2: Inactive Account handling
        acc.suspend();
        try {
            acc.withdraw(1000.0, "1234");
            System.out.println("[Test 2] [FAIL]");
        } catch (InactiveAccountException e) {
            System.out.println("[Test 2] Caught Inactive Account: " + e.getMessage() + " [PASS]");
        } catch (AccountException e) {
            System.out.println("[Test 2] [FAIL]");
        }

        // Test 3: Invalid Amount handling
        acc.activate();
        try {
            acc.deposit(-500.0);
            System.out.println("[Test 3] [FAIL]");
        } catch (InvalidAmountException e) {
            System.out.println("[Test 3] Caught Invalid Amount: " + e.getMessage() + " [PASS]");
        }

        // Test 4: Insufficient Funds handling
        try {
            acc.withdraw(10000.0, "1234");
            System.out.println("[Test 4] [FAIL]");
        } catch (InsufficientBalanceException e) {
            System.out.println("[Test 4] Caught Insufficient Funds: " + e.getMessage() + " [PASS]");
        } catch (AccountException e) {
            System.out.println("[Test 4] [FAIL]");
        }

        // Test 5: Polymorphic Catch with Base Class
        acc.close();
        try {
            acc.withdraw(500.0, "1234");
            System.out.println("[Test 5] [FAIL]");
        } catch (AccountException e) {
            System.out.println("[Test 5] Polymorphic Handler caught: " + e.getMessage() + " [PASS]");
        }

        System.out.println("All exception handling tests completed successfully!");
    }
}
