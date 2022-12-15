def isPrime(x):
    """Returns whether or not the given number x is prime.

    A prime number is a natural number greater than 1 that cannot be formed
    by multiplying two smaller natural numbers.

    For example:
    - Calling isPrime(11) will return True
    - Calling isPrime(71) will return True
    - Calling isPrime(12) will return False
    - Calling isPrime(76) will return False
    """

    # your code here
    prime_numbers = [2, 3]
    not_prime_numbers = [1]
    """Returns whether or not the given number x is prime."""
    for i in range(3, x + 1, 2):
        if x % i == 0 and i != x and x == 1 and x != 2:
            return True
            not_prime_numbers.append(i)
        else:
            return False
            prime_numbers.append(i)
    return prime_numbers
    return not_prime_numbers

print(isPrime(8))

