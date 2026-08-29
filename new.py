
nums = list()
print(f'{nums = }')
print(f'{type(nums) = }')

# Based on Parameter
# 1. Parametric
# 2. Non-Parametric

# Based on Return type
# 1. void
# 2. non-void

# Based on definition
# 1. Pre-defined
# 2. User-defined

# car = AutonomousCar()

# steering wheel
# engine
# gear
# accelerator

# car.drive()
# car.brake()
# car.wipe()


# public class Account {
#     private String name;
#     private int age;
#     private float balance; 

#     Account(String in_name, int in_age, float in_salary) {
        #  name = in_name;
#     }
    
# }

# public static void main(String args[]) {
#     Account user1 = new Account("Rishab", 25, 50000);
# }

# syntax to create a class
class className:
    pass

current_id = 1001


password = {}
details = {}

class Account:

    def __init__(self, in_name, in_age, in_balance):
        global current_id
        global password

        self.name = in_name
        self.age = in_age
        self.balance = in_balance
        self.PIN = 1234
        self.account_number = current_id

        details[self.account_number] = {
            'name': self.name,
            'age': self.age,
            'balance': self.balance,
            'PIN': self.PIN,
        }

        password[self.account_number] = 1234
        current_id += 1

    def showBalance(self):
        print(f'Current Balance: {self.balance}')

    def set_pin(self, pin: int):
        self.PIN = pin
        password[self.account_number] = self.PIN
        details[self.account_number]['PIN'] = self.PIN

    

user1 = Account("Rishab", 25, 50000)
user2 = Account("Divya", 30, 70000)

user1.set_pin(1231)
user2.set_pin(1232)


while True:
    input_ACC = int(input('Enter your ACC_ID: ')) # card implementation
    input_PIN = int(input('Enter your PIN: '))

    if password[input_ACC] == input_PIN:
        print(details[input_ACC])
    else:
        print("Invalid credentials, Retry!!!")
