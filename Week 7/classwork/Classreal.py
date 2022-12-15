# Create a user class, wallet, transaction class
# Each of the other classes should inherit from the User class

 

# Update your code such that some operations can be perform on the user class such as
# 1. Creating a user
# 2. Deleting
# 3. Funding the wallet
# 4. Logging transactions


class User:
    def __init__(self, username, firstname):
        self.username= username
        self.firstname = firstname
        
    
    # def deleting(self):
    #     delete = input("Do you want to delete your account? \n Yes or no?")
    #     if delete == "yes" or delete == "Yes":
    #         print("your wallet has been deleted")
    #     else:
    #         print("Your wallet is intact")

    def funding_wallet(self, balance, amount):
        self.balance = balance
        self.amount = amount
        try:
            print(balance + amount)
        except TypeError as e:
            print(e)
        else:
            print("your wallet has been funded")

    def logging_transaction(self):
        t = input("enter your user_name")
        if t == self.username:
            print("you are looged in")
        else:
            print("incorrect username")
        # y = input("enter your password")
        # print("you are logged in")
        # t = input("enter")
        # print("you are logged in")


class Wallet(User):
    pass


class Transaction(User):
    pass
        
balance = 3000
first_name = input("enter your first name")
last_name = input("enter your lastname")
user_name = first_name + last_name
print(user_name)
# password = input("enter your password")
# print(password)
r = Wallet(user_name, first_name )
m = Transaction(user_name, first_name)
r.deleting()
r.funding_wallet()
r.logging_transaction()




def sign_up(self):
        try:
            print(self.username == self.firstname + self.lastname)
        except TypeError as e: "firstname should be in letters"
        else:
            self.password = input("enter your password")
            if not self.password.isalnum() or len(self.password < 8):
                raise Exception("invalid format, enter password again")
            return self.password


import csv
class Shape:
    def __init__(self, radius, pie, length, breadth, height, base, edge):
        self.radius = radius
        self.pie = pie
        self.length = length
        self.breadth = breadth
        self.height = height
        self.base = base
        self.edge = edge

class TwoDimensional:
    def two_dimensional(self):
        print("Tis is two dimensional")


class ThreeDimensional:
    def three_dimensional(self):
        print("this is three dimensional")


class Circle(Shape, TwoDimensional):
    def circle(self):
        area = self.pie * self.radius ** 2
        print(f"The area of a circle with radius-> {self.radius}m is {area}m2")


class Triangle(Shape, TwoDimensional):
    def right_triangle(self):
        area = (1/2) * self.base * self.height
        print(f"The area of a right-triangle with base->{self.base}m and ->height {self.height}m is {area}m2")


class Square(Shape, TwoDimensional):
    def square(self):
        area = self.length ** 2
        print(f"The area of a square with ->length {self.length}m is {area}m2")


class Sphere(Shape, ThreeDimensional):
    def sphere(self):
        area = 4 * self.pie * self.radius ** 2
        print(f"The area of a sphere with ->radius {self.radius}m is {area}m2")


class Cube(Shape, ThreeDimensional):
    def cube(self):
        area = 6 * self.length ** 2
        print(f"The area of a cube with ->length {self.length}m is {area}m2")


class Tetrahedron(Shape, ThreeDimensional):
    def tetra_hedron(self):
        area = (3 * self.edge **2) **(1/2)
        print(f"The area of a tetrahedron with ->edge {self.edge}m is {area}m2")

    @classmethod
    def instantiate_from_csv(cls):
        with open("oop.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            print(item)



Tetrahedron.instantiate_from_csv()
shape1 = Circle(7, 3.142, 8, 6, 9, 10, 4)
shape2 =Triangle(7, 3.142, 8, 6, 9, 10, 4)
shape3 = Square(7, 3.142, 8, 6, 9, 10, 4)
shape4 = Sphere(7, 3.142, 8, 6, 9, 10, 4)
shape5 = Cube(7, 3.142, 8, 6, 9, 10, 4)
shape6 = Tetrahedron(7, 3.142, 8, 6, 9, 10, 4)
shape1.circle()
shape2.right_triangle()
shape3.square()
shape4.sphere()
shape5.cube()
shape6.tetra_hedron()

with open ("today.txt", "r") as f:
    print(f'{"Account"}{"Name"}{"Balance"}') 
    for record in f:
        account, name, balance = record.split()
        print(f'{account:<10}{name:<10}{balance:>10}')





























# @staticmethod























































































