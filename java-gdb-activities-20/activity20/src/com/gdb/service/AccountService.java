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
    private final Map<Integer, IAccount> accounts;
    private final TransactionLogger logger;
    private final TransferService transferService;
    private int nextAccountNumber;

    public AccountService(TransactionLogger logger) {
        this.logger = logger;
        this.accounts = new HashMap<>();
        this.transferService = new TransferService();
        this.nextAccountNumber = 1001;
    }

    public IAccount openAccount(String type, String name, int age, double initialBalance)
            throws AccountException {
        int accountNumber = nextAccountNumber++;
        IAccount account = AccountFactory.createAccount(type, accountNumber, name, age, initialBalance);
        accounts.put(accountNumber, account);
        return account;
    }

    public void closeAccount(int accountNumber, int pin) throws AccountException {
        IAccount account = accounts.get(accountNumber);
        if (account == null) {
            throw new AccountException("Account not found: " + accountNumber);
        }
        if (!account.verifyPin(pin)) {
            throw new InvalidPinException("Incorrect PIN");
        }
        account.closeAccount();
    }

    public Transaction deposit(int accountNumber, double amount) throws Exception {
        IAccount account = accounts.get(accountNumber);
        if (account == null) {
            throw new AccountException("Account not found: " + accountNumber);
        }
        DepositCommand cmd = new DepositCommand(account, amount);
        cmd.execute();
        if (logger != null) {
            logger.log(cmd);
        }
        return cmd.getTransaction();
    }

    public Transaction withdraw(int accountNumber, double amount, int pin) throws Exception {
        IAccount account = accounts.get(accountNumber);
        if (account == null) {
            throw new AccountException("Account not found: " + accountNumber);
        }
        WithdrawCommand cmd = new WithdrawCommand(account, amount, pin);
        cmd.execute();
        if (logger != null) {
            logger.log(cmd);
        }
        return cmd.getTransaction();
    }

    public Transaction transfer(int fromAccountNumber, int toAccountNumber,
                                double amount, int pin) throws Exception {
        IAccount fromAccount = accounts.get(fromAccountNumber);
        IAccount toAccount = accounts.get(toAccountNumber);
        if (fromAccount == null) {
            throw new AccountException("Source account not found: " + fromAccountNumber);
        }
        if (toAccount == null) {
            throw new AccountException("Destination account not found: " + toAccountNumber);
        }
        TransferCommand cmd = new TransferCommand(fromAccount, toAccount, amount, pin);
        cmd.execute();
        if (logger != null) {
            logger.log(cmd);
        }
        return cmd.getTransaction();
    }

    public IAccount getAccount(int accountNumber) {
        return accounts.get(accountNumber);
    }

    public List<IAccount> getAllAccounts() {
        return new ArrayList<>(accounts.values());
    }

    public List<TransactionCommand> getTransactionHistory() {
        return logger != null ? logger.readAll() : new ArrayList<>();
    }

    public int getNextAccountNumber() {
        return nextAccountNumber;
    }
}
