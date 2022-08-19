def fact(n):
    if n == 0 or n == 1:
        return False
    else:
        fact(n-1)
    return fact(n-1)

print(fact(5))
