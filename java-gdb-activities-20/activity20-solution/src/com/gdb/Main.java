package com.gdb;

import com.gdb.logging.FileLogDestination;
import com.gdb.logging.LogDestination;
import com.gdb.logging.TransactionLogger;
import com.gdb.service.AccountService;
import com.gdb.ui.AccountUI;

public class Main {
    public static void main(String[] args) {
        System.out.println("Booting Global Digital Bank...");

        LogDestination destination = new FileLogDestination();
        TransactionLogger logger = new TransactionLogger(destination);
        AccountService service = new AccountService(logger);
        AccountUI ui = new AccountUI(service);
        ui.start();
    }
}
