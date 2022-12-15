# user_name = input("what is your user_name?")
# pass_word = input("what is your password?")
# if (user_name=="Adebusola") and (pass_word=="redbolt"):
#     print("login successful!")
# else:
#     print("incorrect login!")


# def str_to_list(str) :
#     semi_output= list(str)
#     output= []
#     for char in semi_output:
#         if char != " ":
#             output.append(char)
#     return(output)

# print(str_to_list("5 dollar"))

# x="5 dollar"
# for i in x:
#     y=x.replace(" ", "")
# print(y)
# # # print(str("5 dollar"))

# def remove(string):
#     return "".join(string.split())
     
# # Driver Program
# string = '5 dollar'
# print(remove(string))

# y= "".join(x.split())
# print(list(y))
# def gert():
#     lsk = []
#     x = [345, 10, 9, 5, 2]
#     for i in x:
#         y = str(i)
#         lsk.append(y)
#         # return(lsk)
#     for char in lsk:
#         # print(char)
#         if char.endswith("0"):
#             return("zero")
#         if char.endswith("5"):
#             return("five")
#         else:
#             return 1
# #             # for nm in x:
# #             #     if (nm% 2) == 0:
# #             #         return("even")
# #             #     else:
# #             #         return("odd")

# print(gert())
def gert():
    v = []
    x = ["345", "10", "9", "5", "2"]
    for char in x:
        if char.endswith("0"):
            v.append("zero")
        elif char.endswith("5"):
            v.append("five")
        else:
            v.append(1)
    print(v)

gert()