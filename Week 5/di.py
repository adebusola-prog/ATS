# # spam = {'color': 'red', 'age': 42}
# # print('I am ' + str(spam.get('age', 0)) + 'years')
# # print(spam.values())
# # print(list(spam.keys()))

# # for k, v in spam.items():
# #     print(k,v)
# # if 'color' in spam.keys():
# #     print('color') 


# # picnicItems = {'apples': 5, 'cups': 2}
# # print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# # print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# # if 'beads' not in spam:
# #     spam['beads'] = 'green'
# #     print(spam)


# # spam = {'color': 'red', 'age': 42}
# # spam.setdefault("derty","killi")
# # print(spam)
# # message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# # count = {}



# # for character in message:
# #     count.setdefault(character, 0)
# #     count[character] = count[character] + 1
# # print(count)









# message = "All Things bright and beautiful"
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# print(count)


# print("Hello world")
# feeling = input("How are you feeling")
# while True:
#     if feeling.lower() == "great":
#         print("That's good to hear")
#     else: 
#         print("I am glad you are feeling good")


# x = "tryuy12345"
# y = x.isalnum()
# print(y)


# name = "John", "Peter", "Jona"
# x = ";".join(name)
# print(x)

# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"

# x = mySeparator.join(myDict)

# print(x)


# myDict = ("name", "John", "country", "Norway")
# mySeparator = "TEST"

# x = mySeparator.join(myDict)

# print(x)




# while True:
#     print("enter your name")
#     name = input()
#     if name.isalpha():
#         break
#     else:
#         print("enter your name in letters")

# while True:
#     print("enter your password")
#     password = input()
#     if password.isalnum():
#         break
#     else:
#         print("password has to contain both numbers and letters")



# word = "My name is Simon"
# print(word[5])
# x = word.split('m')
# print(x)
# print(x[1])


#print(chr(1999))

# for i in range(3):
# while True:
#     print("enter a name")
#     name = input()
#     if name == " ":
#         break
#     else:
#         print("you are welcome to Nigeria")

# grocceries = {"Regina":{"apple": 3, "avocado": 4, "teabread":10},
#             "Temiu":{"teabread": 5, "avocado":10 , "apple":8},
#             "refty":{"avocado":3, "apple":12, "teabread": 1}}


# def totalbought(guest, items):
#     numbought = 0
#     for k, v in grocceries.items():
#         numbought = numbought + v.get(items, 0)
#     return numbought


# print("- Apple"    + str(totalbought(grocceries, "apple")))


# dict = {}
# x = input("enter your product name")
# y = input("enter the prices")
# dict.update(x)
# dict.update(y)
# d = dict([("A", 200), ("B", 200)])
# print(d)
# def product_prices ():
#     m = {}
#     while True:
#         x = input("enter your product name")
#         y = int(input("enter the prices"))
#         d = dict([(x, y)])
#         if x == 'none' and y == 0:
#             break
#         else:
#             m.update(d)
#             print(m)
#     return m
# product_prices()

# def main():


   
    # print("what product would you like to know the prices?")
    # z =input("enter the product")
    # if z == x:
    #  print(product_prices(m["x"]))

    # if __name__ == '__main__':
    #             main()

m = {}
while True:
    x = input("enter your product name")
    y = int(input("enter the prices"))
    d = dict([(x, y)])
    if x == 'none' and y == 0:
        break
    else:
        m.update(d)
        print(m)

# print("what product would you like to know?")
# z = input("enter the product")
# print(m.get(z, "it does not exist"))



# print("what product would you like to know the prices?")
# z =input("enter the product")

# print(m["z"])
# print("the product is unavailable")





# m = {}
# while True:
#     x = input("enter your product name")
#     y = int(input("enter the prices"))
#     d = dict([(x, y)])
#     if x == 'none' and y == 0:
#         break
#     else:
#         m.update(d)
#         print(m)

# question = int(input("price"))
# # for k, v in m.items():
#     # print(k, v)
# for v in m.values():
#     if question < v in m.values():
#         print(v)
# hert = {"A": 1, "C": 5, "F": 3, "D": 7, "E": 4}
# items = list(hert)
# for i in items:
#     print(i)


# print(x)
# hert.sorted()
# print(hert)








