n =64
for i in range(1, n):
    if n % i == 0:
       print(i, end=",")

m = (1 + 2 + 4 + 8 + 16 + 32)
print(m)
if m == n:
    print("this is a perfect number")
else:
    print("this is an imperfect number")