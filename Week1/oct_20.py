# from random import sample
# import random
# from re import I
# def sample_name(n):
#    v=[]
#    y=[]
#    for i in range(5):
      
#       x= sample(n, 2)
#       v.append(x)
#       if x not in y:
#          y.append(x)
#    print(v)
#    print(y)

# sample_name(["adeola", "adebusola", "iyanu"])


# def picck(s):
#    for i in range(len(s)):
#       x=random.choice(s)
#       print(x)

# picck("abcvergtutjskslaksjdksk")


# def players(n=list):
#    x=random.shuffle(n)
#    for i in n:
#       print(i, "it's your turn")


# players(['drogba', 'Ronaldo', 'Messi', 'Serena'])



# def decide_name(n):
#    x=n.split()
#    random.shuffle(x)

#    team=[]
#    for i in range(0, len(x), 2):
#       team.append([x[i], x[i+1]])
#    print(team)

# decide_name("DROGBA selina OBAFEMI GORI")

# from string import punctuation
# def word(w, n=str):
#    for c in punctuation:
#       n=n.replace(c, '')
#    n=n.lower()
#    n= n.split()

#    print(w, 'appears', n.count(w), 'times')

# word('ade', 'ade olu wa ni si mi')


# word=input('enter a string: ')
# encrypt = word[0::2] + word[1::2]
# print(encrypt)
# decrypt=encrypt[0::2] + encrypt[1::2]
# print(decrypt)



# i=0
# num=1
# while i< 10 and num >0:
#    num=eval(input("enter a number"))
num=10
v=[]
for i in range(2, num):
   if num % i ==0:
      # v.append(i)
      # print(v)
      break
else:
   print(i)



