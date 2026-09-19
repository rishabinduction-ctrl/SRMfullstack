package com.gdb.exceptions;

/**
 * Domain exception thrown when customer profile data violates age policy rules (e.g. age under 18).
 */
public class InvalidAgeException extends AccountException {

    /**
     * Constructs an InvalidAgeException detailing the age boundary violation.
     *
     * @param message Detailed diagnostic string explaining the invalid age input.
     */
    public InvalidAgeException(String message) {
        // Forward diagnostic detail message to AccountException parent class
        super(message);
    }
}
