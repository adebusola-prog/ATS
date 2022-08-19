# 1 - Create a Computation class with a default constructor (without parameters) allowing to perform various calculations
#  on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
# 4 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
# 5 - Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# 6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.



class Computation:
    
    def __init__(self):
        pass
        # print("These contain different calculations")
        # x = 5
        # y = 6
        # add = x + y
        # print(f"{x} + {y} is {add}")
        # multiply = x * y
        # print(f"{x} * {y} is {multiply}")
        # division = x / y
        # print(f"{x} / {y} is {division}")
        # moduloo = x % y
        # print(f"{x} % {y} is {moduloo}")

    # def suum(self, x, y):
    #     self.x = x
    #     self.y = y
    #     add = x + y
    #     print(f"{self.x} + {self.y} is {add}")
    #     multiply = x * y
    #     print(f"{self.x} * {self.y} is {multiply}")
    #     division = x / y
    #     print(f"{self.x} / {self.y} is {division}")
    #     moduloo = x % y
    #     print(f"{self.x} % {self.y} is {moduloo}")
        
    def factorial(self,n):
        if n < 0:
            return 0
        elif n == 0 or n == 1:
            return 1
        else:
            fact = 1
            while (n>1):
                fact *= n
                n -= 1
            return fact

    def sum(self, n):
        sum = 0
        for i in range (0, n + 1):
            sum = sum + i
        print(f"The sum of the first {n-1} integers is {sum}")

    def prim(self, n):
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
            return True
    
    def testprim(self, x, n):
        v = []
        for i in range(x, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                if i == 1 or i ==0:
                    continue
                else:
                    v.append(i)
        print(f"These are the prime numbers between {x} and {n} -> {v}")
 
    def tableMult(self):
        for i in range(2, 3):
            for j in range(1, 13):
                x = i * j
                print(f"{i} * {j} = {x}")
    
    def alltableMult(self):
        for i in range(2, 10):
            for j in range(1, 13):
                x = i * j
                print(f"{i} * {j} = {x}")
    
    @staticmethod
    def listDiv(num):
        listDiv = []
        for i in range(1, num + 1):
            if num % i == 0:
                listDiv.append(i)
        print(f"The divisors of {num} are {listDiv}")
        return listDiv

    def listDivPrim(num):
        # listDiv = []
        # for i in range(2, num + 1):
        #     if num % i == 0:
        #         listDiv.append(i)
        listDivPrime = Computation.listDiv(num) 
        listDivPrim = []
        for i in listDivPrime:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                listDivPrim.append(i)
        print(f"The prime divisors of {num} are {listDivPrim}")




c = Computation()  
print(c.factorial(5))
c.sum(11)
print(c.prim(53))
# x =int(input("enter a number"))
# n = int(input("enter a number"))
# c.testprim(x, n)
c.tableMult()
c.alltableMult()
Computation.listDivPrim(36)
Computation.listDiv(36)