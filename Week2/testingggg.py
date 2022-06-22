# Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference
#and area. Use the constant value 3.14159 for π. Do these calculations in output statements

r = int(input("what is the radius?"))
p = 3.14159
print("pie is", p)

circumference = 2*p*r
print("circumference is", circumference)

area = p*r**2
print("area is", area)

diameter = 2*r
print("diameter is", diameter)



#Write a program that reads in two integers and determines and prints whether the first is a
#multiple of the second. (Hint: Use the modulus operator.)

a = int(input("what is the first integer?"))
b = int(input("what is the second integer?"))

if b % a == 0:
    print("first integer is a multiple of second integer")
else:
    print("first integer is not a multiple of second integer")