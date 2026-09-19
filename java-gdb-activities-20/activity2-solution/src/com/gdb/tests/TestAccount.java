package com.gdb.tests;

import com.gdb.domain.Account;

public class TestAccount {
    public static void main(String[] args) {
        System.out.println("=== Activity 2: Test Account Suite ===");
        
        Account acc = new Account("ACC1001", "Rajesh Sharma", 28, 5000.0, "SAVINGS", "ACTIVE");
        
        // Test 1: Initial Balance
        boolean t1 = (acc.getBalance() == 5000.0);
        System.out.println("Test 1 (Initial Balance 5000.0): " + (t1 ? "[PASS]" : "[FAIL]"));
        
        // Test 2: Valid Deposit
        boolean depSuccess = acc.deposit(2000.0);
        boolean t2 = (depSuccess && acc.getBalance() == 7000.0);
        System.out.println("Test 2 (Deposit 2000.0 -> Balance 7000.0): " + (t2 ? "[PASS]" : "[FAIL]"));
        
        // Test 3: Negative Deposit
        boolean negDep = acc.deposit(-500.0);
        boolean t3 = (!negDep && acc.getBalance() == 7000.0);
        System.out.println("Test 3 (Negative Deposit -> Rejected): " + (t3 ? "[PASS]" : "[FAIL]"));
        
        // Test 4: Valid Withdrawal
        boolean withSuccess = acc.withdraw(3000.0);
        boolean t4 = (withSuccess && acc.getBalance() == 4000.0);
        System.out.println("Test 4 (Withdraw 3000.0 -> Balance 4000.0): " + (t4 ? "[PASS]" : "[FAIL]"));
        
        // Test 5: Exceeding Withdrawal
        boolean overWith = acc.withdraw(10000.0);
        boolean t5 = (!overWith && acc.getBalance() == 4000.0);
        System.out.println("Test 5 (Exceeding Withdrawal -> Rejected): " + (t5 ? "[PASS]" : "[FAIL]"));
        
        // Test 6: Negative Withdrawal
        boolean negWith = acc.withdraw(-100.0);
        boolean t6 = (!negWith && acc.getBalance() == 4000.0);
        System.out.println("Test 6 (Negative Withdrawal -> Rejected): " + (t6 ? "[PASS]" : "[FAIL]"));
        
        System.out.println("All Account tests completed successfully!");
    }
}
