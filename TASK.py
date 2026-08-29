
"""
Activity 3: Enhanced Account Model
===================================

In Activity 2, we implemented a basic `Account` class with core
account operations such as deposits, withdrawals, and balance tracking.

Today, we shall enhance the Account model to make it more robust, secure, and
closer to a real-world banking system.

Your Task
---------
Enhance the existing `Account` class by implementing the following:

1. Minimum Balance Rules
   - Savings accounts must maintain a minimum balance of Rs. 500.
   - Current accounts must maintain a minimum balance of Rs. 1000.
   - A withdrawal must be rejected if it causes the balance to fall
     below the applicable minimum balance.

2. Defensive Account Creation
   When creating an account:
   - If the customer's age is below 18, get a guardian's name & age and create account for customer
   - If the account type is invalid, default it to "Savings".
   - If the initial balance is below the minimum balance requirement,
     automatically set the balance to the applicable minimum balance.

3. Account Status
   Every account should have one of two states:
       - "Active"
       - "Inactive"

   Implement:
       - close_account()
       - reopen_account()

   Rules:
   - A closed account must not allow deposits or withdrawals.
   - Closing an already inactive account should fail.
   - Reopening an already active account should fail.

4. PIN Security
   Add support for an optional 4-digit PIN.

   Implement:
       - set_pin(pin)
       - verify_pin(pin)
       - has_pin()

   Rules:
   - Only PINs from 1000 to 9999 are valid.
   - If a PIN has been configured, withdrawals must provide
     the correct PIN.
   - If no PIN has been configured, withdrawals should continue
     to work without requiring a PIN.

5. Properties
   Continue exposing account information using read-only properties:
       - account_number
       - name
       - age
       - balance
       - account_type
       - status

Think About
-----------
- Why should minimum balances be stored as class constants?
- How can defensive programming prevent invalid account states?
- How should account status control financial operations?
- How can `None` be used to represent an unconfigured PIN?
- How can short-circuit boolean logic make PIN verification safe?

Example
-------
    account = Account(101, "Ravi", 17, 200, "Savings")

    # Age -> 18
    # Account Type -> Savings
    # Balance -> Rs. 500

    account.deposit(1000)
    account.set_pin(1234)

    account.withdraw(200, 1234)   # Allowed
    account.withdraw(200)         # Rejected - PIN required

    account.close_account()

    account.deposit(500)          # Rejected - account is inactive

    account.reopen_account()

Goal
----
Transform the basic Account model from Activity 2 into a more
defensive, state-aware, and secure banking domain model.

"""