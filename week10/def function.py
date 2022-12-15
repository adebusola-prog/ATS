# # i = 0
# # while i <= 1000:
# #     if i % 2 != 0:
# #         print(i)
# #     i = i+1

# # for i in range(11, 0, -1):
# #     print("*" * i)

# x = "Tola"
# y = x.index("a")
# print(y)


# r = "ssetessfrt"
# print(r.count("s"))

# animals = ["lion", "tiger", "lion", "goat", "kangaroo", "cheetah"]
# print(animals.count("lion"))

# print("Jesulayomi")
# print("ASAKE")

# print(x.upper())


# s = input('Enter a string')


# if s[0].isalpha():
#     print('Your string starts with a letter')
# if not s.isalpha():
#     print('Your string contains a non-letter.')


# print('\\n' * 9)

# x = input("enter a string")
# for i in range(len(x)):
#     if x[i] == "a":
#         print(x[i])

#Binary to decimal
# decimal_list =[]
# c = []
# x = 1101
# y = str(x)
# z = list(y)
# # print(z)
# for i in z:
#     i = int(i)
#     # print(i)
#     c.append(i)
# # print(c)
# n = len(c)-1
# for char in c:
#     answq = char*2**n
#     n -=1
#     decimal_list.append(answq)
# print(sum(decimal_list))
    
#Decimal to Binary
# from itertools import product


# pass

# num = 29
# # for i in range(2, num):
#     if num % i == 0:
#         print("not prime")
#         break
# else:
#     print("this is a prime number")



# for i in range(2, int(num**.5)+1):
#     if num % i == 0:
#         print("not prime")
#         break

# else:
#     print("this is a prime number")


# try:
#     (5/0)
# except Exception as e:
#     print(e)

# for i in range(1, 101):
#     for x in range(1, 101):
#         for j in range(1, 101):
#             if i**2 + x**2 == j **2:
#                 print(i, x, j)


# X = range(1, 101)
# for (x, y, z) in product(X, X, X):
#     if x**2 + y**2 == z**2:
#         print(x, y, z)

# pyth_list = [(x,y,z)for (x,y,z) in product(X, X, X) if x**2 + y**2 == z**2]
# print(pyth_list)

# from Tkinter import *
# from PIL import Image, ImageTk, ImageDraw
# def color_convert(r, g, b):
#     return '#{0:02x}{1:02x}{2:02x}'.format(int(r*2.55),int(g*2.55),
# int(b*2.55))
# max_iter=75


# print(chr(45))
# print(ord("y"))

# x = eval(input("enter a number"))
# print(x)
# L = [[1,2,3],
# [4,5,6],
# [7,8,9]]
# for r in range(5):
#     for c in range(5):
#         print(L[r][c], end=" ")
#     print()


nmb = int(input("enter a number"))

tmp = nmb

revsd = 0

while (nmb > 0):

    digit = nmb% 10

    # rev = rev * 10 + digit

    nmb= nmb// 10

    if (tmp == revsd):

        print("the number is a palindrome")

    else:

        print("not a palindrome")


13











































# for i in range(len(x)):
#     for j in range(len(y)):
#         if x[i] not in v and y[j] not in v:
#             ans = x[i] * (2**y[j])
#             v.append(ans)
# print(v, end = "")

# name = input('Enter your name: ')
# for i in range(len(name)):
#     print(name[:i], end=' ')
 
# p = ["heoll", "makrer", "bob", "vert"]
# p.pop(1)
# print(p)