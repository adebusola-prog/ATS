word = "lion"
x = "_____"
c = input("guess the word")
if c in word:
    word = word.replace(x, c)
    print(word)
else:
    
    