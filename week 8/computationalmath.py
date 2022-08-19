#1 - Create a Computation class with a default constructor (without parameters) allowing to perform various calculations 
# on integers numbers.
# class Computation:
    
#     def __init__(self):
#         # print("These contain different calculations")
#         x = 5
#         y = 6
#         add = x + y
#         print(f"{x} + {y} is {add}")
#         multiply = x * y
#         print(f"{x} * {y} is {multiply}")
#         division = x / y
#         print(f"{x} / {y} is {division}")
#         moduloo = x % y
#         print(f"{x} % {y} is {moduloo}")



# p = Computation()
# print(p)
    
    
    
    
    
    
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
        


def listDiv(num):
        listDi = []
        for i in range(1, num + 1):
            if num % i == 0:
                listDi.append(i)
        print(f"The divisors of {num} are {listDi}")
        return listDi

listDiv(36)

def listDivPrim(num):
    listdivprime = listDiv(num)
    listDivPrim = []
    for i in listdivprime:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            listDivPrim.append(i)
    print(f"The prime divisors of {num} are {listDivPrim}")

listDivPrim(36)


























