package com.gdb.exceptions;

// TODO: Step 1 - AccountException is the base class for every banking exception.
//   It already extends Exception (making it a checked exception) so the rest of the project compiles.
//   Add a public constructor that takes a String message and passes it to the parent with super(message).
//   Note: once this constructor exists, every subclass from Step 2 must declare its own constructor too.
public class AccountException extends Exception {
}
