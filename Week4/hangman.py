# c = []
# x = "password"
# for i in x:
#     i = "_"
#     # print(i)
#     c.append(i)
# print(c)
# import random
# d = ["trials", "faith", "tiger", "Lion"]
# for i in range(5):
#     x = random.choice(d)
#     print(x)
#     y = input("guess the word")
#     if y == x:
#         print("you guessed right")
#     else:
#         print("try again")
# v = " "
# for y in v
# word = "faith"
# for i in word:
#     i = "_"
#     v = v + i
#     # print(v)
#     x = input("guess the letter i the words")
#     if x in word:
#         s = v.replace(x, v)
#     print(s)
#     break
#         print("true")
#     else:
#         print("not true")
#     for y in v:
#         if x in word:
#             v = v.replace(x, y)
#             print(v)




# k = ""
# v = "faith"
# for i in v:
#     print(index(i))
#     print(x)
#     for i in v:
#     i = "_"
#     k = k + i
#     g = input("guess v")
#     # g = g.lower()
#     if g in v:
#         print(v[k.index(g)])





import random
def hangman():
    list_hangman= ["Letter", "Happiness","Backend", "House", "Pneumonoultramicroscopicsilicovolcanoconiosis", "Methionylthreonylthreonylglutaminylarginyl", "Supercalifragilisticexpialidocious", "Pseudopseudohypoparathyroidism", "Antidisestablishmentarianism", "Aequeosalinocalcalinoceraceoaluminosocupreovitriolic"]  
    word = random.choice(list_hangman)
    # print(word)
    fail = 10
    letter_guessed = ""
    while fail > 0:
        # print("_", end="")
        guess = input("\nEnter a letter: ")

        if guess in word:
            pass
        else:
            fail -= 1
            print("Not in the word")

        letter_guessed =  letter_guessed + guess
        wrong = 0

        for letter in word:
            if letter in letter_guessed:
                print(f"{letter}", end="")
            else:
                print("_", end="")
                wrong += 1

        if wrong == 0:
            # print(f"{word}")
            print(f"\nYou won!")
            break
        # elif wrong == 2:
            # print(f"\nYou Lose!")
        # else:
            # print(f"\nYou Lose!")
            # break
hangman()





























