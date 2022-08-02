# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#     print("yes we have a match")
# else:
#     print("no match")

# txt = "hello match"
# x = re.findall("^hello", txt) 
# if x:
#     print("yes")
# else:
#     print("no")

# print(r'\telephant')

# num_list = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i < len(num_list):
#     if num_list[i] % 2 == 0:
#         print(num_list[i])
#     i = i + 1

# num_list = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i < len(num_list):
#     if num_list[i] % 2 == 0:
#         print(num_list[i])
#     i += 1


# for i in num_list:
#     if i % 2 == 0:
#         print(i)

# for i in num_list:
#     if i < 5 and i % 2 ==0:
#             print(i)

    # else:
    #     break

# r = {"name": "Adebusola"}
# # for k, v in r:
# #     print(v + "two")

# print (r["name"] + " Adeyeye")




# x = "two"
# y = x.split()
# print(y)

# def fact(num):
#     sum = 0
#     if num == 0:
#         return 1
#     else:
# #         return 
# def factorial(n):
#     if n < 0:
#         return 0
#     elif n ==1 or n == 0:
#         return 1
#     else:
#         x = 1
#         while (n>0):
#             x = x * n
#             n -=1
#         return x

# print(factorial(5))
# def fact(n):
#     if n == 0:
#         return 1
#     if n< 0:
#         return 0
#     else:
#         return fact(n-1)

# print(fact(5))

#b) Write a program that estimates the value of the mathematical constant e by using the 
# formula [Note: Your program can stop after summing 10 terms.]

# def factorial_n(num):
#     e = 1
#     while (num > 0):
#         e += 1/((factorial(num)))
#         num -= 1
#     return e

# print(factorial_n(10))

# def factorial_n2(x, num):
#     e = 1
#     while (num > 0):
#         e += x**num/(factorial(num))
#         num -= 1
#     return e

# print((factorial_n2(2, 10)))


# v = []
# a, b = 0, 1
# while (a < 10):
#     # a , b = b, a + b
#     print(a)
#     a , b = b, a + b



# list_num = [1,2,3,4,5]

# num = int(input("How many numbers are you adding? "))
# for i in range(num):
#     input_num = int(input("Enter :"))
#     list_num.append(input_num)

# print(list_num)


# list_no = [3,4,5,6]
# for i in range(10):
#     input_num = int(input("enter a number"))
#     list_no.append(input_num)


# print(list_no)







def number(num):
    
    f ={0:'zero',1:'one', 2:'two',3:'three',4:'four', 5:'five',6:'six',7:'seven',8:'eight',9:'nine',
        10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15: 'fifteen',16:'sixteen',17:'seventeen',
        18:'eighteen',19:'nineteen', 20:'twenty',30:'thirty ',40:'fourty',50:'fifty',60:'sixty',70:'seventy',
        80:'eighty',90:'ninety'}

    thousand = 1000


    if num == 0:
        return f[num]
    elif num < 20:
        return f[num]
    elif num < 100:
        if num % 10 == 0:
            return f[num]
        else:
            return f[num // 10 * 10] +' '+f[num %10]
    elif num < thousand:
        if num % 10 ==0:
            return f[num//100] +" hundred " 
        else:
            return f[num//100] + ' hundred and ' + number(num%100)
    elif num < thousand * 1000:
        if num % 100 == 0:
            return number(num//1000) + ' thousand'
        else:
            return number(num//1000) + ' thousand '+ number(num % 1000)
   
ask = int(input("Enter a number :"))    
print(number(ask))























    









































