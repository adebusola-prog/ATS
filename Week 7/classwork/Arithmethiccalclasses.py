class Computation:
    
    def __init__(self):
        print("These contain different calculations")

    
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


    def Prim(self, n):
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
    
    
    # listDiv(36)

    def listDivPrim(num):
        listDiv = []
        for i in range(2, num + 1):
            if num % i == 0:
                listDiv.append(i)
        listDivPrim = []
        for i in listDiv:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                listDivPrim.append(i)
        print(f"The prime divisors of {num} are {listDivPrim}")


    # listDivPrim(36)



c = Computation()
c.suum(5, 6)  
print(c.factorial(5))
c.sum(11)
print(c.Prim(53))
x =int(input("enter a number"))
n = int(input("enter a number"))
print(c.testprim(x, n))
c.tableMult()
c.alltableMult()
Computation.listDivPrim(36)
Computation.listDiv(36)