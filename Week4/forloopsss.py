#Write a for loop that prints out numbers from 1 to 10
for i in range(11):
    print(i)

#Write a for loop that prints out even numbers between 1 and 1000
for i in range(0, 1001, 2):
    print(i)

#Write a for loop that prints out odd numbers between 1 and 1000
for i in range (1, 1000, 2):
    print(i)


#Write a while loop equivalent for the tasks above
n = 1
while n < 11:
    print(n)
    n += 1

n = 2
while n < 1001:
    print(n)
    n += 2

n = 1
while n < 1000:
    print(n)
    n += 2