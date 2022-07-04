#consonant = ("b c d f g h j k l m n p q r s t v w x y z")
#x = consonant.split()
#print(x): check from (aniS)
def prime(num):
     for n in range(2, num-1):
        for x in range (2, num-1):
            if n % x == 0:
                return False
            else:
                return True

print(prime(5))