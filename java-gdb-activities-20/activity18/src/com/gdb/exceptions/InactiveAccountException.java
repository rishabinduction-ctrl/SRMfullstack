package com.gdb.exceptions;

/**
 * Domain exception thrown when financial operations are attempted on a closed or inactive account.
 */
public class InactiveAccountException extends AccountException {

    /**
     * Constructs an InactiveAccountException detailing account inactive status state.
     *
     * @param message Detailed diagnostic string explaining inactive account status.
     */
    public InactiveAccountException(String message) {
        // Forward diagnostic detail message to AccountException parent class
        super(message);
    }
}
