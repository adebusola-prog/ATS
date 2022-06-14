a = int(input('what is the first number'))
b = int(input('what is the second number'))
c = int(input('what is the third number'))
d = int(input('what is the fourth number'))
e = int(input('what is the fifth number'))

if (a/2 == e/2) and (a % 2 == e % 2) and (b/2 == d/2) and (b%2 == d%2):
    print('This is a Palindrome')
else:
    print('This is not a Palindrome')