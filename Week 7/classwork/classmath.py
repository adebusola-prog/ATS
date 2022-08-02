# 1 - Create a Computation class with a default constructor (without parameters) allowing to perform various calculations 
# on integers numbers.
class Computation:

    def __init__(self):
        print("This contain different calculations")

    
    def suum(self, x, y):
        self.x = x
        self.y = y
        add = x + y
        print(f"{self.x} + {self.y} is {add}")
        multiply = x * y
        print(f"{self.x} * {self.y} is {multiply}")
        division = x / y
        print(f"{self.x} / {self.y} is {division}")
        moduloo = x % y
        print(f"{self.x} % {self.y} is {moduloo}")
        
        
# c = Computation()
# c.suum(5, 6)      

# 2 - Create a method called Factorial() which allows to calculate the factorial of an integer. 
# Test the method by instantiating the class.

# class Faactorial:


#     def factorial(n):
#         if n < 0:
#             return 0
#         elif n == 0 or n == 1:
#             return 1
#         else:
#             fact = 1
#             while (n>1):
#                 fact *= n
#                 n -= 1
#             return fact


# f = Faactorial
# print(f.factorial(5))


# 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. 
# Test this method.  
# class Sum:
#     def sum(n):
#         sum = 0
#         for i in range (0, n + 1):
#             sum = sum + i
#         print(f"The sum of the first {n} integers is {sum}")


# s = Sum
# s.sum(10)

# 4 - Create a method called testPrim() in the Calculation class to test the primality of a given integer. Test this method.
# class IsPrime:

#     def testPrim(n):
#         if n == 1 or n == 0:
#             return False
#         elif n == 2:
#             return True
#         elif n < 0:
#             return False
#         else:
#             for i in range(2, n):
#                 if n % i == 0:
#                     return False
#             else:
#                 return True


# p = IsPrime
# print(p.testPrim(5))
# x = testPrim(109)
# print(x)


# 4b - Create  a method called testPrims() allowing to test if two numbers have prime between them.
# def testPrim(x, n):
#         if n == 1 or n == 0 and x == 1 or x == 0:
#             return False
#         elif n == 2 or x == 2:
#             return True
#         elif n < 0 or x < 0:
#             return False
#         else:
#             for i in range(x, n):
#                 if n % i == 0 and x % i == 0:
#                     return False
#             else:
#                 return True



# x = testPrim(14, 16)
# print(x)
# x = 14
# num = 17
# for i in range(2, 7):
#     for j in range(2, i):
#         if i % j == 0:
#             break
            
#     else:
#         for x in range(x, num):
#             if x in i:
#                 print("true")
#             else:
#                 print("false")



# 5 - Create a tableMult() method which creates and displays the multiplication table of a given integer. 
# Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# for i in range(2, 3):
#     for j in range(1, 13):
#         x = i * j
#         print(f"{i} * {j} = {x}")


# for i in range(2, 10):
#     for j in range(1, 13):
#         x = i * j
#         print(f"{i} * {j} = {x}")

# 6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. 
# Create another listDivPrim() method that gets all the prime divisors of a given integer.



# 6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. 
# listDiv = []
# num = int(input("enter a number"))
# for i in range(1, num + 1):
#     if num % i == 0:
#         listDiv.append(i)
# print(f"The divisors of {num} are {listDiv}")

# # Create another listDivPrim() method that gets all the prime divisors of a given integer.
# for i in listDiv:
#     if i % 2 == 0:
        


def testPrim(n):
        if n == 1 or n == 0:
            return False
        elif n == 2:
            return True
        elif n < 0:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            else:
                return True
listDiv = []
num = int(input("enter a number"))
for i in range(1, num + 1):
    if num % i == 0:
        listDiv.append(i)
print(f"The divisors of {num} are {listDiv}")

k = []
for i in range(len(listDiv)):
    if i(testPrim) == False:
        k.append(i)
        print(k)
        
        













    





























        



























