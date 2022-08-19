# key = input("What is the key?")
# chord_type = input('What is the chord type?')
# major = []
# chord = {key:}
# x = "lola"
# print(x.startswith("l"))



# chord = input('what chord do you want')
# if chord == 'major':
#     a = 0
#     b = 4
#     c = 7
# x = input("enter a key")

# for i in range(len(key)):
#     if key[i] == x:
#         key[0] = key[i]
#         print(key)
#print(key[a], key[b], key[c])
#  Below are the notes used in music:
# C C# D D# E F F# G G# A A# B
# The notes for the C major chord are C, E, G. A mathematical way to get this is that E is 4 steps
# past C and G is 7 steps past C. This works for any base. For example, the notes for D major
# are D, F#, A. We can represent the major chord steps as a list with two elements: [4,7]. The
# corresponding lists for some other chord types are shown below:
# Minor [3,7] Dominant seventh [4,7,10]
# Augmented fifth [4,8] Minor seventh [3,7,10]
# Minor fifth [4,6] Major seventh [4,7,11]
# Major sixth [4,7,9] Diminished seventh [3,6,10]
# Minor sixth [3,7,9]
# Write a program that asks the user for the key and the chord type and prints out the notes of
# the chord. Use a dictionary whose keys are the (musical) keys and whose values are the lists
# of steps.
# key = ['C', 'C#', 'D',  'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
# x = input('what note do you want to get its chord?')
# r = key.index(x)
# chord = input('what chord do you want')
# if chord == 'major':
#     a = 0
#     b = 4
#     c = 7
# print(key[r+a], key[r+b], key[r+c])
# # print(r)

chord = {"major": {"C": [a, b, c], "C#": [a, b, c], "D": [a, b, c]},
         "minor": {"C": [a, b, c], "C#": [a, b, c], "D": [a, b, c]}}
print(chord["major"]["C"])
a = 0
b = 4
c = 7

# for k, v in chord[major].items():
#     print(k,v)














# v = []
# x = [1,5,6,7,8,1,5,3,1]
# # x.sort(reverse = True)
# # x.sort(::-1)
# # print(x)
# for row in x:
#     if row not in v:
#         v.append(row)
#         print(v)


# x = [1,5,6,7,8,1,5,3,1]
# y = set(x)
# print(y)























