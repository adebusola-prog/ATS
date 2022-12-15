# for i in range(1, 11):
#         print("*"*i)



# for i in range(11, 0, -1):
#         print("*"*i)



number_stars = 10
for i in range(number_stars):
     for j in range(1, number_stars - i):
        print(" ", end="")
     for k in range(0, i + 1):
        print("*", end="")
     print()



# for a in range(1, 21):
#     for b in range(1, 21):
#         for c in range(1, 21):
#             if c > a and b and b > a:
#                 if c*c == a*a + b*b:
#                     exec(a, b, c)


# s = """x = 3
#         for i in range(4):
#             print(i ** x)"""
      
# exec(s)

# s = """x=3
# for i in range(4):
#     print(i*x)"""
# exec(s)


# s = 'abc'
# L = [10, 20, 30]
# z = zip(s,L)
# print(dict(z))
# from random import shuffle
# word = input('Enter a word: ')
# letter_list = list(word)
# shuffle(letter_list)
# anagram = ''.join(letter_list)
# print(anagram)
# from random import choice
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# s = ''.join([choice(alphabet) for i in range(1000)])
# print(s)























