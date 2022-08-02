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




# profilelist ={"n_1":{"first_name" :"Basheer", "last_name":"Balogun","attendance": 11,"height": 46, "weight": 23,"age":22, "birthday": {"day":8, "month": "april",}},
#              "n_2":{"first_name" :"Abdullahi", "last_name":"Salam","attendance": 11,"height": 25, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
#                 "n_3":{"first_name" :"Faith", "last_name":"Adeosun","attendance": 11,"height": 50, "weight": 23,"age":23, "birthday": {"day":8, "month": "Agu",}},
#                'n_4': {"first_name" :"Ahmad", "last_name":"Sharafudeen","attendance": 11,"height": 71, "weight": 23,"age":23, "birthday": {"day":8, "month": "July",}},
#               "n_5":  {"first_name" :"Toluwanimi", "last_name":"Ogunbiyi","attendance": 11,"height": 34, "weight": 24,"age":21, "birthday": {"day":8, "month": "Nov",}},
#                "n_6": {"first_name" :"Awwal", "last_name":"Adeleke","attendance": 11,"height":49 ,"weight": 23,"age":23, "birthday": {"day":8, "month": "Dec",}},
#                "n_7": {"first_name" :"Abdulwali", "last_name":"Tajudeen","attendance": 11,"height": 78, "weight": 23,"age":27, "birthday": {"day":8, "month": "Mar",}},
#                "n_8": {"first_name" :"Abraham", "last_name":"Adekunle","attendance": 11,"height": 65, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
#                "n_9": {"first_name" :"Yusuff", "last_name":"Oyedele","attendance": 11,"height": 52, "weight": 23,"age":23, "birthday": {"day":8, "month": "Oct",}},
#                "n_10": {"first_name" :"Adebusola", "last_name":"Adeyeye","attendance": 11,"height": 43, "weight": 23,"age":26, "birthday": {"day":8, "month": "Feb",}},
#                "n_11": {"first_name" :"Lukman", "last_name":"Abisoye","attendance": 11,"height": 35, "weight": 54,"age":29, "birthday": {"day":4, "month": "Jan",}}}



# def inc_att(data, firstname, increment = 1):
#    for x in data:
#       if data[x]["first_name"] == firstname:
#          data[x]["attendance"] += increment
#          return data
# print(inc_att(profilelist, input("Enter your first name: "),))

#update profile first name and last name
# def update_fullname(profile, your_age,f_name,l_name:str):
#    for i in profile:
#       if profile[i]["age"] == your_age :
#          profile[i]["first_name"] = f_name
#          profile[i]["last_name"] = l_name
#          return profile
# up=update_fullname(profilelist, int(input("Enter your age: ")), input("Enter Your first name : "), input("Enter Your last name : "))
# print(up)





# function to return full names 
# def f_and_l_title(data):

#    fullname = []
#    for x in data:
#       fullname.append(data[x]['first_name'].title() +" "+ data[x]["last_name"].title())
#       print()

#    return fullname
# print(f_and_l_title(profilelist))


# sales_person1 = [prod1=[300]], [prod2=[400]], [prod3=[500]], [prod4=[600]], [prod5=[700]]]
# sales_person2 = [prod1[200], prod2[400], prod3[600], prod4[700], prod5[900]]
# sales_person3 = [prod1[100], prod2[500], prod3[500], prod4[800], prod5[1000]]
# sales_person4 = [prod1[300], prod2[200], prod3[400], prod4[900], prod5[1100]]



# # sales_person1 = {"prod1":300, "prod2":400, "prod3":500, "prod4":600, "prod5":700}
# # sales_person2 = {"prod1":200, "prod2":400, "prod3":600, "prod4":700, "prod5":900}
# # sales_person3 = {"prod1":100, "prod2":500, "prod3":500, "prod4":800, "prod5":1000}
# # sales_person4 = {"prod1":300, "prod2":200, "prod3":400, "prod4":900, "prod5":1100}


# # v = []
# # x = list(sales_person1.values()) 
# # print(sum(x))

# # y = list(sales_person2.values()) 
# # print(sum(y))

# # z = list(sales_person3.values())
# # print(sum(z))

# # a = list(sales_person4.values())
# # print(sum(a))


# # b = list("prod1".values())
# # print(b)

# import collections


# k = [{"prod1":300, "prod2":400, "prod3":500, "prod4":600, "prod5":700},
#      {"prod1":200, "prod2":400, "prod3":600, "prod4":700, "prod5":900},
#      {"prod1":100, "prod2":500, "prod3":500, "prod4":800, "prod5":1000},
#      {"prod1":300, "prod2":200, "prod3":400, "prod4":900, "prod5":1100}]


# # counter = collections.Counter()
# # for d in k:
# #     counter.update(d)

# # n = dict(counter)

# # print("New dict : ", n)




# cross_addition = collections.Counter()
# for i in k:
#        cross_addition.update(i)

# n = dict(cross_addition)
# print(n)
# k = list(n.values())
# print(k)


# def prime(n):
#    v = []
#    for i in range(2, n):
#       if n % 2 == 0 or n % 3 == 0:
#          return 0
#       if n == 0 or n == 1:
#          break
#       else:
#         v.append(i)
#         print(i)

# prime(1001)


# points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
# 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
# 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
# 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}

# # total = 0
# # for c in points:
# #     total += points[c]
# # print(total)

# score = sum([points[c] for c in points])
# print(score)

# d = {"A": 200, "B": 100}

# letter = input("enter a letter")
# if letter in d:
#     print("the value is", d[letter])



# or i in range(2, 101):
# #     v = []
# #     n = 100
# #     x = (4, n+1, 2)
# #     y = (6, n+1, 3)
# #     z = (10, n+1, 5)
# #     a = (14, n+1, 7)
# #     for i in range(2, 101):
# #         if i != x and i != y and i != z and i !=a:
# #             if i not in v:
# #                 v.append(i)
# # print(v)

# numbers = [1,2,3,4,5,61,2,3,6,7,8,9,4,3,10,45,47,18,19,20]
# k = []
# for i in numbers:
#     if i not in k:
#         k.append(i)
# print(k)

# def bubble_sort(numbers):
#     for i in range(len(numbers)):
#         for j in range (len(numbers) -1):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]



# numbers = [3,2,5,4,1,7,6,5,4,8,9,0,4,2,1,0]
# print(numbers)
# bubble_sort(numbers)
# print(numbers)

# numbers = [1,2,3,4,5,61,2,3,6,7,8,9,4,3,10,45,47,18,19,20]
# k = []
# for i in range(len(numbers)):
#     if i not in (len(numbers)):
#         k.append(i)
# print(k)


# import random
# x = {}
# for v in range(1,21):
#     z = random.randint(1,100)
#     x.update({str(z) : z})


# print((x))





# def bubble_sort(numbers):
#     for i in range(len(numbers)):
#         for j in range (len(numbers) -1):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]



# numbers = [3,2,5,4,1,7,6,5,4,8,9,10,4,2,1,0]
# print(numbers)
# bubble_sort(numbers)
# print(numbers)

import random
x = {}
for v in range(1,21):
    z = random.randint(1,100)
    x.update({str(z) : z})

print(x)
d = {}
for key, value in x:
    if value not in d:
        d[key] = value
print(d)



























