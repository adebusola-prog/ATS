def isPrime(n):
    prime_numbers = [2, 3]
    not_prime_numbers = [1]
    for i in range(3, n+1, 2):
        if n%i == 0 and n == 1 and n!=1 and n == 2:
            return False
            not_prime_numbers.append(i)
        else:
            return True
            prime_numbers.append(i)
    return prime_numbers
    return not_prime_numbers

print(isPrime(5))
