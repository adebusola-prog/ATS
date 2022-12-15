def word_search(key, filename):
    dicty = {}
    convertedList = []
    with open(filename) as file: 
        lines = file.readlines() 
    #print(lines) 
    for number, line in enumerate(lines, 1): 
        if key in line:
            t = list(str(number))
            # answer = (f'{key} : {t}') 
            #print(answer)
            #print(t)
            # m = str(number)
            dicty.update({str(key) : t})
           

    for i in dicty:
        convertedList.append([i, dicty[i]])
    print(convertedList)

    # l = [dict(zip([key],[t]))]
    # print(l)









           # res = sum(dict.values(), [])
            
            #dict[key] = dict.get(str(key), 0) + t
          #
# strings = input("Enter all the strings use to wish to search separated by space:\n")
# string_list = list(strings.split())
# print(string_list)
# for item in string_list:
#     word_search(item,'exam.txt')

# x = [3, 4, 5, 6]
# for index, item in enumerate([3, 4, 5, 6]):
#     print(index, item)


import string
consonants = "bcdfghjklmnpqrstvwxyz"
vowel = "aeiou"
with open("exam.txt") as txt:
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

y = d.values()
print(x)
# print(y)
# strings = input("Enter all the strings use to wish to search separated by space:\n")
# string_list = list(strings.split())
# print(string_list)
for item in x:
    z = word_search(item,'exam.txt')



