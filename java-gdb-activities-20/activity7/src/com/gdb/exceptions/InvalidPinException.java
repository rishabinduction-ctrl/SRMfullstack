package com.gdb.exceptions;

public class InvalidPinException extends AccountException {
    public InvalidPinException(String message) {
        super(message);
    }
}
