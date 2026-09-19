package com.gdb.exceptions;

public class InactiveAccountException extends AccountException {
    public InactiveAccountException(String message) {
        super(message);
    }
}
