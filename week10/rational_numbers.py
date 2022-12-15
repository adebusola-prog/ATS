#find the HCF of the smallest integer out of the denominator or numerator. here, it is the numerator 
class Rational:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2
    
    def reduced_form(self, numerator, denominator):
        self.numerator = numerator
        self.denominator= denominator
        g =[]
        h =[]
        f = []
        v = []
        if self.denominator > self.numerator:
            for i in range(1, self.numerator+1):
                if self.numerator % i == 0:
                    v.append(i)
            print(v)
            for i in v:
                if self.denominator % i == 0:
                    f.append(i)
            div_no =max(f)
            reduced_numerator = self.numerator/ div_no
            reduced_denominator = self.denominator / div_no
            print(f"{reduced_numerator} / {reduced_denominator}")


        elif numerator > self.denominator:
            for i in range(1, self.denominator+1):
                if self.denominator % i == 0:
                    h.append(i)
            print(h)
            for i in h:
                if self.numerator % i == 0:
                    g.append(i)
            div_no2 = max(g)
            reduced_numerator = self.numerator/ div_no2
            reduced_denominator = self.denominator / div_no2
            print(f"{reduced_numerator} / {reduced_denominator}")

    def add_rational(self, num1, num2, den1, den2):
        red1 = self.reduced_form(num1, den1)
        red2= self.reduced_form(num2, den2)
        x = (den1 * den2) / (den1) * (num1)
        y = (den1 * den2) / (den2) * (num2)
        z = (x + y)
        h = (den1 * den2)
        answer = self.reduced_form(z, h)
        # print(answer)
        
    def subtract_rational(self, num1, num2, den1, den2):
        red1 = self.reduced_form(num1, den1)
        red2= self.reduced_form(num2, den2)
        x = (den1 * den2) / (den1) * (num1)
        y = (den1 * den2) / (den2) * (num2)
        z = (x - y)
        h = (den1 * den2)
        answer = self.reduced_form(z, h)

    def division_rational(self, num1, num2, den1, den2):
        red1 = self.reduced_form(num1, den1)
        red2= self.reduced_form(num2, den2)
        x = (num1 * den2) 
        y = (num2 * den1)
        h = self.reduced_form(x, y)

    def multiply_rational(self, num1, num2, den1, den2):
        # red1 = self.reduced_form(num1, den1)
        # red2= self.reduced_form(num2, den2)
        red3 = (num1 * num2) 
        red4 = (den1 * den2)
        h = self.reduced_form(red3, red4)
    

# rational = Rational((9/12), (2/4))
# rational.reduced_form(444, 33)
# rational.add_rational(4,3,2,6)
# rational.subtract_rational(4,3,2,6)
# rational.division_rational(4,3,2,6)
# rational.multiply_rational(10,3,2,6)


def sect():
    import random
    d = ["faith", "tiger", "Lion"]
    # for i in range(5):
    x = random.choice(d)
    k = len(x)
    v = "_"
    r = v*k 
    print(r)
    print(x)
    


    alphabet = x
    v = ""
    while True:
        secret_message = input('guess the word ')
        secret_message = secret_message.lower()
        # while secret_message != x:
        # for i in range(5):
        for c in secret_message:
            if c in x:
                c = (x[secret_message.index(c)])
                # print (x[secret_message.index(c)])
                v = v + c
                
                continue
                
            if c not in x:
                c = "_"
                v = v + c
        print(v)
                
            
        if v == x:
            print("you win")
        else:
            print("try again")

           
    

sect()
