# OOP - Object Oriented Programming Paradigm
current_acc_number = 1001
default_PIN = 1234

class Account:
    
    def __init__(user, inp_name, inp_balance, inp_PAN, inp_email, inp_phone, inp_acc_type = 'savings', inp_age = 18):
        global current_acc_number
        global default_PIN

        user.name = inp_name
        user.balance = inp_balance
        user.PAN = inp_PAN
        user.email = inp_email
        user.phone = inp_phone
        user.acc_type = inp_acc_type
        user.age = inp_age
        user.account_id = current_acc_number
        user.PIN = default_PIN

        current_acc_number += 1

    def deposit(user, amount: int) -> bool:
        if amount > 0:
            user.balance += amount
            return True
        return False

    def withdraw(user, amount: int):
        if 0 < amount < user.balance:
            user.balance -= amount
            return amount
        else:
            return 0
        
    def bank_tranfer(user, target_user, amount: int):
        if target_user and user.balance >= amount:
            user.balance -= amount
            target_user.balance += amount
            print("Transaction succesful!")
        else:
            print("Insufficient Balance")

    def view_balance(user):
        print(f'{user.balance = }')

    def reset_PIN(user):
        

    def close_account():
        pass

    def __str__(user):
        return f"ACCOUNT DETAILS\n{user.name = }\n{user.balance = }\n{user.PAN = }\n{user.email = }\n{user.phone = }\n{user.acc_type = }\n{user.age = }\n{user.account_id = }\n\n"
        

'''
Create a class `Account` that facilites
the following features:

1. Creating Bank Users
2. Allowing Withdrawal, Deposit, Bank Tranfers
3. Authentication 
4. ATM **

Oprations: (actions), deposit, withdraw, availLoan, bankTransfer, viewBalance, closeAccount
'''

PAN1 = 'ABCDE1234X'
PAN2 = 'ABCDF1235Y'

user1 = Account('ramesh', 10000, PAN1, 'ramesh@gmail.com', '9876543210', 'savings', 40)
user2 = Account('suresh', 20000, PAN2, 'suresh@gmail.com', '9876543211', 'current', 20)

# user1.bank_tranfer(user2, 5000)
# user1.bank_tranfer()

print(type(user1))