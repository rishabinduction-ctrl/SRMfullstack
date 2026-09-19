package com.gdb.tests;

import com.gdb.domain.*;

public class TestInterfaceFactory {
    public static void main(String[] args) {
        System.out.println("=== Activity 11: Interface & Factory Pattern Test ===");
        IAccount acc1 = AccountFactory.createAccount("SAVINGS", "SAV1001", "Rajesh Sharma", 28, 5000.0, "ACTIVE", "1234");
        System.out.println("Factory created: " + acc1.getAccountType() + " account for " + acc1.getName());

        IAccount acc2 = AccountFactory.createAccount("CURRENT", "CUR1001", "Priya Patel", 34, 10000.0, "ACTIVE", "5678");
        System.out.println("Factory created: " + acc2.getAccountType() + " account for " + acc2.getName());

        IAccount acc3 = AccountFactory.createAccount("FIXED_DEPOSIT", "FD1001", "Amit Kumar", 45, 50000.0, "ACTIVE", "1111");
        System.out.println("Factory created: " + acc3.getAccountType() + " account for " + acc3.getName());

        IAccount acc4 = AccountFactory.createAccount("SALARY", "SAL1001", "Sneha Verma", 26, 30000.0, "ACTIVE", "2222");
        System.out.println("Factory created: " + acc4.getAccountType() + " account for " + acc4.getName());

        System.out.println("All accounts successfully created through AccountFactory!");
    }
}
