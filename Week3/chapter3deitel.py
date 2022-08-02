#(1) factorial of a non negative number
'''n = 5
fact = 1
for i in range(1, n+1):
    fact *=i
print(fact)'''

def fac(n):
    if n == 0 or n == 1:
         return 1
    elif n < 0:
        return 0
    else:
        fact = 1
        while(n>1):
            fact *= n
            n -= 1
        return fact

            
num= int(input("enter a number"))
print(fac(num))


# #(2) fractional factorial
# def factorial(n):
#     e = 1
#     while n > 0: 
#         e += 1/(fac(n))
#         n -= 1
#     return e

# num = int(input("the last term"))
# print(factorial(num))


# (3)fractional factorial
# def factrorial_ex(n):
#     e_power_X = 1
#     n = 0

#     while n <= 10:
#         e_power_X += (1**x)/(fac(n))
#         x +=1
#         n -=1
#     return e_power_X

# num = int(input("the last term"))
# print(factrorial_ex(num))

# #(4) palindrome
# number = "12321"
# x = "  "
# for r in number:
#     x = r + x
# print(x)

# a = int(input("enter the first number"))
# b = int(input("enter the second number"))
# c = int(input("enter the third number"))
# d = int(input("enter the fourth number"))
# e = int(input("enter the fifth number"))

# if (a/2 == e/2) and (a%2 == e%2) and (b/2 == d/2) and (b%2 == d%2):
#     print("the number is a palindrome")
# else:
#     print("the number is not a palindrome")



# (5)x = "*" + "\n* *" + "\n* * *" + "\n* * * *" + "\n* * * * *" + "\n* * * * * *" + "\n* * * * * * *" + "\n* * * * * * * *" + "\n* * * * * * * * *" + "\n* * * * * * * * * *"


#y = "* * * * * * * * * *" + "\n* * * * * * * * *" + "\n* * * * * * * *" + "\n* * * * * * *" + "\n* * * * * *" + "\n* * * * *" + "\n* * * *" + "\n* * *" + "\n* *" + "\n*"

# for z in range(4):
#     for i in range(1, 11):
#         print("*"*i)

#     for i in range(11, 0, -1):
#         print("*"*i)





