# import math
# def is_prime(n):
#     for i in range(2,int(math.sqrt(n))+1):
#         if (n%i) == 0:
#             return  False
#         else:
#             return True


# is_prime(8)


# def multiple_print(string, n, bad_words):
#     if string in bad_words:
#         return
#     print(string * n)
#     print()

# print(multiple_print())


# f = [True, False, True, False]
# f.insert(1, "terabyte")
# print(f)

# season = ''
# while season != "raining":
#     print("what season are we?")
#     season = input()
#     print("continue to irrigate")


# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')


# list_name = []
# while True:
#     print("enter your name")
#     name = input()
#     # list_name.append(name)
#     # print(list_name)
#     if name == "your name" or name == "ade":
#         break
#     list_name.append(name)
#     print(list_name)


# while True:
#     print("who are you")
#     name = input()
#     if name != "Joe":
#         continue
#     print("Hello Joe, what is the password? (It is a fish)")
#     pass_word = input("enter the password")
#     if pass_word == "sword fish":
#         break
# print("access granted")


# name = ''
# while not name:
#     print('Enter your name:')
#     name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:
#     print('Be sure to have enough room for all your guests.')
# print('Done')


# temp = 0
# while temp!=-1000:
#     temp = eval(input('Enter a temperature (-1000 to quit): '))
#     if temp!=-1000:
#         print('In Fahrenheit that is', 9/5*temp+32)
#     else:
#         print('Bye!')


from random import randint
secret_num = randint(1,100)
num_guesses = 0
guess = 0
while guess != secret_num and num_guesses <= 4:
    guess = eval(input('Enter your guess (1-100): '))
    num_guesses = num_guesses + 1
    if guess < secret_num:
        print('HIGHER.', 5-num_guesses, 'guesses left.\n')
    elif guess > secret_num:
        print('LOWER.', 5-num_guesses, 'guesses left.\n')
    else:
        print('You got it!')
    if num_guesses==5 and guess != secret_num:
        print('You lose. The correct number is', secret_num)












































