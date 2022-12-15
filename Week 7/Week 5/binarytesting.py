# def binary_search(numbers, search_element, Low, High):
#     if Low > High:
#         return False
#     else:
#         Mid = (Low + High)//2
#         if numbers[Mid] == search_element:
#             return Mid
#         else:
#             if search_element < numbers[Mid]:
#                 return binary_search(numbers, search_element, Low, Mid-1)
#             elif search_element > numbers[Mid]:
#                 return binary_search(numbers, search_element, Mid + 1, High)
#             else:
#                 return -1


# search_element = 16
# numbers = [2,5,6,8,10,11,13,15,16]
# result = binary_search(numbers, search_element, 0, len(numbers)-1)
# if result != -1:
#     print("Index", result)








# Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):
#   if high >= low:







#5.5 The Sieve of Eratosthenes) A prime integer is any integer greater than 1 that is evenly divisible only by itself and 1. The Sieve of Eratosthenes is a method of finding prime numbers. It operates

# def prime(numbers):
#     v = []
#     for i in range (2, numbers):
#         if i not in v:
#             print(i)
#             for j in range (i*i, numbers+1, i ):
#                 v.append(j)


# print(prime(1000))


#     mid = (high + low) // 2
#     if arr[mid] == x:
#       return mid
#     elif arr[mid] > x:
#       return binary_search(arr, low, mid - 1, x)
#     else:
#       return binary_search(arr, mid + 1, high, x)

#   else:
#     return -1

# arr = [ 2, 3, 4, 10, 40 ]
# x = 10

# result = binary_search(arr, 0, len(arr)-1, x)

# if result != -1:
#   print(result)
# else:
#   print("Element is not present in array")



# def bubble_sort(numbers):
#     for i in range(len(numbers)):
#         for j in range (len(numbers)-1):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]



# numbers = [3,2,5,4,1,7,6,5,4,8,9,10,4,2,1,0]
# print(numbers)
# bubble_sort(numbers)
# print(numbers)
# t = []
# L = [2,3,4,5,6]
# for i in range (len(L)):
#     L[i] == L[i]**2
#     t.append(L[i]**2)
# print(t)

# import random
# L = []
# for i in range(20):
#     L = L + [random.randint(1,80)]
    

# print(L)

# L = [1,3,5,2,3,6,7,8,3,2]
# count = 0
# for i in L:
#     if i ==3:
#         count = count + 1
# print(count)




# scores = [1,2,3,5,5,56,67,100,4,100,101,100,100,5,6,3,2,1,7,8]
# frequencies = []
# for i in range(1):
#     frequencies.append(L.count(100))
#     print(frequencies)
# x = sorted(scores)
# print(x)
# print(x[0], x[1])
# print(x[-1], x[-2])
# num_right = 0
# print('What is the capital of France?', end=' ')
# guess = input()
# if guess.lower()=='paris':
#     print('Correct!')
#     num_right+=1
# else:
#     print('Wrong. The answer is Paris.')
#     print('You have', num_right, 'out of 1 right')
# #Question 2
# print('Which state has only one neighbor?', end=' ')
# guess = input()
# if guess.lower()=='maine':
#     print('Correct!')
#     num_right+=1
# else:
#     print('Wrong. The answer is Maine.')
#     print('You have', num_right, 'out of 2 right,')


# questions = ['What is the capital of France?',
# 'Which state has only one neighbor?']
# answers = ['Paris','Maine']
# num_right = 0
# for i in range(len(questions)):
#     guess = input(questions[i])
#     if guess.lower()==answers[i].lower():
#         print('Correct')
#         num_right=num_right+1
#     else:
#         print('Wrong. The answer is', answers[i])
#     print('You have', num_right, 'out of', i+1, 'right.')





# questions = ["what is the capital of France?",
#             "which stat has no neighbours?"]

# answers = ["paris", "maine"]
# answer_right = 0
# for i in range(len(questions)):

#     guess = input(questions[i])
#     if guess.lower() == answers[i].lower():
#         print("Correct")

# v = []
# x = int(input("enter the first integer"))
# y = int(input("enter the second integer"))
# z = int(input("enter the third integer"))
# a = int(input("enter the fifth integer"))
# f = x + y + z + a
# print(f)
# v.append(x)
# v.append(y)
# v.append(z)
# v.append(a)
# print(v)
# s = v[0]
# print(s)
# k = v[-1]
# print(k)

# if 5 in v:
#     print("yes")
# else:
#     print("no")
# count = 0
# for i in range(len(v)):
#     count += 1
# print(count)




# h = v[::-1]
# print(h)







# Bubble sort
# def bubble_sort(list_a):
#     indexing_length = len(list_a)-1
#     sorted = False
#     while not sorted:
#         sorted = True
#         for i in range(0, indexing_length):
#             if list_a[i] > list_a[i+ 1]:
#                 sorted = False
#                 list_a[i], list_a[i + 1] = list_a[i + 1],  list_a[i]


#     return list_a
# print(bubble_sort([2,3,1,4,5,2,3,7,8,9,12,6,67]))

# import random
# x = {}
# for v in range(1,21):
#     z = random.randint(1,100)
#     x.update({str(z) : z})


# val = []
# for char in x.values():
#     val.append(char)


# f = set(val)
# if len(f) == len(val):
#     print("no duplicates")
# else:
#     print("there are duplicates")








# numbers = [2,5,6,8,1,4,11,13,15,16]
# x = sorted(numbers)
# print(x)




# x = int(input("enter the first ID"))
# for i in range(x, 2021):
#     print(i)


# import random
# x = {}
# for v in range(1,21):
#     z = random.randint(1,100)
#     x.update({str(z) : z})

# print(x)
# d = {}
# for key, value in x:
#     if value not in d:
#         d[key] = value
# print(d)

# import random
# x = {}
# for v in range(1,21):
#     z = random.randint(1,100)
#     x.update({str(z) : z})
# # print(x)

# val = [value for value in x.values()]
# f = set(val)
# if len(f) == len(val):
#     print("no duplicates")
# else:
#     print("there are duplicates")





# def bubble_sort(numbers):
#     for i in range(len(numbers)):
#         for j in range (len(numbers) -1):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# numbers = [3,2,5,4,1,7,6,5,4,8,9,10,4,2,1,0]
# # print(numbers)
# bubble_sort(numbers)
# print(numbers)
















import random
def CAI():
    x = random.randrange(1, 10)
    y = random.randrange(1, 10)
    m = x * y
   

    while True:
        k = input(str(f"How much is {x} times {y}?"))
        h = int(k)
        if  h == m:
            print("Very good!!!")
            CAI()
            break
        else:
            print("No, please Try again")
    

CAI()

# def binary_search(numbers, search_element, Low, High):
#     if Low > High:
#         return False
#     else:
#         Mid = (Low + High)//2
#         if numbers[Mid] == search_element:
#             return Mid
#         else:
#             if search_element < numbers[Mid]:
#                 return binary_search(numbers, search_element, Low, Mid - 1)
#             elif search_element > numbers[Mid]:
#                 return binary_search(numbers, search_element, Mid + 1, High)
#             else:
#                 return -1


# search_element = 14
# numbers = [2,5,6,8,10,11,13,14,16]
# result = binary_search(numbers, search_element, 0, len(numbers)-1)
# if result != -1:
#     print("Index", result)






































































































