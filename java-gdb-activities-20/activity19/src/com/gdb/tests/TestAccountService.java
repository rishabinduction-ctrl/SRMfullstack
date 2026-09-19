package com.gdb.tests;

import com.gdb.domain.IAccount;
import com.gdb.domain.Transaction;
import com.gdb.command.TransactionCommand;
import com.gdb.logging.*;
import com.gdb.service.AccountService;
import com.gdb.exceptions.AccountException;
import com.gdb.exceptions.InvalidPinException;
import java.util.List;

public class TestAccountService {
    public static void main(String[] args) throws Exception {
        System.out.println("=".repeat(60));
        System.out.println("  ACTIVITY 19 — ACCOUNT SERVICE DEMO");
        System.out.println("=".repeat(60));

        // ============================================================
        // 📝 STEP 12: Set Up The Service
        //
        // INSTRUCTIONS:
        //   1. LogDestination dest = new MemoryLogDestination();
        //   2. TransactionLogger logger = new TransactionLogger(dest);
        //   3. AccountService service = new AccountService(logger);
        // ============================================================
        // TODO: initialize MemoryLogDestination, TransactionLogger, and AccountService

        // ============================================================
        // 📝 STEP 13: Open Two Accounts
        //
        // INSTRUCTIONS:
        //   1. IAccount john = service.openAccount("SAVINGS", "John Doe", 25, 15000);
        //   2. john.setPin(1234);
        //   3. IAccount jane = service.openAccount("SAVINGS", "Jane Smith", 30, 10000);
        //   4. jane.setPin(5678);
        //   5. Print both accounts using getAccountInfo().
        // ============================================================
        // TODO: open accounts for John and Jane

        // ============================================================
        // 📝 STEP 14: Deposit into John's Account
        //
        // INSTRUCTIONS:
        //   1. Transaction txn = service.deposit(john.getAccountNumber(), 5000);
        //   2. Print txn.
        // ============================================================
        // TODO: execute deposit through service

        // ============================================================
        // 📝 STEP 15: Withdraw from John's Account
        //
        // INSTRUCTIONS:
        //   1. Transaction wtxn = service.withdraw(john.getAccountNumber(), 2000, 1234);
        //   2. Print wtxn.
        // ============================================================
        // TODO: execute withdrawal through service

        // ============================================================
        // 📝 STEP 16: Transfer from John to Jane
        //
        // INSTRUCTIONS:
        //   1. Transaction ttxn = service.transfer(john.getAccountNumber(), jane.getAccountNumber(), 1000, 1234);
        //   2. Print ttxn.
        // ============================================================
        // TODO: execute transfer through service

        // ============================================================
        // 📝 STEP 17: Print Final Balances
        //
        // INSTRUCTIONS:
        //   Print john.getBalance() and jane.getBalance().
        // ============================================================
        // TODO: print updated balances

        // ============================================================
        // 📝 STEP 18: Print Transaction History
        //
        // INSTRUCTIONS:
        //   1. List<TransactionCommand> history = service.getTransactionHistory();
        //   2. Print size and each command's transaction.
        // ============================================================
        // TODO: print full transaction history

        // ============================================================
        // 📝 STEP 19: Test Error Cases
        //
        // INSTRUCTIONS:
        //   1. Try deposit to non-existent account 9999 -> catch AccountException.
        //   2. Try withdraw with wrong PIN -> catch InvalidPinException.
        // ============================================================
        // TODO: verify exception handling for invalid operations
    }
}
