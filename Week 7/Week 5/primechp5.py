# for i in range(2, 1000):
#     if len(i)== 1:
#         print(1)
# def prime(n):
#     for i in range(n):
#         if n == 1 or n < 1:
#             return 0
#         elif n ==2:
#             return 1
#         elif n % 2 == 0:
#             return 0
#         else:
#             for i in range(2, n):
#                 if n % i == 0:
#                     return 0
#                 else:
#                     return 1
# print(prime(22)



# v = []
# for i in range(2, 100):
#     for j in range(2, i):
#             if i % j == 0:
#                 i = 0
#                 v.append(i)
            
#                 break
#     else:
#         i = 1
#         v.append(i)
# print(v)



v = []
for i in range (2, 1000):
    for j in range(2,i):
        if i % j == 0:
            i = 0
            v.append(i)
            break

    else:
        i = 1
        v.append(i)
print(v)














