class BankAccount:

    def __init__(self, account_number, name, age, balance, account_type):

        # Validation logic mixed directly into the constructor
        if age < 18:
            print("Age was below 18, correcting to 18")
            age = 18

        minimum_balance = 500.0 if account_type == "Savings" else 1000.0

        if balance < minimum_balance:
            print(
                f"Initial balance below minimum, correcting to {minimum_balance}"
            )
            balance = minimum_balance

        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = balance
        self.account_type = account_type
        self.status = "Active"

        # Java Integer pin = null
        # Python equivalent is None
        self.pin = None

        # Java List<String> transactionLog = new ArrayList<>()
        # Python equivalent is a list
        self.transaction_log = []

    # ----------------------------------------------------
    # Account operations, tangled with logging + notification
    # ----------------------------------------------------

    def deposit(self, amount):

        if self.status != "Active":
            print("Account is not active")
            return False

        if amount <= 0:
            print("Invalid deposit amount")
            return False

        self.balance += amount

        # Logging responsibility
        self.transaction_log.append(
            f"DEPOSIT: Rs. {amount} | New balance: {self.balance}"
        )

        # Notification responsibility
        self.send_email(
            self.name,
            f"Your deposit of Rs. {amount} was successful. "
            f"New balance: {self.balance}"
        )

        # Persistence responsibility
        self.save_to_database()

        return True

    def withdraw(self, amount, entered_pin):

        if self.status != "Active":
            print("Account is not active")
            return False

        if self.pin is not None:

            if entered_pin is None or entered_pin != self.pin:
                print("Incorrect PIN")
                return False

        if amount <= 0:
            print("Invalid withdrawal amount")
            return False

        minimum_balance = (
            500.0 if self.account_type == "Savings" else 1000.0
        )

        if self.balance - amount < minimum_balance:
            print("Withdrawal would breach minimum balance")
            return False

        self.balance -= amount

        self.transaction_log.append(
            f"WITHDRAW: Rs. {amount} | New balance: {self.balance}"
        )

        self.send_email(
            self.name,
            f"Your withdrawal of Rs. {amount} was successful. "
            f"New balance: {self.balance}"
        )

        self.save_to_database()

        return True

    def close_account(self):

        if self.status == "Inactive":
            return False

        self.status = "Inactive"

        self.send_email(
            self.name,
            "Your account has been closed."
        )

        self.save_to_database()

        return True

    def reopen_account(self):

        if self.status == "Active":
            return False

        self.status = "Active"

        self.send_email(
            self.name,
            "Your account has been reopened."
        )

        self.save_to_database()

        return True

    def set_pin(self, new_pin):

        if 1000 <= new_pin <= 9999:
            self.pin = new_pin
            return True

        return False

    def verify_pin(self, entered_pin):

        return self.pin is not None and self.pin == entered_pin

    # ----------------------------------------------------
    # Interest calculation
    # ----------------------------------------------------

    def calculate_interest(self):

        if self.account_type == "Savings":
            return self.balance * 0.04

        elif self.account_type == "Current":
            return self.balance * 0.01

        else:
            return 0.0

    # ----------------------------------------------------
    # Persistence
    # ----------------------------------------------------

    def save_to_database(self):

        # Pretend this talks to MySQL
        print(
            f"[DB] Saving account {self.account_number} to MySQL..."
        )

    # ----------------------------------------------------
    # Notification
    # ----------------------------------------------------

    def send_email(self, recipient, message):

        # Pretend this talks to an SMTP server
        print(
            f"[EMAIL] To: {recipient} | {message}"
        )

    # ----------------------------------------------------
    # Statement generation
    # ----------------------------------------------------

    def print_statement(self):

        print(
            f"---- Statement for Account #{self.account_number} "
            f"({self.name}) ----"
        )

        for entry in self.transaction_log:
            print(entry)

        print(f"Current Balance: Rs. {self.balance}")

        print(
            "-----------------------------------------------------"
        )

    # ----------------------------------------------------
    # Getters
    # ----------------------------------------------------

    def get_account_number(self):
        return self.account_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_balance(self):
        return self.balance

    def get_status(self):
        return self.status

    def get_account_type(self):
        return self.account_type

    def has_pin(self):
        return self.pin is not None