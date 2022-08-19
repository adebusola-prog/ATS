from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return (f"({self.x} {self.y})")
    
    def move(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
        newx = self.x + self.x2
        newy = self.y + self.y2
        return(f"({newx} {newy})")

    def dist(self, p):
        return (sqrt((self.x - p.x)**2) + ((self.y - p.y)**2))

    # def dist(self, point):
        #return (sqrt((self.x - point.x)**2) + ((self.y - point.y)**2))

# p1 = Point(2, 3)
# p2 = Point(3, 3)
# print(p1.show())
# print(p1.move(10, -10))
# print(p2.show())
# print(p1.dist(p2))














def rand_sent(num):
    import random
    subjects =["Dele", "she", "He", "Ade", "Olu", "Ope"]
    verbs = ["is", "come", "go", "read", "sit", "leave"]
    objects = ["there", "going", "happy", "here", "reading", "dancing"]
    sentence = []
    for i in range(num): 
        x = random.choice(subjects)
        y = random.choice(verbs)
        z = random.choice(objects)
        sentences = x + " " + y + " " + z
        sen = sentences.split(",")
        for i in sen:
            if sen not in sentence:
                sentence.append(sen)
        print(sentence)

        # print(sen)
        # sentence.append(sen)
        # for i in sentence:
        #     print(i)



        for i in sentences:
            if sentences not in sentence:
                sentence.append(sentences)
        else:
            print("no more word to form") 
    sentence.append(sentences)
    print(sentence)

rand_sent(10)

























# def ordinal(x):
    
#     if x[-1] == "0":
#         return x + "th"
#     elif x[-1] == "4" or x[-1] == "5" or x[-1] =="6" or x[-1]==7 or x[-1]==8 or x[-1]==9:
#         return x + "th"
#     elif x[-1] == "2":
#         return x + "nd"
#     elif x[-1] == "3":
#         return x + "rd"

# x = input("enter a number")
# print(ordinal(x))