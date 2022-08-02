'''temp =eval(input("enter a temperature in celsius"))
print("In fanherit, that is", 9/5*temp+32)'''

'''num1 = eval(input("enter the first number"))
num2 = eval(input("enter the second number"))
print("the average of the two numbers is", (num1+num2)/2)'''

'''print('A', 1, 'b', 1+2)'''

'''print ('The value of 3+4 is', 3+4, '.')

print ('The value of 3+4 is', 3+4, '.')
print ('The value of 3+4 is ', 3+4, '.', sep='')

print('The value of 3 + 4 is', 3 + 4, '.')
print('The value of 3+4 is', 3+4, ':', sep='    ')
print("tuna", "red", "blue", "green", ":", sep="/")'''


# 'end' is used in python if you dont want two arguments to be on different lines. you want them to be on a straight line.
# 'sep' is used to either remove space betweeen arguments or to specity the kind of symbol you want to separate an agrument with



'''for i in range(3):
    num = eval(input("enter a number"))
    print("the square of your number is:", num*num)
print("the loop is over")'''



# x = 0
# y = 0
# x = []
# y = []
# if x != -1 and y != 0:
#     while True:
#         num = eval(input("enter a number"))
#         num2 = eval(input("enter the second number"))
#         x.append(num)
#         y.append(num2)
# print(x)
# print(y)



'''for i in range(10):
    print("*"*4)'''


'''for i in range(11):
    print("*"*(i +1))'''

'''for i in range(1, 11):
    print("*"*i)'''


'''for i in range(3):
    print(i+1, '---Hello')'''

'''for i in range(10):
    print(i, "ade")'''


#fibonacci series
# a = 0
# b = 1
# print(a)
# while b < 50:
#     print(b)
#     a, b = b, a+b

# a, b = 0, 1    #first declare a as 0 and b as 1
# while a < 50:  # 10 is the limit for the fibonacci I want to use
#     print(a)
#     a, b = b, a + b    # declare a as b and b as a + b

# def fib():
#     a, b = 0 , 1
#     while a < 10:
#         print(a)
#         a, b = b, a + b

# fib()




# def fib(n):
#     numbers = []
#     for i in range(n-1):
#         if i == 0 or i == 1:
#             numbers.append(i)
#         else:
#             numbers.append(numbers[i-1] + numbers[i-2])
#     print(numbers)


# fib(100)


def fib(n):
    number = []
    for i in range(n):
        if i == 0 or i == 1:
            number.append(i)
        else:
            number.append(number[i-1] + number[i-2]) 
    print(number)


fib(10)







'''i = 0
while i < 50:
    print(i)

for i in range(10):
    if i == 0:
        i = eval(input("enter the nujm"))
        print()
        break
    else'''

        