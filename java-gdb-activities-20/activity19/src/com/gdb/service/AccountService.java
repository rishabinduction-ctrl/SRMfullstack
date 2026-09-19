package com.gdb.service;

import com.gdb.domain.IAccount;
import com.gdb.domain.Transaction;
import com.gdb.domain.AccountFactory;
import com.gdb.exceptions.AccountException;
import com.gdb.exceptions.InvalidPinException;
import com.gdb.logging.TransactionLogger;
import com.gdb.command.DepositCommand;
import com.gdb.command.WithdrawCommand;
import com.gdb.command.TransferCommand;
import com.gdb.command.TransactionCommand;

import java.util.*;

public class AccountService {
    // ============================================================
    // 📝 STEP 1: Declare Fields
    // ============================================================
    // TODO: declare accounts map, logger, transferService, and nextAccountNumber

    // ============================================================
    // 📝 STEP 2: Constructor
    //
    // INSTRUCTIONS:
    //   1. Accept TransactionLogger parameter.
    //   2. Assign this.logger = logger.
    //   3. Initialize accounts = new HashMap<>().
    //   4. Initialize transferService = new TransferService().
    //   5. Initialize nextAccountNumber = 1001.
    // ============================================================
    // TODO: implement constructor
    public AccountService(TransactionLogger logger) {
        // TODO: Step 2 - implement constructor
    }

    // ============================================================
    // 📝 STEP 3: Implement openAccount
    //
    // INSTRUCTIONS:
    //   1. int accountNumber = nextAccountNumber++;
    //   2. IAccount account = AccountFactory.createAccount(type, accountNumber, name, age, initialBalance);
    //   3. accounts.put(accountNumber, account);
    //   4. return account;
    // ============================================================
    // TODO: open and register a new account
    public IAccount openAccount(String type, String name, int age, double initialBalance)
            throws AccountException {
        // TODO: Step 3 - implement openAccount
        return null;
    }

    // ============================================================
    // 📝 STEP 4: Implement closeAccount
    //
    // INSTRUCTIONS:
    //   1. IAccount account = accounts.get(accountNumber);
    //   2. If null -> throw new AccountException("Account not found: " + accountNumber);
    //   3. If !account.verifyPin(pin) -> throw new InvalidPinException("Incorrect PIN");
    //   4. Call account.closeAccount();
    // ============================================================
    // TODO: close account after PIN verification
    public void closeAccount(int accountNumber, int pin) throws AccountException {
        // TODO: Step 4 - implement closeAccount
    }

    // ============================================================
    // 📝 STEP 5: Implement deposit
    //
    // INSTRUCTIONS:
    //   1. Look up account; throw AccountException if not found.
    //   2. DepositCommand cmd = new DepositCommand(account, amount);
    //   3. cmd.execute();
    //   4. logger.log(cmd);
    //   5. return cmd.getTransaction();
    // ============================================================
    // TODO: execute and log deposit command
    public Transaction deposit(int accountNumber, double amount) throws Exception {
        // TODO: Step 5 - implement deposit
        return null;
    }

    // ============================================================
    // 📝 STEP 6: Implement withdraw
    //
    // INSTRUCTIONS:
    //   1. Look up account; throw AccountException if not found.
    //   2. WithdrawCommand cmd = new WithdrawCommand(account, amount, pin);
    //   3. cmd.execute();
    //   4. logger.log(cmd);
    //   5. return cmd.getTransaction();
    // ============================================================
    // TODO: execute and log withdraw command
    public Transaction withdraw(int accountNumber, double amount, int pin) throws Exception {
        // TODO: Step 6 - implement withdraw
        return null;
    }

    // ============================================================
    // 📝 STEP 7: Implement transfer
    //
    // INSTRUCTIONS:
    //   1. Look up fromAccount and toAccount; throw AccountException if either missing.
    //   2. TransferCommand cmd = new TransferCommand(fromAccount, toAccount, amount, pin);
    //   3. cmd.execute();
    //   4. logger.log(cmd);
    //   5. return cmd.getTransaction();
    // ============================================================
    // TODO: execute and log transfer command
    public Transaction transfer(int fromAccountNumber, int toAccountNumber,
                                double amount, int pin) throws Exception {
        // TODO: Step 7 - implement transfer
        return null;
    }

    // ============================================================
    // 📝 STEP 8: Implement getAccount
    //
    // INSTRUCTIONS:
    //   return accounts.get(accountNumber);
    // ============================================================
    // TODO: return account by number
    public IAccount getAccount(int accountNumber) {
        // TODO: Step 8 - return account by number
        return null;
    }

    // ============================================================
    // 📝 STEP 9: Implement getAllAccounts
    //
    // INSTRUCTIONS:
    //   return new ArrayList<>(accounts.values());
    // ============================================================
    // TODO: return list of all active accounts
    public List<IAccount> getAllAccounts() {
        // TODO: Step 9 - return list of all active accounts
        return new ArrayList<>();
    }

    // ============================================================
    // 📝 STEP 10: Implement getTransactionHistory
    //
    // INSTRUCTIONS:
    //   return logger != null ? logger.readAll() : new ArrayList<>();
    // ============================================================
    // TODO: return all logged transaction commands
    public List<TransactionCommand> getTransactionHistory() {
        // TODO: Step 10 - return all logged transaction commands
        return new ArrayList<>();
    }

    // ============================================================
    // 📝 STEP 11: Implement getNextAccountNumber
    //
    // INSTRUCTIONS:
    //   return nextAccountNumber;
    // ============================================================
    // TODO: return next available account number
    public int getNextAccountNumber() {
        // TODO: Step 11 - return next available account number
        return 0;
    }
}
