def factorial(num):
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        while(num >1):
            fact *= num
        for i in range(1,num + 1):
            
print("The factorial of", num, "is", factorial(num))
        



