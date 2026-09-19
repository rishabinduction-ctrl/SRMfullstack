package com.gdb.exceptions;

/**
 * Root domain exception class for the Global Digital Bank (GDB) application core.
 * <p>
 * Architectural Role: Serves as the top-level parent checked exception for all custom
 * domain failures across banking entities, services, and factories.
 * Inheriting from java.lang.Exception mandates explicit exception handling across application layers.
 * </p>
 */
public class AccountException extends Exception {

    /**
     * Constructs a new AccountException with a diagnostic error message string.
     * Delegates message initialization to the java.lang.Exception superclass constructor.
     *
     * @param message Explanatory diagnostic string describing the failure cause.
     */
    public AccountException(String message) {
        // Forward diagnostic detail message to java.lang.Exception superclass
        super(message);
    }
}
