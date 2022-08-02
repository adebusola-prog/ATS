'''Create a User class that can be instantiated with the attributes username, first_name, last_name, email and password. 
Email should be a read only attribute and password should be a private method. 
Define methods that can be used to update each of the attributes. 
Define methods that can be used to get the values for email and password. Submission is tomorrow morning'''
profile = {"person1":{"first_name": "Adebusola", "last_name": "Adeyeye", "username": "Adebusola Adeyeye", "password": "remi345", "email": "adeiyanu@gmail.com"},
          "person2":{"first_name": "Adeola", "last_name": "Adebunmi", "username": "Adeola Adebunmi", "password": "67rehyure", "email": "bunmi345@gmail.com"}}



class User:
    def __init__(self, profile, person):
        self.data = profile[person]
        self.first_name = profile[person]["first_name"]
        self.last_name = profile[person]["last_name"]
        self.username = profile[person]["username"]
        self._email = profile[person]["email"]
        self.__password =profile[person]["password"]

    def update_firstname(self, new_firstname):
        self.first_name == new_firstname
        return self.data

    def update_lastname(self):
        self.data["first_name"] == "Adeola"
        self.data["last_name"] = "Iyinoluwa"
        return self.data

    def update_username(self):
        self.data["first_name"] == "Adebusola"
        self.data["username"] = "Adebusola Felix"
        return profile

    def update_email(self):
        self.data["first_name"] == "Adebusola"
        self.data["email"] = "adebusolafelix@gmail.com"
        return self.data 

    def update_password(self):
        self.data["first_name"] == "Adeola"
        self.data["password"] = "deret567"
        return self.data


    def get_email(self):
        return self.data["email"]

    def get_password(self):
        return self.data["password"]


user1 = User(profile, "person1")
user2 = User(profile, "person2")
print(user1.update_firstname("Dele"))
# print(user2.update_lastname())
# print(user1.update_username())
# print(user1.update_email())
# print(user2.update_password())
# print(user1.get_email())
# print(user2.get_password())

