def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n >1):
            fact *= n
            n -= 1
        return fact

def binomial(n, k):
    a = factorial(n)/factorial(k) * factorial(n-k)
    return a

print(binomial(100, 4))




# for a in range(1, 21):
#     for b in range(1, 21):
#         for c in range(1, 21):
#             if c > a and b and b > a:
#                 if c*c == a*a + b*b:
#                     print(a, b, c)   








