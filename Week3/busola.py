'''def sum_digit(k=45678):
    n = str(k)

    answer = 0
     
    for i in range(len(n)):
        answer = answer + int(n[i])
   
        
    
    return answer
       
print(sum_digit())


def binomial(n, k):
    if n < 0 and k < 0:
        return 0
    elif n == 0 or n ==1 and k ==0 or k ==1:
        return 1
    else:
        fact = 1
        while (n > 1) and (k > 1):
            fact *= n/(k*(n-k))
            n -= 1 
            k -= 1
        return fact

num = int(input("enter a number for n"))
num2 = int(input("enter a number for k"))
print(binomial(num, num2))'''

'''def hypothenus(a, b, c):
    for i in range(a, b, c):
        if a < 1 and b < 1 and c < 1:
            return False
        if a <= 20 and b <= 20 and c <= 20:
            return True '''




























































