#.1
'''def rectangle(m, n):
    print("*" * n)
    print("*" * m)


rectangle(4, 4)

#2
def add_excitement(m:str, n:str,o:str):
    print("hello", end= " !")
    print("dear", end= " !")
    print("Tosin", end= " !")


add_excitement("m", "n", "o")

#3
def sum_digits(num):
    sum = 0
    for i in range(num+1):
        sum = sum + i
        if i != num:
            continue
        print(sum)

sum_digits(10)

#4a
sum_digit = str(47)
x = int(sum_digit[0]) + int(sum_digit[1])
print(x)'''




#4b
'''def sum_digit(n= "45678"):
    answer = 0
        for i in range(len(n)):
            answer = answer + int(n[i])
        print(answer)
        
sum_digit()

#
s = ' '
for i in range(10):
    t = input('Enter a letter:')
    if t=='a' or t=='d' or t=='e' or t=='y' or t=='e':
        s = s + t
print(s)


#6
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n >1):
            fact *= n
            n -= 1
        return fact

def binomial(n, k):
    a = factorial(n)/factorial(k) * factorial(n-k)
    return a

print(binomial(100, 4))
#9. Write a function called factors that takes an integer and returns a list of its factors
def factors(n):
    fac = []
    for i in range(1, n+1):
        if n % i == 0:
            fac.append(i)
    return fac
print(factors(24))



#8. Write a function called number_of_factors that takes an integer and returns how many factors the number has.
def number_of_factors(k):
    a = len(factors(k))
    return a

print(number_of_factors(54))'''



'''10. Write a function called closest that takes a list of numbers L and a number n and returns
the largest element in L that is not larger than n. For instance, if L=[1,6,3,9,11] and n=8,
then the function should return 6, because 6 is the closest thing in L to 8 that is not larger than
8. Don’t worry about if all of the things in L are smaller than n. '''  

'''def closest(L, n):
    s = []
    for i in L:
        if i < n:
            s.append(i)
    return max(s)


print(closest([19,10,3,9,11], 20))'''


''' 11 Write a function called matches that takes two strings as arguments and returns how many
matches there are between the strings. A match is where the two strings have the same character at the same index. For instance, 'python' and 'path' match in the first, third, and
fourth characters, so the function should return 3.'''


# def matches(m, n):
    # s = ""
    # for charr in m:
        # if charr in n:
            # s = s + charr
    # print(len(s))
    # return s
   
# print(matches("adenbi", "adebusola"))


'''Recall that if s is a string, then s.find('a') will find the location of the first a in s. The
problem is that it does not find the location of every a. Write a function called findall that
given a string and a single character, returns a list containing all of the locations of that character in the string. 
It should return an empty list if there are no occurrences of the character in the string.'''

'''ring = 'WEDDING RING'
x = ring.find("K")
print(x)'''

        

'''s = " "
f = "adebusola"
g = "a"
for i in range (len(f)):
    if g in f:
        s = s + 
        print(s)'''

'''r = []
s = input('Enter some text: ')
for i in range(len(s)):
    if s[i]=='a':
        r.append(i)
        print(r)'''



'''def find_all(s, n="a"):
    for i in range(len(s)):
        if n in s[i]:
            print(i)
    return [i]


find_all("adebusola", "a")'''



'''Write a function called change_case that given a string, returns a string with each upper
case letter replaced by a lower case letter and vice-versa.'''


'''def change_case(x):
    y = x.upper()
    print(y)
    return y


change_case("suPPer")'''

s = "suPPEr"
for i in s:
    if i in s==s.upper():
        y = s.lower()
    print(y)



































        







