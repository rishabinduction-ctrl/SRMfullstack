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

        // 📝 STEP 12 — Set up the service
        LogDestination dest = new MemoryLogDestination();
        TransactionLogger logger = new TransactionLogger(dest);
        AccountService service = new AccountService(logger);

        // 📝 STEP 13 — Open two accounts
        IAccount john = service.openAccount("SAVINGS", "John Doe", 25, 15000);
        john.setPin(1234);
        IAccount jane = service.openAccount("SAVINGS", "Jane Smith", 30, 10000);
        jane.setPin(5678);
        System.out.println("[STEP 13] Opened: " + john.getAccountInfo());
        System.out.println("[STEP 13] Opened: " + jane.getAccountInfo());

        // 📝 STEP 14 — Deposit into John's account
        Transaction txn = service.deposit(john.getAccountNumber(), 5000);
        System.out.println("\n[STEP 14] Deposit: " + txn);

        // 📝 STEP 15 — Withdraw from John's account
        Transaction wtxn = service.withdraw(john.getAccountNumber(), 2000, 1234);
        System.out.println("[STEP 15] Withdrawal: " + wtxn);

        // 📝 STEP 16 — Transfer from John to Jane
        Transaction ttxn = service.transfer(john.getAccountNumber(), jane.getAccountNumber(), 1000, 1234);
        System.out.println("[STEP 16] Transfer: " + ttxn);

        // 📝 STEP 17 — Print final balances
        System.out.println("\n[STEP 17] Final Balances:");
        System.out.println("  John (Account #" + john.getAccountNumber() + "): Rs. " + john.getBalance());
        System.out.println("  Jane (Account #" + jane.getAccountNumber() + "): Rs. " + jane.getBalance());

        // 📝 STEP 18 — Print transaction history
        List<TransactionCommand> history = service.getTransactionHistory();
        System.out.println("\n[STEP 18] Transaction History (" + history.size() + " records):");
        for (int i = 0; i < history.size(); i++) {
            System.out.println("  [" + (i + 1) + "] " + history.get(i).getTransaction());
        }

        // 📝 STEP 19 — Try invalid cases
        System.out.println("\n[STEP 19] Error Handling Checks:");
        try {
            service.deposit(9999, 1000);
        } catch (AccountException e) {
            System.out.println("  Deposit to missing account caught: " + e.getMessage() + " [PASS]");
        }

        try {
            service.withdraw(john.getAccountNumber(), 500, 9999);
        } catch (InvalidPinException e) {
            System.out.println("  Withdrawal with wrong PIN caught: " + e.getMessage() + " [PASS]");
        }
    }
}
