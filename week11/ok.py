# # input text file
# inputFile = "exam.txt"

# # storing the current line number
# lineNumber = 1

# # Enter the word 
# givenWord = "Twinkle"
# print('The word {givenWord} is present in the following lines:')

# with open(inputFile, 'r') as fileData: 
#     for textline in fileData:
#         wordsList = textline.split()
#         print(wordsList)
#         if givenWord in wordsList:
#             print(lineNumber)
#             lineNumber += 1
       


# fileData.close()


# # print("hello")
# # # def index (filename, lst):
# # infile = open('exam.txt', 'r')
# # lines =  infile.readline()
# # words = []
# # dic = {}

# # for line in lines:
# #     line_words = line.split(' ')
# #     words.append(line_words)
# #     print(line_words)
# # for i in range(len(words)):
# #     for j in range(len(words[i])):
# #         if words[i][j] in lst:

# #             dic[words[i][j]] = i

# # return dic

# # index("exam.txt", ["twinkle", "little", "stars"])

# # word = "Twinkle"
# # with open("exam.txt") as txt:
# #     word = "sky"
# #     for read in txt:
# #         # text = read.lower()
# #         # wordlist = text.split()
# #         # print(wordlist)
# #         for index, item in enumerate(read, 1):
# #             if word in item:
# #                 print("it is found at line", index) 


consonants = "bcdfghjklmnpqrstvwxyz"
vowel = "aeiou"
word = ["sky", "get", "I"]

for i in consonants:
    for j in vowel:
        for k in word:
            for l in k:
                if l not in consonants:
                    print(l, "vowel")
                    break
                elif l in 


                
                
# for i in range(len(word)):
#     if word[i] == consonants[i]:
#         print("it is there")
#         break
# else:
#     print("it is not there")




# uniq = []
# import string
# consonants = "bcdfghjklmnpqrstvwxyz"
# vowel = "aeiou"
# with open("exam.txt") as txt:
#     text = txt.read()
# from string import punctuation
# text = text.lower()
# for char in punctuation:
#     text = text.replace(char, '')
# words = text.split()

# for i in words:
#     if i not in uniq:
#         uniq.append(i)
# print(uniq)
# # print(words)




import random
x = {}
for v in range(1,21):
    z = random.randint(1,100)
    print(z)
    x.update({str(z) : z})
# print(x)





















