# READ FILE
text = open("exam.txt")

# read file
read = text.read()
print(read)

# return cursor to
# the beginning
# of the file.
text.seek(0)



# create empty list
wordlist = []

# count number of
# lines in the file
line = 1
for word in read:
	if word == '\n':
		line += 1
	print("Number of lines in file is: ", line)

for i in range(line):
	# readline() method,
	# reads one line at
	# a time
	wordlist.append(text.readline())
print(wordlist)

# Function that will return
# line in which word is present
def findline(word):
	for i in range(len(wordlist)):
		if word in wordlist[i]:
			print(i+1, end=", ")
	for word in read:
    		

findline(word)
