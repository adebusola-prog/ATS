from tkinter import N


def fac(n):
    FAC = []
    for i in range(1, n+1):
        if n % i == 0:
            FAC.append(i)
    return(FAC)

num = int(input("enter number"))
x = print(fac(num))


        
