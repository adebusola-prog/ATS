# d. a function that adds new profile to class
# e. a function that gets the number of student in class
# f. function that remove a profile
# g. function that gets the birth month of a particular profile
# h. function that group profiles by birth month
# i. function that returns a list of initials
# j. function that returns BMI of a profile
# k. function that returns minimum age of the class
# l. function that returns maximum age of the class
# m. function that returns average age of the class
# n. function that returns the birth year of a profile

profilelist =[{"first_name" :"Basheer", "last_name":"Balogun","attendance": 11,"height": 46, "weight": 23,"age":22, "birthday": {"day":8, "month": "april",}},
             {"first_name" :"Abdullahi", "last_name":"Salam","attendance": 11,"height": 25, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
             {"first_name" :"Faith", "last_name":"Adeosun","attendance": 11,"height": 50, "weight": 23,"age":23, "birthday": {"day":8, "month": "Agu",}},
             {"first_name" :"Ahmad", "last_name":"Sharafudeen","attendance": 11,"height": 71, "weight": 23,"age":23, "birthday": {"day":8, "month": "July",}},
            {"first_name" :"Toluwanimi", "last_name":"Ogunbiyi","attendance": 11,"height": 34, "weight": 24,"age":21, "birthday": {"day":8, "month": "Nov",}},
            {"first_name" :"Awwal", "last_name":"Adeleke","attendance": 11,"height":49 ,"weight": 23,"age":23, "birthday": {"day":8, "month": "Dec",}},
            {"first_name" :"Abdulwali", "last_name":"Tajudeen","attendance": 11,"height": 78, "weight": 23,"age":27, "birthday": {"day":8, "month": "Mar",}},
            {"first_name" :"Abraham", "last_name":"Adekunle","attendance": 11,"height": 65, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
            {"first_name" :"Yusuff", "last_name":"Oyedele","attendance": 11,"height": 52, "weight": 23,"age":23, "birthday": {"day":8, "month": "Oct",}},
            {"first_name" :"Adebusola", "last_name":"Adeyeye","attendance": 11,"height": 43, "weight": 23,"age":26, "birthday": {"day":8, "month": "Feb",}},
            {"first_name" :"Lukman", "last_name":"Abisoye","attendance": 11,"height": 35, "weight": 54,"age":29, "birthday": {"day":4, "month": "Jan",}}]

# b. Write a function that updates firstname and lastname
def profile(n:str):
    # for i in profilelist:
    if profilelist[10]["first_name"] == n:
        profilelist[10]["first_name"] = "Fellas"        
        return profilelist


# print(profile("Lukman"))

# a. Write a function that increment the attendance of a particular student
def atten_dance():
    profilelist[0]["attendance"] += 1
    return profilelist[0]["attendance"]


# print(atten_dance())

# c. a function that returns the fullname in title case
def title_case(): 
    for i in range(len(profilelist)-1):
        return profilelist[:2]["first_name"].upper() + " " + profilelist["last_name"][:2].upper()



# print(title_case())

def poof():
    for index in range(len(profilelist)):
        for key in profilelist[index]:
            return profilelist[index][key]              
            # ["first_name"].upper() + " " + profilelist[index][key]["last_name"].upper()


# print(poof())

# dataList = [{'a': 1}, {'b': 3}, {'c': 5}]
# for index in range(len(dataList)):
#     for key in dataList[index]:
        # print(dataList[index][key])



# for dict_item in dataList:
#   for key in dict_item:
#     print dict_item[key]

# for i in profilelist:
#     for x in i:
#         for k in i[x]
        # print(i[x])
        # print(i[x].upper() + " " + profilelist[i][x].upper())


for i in range(10, 10001):
#convert i to string by giving it a varaible and passing a str to i
    s = str(i)
    if s == s[::-1]:
        print(s)



import csv
with open("countries.csv", "r") as f:
    reader = csv.DictReader(f)
    print(type(reader))
    print(reader.fieldnames)



#In order to print each line in a csvfile:
for row in reader:
    print(row)


with open("keep.csv", "r") as f:
    x = csv.DictReader(f)

for line in x:
    print(line)

with open("countries.csv" "r") as f:
    reader = csv.DictReader(f)

for row in reader:
    rows = 5
    rows-=1
    if rows > 0:
        print(row)
    else: 
        break



#to get the length of the file, first append it to a list
v = []
for row in reader:
    v.append(f)
    print(len(v))



#note, it is better to append ur csv file to a list before looping through





















