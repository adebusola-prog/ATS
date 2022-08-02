
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




# for i in range(2, 1001):
#     for j in range(2, i):
#         if i % j == 0:
#             break
# else:
#     print(i)



# from setuptools import PEP420PackageFinder


# n = 64
# peg1 = []
# peg2 = []
# peg3 = []

# for i in range(1, 65): 
#     peg1.append(i)
# # print(peg1)

# def tower_of_hanoi(disks, source, auxiliary, target):  
#     if(disks == 1):  
#         print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
#         return  
#     # function call itself  
#     tower_of_hanoi(disks - 1, source, target, auxiliary)  
    
    
#     print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    
    
#     tower_of_hanoi(disks - 1, auxiliary, source, target)  
  
  
# disks = int(input('Enter the number of disks: '))  
# # We are referring source as A, auxiliary as B, and target as C  
# tower_of_hanoi(disks, 'A', 'B', 'C')  # Calling the function  



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




























