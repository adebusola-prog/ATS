profilelist ={"n_1":{"first_name" :"Basheer", "last_name":"Balogun","attendance": 11,"height": 46, "weight": 23,"age":22, "birthday": {"day":8, "month": "april",}},
             "n_2":{"first_name" :"Abdullahi", "last_name":"Salam","attendance": 11,"height": 25, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
                "n_3":{"first_name" :"Faith", "last_name":"Adeosun","attendance": 11,"height": 50, "weight": 23,"age":23, "birthday": {"day":8, "month": "Agu",}},
               'n_4': {"first_name" :"Ahmad", "last_name":"Sharafudeen","attendance": 11,"height": 71, "weight": 23,"age":23, "birthday": {"day":8, "month": "July",}},
              "n_5":  {"first_name" :"Toluwanimi", "last_name":"Ogunbiyi","attendance": 11,"height": 34, "weight": 24,"age":21, "birthday": {"day":8, "month": "Nov",}},
               "n_6": {"first_name" :"Awwal", "last_name":"Adeleke","attendance": 11,"height":49 ,"weight": 23,"age":23, "birthday": {"day":8, "month": "Dec",}},
               "n_7": {"first_name" :"Abdulwali", "last_name":"Tajudeen","attendance": 11,"height": 78, "weight": 23,"age":27, "birthday": {"day":8, "month": "Mar",}},
               "n_8": {"first_name" :"Abraham", "last_name":"Adekunle","attendance": 11,"height": 65, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
               "n_9": {"first_name" :"Yusuff", "last_name":"Oyedele","attendance": 11,"height": 52, "weight": 23,"age":23, "birthday": {"day":8, "month": "Oct",}},
               "n_10": {"first_name" :"Adebusola", "last_name":"Adeyeye","attendance": 11,"height": 43, "weight": 23,"age":26, "birthday": {"day":8, "month": "Feb",}},
               "n_11": {"first_name" :"lukman", "last_name":"Abisoye","attendance": 11,"height": 35, "weight": 54,"age":29, "birthday": {"day":4, "month": "Jan",}}}



# a function that returns the fullname in title case. 
def f_l_tit(profilelist):
   # for i in profilelist:
      # if profilelist[i]["first_name"] == f_name:
      #    profilelist[i]["first_name"] =  profilelist[i]["first_name"].title()  
      #    return profilelist
   v = []
   for i in profilelist:   
      v.append(profilelist[i]["first_name"].title() + " " + profilelist[i]["last_name"].title())
   return v

# c = f_l_tit(profilelist)
# print(c)

def remove_profile(profilelist):
   for x in profilelist:
      if profilelist[x]["first_name"] == "Basheer":
         del profilelist[x]
         return profilelist


# f = remove_profile(profilelist)
# print(f)


# for x in profilelist:
#    print(profilelist[x]["first_name"][0] + profilelist[x]["last_name"][0])












#a. Write a function that increment the attendance of a particular studentb. 
# Write a function that updates firstname and lastname. 
# a function that returns the fullname in title case. 
# a function that adds new profile to class.
# a function that gets the number of student in class. 
# function that remove a profile. 
# function that gets the birth month of a particular profile. 
# function that group profiles by birth month. 
# function that returns a list of initials. 
# function that returns BMI of a profile. 
# function that returns minimum age of the class. 
# function that returns maximum age of the class. 
# function that returns average age of the class. 
# function that returns the birth year of a profile.
# describe the class
# def prof():
#    for c in profilelist:
#          if profilelist[c]["first_name"] == "Bashee":
#             return profilelist
#          else:
#             return 0


# print(prof())


def update_fl(profilelist, your_age, f_name, l_name):
   for m in profilelist:
      if profilelist[m]["age"] == your_age:
           profilelist[m]["first_name"] = f_name 
           profilelist[m]["last_name"] = l_name
           return profilelist 
      

# x = update_fl(profilelist, int(input("enter your age")), input("enter your first name "), input("enter your lastname"))
# print(x)








# def update_fullname(profilelist, your_age,f_name,l_name:str):
#    for i in profilelist:
#       if profilelist[i]["age"] == your_age :
#         profilelist[i]["first_name"] = f_name
#         profilelist[i]["last_name"] = l_name
#         return profilelist
# # up=update_fullname(profilelist, int(input("Enter your age: ")), input("Enter Your first name : "), input("Enter Your last name : "))
# # print(up)


# function that returns minimum age of the class
# function that returns maximum age of the class
v = []
for i in profilelist:
   v.append(profilelist[i]["age"])
print(v)
s = sorted(v)
print(s)
print(s[0])
print(s[-1])
   


















# my_list = {"bags": "Gucci", "combs": "Iyarun", "shoes":"Keehto"}
# print(my_list["bags"]) # the parameter e.g bag has to be a key
# print(my_list["shoes"])
# for k, v in my_list.items():
#        print([(k, v)])
# for v in my_list.values():
#        print(v)
# for k in my_list.keys():
#        print(k)

# my_list["bags"] == "Dior"

# points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
# 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
# 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
# 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}

# word = "WELL"
# total = 0
# for c in word:
#       total += points[c]
# print(total)































       













