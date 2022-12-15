# 2. Census program that stores firstname, lastname, middle name, age, gender, dob, occupation, marital status, email
# a. validates input
# b. saves in a csv file
# c. Ability to search by taking a search term and return matches

import csv 



def validate_firstname():
    firstname = input(f"what is your firstname ? \n")
    if firstname.isalpha():
        return firstname
    else:
        print("Error! Invalid entry")
        return validate_firstname()

def validate_lastname():
    lastname = input(f"what is your lastname ? \n")
    if lastname.isalpha():
        return lastname
    else:
        print("Error! Invalid entry")
        return validate_lastname()



# # validate_firstname()
# def csvfiler():
header = ["firstname","lastname", "middle name", "age", "gender", "dob", "occupation", "marital status", "email"]
census = []
x = validate_firstname()
y = validate_lastname()
z = input("enter your middle name")
a = int(input("enter your age"))
b = input("enter your gender")
c = input("enter your dob")
d = input("occupation")
e = input("marital status")
f = input("email")
if ".com" not in f:
    print("invalid email")
else:
    census.append(x)
    census.append(y)
    census.append(z)
    census.append(a)
    census.append(b)
    census.append(c)
    census.append(d)
    census.append(e)
    census.append(f)

    print(census)

    with open("ade.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(census)

with open("ade.csv", "r") as f:
    reader = csv.DictReader(f)
    f = []
    for row in reader:
        f.append(row)
        # print(f)
    for row in f:
        if row["email"] == "der@gmail.com" and row["firstname"] == "Ade":
            row["gender"] = "amaphrodite"
            print(f)

            

                # print (row["email"], "in", row["firstname"])
                # print(row["firstname"])
                # # get_row = [[row for row in row["Name"], "in a", row["occupation"]]



# csvfiler()


# 3.  A signup and sign-in program that take basic info:
# on signup - username, first name, lastname, password and confirm password and saves it in a csv file.
# On signin, it takes username and password and return a message saying login successful or invalid login credentials. Add validation. Password must be minimum of 8 characters.
def csvfilee():
    header = ["firstname", "lastname", "username", "password", "confirm password"]
    details = []
    firstname = validate_firstname()
    lastname = validate_lastname()
    username = firstname + lastname
    password = input("enter your password")
    confirmpassword = input('enter your password again')
    if confirmpassword != password:
        print("invalidpassword")
    if password.isalnum == False:
        print("password should contain numbers and letters")
    if len(password) < 8:
        print("password should be a minimum of 8 characters")
    else:   
        details.append([firstname, lastname, username, password])
        print("sign in again by confirming your details")
        usernameA = input("enter your username")
        passwordB = input("enter your password")
        if usernameA == username and passwordB == password:
            print("valid login credentials")
        else:
            print("invalid login credentials")
        

        with open("keep.csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(details)


# csvfilee()


# 4. Modify (3) to include:
# a. After successful signup, it should prompt the user to signin.
# b. After successful signin, user should be presented with the options: Edit profile, Change password, Logout.
# c. Edit profile should ask for more information like phone_number (required), address (optional), date of birth (optional) and gender (compulsory)

import csv
def updaty():
    print("sign in again by confirming your details")
    firstname = validate_firstname()
    lastname = validate_lastname()
    username = input("enter your username")
    password = input("enter your password")
    usernameA = input("enter your username")
    passwordB = input("enter your password")
    if usernameA != username and passwordB != password:
        print("invalid login credentials")
    else:
        print("valid login credentials, you have successfully signed in")
        print("you can now edit your profile, change password or logout")
        m = ["phone number", "Address", "DOB", "gender"]
        j = []
        c = ["A", "B", "C"]
        g = input("type A B or C->")
        for i in c:
            if i == "A" == g:
                print("you can now edit your profile")
                ph = int(input("enter your phone number"))
                address = input("enter your address")
                dob = input("enter your date of birth")
                gender = input("enter your gender")
                j.append([ph, address,dob, gender])
            if i == "B" == g:
                print("you can now change your password")
                passwrd = input("enter an 8 character password")
            if i == "C" == g:
                print("you can now log out!!\nlog out")

            with open("keep.csv", "w") as cf:
                writer = csv.writer(cf)
                writer.writerow(m)
                writer.writerow(j)

            with open("keep.csv", "r") as cf:
                reader = csv.reader(cf)
                # s = []
                for row in reader:
                    # s.append(row)
                    print(row)


# updaty()
















