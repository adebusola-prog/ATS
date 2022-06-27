def isPrime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n%i == 0:
            return False
    else:
         return True


num = int(input("enter a number"))

if isPrime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")