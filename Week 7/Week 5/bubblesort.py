#5.6(Bubble Sort) Sorting data
# def bubble_sort(list_a):
#     indexing_length = len(list_a)-1
#     sorted = False
#     while not sorted:
#         sorted = True
#         for i in range(0, indexing_length):
#             if list_a[i] > list_a[i+ 1]:
#                 sorted = False
#                 list_a[i], list_a[i + 1] = list_a[i + 1],  list_a[i]


#     return list_a
# print(bubble_sort([2,3,1,4,5,2,3,7,8,9,12,6,67]))



# s = [2,3,1,4,5,2,3,7,8,9,12,6,67]
# for i in range(len(s)):
#     print(len(s))
#         # s[i], s[i + 1] = s[i + 1], s[i]
#     # print(s)

# c = "pizza"

# for i in range(len(c)):
#     print(c[1])
#     # if i == 'a':
#     #     i = 'y'
#     # sww2print(i)

class Enemy:
    life = 3

    def __init__(self):
        print("game starts now!!!!!!!!!!!")
        
    def attack(self):
        print("ouch!!!")
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print("I will attack you!!")
           
        else:
            print("I have " + str(self.life) +  " life")


x = Enemy()
x.attack()
x.attack()
x.attack()
x.check_life()

































