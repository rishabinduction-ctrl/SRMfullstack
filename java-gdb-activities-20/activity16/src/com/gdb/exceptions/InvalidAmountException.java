package com.gdb.exceptions;

/**
 * Domain exception thrown when a non-positive monetary amount (zero or negative) is supplied to a transaction.
 */
public class InvalidAmountException extends AccountException {

    /**
     * Constructs an InvalidAmountException detailing the invalid monetary input amount.
     *
     * @param message Detailed diagnostic string specifying the invalid numeric amount.
     */
    public InvalidAmountException(String message) {
        // Forward diagnostic detail message to AccountException parent class
        super(message);
    }
}
