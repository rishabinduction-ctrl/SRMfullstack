package com.gdb.tests;

import com.gdb.domain.Account;
import com.gdb.exceptions.*;

public class TestAccountExceptions {
    public static void main(String[] args) {
        System.out.println("=== Activity 6: Exception Handling Suite ===");

        // NOTE: If you completed Activity 5 successfully, paste your working Account.java into src/com/gdb/domain and your exception classes into src/com/gdb/exceptions (replacing the provided versions).

        Account acc = new Account("ACC1001", "Rajesh Sharma", 28, 5000.0, "SAVINGS", "ACTIVE", "1234");

        // TODO: Step 1 - Test Invalid PIN Exception & Catch InvalidPinException specifically

        // TODO: Step 2 - Test Inactive Account Exception (Suspend account, attempt withdrawal, catch InactiveAccountException)

        // TODO: Step 3 - Test Invalid Amount Exception (Deposit negative amount, catch InvalidAmountException)

        // TODO: Step 4 - Test Insufficient Balance Exception (Withdraw > balance, catch InsufficientBalanceException)

        // TODO: Step 5 - Test Polymorphic Catch with Base AccountException (Close account, attempt withdrawal, catch AccountException)

        System.out.println("=== Complete Activity 6 exception handling tests and verify output ===");
    }
}
