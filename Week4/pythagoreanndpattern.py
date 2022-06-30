for i in range(1, 11):
        print("*"*i)



for i in range(11, 0, -1):
        print("*"*i)



number_stars = 10
for i in range(number_stars):
    for j in range(1, number_stars - i):
        print(" ", end="")
    for k in range(0, i + 1):
        print("*", end="")
    print()



for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            if c > a and b and b > a:
                if c*c == a*a + b*b:
                    print(a, b, c)



      

