# OOPs - Encapsulation, Abstraction, Inheritance, Polymorphism 


'''
Implement a class `Account` with the following features:
    1. Account Creation
    2. Deposit, Withdraw, Bank Transfer
    3. Account Deletion
    4. Authentication

Features:
name, balance, email, PIN

Actions:
    Account Creation,
    Deposit, Withdraw, Transfer,
    Account Deletion,
    Authentication
'''


'''
Create a User hashtable, which stores the account_id as the key
and the login credentials as the value {'email': mail@gmail.com, 'PIN': pin}
'''

'''
1 Login or 
2 SignUp
0 Exit


----- Login Page -----
1. Login as Customer
2. Login as Staff
'''


UserData = {}

current_account_id = 1001

class Account:
    def __init__(user, in_name, in_balance, in_email):
        global current_account_id        

        user.name = in_name
        user.balance = in_balance
        user.email = in_email
        user.account_id = current_account_id
        user.PIN = '1234'
        current_account_id += 1

        print(f'Account created successfully for {user.name}: {user.account_id} [PIN = 1234]')
        # global UserData
        # UserData[current_account_id] = {'email': in_email, 'PIN': 1234}
                

    # by default, all functions in a class
    # have the object as the first parameter

    def withdraw(user, amount: int):  # specify the amount to be withdrawn
        if 0 < amount < user.balance: # check for the sufficient balance
            user.balance -= amount    # deduct the amount from the balance
            return amount             # return the amount
        return 0                      # return 0 if amount cant be withdrawn

    def deposit(user, amount: int):   # specify the amount to be deposited 
        if amount > 0:                # if the amount is positive
            user.balance += amount    # add the amount to the balance
            return True               # return Success
        return False                  # return Failure otherwise

    def transfer(user, target_user, amount: int):     # specify the target_user and the amount to be transfered
        if target_user and 0 < amount < user.balance: # check if the target exists and balance is sufficient
            user.balance -= amount                    # deduct the amount from the user's balance
            target_user.balance += amount             # add the amount to the target's balance
            return True                               # return Success
        return False                                  # return Failure otherwise     

    def check_balance(user): # do not specify anything
        print(f'{user.balance = }')

    def reset_pin(user, new_pin: str): # specify the new pin
        global UserData
        if len(new_pin) == 4 and new_pin.isnumeric():
            user.PIN = new_pin
            UserData[user.account_id] = {'email': {user.email}, 'PIN': new_pin}
            return True
        return False

    def __repr__(user):
        return f"{user.name = }\n{user.account_id = }\n{user.balance = }\n{user.email = }\n\n"


# while True:
#     choice = int(input('Enter: ')) 

#     if choice == 0: # Exit the program
#         break

#     elif choice == 1: # Login as a Customer / Staff
#         # account_id <-> staff_id, email <-> email, PIN <->Password
#         ID = int(input('Enter your ID: '))
#         Mail = input('Enter your mail: ')
#         PWD = input('Enter your password: ')

#         if ID in UserData and UserData[ID]['email'] == Mail and UserData[ID]['PIN'] == PWD:
#             print('Authentication Successful')
#             print('DashBoard')

#     elif choice == 2: # Register as a Customer / Staff
#         user_type = input('Customer or Staff [C/S]: ').lower()

#         if user_type == 'c':
#             # Ask for account details
#             name, balance, mail = input('Enter your name, balance, mail: ')

#         elif user_type == 's':
#             # Ask for staff details
#             pass


class Student:
    # create a function named __init__ to call the Constructor
    def __init__(student, in_name, in_clg, in_dept):
        student.name = in_name
        student.clg = in_clg
        student.dept = in_dept


user1 = Account("Ramesh", 2000, "ramesh@gmail.com") # 1001, 1234
user2 = Account("Suresh", 4000, "suresh@gmail.com") # 1002, 1234
user3 = Account("Dinesh", 5000, "dinesh@gmail.com") # 1002, 1234
user4 = Account("Mukesh", 3000, "mukesh@gmail.com") # 1002, 1234

print('Sample Tests')
print('\nUser1 viewing his bank balance')
user1.check_balance()

print('\nUser3 deposits 4000')
print('Before')
print(user3)
user3.deposit(4000)
print('After')
print(user3)

print('\nUser4 withdraws 400000')
print('Before')
print(user4)
user4.withdraw(400000)
print('After')
print(user4)

print('\nBefore User1 transfering 500 to User2')
print(user1)
print(user2)
user1.transfer(user2, 500)
print('After User1 transfering 500 to User2')
print(user1)
print(user2)

