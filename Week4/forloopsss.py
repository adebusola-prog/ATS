#Write a for loop that prints out numbers from 1 to 10
for i in range(11):
    print(i)

#Write a for loop that prints out even numbers between 1 and 1000
for i in range(1000): # range(1,1000)
    if i != 0 and i%2 == 0:
        print(i)
  

#Write a for loop that prints out odd numbers between 1 and 1000
for i in range(1000):
    if i !=0 and  i%2 != 0:
        print(i)


#Write a while loop equivalent for the tasks above
n = 1
while n < 11:
    print(n)
    n += 1

i= 0
while i <= 1000:
    if i % 2 == 0:
        print(i)
    i = i+1
    

i = 0
while i <= 1000:
    if i % 2 != 0:
        print(i)
    i = i+1