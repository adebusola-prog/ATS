'''Create a User class that can be instantiated with the attributes username, first_name, last_name, email and password. 
Email should be a read only attribute and password should be a private method. 
Define methods that can be used to update each of the attributes. 
Define methods that can be used to get the values for email and password. Submission is tomorrow morning'''
class User:
    def __init__(self, firstname, lastname, username, email, password):
    
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self._email = email
        self.__password = password

    def update_firstname(self, new_firstname):
        self.first_name = new_firstname
        return self.first_name

    def update_lastname(self, new_lastname):
        self.last_name = new_lastname
        # return self.last_name

    def update_username(self, new_username):
        self.username = new_username
        return self.username

    def update_email(self, new_email):
        self._email = new_email
        # return self._email

    def update_password(self, new_password):
        self.__password = new_password
        return self.__password

    def get_password(self):
        return self.__password

    def get_email(self):
        return self._email



user1 = User("Adebusola", "Adeyeye", "Adebusola Adeyeye", "adeiyanu@gmail.com", "debbi345")
# print(user1.update_firstname("Dele"))
# print(user1.update_lastname("Safa"))
# print(user1.update_username("Dele Safa"))
print(user1.get_email())
user1.update_email("dele@gmail.com")
print(user1.get_email())
# print(user1.update_password("rett56"))
# print(user1.get_password())










































