package com.gdb.exceptions;

/**
 * Domain exception thrown when a withdrawal request exceeds total available account funds.
 */
public class InsufficientBalanceException extends AccountException {

    /**
     * Constructs an InsufficientBalanceException detailing requested vs available funds.
     *
     * @param message Detailed diagnostic string specifying balance state breakdown.
     */
    public InsufficientBalanceException(String message) {
        // Forward diagnostic detail message to AccountException parent class
        super(message);
    }
}
