#(1) fibonnaci series
def fib(n):
    numbers = []
    for i in range(n-1):
        if i == 0 or i == 1:
            numbers.append(i)
        else:
            numbers.append(numbers[i-1] + numbers[i-2])
    print(numbers)


fib(100)

#(2) converting celsius to fahrenheit
def convert(n):
    celsius = ["C"] + list(range(n+1))
    f_list = ["F"]
    for i in range(0, n+1):
        x = (i*9/5) + 32
        f_list.append(x)
    x = 0
    while x <= n + 1:
        print(f"{celsius[x]} : {f_list[x]}")
        x += 1
        
    
convert(100)


#(3a) prime numbers
def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    for i in range(2, n): # 2 in the range already limit the number  being divided by one. since n is being divided by i, it 
        if n % i == 0:    #will automatically not pickitself because the index will not reach the number itself
            return False
    else:
            return True


print(is_prime(109))


#(3b) Use this function in a program that determines and prints all the prime numbers between 2 and 1000
for i in range(2, 1001):
    for j in range(2, i):
            if i % j == 0:
                
                break
    else:
        print(i)
    

# 3(c) #Initially, you might think that n/2 is the upper limit for which you must test to see whether
# a number is prime, but you need go only as high as the square root of n. Rewrite the pro
# gram and run it both ways to show that you get the same result.


import math
from re import A

num = eval(input("enter a number"))
x = round(math.sqrt(num))
# print(x)
for i in range (2, x + 1):
    if num % i == 0:
        print(num, "is not a prime number")
        break
    else:
        print(num, "is a prime number")
        break



# (4) Perfect numbers
def perfect(n):
    v = []
    for i in range(1, n):
        if n % i == 0:
            v.append(i)
    print(v)
    s = (sum(v))
    print(s)
    if s == n:
        print(n, "is a perfect number")
    else:
        print(n, "is not a perfect number")

num = int(input("enter a number"))
perfect(num)


# 4(c)
def perfect(n):
    v = []
    for i in range(1, n):
        if n % i == 0:
            v.append(i)
    s = (sum(v))
    if s == n:
        return n == s
for x in range(1, 100000000):
    if perfect(x):
        print(x, "is a perfect number")



#(5)computer-assisted instruction (CAI)( multiplication table)
import random

def CAI():
    x = random.randrange(1, 10)
    y = random.randrange(1, 10)
    m = x * y
   

    while True:
        k = input(str(f"How much is {x} times {y}?"))
        h = int(k)
        if  h == m:
            print("Very good!!!")
            CAI()
            break
        else:
            print("No, please Try again")
    

CAI()



#(6) #game of guess
import random
def game_guess():   
    x = random.randrange(1, 1000)
    print(x)
    print("I have a guess between 1 and 1000.")
    print("can you guess my number?") 

    while True:
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


game_guess()

# (7) Towers of Hanoi
peg1 = "1"   #root
peg2 = "2"   #permanaent
peg3 = "3"   #temporary

def tower_of_hanoi(disks, peg1, peg2, peg3):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(peg1, peg2))  
        return    
    tower_of_hanoi(disks - 1, peg1, peg2, peg3)  
    
    
    print('Move disk {} from rod {} to rod {}.'.format(disks, peg1, peg2))  
    
    
    tower_of_hanoi(disks - 1, peg3, peg1, peg2)  
  
  
disks = int(input('Enter the number of disks: '))  

tower_of_hanoi(disks, peg1, peg3, peg2) 








a, b = 0 , 1
while a < 10:
    print(a)
    a, b = b, a + b
































































