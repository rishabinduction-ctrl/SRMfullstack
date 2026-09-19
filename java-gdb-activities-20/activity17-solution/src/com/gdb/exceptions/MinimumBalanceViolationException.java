package com.gdb.exceptions;

/**
 * Domain exception thrown when a transaction would cause balance to fall below required minimum limits.
 */
public class MinimumBalanceViolationException extends AccountException {

    /**
     * Constructs a MinimumBalanceViolationException detailing the minimum balance rule violated.
     *
     * @param message Detailed diagnostic string explaining post-transaction balance failure.
     */
    public MinimumBalanceViolationException(String message) {
        // Forward diagnostic detail message to AccountException parent class
        super(message);
    }
}
