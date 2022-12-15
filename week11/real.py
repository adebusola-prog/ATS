def word_search(key, filename):
    dict = {}
    with open(filename) as file: 
        lines = file.readlines()  
    for number, line in enumerate(lines, 1): 
        if key in line:
            t = str(number)
            answer = (f'{key} : {t}') 
            print(answer)
            # m = str(number)
            # dict.update({str(key) : list(m)})
            
            # dict[key] = dict.get(str(key), 0) + list(m)
    # print(dict) 




import string
consonants = "bcdfghjklmnpqrstvwxyz"
vowel = "aeiou"
with open("C:/Users/zeu/Documents/Exam_First/exam.txt") as txt:
    text = txt.read()
from string import punctuation
text = text.lower()
for char in punctuation:
    text = text.replace(char, '')
uniq = []
words = text.split()
for i in words:
    if i not in words:
        uniq.append(i)
# print(uniq)
# print(words)
l = set(words)

d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
# print(d)
x = d.keys()
print(x)

y = d.values()
# print(x)
# print(y)
# strings = input("Enter all the strings use to wish to search separated by space:\n")
# string_list = list(strings.split())
# print(string_list)
for item in x:
    z = word_search(item, "C:/Users/zeu/Documents/Exam_First/exam.txt")

# import csv

# k = ['twinkle', 'twinkle', 'little', 'stars', 'how', 'i', 'wonder', 'what', 'you', 'are', 'up', 'above', 'the', 'world',]
# for a in k:
#     f = a
#     print(f)
# header = ["unique word", "number appearance", "linenumbers"]
# footer = [f, y, z]
# # for row in words:
# #     footer.append(row)
# #     # print(j)
# with open("exam.csv", "w") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(header)
#     writer.writerow(footer)

