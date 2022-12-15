def word_search(key, filename):
    with open(filename) as file: 
        lines = file.readlines()  
    for number, line in enumerate(lines, 1): 
        if key in line:
            print(f'{key} is on line {number}') 





strings = input("Enter all the strings use to wish to search separated by space:\n")
string_list = list(strings.split())
print(string_list)
for item in string_list:
    word_search(item,'exam.txt')