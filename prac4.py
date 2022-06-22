#consonant = ("b c d f g h j k l m n p q r s t v w x y z")
#x = consonant.split()
#print(x): check from (aniS)
def prime(num):
     for n in range(2, num):
        for x in range (2, num):
            if n % x == 0:
                return False
            else:
                return True

prime(5)