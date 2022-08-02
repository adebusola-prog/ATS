
def minimum_age(data):
   emp_list = []
   for i in data:
      emp_list.append(i["age"])

   sorted_list = sorted(emp_list)[0]
#    print(f'minimum age is {sorted_list}')

# minimum_age(profilelist)

def age(data,year):

   current_year = 2022
   for i in data:
      if data[i]["age"]==year:
         current_year = current_year - year
      print(f"You were born in {current_year}")

# print(age(profilelist,int(input("Enter your age : "))))

