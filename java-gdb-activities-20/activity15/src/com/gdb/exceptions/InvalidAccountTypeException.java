package com.gdb.exceptions;

/**
 * Domain exception thrown when an unsupported or unrecognized account category string is supplied.
 */
public class InvalidAccountTypeException extends AccountException {

    /**
     * Constructs an InvalidAccountTypeException detailing the invalid account type category.
     *
     * @param message Detailed diagnostic string explaining the unrecognized account type.
     */
    public InvalidAccountTypeException(String message) {
        // Forward diagnostic detail message to AccountException parent class
        super(message);
    }
}
