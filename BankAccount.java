import java.util.ArrayList;
import java.util.List;

/**
 * GreenLeaf Bank — Legacy BankAccount class
 *
 * This class is intentionally messy.
 * It mixes account state, validation, persistence, notification,
 * statement formatting, and interest calculation all in one place.
 * Refactor this across by implementing the lab tasks onward.
 */
public class BankAccount {

    private int accountNumber;
    private String name;
    private int age;
    private double balance;
    private String status;
    private Integer pin;
    private String accountType; // "Savings" or "Current"

    // Every deposit/withdrawal gets logged here as a plain string —
    // logging logic is mixed directly into deposit()/withdraw().
    private List<String> transactionLog = new ArrayList<>();

    public BankAccount(int accountNumber, String name, int age, double balance, String accountType) {

        // Validation logic mixed directly into the constructor
        if (age < 18) {
            System.out.println("Age was below 18, correcting to 18");
            age = 18;
        }

        double minimumBalance = accountType.equals("Savings") ? 500.0 : 1000.0;
        if (balance < minimumBalance) {
            System.out.println("Initial balance below minimum, correcting to " + minimumBalance);
            balance = minimumBalance;
        }

        this.accountNumber = accountNumber;
        this.name = name;
        this.age = age;
        this.balance = balance;
        this.accountType = accountType;
        this.status = "Active";
        this.pin = null;
    }

    // ----------------------------------------------------
    // Account operations, tangled with logging + notification
    // ----------------------------------------------------

    public boolean deposit(double amount) {

        if (!status.equals("Active")) {
            System.out.println("Account is not active");
            return false;
        }

        if (amount <= 0) {
            System.out.println("Invalid deposit amount");
            return false;
        }

        balance += amount;

        // Logging responsibility, baked directly into deposit()
        transactionLog.add("DEPOSIT: Rs. " + amount + " | New balance: " + balance);

        // Notification responsibility, baked directly into deposit()
        sendEmail(name, "Your deposit of Rs. " + amount + " was successful. New balance: " + balance);

        // Persistence responsibility, baked directly into deposit()
        saveToDatabase();

        return true;
    }

    public boolean withdraw(double amount, Integer enteredPin) {

        if (!status.equals("Active")) {
            System.out.println("Account is not active");
            return false;
        }

        if (pin != null) {
            if (enteredPin == null || !enteredPin.equals(pin)) {
                System.out.println("Incorrect PIN");
                return false;
            }
        }

        if (amount <= 0) {
            System.out.println("Invalid withdrawal amount");
            return false;
        }

        double minimumBalance = accountType.equals("Savings") ? 500.0 : 1000.0;
        if (balance - amount < minimumBalance) {
            System.out.println("Withdrawal would breach minimum balance");
            return false;
        }

        balance -= amount;

        transactionLog.add("WITHDRAW: Rs. " + amount + " | New balance: " + balance);

        sendEmail(name, "Your withdrawal of Rs. " + amount + " was successful. New balance: " + balance);

        saveToDatabase();

        return true;
    }

    public boolean closeAccount() {
        if (status.equals("Inactive")) return false;
        status = "Inactive";
        sendEmail(name, "Your account has been closed.");
        saveToDatabase();
        return true;
    }

    public boolean reopenAccount() {
        if (status.equals("Active")) return false;
        status = "Active";
        sendEmail(name, "Your account has been reopened.");
        saveToDatabase();
        return true;
    }

    public boolean setPin(int newPin) {
        if (newPin >= 1000 && newPin <= 9999) {
            this.pin = newPin;
            return true;
        }
        return false;
    }

    public boolean verifyPin(int enteredPin) {
        return pin != null && pin.equals(enteredPin);
    }

    // ----------------------------------------------------
    // Interest calculation — an if/else chain baked into the account itself
    // ----------------------------------------------------

    public double calculateInterest() {
        if (accountType.equals("Savings")) {
            return balance * 0.04;
        } else if (accountType.equals("Current")) {
            return balance * 0.01;
        } else {
            return 0.0;
        }
    }

    // ----------------------------------------------------
    // "Persistence" — pretend database logic living inside the account
    // ----------------------------------------------------

    private void saveToDatabase() {
        // Pretend this talks to MySQL. In reality just prints.
        System.out.println("[DB] Saving account " + accountNumber + " to MySQL...");
    }

    // ----------------------------------------------------
    // "Notification" — pretend email logic living inside the account
    // ----------------------------------------------------

    private void sendEmail(String recipient, String message) {
        // Pretend this talks to an SMTP server. In reality just prints.
        System.out.println("[EMAIL] To: " + recipient + " | " + message);
    }

    // ----------------------------------------------------
    // "Statement generation" — formatting logic living inside the account
    // ----------------------------------------------------

    public void printStatement() {
        System.out.println("---- Statement for Account #" + accountNumber + " (" + name + ") ----");
        for (String entry : transactionLog) {
            System.out.println(entry);
        }
        System.out.println("Current Balance: Rs. " + balance);
        System.out.println("-----------------------------------------------------");
    }

    // ----------------------------------------------------
    // Getters
    // ----------------------------------------------------

    public int getAccountNumber() { return accountNumber; }
    public String getName() { return name; }
    public int getAge() { return age; }
    public double getBalance() { return balance; }
    public String getStatus() { return status; }
    public String getAccountType() { return accountType; }
    public boolean hasPin() { return pin != null; }
}
