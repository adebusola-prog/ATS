# class Parent:
    

#     def __init__(self, a):
#         self.a = a
        

#     def print_var(self):
#         print("this is my doing and not yours")
#         print(self.a)



# class Child(Parent):
#     def __init__(self,a,b):
#         Parent.__init__(self,a)
#         self.b = b

#     def print_var(self):
#         Parent.print_var(self)
#         print(self.b)


# c = Parent("hellooo")
# c2= Child("hello", "Sule")
# print(c.print_var)
# c2.print_var

# v = " "

# name = "Adebusola"
# for i in name:
#     x =i * 2
#     v = v + x
# print(v)


name = "ELVIS"
# print(len(name))

# for i in range(len(name)):
    # print(name[:i+1], end = ' ')

# s = "0ame"
# for i in s:
#     if s[].isalpha:
#         print("yes")
# else:
#     print("no")

# s = input('Enter a string')
# if s[0].isalpha():
#     print('Your string starts with a letter')
# if not s[0].isalpha():
#     print('Your string contains a non-letter.')


# d = {"name": "Ade", "class": "sophomore"}
# for k in d.keys():
    
# s = "Hello"
# s = s.lower()
# print(s)

# concatenated_list = [10, 20, 30, 40, 50]
# for i in range(len(concatenated_list)):
#     print(f"{i} : {concatenated_list[i]}")

# numbers = list(range(0,10))
# print(numbers)

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
# for i in responses:
f = responses.count(i)
print(f"{i} : {f}")


responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
for i in range(1, 6):
    print(f'{i} appears {responses.count(i)} times in responses')


















































