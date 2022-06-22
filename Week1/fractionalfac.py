n = 1
m = 2
o = 3
fact = 1
for i in range(1, n+1):
   fact *= i
   k =(1/fact)
for i in range(1, m+1):
    fact *= i
    q =(1/fact)
for i in range(1, o+1):
    fact *= i
    r = (1/fact)

print(k +q + r)
            