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
        return self.last_name

    def update_username(self, new_username):
        self.username = new_username
        return self.username

    def update_email(self, new_email):
        self._email = new_email
        return self._email

    def update_password(self, new_password):
        self.__password = new_password
        return self.__password

    @property
    def get_password(self):
        print("@propertymethod")
        return self.__password

    @get_password.setter
    def get_password(self, value):
        self.__password = value

    @property
    def get_email(self):
        return self._email
    
    @get_email.setter
    def get_email(self, value):
        print("@setter method" )
        self._email = value






user1 = User("Adebusola", "Adeyeye", "Adebusola Adeyeye", "adeiyanu@gmail.com", "debbi345")
# print(user1.update_firstname("Dele"))
# print(user1.update_lastname("Safa"))
# print(user1.update_username("Dele Safa"))
# print(user1.update_email("dele@gmail.com"))
# print(user1.update_password("rett56"))
# print(user1.get_password)
#@property method use the object to call it and then call the method in a variable form. note- 
# It takes just self and no other parameter 
user1.get_password = "ADE354"
print(user1.get_password)
# @settermethod first, name it with the method name used in @property (e.g @get_password.setter, it takes 2 parameter:self and the value
#  and then use the class name and not object to call it in a variable format. That is, it does not have a "()")
user1.get_password = "ATS"
print(user1.get_password)
user1.get_email = "derin@gmail.com"
print(user1.get_email)






