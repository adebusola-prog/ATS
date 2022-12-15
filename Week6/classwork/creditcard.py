#write a function that accepts a credit card number. It should return a string where all the characters are hidden with an 
#asteriks except the last four
v = []
s = [1,2,3,4,5,6,7,8,9,0,1,2,4,5,6,7]
for x in s[:12]:
    x = "*"
    v.append(x)
for y in s[12:]:
    v. append(y)
# print(v)

m = ' '.join(str(f) for f in v)
print(m)


If not 16 digit(it should return an error)
def creditCard(s:list):
    v = []
    for x in s[:12]:
        x = "*"
        v.append(x)
    for y in s[12:]:
        v. append(y)
    print(v)
    # print(str(v))

    m = ' '.join(str(f) for f in v)
    print(m)


creditCard([1234567890987654])



import os

files = os.listdir("journal")
print(files)


peg1 = "1"   #root
peg2 = "2"   #permanaent
peg3 = "3"   #temporary

def tower_of_hanoi(disks, peg1, peg2, peg3):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(peg1, peg2))  
        return    
    tower_of_hanoi(disks - 1, peg1, peg2, peg3)  
    
    
    print('Move disk {} from rod {} to rod {}.'.format(disks, peg1, peg2))  
    
    
    tower_of_hanoi(disks - 1, peg3, peg1, peg2)  
  
  
disks = int(input('Enter the number of disks: '))  

tower_of_hanoi(disks, peg1, peg3, peg2) 























































