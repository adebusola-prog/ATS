# def listDivPrim(num):
#     listDiv = []
#     num = int(input("enter a number"))
#     for i in range(2, num + 1):
#         if num % i == 0:
#             listDiv.append(i)
#     print(f"The divisors of {num} are {listDiv}")

#     v = []
#     for i in listDiv:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             v.append(i)
#     print(f"The prime divisors of {num} are {v}")
def testprim(x, n):
    v = []
    for i in range(x, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            if i == 1 or i ==0:
                continue
            else:
                v.append(i)
    print(f"These are the prime numbers between {x} and {n} -> {v}")
 

x =int(input("enter a number"))
n = int(input("enter a number"))
testprim(x, n)