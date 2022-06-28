# (no 1) Write a program to print the following number pattern using a loop.
plus = "12345"
x = " "
for i in plus:
    x = (x + i)
    print(x)
    



#(no 2) For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
plus = []
num = eval(input("enter a number"))
for i in range(1, num+1):
    plus.append(i)
    s = print(plus)
print(sum(plus))






# (no 3) Write a program to print multiplication table of a given number till 12
prod = int(input("what is the number times-table?"))
num = int(input("enter the number you want it to stop at"))
for i in range(1, num+1):
    x = prod * i
    print(prod, "x", i, "=", x)
    





# (no 4) Write a program to display only those numbers from a list that satisfy the following conditions
#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop

numb = [12, 75, 150, 180, 145, 525, 50]
n = []
for r in numb:
    if r > 150 and r <= 500:
        continue
    if r > 500:
        break
    if r % 5 == 0:
        n.append(r)

print(n)





#(5)Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)







