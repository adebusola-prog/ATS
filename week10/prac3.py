# import string
# x = string.ascii_lowercase
# for i in x:
#     print(i)
# s = "adeola"
# if any in s:


# print(x)
# y = string.ascii_uppercase
# print(y)
# z = string.digits
# print(z)


# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*fact(n-1)


# print(fact(6))


# password = input("enter your password")
# if password in string.ascii_lowercase and password in string.ascii_uppercase:
#     print("yes")
# else:
#     print("no")
# for j in x:
#     for m in y:
#         if j in password and m in password:
#             print("correct password")
#         else:
#             print("password should contain lower and upper")

# s = "adeola"
# s = s[:3] + "******" + s[4:]
# print(s)



alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'xznlwebgjhqdyvtkfuompciasr'
secret_message = input("enter a message")
secret_message = secret_message.lower()
for i in secret_message:
    print(alphabet[key.index(i)], end="")