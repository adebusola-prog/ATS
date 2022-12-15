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

# from pathlib import Path
# import os
# print("Hi")
# print(Path.cwd())


# with open(r'C:\Users\zeu\AppData\Local\Programs\Python\Python38\ASS.txt') as f:
#     f.read()


# import os
# os.chdir(r'C:\Users\Documents\ATS\star_poem.txt')
# file = open('ASS.txt')
# print(file)

# from pathlib import Path
# p = Path('spam.txt')
# p.write_text('Hello, world!')
# 13
# p.read_text()








#solve for musidict
# x = 1
# y = 2
# j = 3

# val = {"name": x, "class": y, "school": j}
# print(val["name"], val["class"], val["school"])




# text = "Behold, I come."
# # print(text)
# from string import punctuation
# text = text.lower()   #to change to lower case
# # print(text)
# for p in punctuation:
#     text = text.replace(p, '') # to replace the puctuations in the word given
#     print(text)
# words = text.split()      # to change to a list use split()
# print(words)


# items = ("aber", "bert", "deret", "carqer")
# # s = list(d)
# # print(s[1], s[0])
# # items = [(i[1], i[0]) for i in items]
# # items.sort()
# # for i in items:
# #     x = (i[0], i[1])
# #     print(x)

# items = [(i[1], i[0]) for i in items]
# items.sort
# print(items)
# # for i in items:
# #     print(i)




# text = "Behold, I come. I hope you take me away nooo, yes, I am going"
# from string import punctuation
# text = text.lower()
# for p in punctuation:
#     text = text.replace(p, '')
# words = text.split()
# print(words)

# d = {}
# for w in words:
#     if w in d:  
#         d[w] = d[w] + 1
#     else:
#         d[w] = 1
# print(d)

# items = list(d.items())
# items.sort()
# for i in items:
#     print(i)

# items = list(d.items())
# items = [(i[1], i[0]) for i in items]
# items.sort()
# for i in items:
#     print(i)


# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# key = 'xznlwebgjhqdyvtkfuompciasr'
# secret_message = input('Enter your message: ')
# secret_message = secret_message.lower()
# for c in secret_message:
#     if c.isalpha():
#         print(key[alphabet.index(c)],end='')
#     else:
#         print(c, end='')
# The string key is a random reordering of the alpha





# with open("today.txt") as f:
#     # print(f.read())
#     x = f.split()
#     # print(f.readlines())
#     print(x)

# lines = [line.strip() for line in open("today2.txt")]
# print(lines)
# # lines.close()
# games = [line.split(",")for line in lines]
# # print(games)
# # f = [line.split(",") for line in games]
# # print(f)
# for i in games: 
#     print(games[0])


# text = "Behold, I come. I hope you take me away nooo, yes, I am going"
# from string import punctuation
# text = text.lower()
# for p in punctuation:
#     text = text.replace(p, '')
# words = text.split()
# print(words)


# wordlist = [line.strip() for line in open("today2.txt")]
# # print(wordlist)
# for word in wordlist:
#     if len(word) == 3:
#         print(word)

lines = [line.strip() for line in open('today2.txt')]
print(lines)
games = [line.split(',') for line in lines]
print(games)
print(max([abs(int(g[2])-int(g[4])) for g in games]))




















































































