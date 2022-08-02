# while True:
#     pass_wrd = input("enter your password")
#     if not pass_wrd.isalnum():
#         raise Exception



# def funding_wallet(balance, amount):
#     print(balance + amount)
#     # if balance < 0:
#     #     raise ValueError("your balance cannot be less than zero")

#     # else:
#     #     print("your wallet has been funded")

#     try:
#         funding_wallet()
#     except TypeError as e:
#         print("int and not strings")
#     else:
#         funding_wallet()


# funding_wallet(20, 30)


from unicodedata import name


class Time:

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, ' + 
            f'second={self.second})')

    def __str__(self):
        """Print Time in 12-hour clock format."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) + 
        f':{self.minute:0>2}:{self.second:0>2}' + 
        (' AM' if self.hour < 12 else ' PM'))



t = Time(6, 30, 0)
# print(t)





# def validate_phone():
#         p_number = input(
#             'Kindly type the new phone number , (add your country code and omit the first zero in your phone number) ')
#         if len(p_number) == 14 and p_number.startswith('+'):
#             print("succesful")
#             return p_number
#         return validate_phone()


# validate_phone()

def gen_der():
    x = input("enter your gender by typing 1 for male, 2 for female and 3 for LQBTQ")
    if x == "1":
        return "Male"
    elif x == "2":
        return "Female"
    elif x == "3":
        return "LGBTQ-confused lots"
    else:
        print("no gender")
        return gen_der()



# print(gen_der())


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f" a {self.mileage} car"

    def __repr__(self):
       return (f'{self.__class__.__name__}('
           f'{self.color!r}, {self.mileage!r})')

my_car = Car("red", "345")
# print(my_car)
# print(my_car.color, my_car.mileage)
# print(str(my_car))
# print(repr(my_car))
# print('{}'.format(my_car))


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return '__str__ for car'

    def __repr__(self):
        return f'{self.mileage}'


# mycar = Car("red", [3452])
# print(mycar)
# print('{}'.format(mycar))
# print(repr(mycar))

# import datetime
# today = datetime.date.today()

# print(str(today))

# print(repr(today))


# print(__name__)

# print("first module's name: {}.format(__name__)")


#private vs public variables
class PlayerCharacter:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"my name is {self.__name} and I am {self.age} years old")




player1 = PlayerCharacter("andrei", 100)
# player1.__name = "!!!!!"
# print(player1.__name) #when you try to change the attribute name outside of the class and try to print it individually,
# player1.age =500    #it will print, but when you try to use the attribute in the function you have created, it won't change
# print(player1.age)
# player1.speak()
# player1.run()
# player1.__speak()


# player1.name = "!!!!!"


# player1.speak = "BOOO"
# player1.speak()



#property decorator- it allows us to define a class method that can be access like an attribute

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def email(self):
        return '{} {}'.format(self.first, self.last)
    
    
    def full_name(self):
        return '{} {}@email.com'.format(self.first, self.last)

emp1 = Employee("John", "Smith")
emp1.first = "Tola"
# print(emp1.first)
# print(emp1.last)
# print(emp1.email())






# def hello(func):
#     func()


# def greet():
#     print("I am still here")

# x = hello(greet)


# def summ(n):
#     n()


# def divide():
#     print(68/2)


# summ(divide)


def multiply(string, n , badwords):
    if string in badwords:
        return
    print(string * n)
    print()


# multiply("zzz", 20, "zzzaderep")


def piii(n):
    return n * 2

# print(piii("hello"))


def reset(time_left):
    # global time_left
    time_left = 0

def print_time():
    print(time_left)
    
# time_left=30    
# print_time()











class User():
    def __init__(self,email):
        self.email = email
        
    def sign_in(self):
        print("you are logged in")

    def attack(self):
        print("do nothing")

class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows : arrows left {self.num_arrows}")


# wizard1 = Wizard("Goblin", 50, "yeye@gmail.com")
# archer1 = Archer("Marioo", 90)
# wizard1.attack()
# print(wizard1.email)
# archer1.attack()
# wizard1.sign_in()
# archer1.sign_in()
# wizard1.attack ={"makaroni": 60}
# for x in wizard1.attack:
#     print(wizard1.attack["makaroni"])
# print(isinstance(wizard1, object))
def player_attack(char):
    char.attack()

# player_attack(archer1)

# for char in [wizard1, archer1]:
#     char.sign_in()



class Cube:
    def __init__(self, name, length_of_side="0.5cm"):
        self.name = name
        self.length_of_side = length_of_side

    def __str__(self):
        return f'{self.name} cube'


# maggi = Cube('Maggi', "0.4cm")
# print(maggi)
# print(maggi.name)
# print(maggi.length_of_side)

# choco_milo = Cube('Choco-Milo', "0.5cm")
# print(choco_milo)

class User():
    def sign_in(self):
        print("you are logged in")

    
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f"attacking with arrows : arrows left {self.num_arrows}")


    def run(self):
        print("ran really fast")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg("Bethlin", 20, 100) 
# print(hb1.check_arrows())























































































































