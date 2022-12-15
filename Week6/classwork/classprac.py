class Enemy:
    life = 3

    def attack(self):
        print("ouch!!")
        self.life -= 1
        # if self.life <= 0:
        #     print("I am dead")
        # else:
        #     print(str(self.life) + "life left")

    def check_life(self):
        # self.life -= 1
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + "life left")


e = Enemy()
e1 = Enemy()



e.attack()
e.check_life()
e.check_life()
e1.check_life()



class Enemy:
    def __init__(self, x):
        self.energy = x

    def rem_energy(self):
        print(self.energy)



flipper = Enemy(5)
glipper = Enemy(34)

flipper.rem_energy()
glipper.rem_energy()


class Girl:
    gender = "female"

    def __init__(self, name):
        self.name = name


g = Girl("Becky")
h = Girl("Umi")
print(g.name)
print(h.name)
print(g.gender)
print(h.gender)

class Parent():
    def last_name(self):
        print("Adeyeye")

class Child(Parent):
    def first_name(self):
        print("Adebusola")
    # def last_name(self):
    #     print("Iyanu")
c = Child()
c.last_name()
# c.first_name()

class Mario():
    def move(self):
        print("I am moving")

class Shroom():
    def running(self):
        print("I am big")


class Frety(Mario, Shroom):
    pass

b = Frety()
b.move()
b.running()


import threading

class Ght(threading.Thread):
    def take(self):
        for i in range(10):
            print(threading.current_thread().getName())

v = Ght(name = "send me my food")
b = Ght(name ="I will deal with you")
v.start()
b.start()







class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

e = Example(8, 6)
print(e.add())


a = 6
try:
    c = a/0
except Exception as f:
    print(f)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
    	print(self.name)
   
r = Person("Peter", 35) 
r.myfunc()


def act(n):
    if n==0:
        return 1
    else:
        return n*act(n-1)

x = act(10)
print(x)





def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


print(fact(6)) 









# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
        

# print(fact(5))

































































        


        






























