# count = 0
# word = ["ade", "gbenga", "Tolu", "ehii", "ola", "umi"]
# for w in word:
#     if w[:2] == "gb" or w[:2] == "To":
#         print(w)

# for x in range(-50,51):
#     for y in range(-50,51):
#         if 2*x+3*y==4 and x-y==7:
#             print(x,y)

# count = 0
# for word in wordlist:
# if word[0] in 'aeiou':
# count=count+1
# print(100*count/len(wordlist))




count = 0
word = ["ade", "gbenga", "Tolu", "ehii", "ola", "umi"]
for w in word:
    if w[0] in "aeiou":
        count = count+1
print(100*count/len(word))
