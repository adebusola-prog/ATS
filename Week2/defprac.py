def fib(n):
    result = []
    a, b = 0 , 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result 

fib(1000)
print(fib(1000))


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


def f(a, L=None):
    if L == None:
        L= []
        L.append(a)
        return L

print(f(1))
print(f(2))
print(f(3))



def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))



def f(a, L = None):
    L=[]
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))