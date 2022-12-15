#Question 1
import random
from re import I
from unicodedata import digit
def game_guess():   
    x = random.randrange(1, 1000)
    print(x)
    print("I have a guess between 1 and 1000.")
    print("can you guess my number?") 

    # while True:
    for i in range(5):    
        n = int(input("please type your guess->"))
        if x == n:
            print("excellent! You guessed the number right!. would you like to try again?")
            a = input("y(yes) or n(no)?->")
            if a == "y" or a == "yes" or a == "YES" or a == "Yes" or a=="y(yes)":
                game_guess()
            break
        elif x > n:
            print("Too low. Try again")
        else:
            print("Too high. Try again")


# game_guess()

#Question 2
def ordinal(x):
    f = {"11": "11th", "12": "12th", "13": "13th"}
    if x in f:
        return f[x]
    else:
        if x[-1] == "0":
            return x + "th"
        elif x[-1] == "4" or x[-1] == "5" or x[-1] =="6" or x[-1] == "7" or x[-1]== "8" or x[-1] == "9":
            return x + "th"
        elif x[-1] == "2":
            return x + "nd"
        elif x[-1] == "3":
            return x + "rd"
        else:
            return x + "st"

# x = input("enter a number")
# print(ordinal(x))

# Question 3
def cal():
    action = input("what calculations do you want to make?, A for add, S for subtraction D for division and m for multiplication")
    v = []
    if action == "A":
        while True:
            x = int(input("enter the numbers you want to calculate one after the other"))
            v.append(x)
            question = input("do you want to enter another number, y(yes), n(no)->")
            if question == "y":
                continue
            else:
                print(v)
                to_do = int(input("1 for add, 2 for multiply"))
                if to_do == 1:
                    g = 0
                    for i in v:
                        g += i
                    print(g)
                elif to_do == 2:
                    h = 1
                    for i in v:
                        h *= i
                    print(h)
                    break
                    
                
    elif action == "D":
            # div_subt = input("this is for division and subtraction, type 1 for division and 2 for subtraction")
            # if div_subt == 1:
        m = int(input("enter the first number"))
        y = int(input("enter the second number"))
        print(m / y)
    
    elif action == 'S':
        t = int(input("enter the first number"))
        r = int(input("enter the second number"))
        print(t - r)

# print(cal())

#Question 4
import random
import string
def password_generator():
    f = []
    y = string.ascii_lowercase
    z = string.ascii_uppercase
    t = string.digits
    r = "/^(<>%#*&@*!}{|\"'[]"
    while True:
        x = "".join(random.sample(y, 2)) + "".join(random.sample(z, 3)) + "".join(random.sample(t, 2) + random.sample(r, 1)) 
        f.append(x)
        return(f)

print(password_generator())


#Question 5
#find the HCF of the smallest integer out of the denominator or numerator. here, it is the numerator 
class Rational:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2
    
    def reduced_form(self, numerator, denominator):
        self.numerator = numerator
        self.denominator= denominator
        g =[]
        h =[]
        f = []
        v = []
        if self.denominator > self.numerator:
            for i in range(1, self.numerator+1):
                if self.numerator % i == 0:
                    v.append(i)
            print(v)
            for i in v:
                if self.denominator % i == 0:
                    f.append(i)
            div_no =max(f)
            reduced_numerator = self.numerator/ div_no
            reduced_denominator = self.denominator / div_no
            print(f"{reduced_numerator} / {reduced_denominator}")


        elif numerator > self.denominator:
            for i in range(1, self.denominator+1):
                if self.denominator % i == 0:
                    h.append(i)
            print(h)
            for i in h:
                if self.numerator % i == 0:
                    g.append(i)
            div_no2 = max(g)
            reduced_numerator = self.numerator/ div_no2
            reduced_denominator = self.denominator / div_no2
            print(f"{reduced_numerator} / {reduced_denominator}")

    def add_rational(self, num1, num2, den1, den2):
        red1 = self.reduced_form(num1, den1)
        red2= self.reduced_form(num2, den2)
        x = (den1 * den2) / (den1) * (num1)
        y = (den1 * den2) / (den2) * (num2)
        z = (x + y)
        h = (den1 * den2)
        answer = self.reduced_form(z, h)
        print(answer)
        
    def subtract_rational(self, num1, num2, den1, den2):
        red1 = self.reduced_form(num1, den1)
        red2= self.reduced_form(num2, den2)
        x = (den1 * den2) / (den1) * (num1)
        y = (den1 * den2) / (den2) * (num2)
        z = (x - y)
        h = (den1 * den2)
        answer = self.reduced_form(z, h)

    def division_rational(self, num1, num2, den1, den2):
        red1 = self.reduced_form(num1, den1)
        red2= self.reduced_form(num2, den2)
        x = (num1 * den2) 
        y = (num2 * den1)
        h = self.reduced_form(x, y)

    def multiply_rational(self, num1, num2, den1, den2):
        # red1 = self.reduced_form(num1, den1)
        # red2= self.reduced_form(num2, den2)
        red3 = (num1 * num2) 
        red4 = (den1 * den2)
        h = self.reduced_form(red3, red4)
    

# rational = Rational((9/12), (2/4))
# rational.reduced_form(444, 33)
# rational.add_rational(4,3,2,6)
# rational.subtract_rational(4,3,2,6)
# rational.division_rational(4,3,2,6)
# rational.multiply_rational(10,3,2,6)


# Question 6
class Komplex:
    def __init__(self):
        pass

    def add_complex(self):
        complex_1 = complex(3,  2)
        complex_2 = complex(2, 4)
        return (complex_1 + complex_2)

    def subtract_complex(self):
        complex_1 = complex(3, 2)
        complex_2 = complex(2, 4)
        return (complex_1 - complex_2)

    def multiply_complex(self):
        complex_1 = complex(3, 2)
        complex_2 = complex(2, 4)
        return (complex_1 * complex_2)

    def divide_complex(self):
        complex_1 = complex(3, 2)
        complex_2 = complex(2, 4)
        return (complex_1 / complex_2)



# komp = Komplex()
# print(komp.add_complex())
# print(komp.subtract_complex())
# print(komp.multiply_complex())
# print(komp.divide_complex())

#Question 7
class Rectangle:
    def __init__(self, __length=1, __width=1):
        self.__length = __length
        self.__width = __width

    # def __str__(self):
        # return self.__length

    @property 
    def get_length(self):
        return self.__length
    
    @get_length.setter
    def get_length(self, value):
        if 0 < value < 20:
            self.__length = value

    @property
    def get_width(self):
        return self.__width

    @get_width.setter
    def get_width(self, value):
        if 0 < value < 20:
            self.__width = value

    def perimeter(self):
        return(2*(self.__length) + self.__width)

    def area(self):
        return(self.__length * self.__width)


# rectangle = Rectangle()
# print(rectangle.perimeter())
# print(rectangle.area())
# print(rectangle.get_length)
# rectangle.get_length = 3
# print(rectangle.get_length)
# print(rectangle.get_width)
# rectangle.get_width = 19
# print(rectangle.get_width)

#Question 8
# Create a more sophisticated Rectangle class than the one you created in Exercise 7.6. This
# class stores only the x-y coordinates of the upper left-hand and lower right-hand corners of the rectangle. 
# constructor calls a set function that accepts two tuples of coordinates and verifies that each
# of these is in the first quadrant, with no single x or y coordinate larger than 20.0. Methods calculate
# the length, width, perimeter and area. The length is the larger of the two dimensions. Include a predicate method 
# isSquare that determines whether the rectangle is a square. Write a driver program to test the class

class RectangleCoordinates:
    def __init__(self, x, y):
        if 0 <= x < 20 and 0 < y < 20 :
           length= self.x = x 
           width= self.y = y 
        
    def perimeter(self):
        if self.x > self.y:
            return 2*(self.x + self.y)

    def area(self):
        if self.x > self.y:
            return self.x * self.y

    def is_square(self, point):
        if point.x == point.y:
            print("the rectangle is a square")
        else:
            print("the rectangle is not a sqare")


# rect_coordinates = RectangleCoordinates(12, 10)
# print(rect_coordinates.perimeter())
# print(rect_coordinates.area())
# rect_coordinates.is_square(rect_coordinates)

# Question 9
def hangman():
    import random
    list_words = ["hello", "password", "real", "help"]
    word = random.choice(list_words)
    print(word)
    print("_" * len(word))
    guess_letter = ""
    for i in range(len(word)):
        guess = input("can you guess the letters in the word")
        guess_letter += guess
        for x in word:
            if x in guess_letter:
                print(f"{x}", end="")
            else:
                print("_", end=" ")
        y = len(x)
        print(f"\nyou guessed {y} letters right")
        # break


hangman()




































