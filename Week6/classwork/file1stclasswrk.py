#A program that asks for your username, first name, last name, password, 
# password confirmation and saves it in a text file with name as username


# with open("bank_details.txt", "w") as x:
#     d = " "
#     first_Name = input("what is your first name?")
#     last_Name = input("what is your last name")
#     password = input("what password would you like to use?")
#     username = first_Name + last_Name
#     d = d + first_Name + last_Name + password
#     x.write(d)



# fn= input("what is the key for first name?")
# ln = input("what is the key for last name?")
# ps = input("what is the key for password?")
# un = input("what is the key for username?")



first_Name = input("what is your first name?")
last_Name = input("what is your last name")
password = input("what password would you like to use?")
username = first_Name + last_Name
filename = username +".txt"
with open (filename, "w") as x:
    m = dict([("first name", first_Name), ("last_name", last_Name), ("password", password), ("User_name", username)])
    print(m)
    x.write(str(m))





