import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return  False
        else:
            return True


is_prime(8)
