def fib(n):
    numbers = []
    for i in range(n-1):
        if i == 0 or i == 1:
            numbers.append(i)
        else:
            numbers.append(numbers[i-1] + numbers[i-2])
    print(numbers)


fib(100)


# cars = {"brand": "Toyota", "Year": 2019}
# x = cars.keys()
# print(x)

# def fac(n):
#     result = n
#     while n > 1:
#         n -= 1
#         result *= n
#     return result

# print(fac(5))

