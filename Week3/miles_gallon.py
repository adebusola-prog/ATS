#The program should calculate and display the miles per gallon obtained for each tankful. 
# Total miles driven divide by total gallons used


miles = []
gallon= []
while True:
    a = float(input("what is the mile driven?"))
    b = float(input("what is the gallon used?"))
    if a == 1 and b == -1:
        print("not possible")
        break
    miles.append(a)  
    gallon.append(b)
    print(miles)
    print(gallon)
    average = sum(miles)/ sum(gallon)
    print(average)