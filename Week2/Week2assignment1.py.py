
Adebusola = {
                "first_name": "Adebusola",
                "last_name": "Adeyeye",
                "Birth": 2202,
                "attendance": 11,
                "height": 5,
                "weight": 45,
                "age": 23}

Awaaal = {
             "first_name": "Awaaal",
             "last_name": "Adeleke",
             "Birth": 1203,
             "attendance": 10,
             "height": 4,
             "weight": 47,
             "age": 24}

Abdulwali = {
                "first_name": "Abdulwali",
                "last_name": "Tajudeen",
                "Birth": 2204,
                "attendance": 5,
                "height": 3,
                "weight": 48,
                "age": 25}

Abraham = {
              "first_name": "Abraham",
              "last_name": "Adekunle",
              "Birth": 1005,
              "attendance": 6,
              "height": 2,
              "weight": 50,
              "age": 26}

Yusuff = {
             "first_name": "Yusuff",
             "last_name": "Oyedele",
             "Birth": 1312,
             "attendance": 11,
             "height": 5,
             "weight": 43,
             "age": 27}

Abdullahi = {
                "first_name": "Abdullahi",
                "last_name": "Salaam",
                "Birth": 1411,
                "attendance": 10,
                "height": 5,
                "weight": 45,
                "age": 28}

Faith = {
            "first_name": "Faith",
            "last_name": "Adeosun",
            "Birth": 1504,
            "attendance": 2,
            "height": 5,
            "weight": 47,
            "age": 29}

Ahmad = {
            "first_name": "Ahmad",
            "last_name": "Sharafudeen",
            "Birth": 1612,
            "attendance": 1,
            "height": 5,
            "weight": 46,
            "age": 30}

Lukman = {
             "first_name": "Lukman",
             "last_name": "Abisoye",
             "Birth": 2207,
             "attendance": 5,
             "height": 5,
             "weight": 42,
             "age": 31}

Toluwanimi = {
                 "first_name": "Toluwanimi",
                 "last_name": "Ogunbiyi",
                 "Birth": 2210,
                 "attendance": 7,
                 "height": 5,
                 "weight": 43,
                 "age": 32}

Basheer = {
    "first_name": "Basheer",
    "last_name": "Balogun",
    "Birth": 2206,
    "attendance": 8,
    "height": 5,
    "weight": 41,
    "age": 33}

Names = {"1": Adebusola,
         "2": Awaaal,
         "3": Abdulwali,
         "4": Abraham,
         "5": Yusuff,
         "6": Abdullahi,
         "7": Faith,
         "8": Ahmad,
         "9": Lukman,
         "10": Toluwanimi,
         "11": Basheer
         }

# (1) A function that will return the average age of the class, minimum age and maximum age
age = max(23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33)
print(age)
print
age = min(23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33)
print(age)
print()
def Average(lst):
    return sum(lst) / len(lst)


lst = [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
average = Average(lst)
print( "Average of the list = ", round(average, 2))


#(2) A function that will return the list of full names in title case
full_name = "adebusola adeyeye"
x = full_name.title()
print(x)


#(3)A function that can add profile to the class
Names.update(new_name)

print(new_name)
print(Names)



full_name = []
items = Names.items()
for key, value in items:
    for f in value["first_name"]:
        for g in value ["last_name"]:
            full_name.append(f)
            full_name.append(g)


# (4)A function that will calculate profile BMI
b = int(input("What is weight"))
c = int(input("What is the height"))
d = (b/c)**2
print("your BMI is:", d)