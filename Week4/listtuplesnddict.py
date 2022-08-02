# # # # # # # aList = []
# # # # # # # for numbers in range(1, 11):
# # # # # # #     aList = aList + [numbers]
# # # # # # # print(aList)

# # # # # # aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # # # # for item in aList:
# # # # # #     print(item)

# # # # # aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # # # for i in range(len(aList)):
# # # # #     print(i, (aList[i]))


# # # # aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # # aList[0] = 100
# # # # aList[3] = 50
# # # # print(aList)


# # # values = []
# # # for i in range(10):
# # #     newValue = int(input( "Enter integer %d: " % (i)))
# # #     values += [ newValue ]
# # #     print(values)

# # # to unpack
# # aString = "abc"
# # aList = [ 1, 2, 3 ]
# # aTuple = "a", "A", 1
# # first, second, third = aList
# # print(first, second, third)

# # first, second, third = aString
# # print(first, second, third)



# # L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,15,78,56,67,100,98,12,23,1,2,3,5,4,4,4,3,2,88,88,]
# # frequencies = []
# # for i in range(1,101):
# #     frequencies.append(L.count(i))
# # print(frequencies)

# # S= []
# # L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,15,78,56,67,100,98,12,23,1,2,3,5,4,4,4,3,2,88,88,]
# # for i in L:
# #     S.append(L)
# #     print(S)
# s = []       
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,15,78,56,67,100,98,12,23,1,2,3,5,4,4,4,3,2,88,88,]
# for item in L:
#     if item in S:
#         s.remove(item)
#     s.append(item)
# print(s)
# responses = [1,2,3,4,5,6,7,6,4,5,23,2,3,4,5,6,12,9,10]
# for item in responses:
#     print(item)
#     responses.sort()


# Use a list to solve the following problem: Read in 20 numbers. As each number is read, print
# it only if it is not a duplicate of a number already read.

numbers = [1,2,3,4,5,61,2,3,6,7,8,9,10,45]
# print(list(set(numbers)))
der = set()
for i in numbers:
    if i not in der:
        der.add(i)
print(der)



#Create a dictionary of 20 random values in the range 1–99. Determine whether there are any duplicate values in the dictionary. (Hint: you many want to sort the list first.
import random
c = list(range(20))
v = []
for i in range(20):
    x = random.randint(1, 99)
    v.append(x)
print(f"c{})
c = dict(v)