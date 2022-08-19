# Create a user class, wallet, transaction class
# Each of the other classes should inherit from the User class
# Update your code such that some operations can be perform on the user class such as
# 1. Creating a user
# 2. Deleting
# 3. Funding the wallet
# 4. Logging transactions
import random
import string
import sys

class User:
    pin = string.digits
    my_user_name = string.ascii_letters
    info =[]


    def __init__(self, firstname:str, lastname:str, password):
        self.__firstname = firstname
        self.__lastname = lastname
        self.username = self.__firstname[0].lower() + self.__lastname[1:3].upper() + "".join(random.sample(User.my_user_name, 2))
        self.__password = password
        self.pin = "".join(random.sample(User.pin, 4))
        if self.__password.isalnum() and len(self.__password) > 6:
            print("correct password")
        
        User.info.append(self)
        
    def __str__(self):
        return f'"firtsname": {self.__firstname}, "lastname":{self.__lastname},"Username:"{self.username}, {self.pin}'

    @property
    def get_firstname(self):
        return self.__firstname

    @get_firstname.setter
    def get_firstname(self, new_firstname):
        self.__firstname = new_firstname

    @property
    def get_lastname(self):
        return self.__lastname

    @get_lastname.setter
    def get_lastname(self, new_lastname):
        self.__lastname = new_lastname
        
        # usr_name = input("enter your user_name")
        # pass_wrd = input("enter your password")
        # if usr_name == self.username and pass_wrd == self.password :
        #     print("you are logged in")
        # else:
        #     return self.logging_transaction()

    def deleting(self, delete):
        self.delete = delete
        if delete == "yes" or delete == "Yes":
            # print("your wallet has been deleted")
            sys.exit()
        print("Your wallet is intact")

        
class Wallet(User):
    def funding_wallet(self, balance, amount):
        self.logging_transaction()
        if balance > 0:
            return (f'your account balance is now-> N{balance + amount}')
        raise ValueError("your balance cannot be less than zero")


class Transaction(User):
    def logging_transaction(self):
        return (f'"Username":{self.username}, "you are logged in"')
    


# r = Wallet("Adebusola", "Adeyeye", "remi345667")
# # print(r)
# # print(r.pin)
# # print(User.info)
# r.get_firstname = "Iyanu"
# print(r.get_firstname)
# # print(User.firstname())
# r.get_lastname = "Grace"
# print(r.get_lastname)
# m = Transaction("Adebusola", "Adeyeye", "remi34566")
# print(r.logging_transaction())
# print(r.funding_wallet(5000, 4000))
# r.deleting("yes")

# x = "Adebusola"
# print(x.isalnum())
# # print(y)
# if x.isalnum() and len(x) > 6:
#     print(f'your password is correct')
# else:
#     print("you are wrong")




