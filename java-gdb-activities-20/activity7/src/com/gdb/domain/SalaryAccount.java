package com.gdb.domain;

// TODO: Step 4.1 - Make SalaryAccount extend Account.
public class SalaryAccount {
    // TODO: Step 4.2 - Declare private fields employerName (String) and inactiveMonths (int, default 0).

    public SalaryAccount(String accountNumber, String name, int age, double balance, String status, String pin) {
        // TODO: Step 4.3 - Call super(...) as the FIRST statement, passing "SALARY" as the account type.
    }

    public SalaryAccount(String accountNumber, String name, int age, double balance, String status, String pin, String employerName) {
        // TODO: Step 4.3 - Call super(...) with "SALARY", then store employerName and set inactiveMonths to 0.
    }

    // TODO: Accessors for the new fields (getEmployerName is used by the test program;
    //   the inactiveMonths helpers are used in later activities).
    public String getEmployerName() {
        return null;
    }

    public int getInactiveMonths() {
        return 0;
    }

    public void setInactiveMonths(int inactiveMonths) {
    }

    public void incrementInactiveMonths() {
    }
}
