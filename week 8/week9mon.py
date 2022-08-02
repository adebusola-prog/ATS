# fruit = "banana"
# # index = 0
# # while index < len(fruit):
# #     letter = fruit[index]
# #     print(index, letter)
# #     index += 1
# for letter in fruit: 
#     print(letter)


# person = {"name": "zed", "age": 39, "height": 6 * 12 + 2, "college":" "}
# person.setdefault()

# print(type(person))
# print(person["age"])
# person["age"]= 560
# print(person)
# person["height"] = person["height"] + 5
# print(person)
# person["hobby"] = "singing"
# print(person)
# person.pop("height")  #since pop is a method, specify the key to be removed inside the bracket
# print(person)
# del person["name"]
# print(person)
# person.popitem()
# print(person)
# print(person.fromkeys("name" "zed"))
# person_attribute = {"marital status":"single", "gender": "female"}
# person.update([("gender", "hermaphrodite"), ("Best food", "Crab and mango")])
# print(person)
# courses = {}
# courses["AGE"] = "Intro to Agric economics"
# courses.update({"AGY": "Intro to data"})
# print(courses)
# courses = dict([("name", "car"), ("brand", "Toyota")])
# print(courses)
# import random
# x = {}
# for i in range(100):
#     y = random.randint(1,100)
#     x.update({str(y):y})
# print(x)



# val = [value for value in x.values()]
# f = set(val)
# if len(f) == len(val):
#     print("no duplicates")
# else:
#     # print("there are duplicates")

# m = ["name", "class", "school", "religion"]
# n = ["Derin", "Sophomore", "First Technical University", "Buddhism"]
# zipped = zip(m,n)
# x = dict(zipped)
# print(x)
# for k,v in x.items():
    # print((k,v))
# for k in x.keys():
#     print(k, end = " ")
# for v in x.values():
#     print(v)



# print(x["name"]["lastname"])
# word = "ADEMRI"
# points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
# 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
# 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
# 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}
# f = points.copy()
# # print(f)
# for key in points:
#     print(points[key])
# # total = 0
# # for c in word:
# #     total = total + points[c]
# # print(total)
# v =[]
# for c in word:
#     x = points[c]
#     v.append(x)
# print(v)
#     # points[c] += 1
# print(sum(v))  
# from random import shuffle
# deck = [{'value':i, 'suit':c} for c in ['spades', 'clubs', 'hearts', 'diamonds'] for i in range(2,15)]
# shuffle(deck)
# print(deck[0]['value'])
# print(deck[0]['suit'])
# for i in range(2,15):
#     for c in ['spades', 'clubs', 'hearts', 'diamonds']:
    
#         deck = [i, c]
#         shuffle(deck)
#         print(deck)
        # print(deck['value'])
        # print(deck['suit'])

L = [[1,2,3],
[4,5,6],
[7,8,9]]

x = L[2][1]
print(x)




































