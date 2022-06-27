'''def perfect(n):
    factor=0
    if n == 2:
        return False
    for i in range(1,n):
        if n%i == 0:
            factor +=i
    if factor == n:
        return True
    else:
        return False

num = int(input("enter a number"))
if perfect(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number" )'''



def isPerfect(n):
    factor = 0
    if n == 2:
        return False
    for i in range(1, n):
        if n%i == 0:
            factor +=i
    if factor == n:
        return True
    else:
        return False


num = int(input("enter a number"))
print(isPerfect(num))

if isPerfect(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")













