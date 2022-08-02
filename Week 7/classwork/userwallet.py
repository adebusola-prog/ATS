# Create a user class, wallet, transaction class
# Each of the other classes should inherit from the User class

 

# Update your code such that some operations can be perform on the user class such as
# 1. Creating a user
# 2. Deleting
# 3. Funding the wallet
# 4. Logging transactions


class User:
    def __init__(self):
        print("You are welcome!!!")
        
    
    def sign_up(self):
        self.firstname = input("enter your firstname")
        self.lastname = input("enter your lastname")
        self.username = self.__firstname + self.__lastname
        self.password = input("enter your password")
        if self.password.isalnum() and len(self.password) > 6:
            print("correct password")
            return self.password
        return self.sign_up()

    def logging_transaction(self):
        usr_name = input("enter your user_name")
        pass_wrd = input("enter your password")
        if usr_name == self.username and pass_wrd == self.password :
            print("you are logged in")
        else:
            return self.logging_transaction()


    def funding_wallet(self, balance, amount):
        self.logging_transaction()
        print(balance + amount)
        if balance < 0:
            raise ValueError("your balance cannot be less than zero")
        else:
            print("your wallet has been funded")
        


    def deleting(self):
        delete = input("Do you want to delete your account? \n Yes or no?")
        if delete == "yes" or delete == "Yes":
            print("your wallet has been deleted")
        else:
            print("Your wallet is intact")

        
class Wallet(User):
    pass


class Transaction(User):
    pass


r = Wallet()
# m = Transaction()
# r.sign_up()
# r.logging_transaction()
# print(r.funding_wallet(-1, 4000))
# r.deleting()


