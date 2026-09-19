package com.gdb.exceptions;

/**
 * Domain exception thrown when withdrawal authorization fails due to incorrect or unconfigured PIN.
 */
public class InvalidPinException extends AccountException {

    /**
     * Constructs an InvalidPinException detailing PIN authorization failure.
     *
     * @param message Detailed diagnostic string explaining PIN authorization failure cause.
     */
    public InvalidPinException(String message) {
        // Forward diagnostic detail message to AccountException parent class
        super(message);
    }
}
