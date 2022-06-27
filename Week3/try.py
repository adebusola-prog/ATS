num1 = float(input("Enter numerator?"))
num2 = float(input("Enter denominator"))
try:
    result = num1/num2
except ValueError:
    print("This is not a number")
except ZeroDivisionError:
    print("Attempt to divide by zero")
else:
    print (" %.3f / %.3f  =  %.3f" % (num1, num2, result))
