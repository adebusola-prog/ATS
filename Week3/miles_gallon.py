# The program should calculate and display the miles per gallon obtained for each tankful. 
# Total miles driven divide by total gallons used


miles = []
gallon= []
while True:
    a = float(input("what is the mile driven?"))
    b = float(input("what is the gallon used?"))
    if a==1 or b == -1:
        break
    miles.append(a)  
    gallon.append(b)
    print('The miles / gallon for this tank was ', a/b)
    #print(miles)
    #print(gallon)

average = sum(miles)/ sum(gallon)
print("The overall average miles/gallon was ", average)