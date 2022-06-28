prod = int(input("what is the number times-table?"))
num = int(input("enter the number you want it to stop at"))
for i in range(1, num+1):
    x = prod * i
    print(prod, "x", i, "=", x)
    
