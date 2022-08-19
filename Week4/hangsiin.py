# def sect():
#     import random
#     d = ["faith", "tiger", "Lion"]
#     # for i in range(5):
#     x = random.choice(d)
#     k = len(x)
#     v = "_"
#     r = v*k 
#     print(r)
#     print(x)
    


#     alphabet = x
#     v = ""
#     while True:
#         secret_message = input('guess the word ')
#         secret_message = secret_message.lower()
#         # while secret_message != x:
#         # for i in range(5):
#         for c in secret_message:
#             if c in x:
#                 c = (x[secret_message.index(c)])
#                 # print (x[secret_message.index(c)])
#                 v = v + c
#                 continue
                
#             elif c not in x:
#                 c = "_"
#                 # v = v + c
#         print(v)
                
            
#         # if v == x:
#         #     print("you win")
#         # else:
#         #     print("try again")

           
    

# sect()
            
# #     # for i in y:
# #     #     word = random.choice(d)
# #     #     for i in word:
# #     #         i = "_"
# #     #         v = v + i
# #     #         s = v.replace(x, v)





# #(5)computer-assisted instruction (CAI)( multiplication table)
# # import random

# # def CAI():
# #     x = random.randrange(1, 10)
# #     y = random.randrange(1, 10)
# #     m = x * y
   

# #     while True:
# #         k = input(str(f"How much is {x} times {y}?"))
# #         h = int(k)
# #         if  h == m:
# #             print("Very good!!!")
# #             CAI()
# #             break
# #         else:
# #             print("No, please Try again")

# # CAI()
import random
list_words = ["hello", "password", "real", "help"]
word = random.choice(list_words)
print(word)
print("_" * len(word))
guess_letter = ""
for i in range(len(word)):
    guess = input("can you guess the letters in the word")
    guess_letter += guess
    for x in word:
        if x in guess_letter:
            print(f"{x}", end="")
        else:
            print("_", end=" ")



























