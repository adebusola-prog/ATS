#(1) fibonnaci series
# def fib(n):
#     numbers = []
#     for i in range(n-1):
#         if i == 0 or i == 1:
#             numbers.append(i)
#         else:
#             numbers.append(numbers[i-1] + numbers[i-2])
#     print(numbers)


# fib(100)

# #(2) converting celsius to fahrenheit
# def convert(n):
#     celsius = ["C"] + list(range(n+1))
#     f_list = ["F"]
#     for i in range(0, n+1):
#         x = (i*9/5) + 32
#         f_list.append(x)
#     x = 0
#     while x <= n + 1:
#         print(f"{celsius[x]} : {f_list[x]}")
#         x += 1
        
    
# convert(100)


# #(3a) prime numbers
# def is_prime(n):
#     if n == 1 or n == 0:
#         return False
#     if n == 2:
#         return True
#     for i in range(2, n): # 2 in the range already limit the number  being divided by one. since n is being divided by i, it 
#         if n % i == 0:    #will automatically not pickitself because the index will not reach the number itself
#             return False
#     else:
#             return True


# print(is_prime(109))


#(3b) Use this function in a program that determines and prints all the prime numbers between 2 and 1000
# for i in range(2, 1001):
#     for j in range(2, i):
#             if i % j == 0:
                
#                 break
#     else:
#         print(i)
    

# 3(c) #Initially, you might think that n/2 is the upper limit for which you must test to see whether
# a number is prime, but you need go only as high as the square root of n. Rewrite the pro
# gram and run it both ways to show that you get the same result.


# import math

# num = eval(input("enter a number"))
# x = round(math.sqrt(num))
# # print(x)
# for i in range (2, x + 1):
#     if num % i == 0:
#         print(num, "is not a prime number")
#         break
#     else:
#         print(num, "is a prime number")
#         break



# # (4) Perfect numbers
# def perfect(n):
#     v = []
#     for i in range(1, n):
#         if n % i == 0:
#             v.append(i)
#     print(v)
#     s = (sum(v))
#     print(s)
#     if s == n:
#         print(n, "is a perfect number")
#     else:
#         print(n, "is not a perfect number")

# num = int(input("enter a number"))
# perfect(num)


# # 4(c)
# def perfect(n):
#     v = []
#     for i in range(1, n):
#         if n % i == 0:
#             v.append(i)
#     s = (sum(v))
#     if s == n:
#         return n == s
# for x in range(1, 100000000):
#     if perfect(x):
#         print(x, "is a perfect number")



# #(5)computer-assisted instruction (CAI)( multiplication table)
# import random

# def CAI():
#     x = random.randrange(1, 10)
#     y = random.randrange(1, 10)
#     m = x * y
   

#     while True:
#         k = input(str(f"How much is {x} times {y}?"))
#         h = int(k)
#         if  h == m:
#             print("Very good!!!")
#             CAI()
#             break
#         else:
#             print("No, please Try again")
    

# CAI()



#(6) #game of guess
# import random
# def game_guess():   
#     x = random.randrange(1, 1000)
#     print(x)
#     print("I have a guess between 1 and 1000.")
#     print("can you guess my number?") 

#     while True:
#         n = int(input("please type your guess->"))
#         if x == n:
#             print("excellent! You guessed the number right!. would you like to try again?")
#             a = input("y(yes) or n(no)?->")
#             if a == "y" or a == "yes" or a == "YES" or a == "Yes" or a=="y(yes)":
#                 game_guess()
#             break
#         elif x > n:
#             print("Too low. Try again")
#         else:
#             print("Too high. Try again")


# game_guess()

# (7) Towers of Hanoi
# peg1 = "1"   #root
# peg2 = "2"   #permanaent
# peg3 = "3"   #temporary

# def tower_of_hanoi(disks, peg1, peg2, peg3):  
#     if(disks == 1):  
#         print('Move disk 1 from rod {} to rod {}.'.format(peg1, peg2))  
#         return    
#     tower_of_hanoi(disks - 1, peg1, peg2, peg3)  
    
    
#     print('Move disk {} from rod {} to rod {}.'.format(disks, peg1, peg2))  
    
    
#     tower_of_hanoi(disks - 1, peg3, peg1, peg2)  
  
  
# disks = int(input('Enter the number of disks: '))  

# tower_of_hanoi(disks, peg1, peg3, peg2) 








# a, b = 0 , 1
# while a < 10:
#     print(a)
#     a, b = b, a + b



# num = int(input("enter a number"))
# print(num)


# print(num:= int(input("enter a number")))




# def composite(n):
#     if n == 0 or n == 1 or n == 2:
#         return False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return True
#             else:
#                 return False



# # print(composite(24))

# def narcis_tic(n):
#     return n == sum([int(x) ** len(str(n))for x in str(n)])

# print(narcis_tic(271))



# c = []
# x = "password"
# for i in x:
#     i = "_"
#     # print(i)
#     c.append(i)
# print(c)
# import random
# d = ["trials", "faith", "tiger", "Lion"]
# for i in range(5):
#     x = random.choice(d)
#     print(x)
#     y = input("guess the word")
#     if y == x:
#         print("you guessed right")
#     else:
#         print("try again")
# v = " "
# for y in v
# word = "faith"
# for i in word:
#     i = "_"
#     v = v + i
#     # print(v)
#     x = input("guess the letter i the words")
#     if x in word:
#         s = v.replace(x, v)
#     print(s)
#     break
    #     print("true")
    # else:
    #     print("not true")
    # for y in v:
    #     if x in word:
    #         v = v.replace(x, y)
    #         print(v)




# k = ""
# v = "faith"
# for i in v:
#     print(index(i))
    # print(x)
    # for i in v:
#     i = "_"
#     k = k + i
#     g = input("guess v")
#     # g = g.lower()
#     if g in v:
#         print(v[k.index(g)])


# def number(num):
#     f = {0:"zero", 1:"one", 2: "two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
#         10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14: "fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 
#         18:"eighteen", 19: "nineteen", 20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80: "eighty",
#         90:"ninety"}

#     thousand = 1000


#     if num in f:
#         return (f[num])
#     else:
#         if num < 100:
#             return(f[num//10*10] + " " + f[num%10])
#         elif 100 < num < thousand:
#             if num % 100 == 0:
#                 return (f[num//100] + " " + "hundred")
#             else:
#                 return (f[num//100] + " hundred and " + number(num%100))
#         elif num < thousand * 1000:
#             if num % 100 == 0:
#                 return number(num//1000) + ' thousand '
#             else:
#                 return number(num//1000) + ' thousand ' + number(num % 1000)



# def cardinal(num):
#     return(number(num) + "th")

# print(cardinal(34))























# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# key = 'xznlwebgjhqdyvtkfuompciasr'
# secret_message = input('Enter your message: ')
# secret_message = secret_message.lower()
# for c in secret_message:
#     if c.isalpha():
#         print(key[alphabet.index(c)],end='')
#     else:
# print(c, end='')




# a = 9
# b = 27
# c = a/b 
# print(c)
# d = str(c)
# e = len(d)
# f = e - 2
# g = 10 * f
# print(g)

# x_6 = [1, 2, 3, 6]
# y_15 = [1, 3, 5]
# for i in x_6:
#     if 15 % i == 0:
#         print(i)

x_55 = [1, 5, 11, 55]
y_100 = [1, 2, 4, 5, 10, 20, 25, 50, 100]
for i in x_55:
    if 100 % i == 0:
        print(i)