import random

names = ["Tayo", "Titi", "Shola", "Pelumi", "Abayomi"]
Verbs = ["goes", "comes", "brings", "tells", "picks"]
objects = ["home", "back", "it", "lies", "all"]
def generate_words(n: int):
    sentences = []
    for i in range(n):
        sentence = f'{random.choice(names)}' {random.choice(Verbs)} {random.choice(objects)}
        if sentence not in sentences:
            print(sentence)
            sentences.append(sentence) 
        print(len(sentences))
        generate(1000)
for i in range(0, 10):
     subject = (random.choice(names))
     action = (random.choice(Verbs))
     object = (random.choice(objects))
     print("{} {} {}". format(subject,action,object))

# A generator function that can take an integer and will print n number of sentences 
def make(p):
    for i in range(0, p):
        subject = (random.choice(names))
        action = (random.choice(Verbs))
        object = (random.choice(objects))
        print("{} {} {}". format(subject,action,object))
make(5)

# question 3
a = input("what is the first sentence?")
sentence_1 = ["Pelumi picks home", "Abayomi goes home", "Abayomi brings it", "Titi tells back", "Shola brings lies"]
if sentence_1 == "a":
    print("Abayomi goes home")
elif sentence_1 != "a":






    
    
