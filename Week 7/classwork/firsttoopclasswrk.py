profilelist ={"n1":{"first_name" :"Basheer", "last_name":"Balogun","attendance": 11,"height": 46, "weight": 23,"age":22, "birthday": {"day":8, "month": "april",}},
             "n2":{"first_name" :"Abdullahi", "last_name":"Salam","attendance": 11,"height": 25, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
                "n3":{"first_name" :"Faith", "last_name":"Adeosun","attendance": 11,"height": 50, "weight": 23,"age":23, "birthday": {"day":8, "month": "Agu",}},
               'n4': {"first_name" :"Ahmad", "last_name":"Sharafudeen","attendance": 11,"height": 71, "weight": 23,"age":23, "birthday": {"day":8, "month": "July",}},
              "n5":  {"first_name" :"Toluwanimi", "last_name":"Ogunbiyi","attendance": 11,"height": 34, "weight": 24,"age":21, "birthday": {"day":8, "month": "Nov",}},
               "n6": {"first_name" :"Awwal", "last_name":"Adeleke","attendance": 11,"height":49 ,"weight": 23,"age":23, "birthday": {"day":8, "month": "Dec",}},
               "n7": {"first_name" :"Abdulwali", "last_name":"Tajudeen","attendance": 11,"height": 78, "weight": 23,"age":27, "birthday": {"day":8, "month": "Mar",}},
               "n8": {"first_name" :"Abraham", "last_name":"Adekunle","attendance": 11,"height": 65, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
               "n9": {"first_name" :"Yusuff", "last_name":"Oyedele","attendance": 11,"height": 52, "weight": 23,"age":23, "birthday": {"day":8, "month": "Oct",}},
               "n10": {"first_name" :"Adebusola", "last_name":"Adeyeye","attendance": 11,"height": 43, "weight": 23,"age":26, "birthday": {"day":8, "month": "Feb",}},
               "n11": {"first_name" :"Lukman", "last_name":"Abisoye","attendance": 11,"height": 35, "weight": 54,"age":29, "birthday": {"day":4, "month": "Jan",}}}



class Profile:
    length_of_data = 11 

    def __init__(self, n):
        self.data = profilelist[n]
    
    def inc_att(self, increment):
        self.data["attendance"] += increment
        return self.data["attendance"]

    def update_fullname(self, your_age,f_name, l_name:str):
        if self.data["age"] == your_age:
            self.data["first_name"] = f_name 
            self.data["last_name"] = l_name
            return self.data    
    
    def f_and_l_title(self):
        # fullname = []
        # fullname.append(self.data['first_name'].title() +" "+ self.data["last_name"].title())
        # return fullname
        self.data['first_name'].title() +" "+ self.data["last_name"].title()

    def remove_profile(self):
            del self.data
            # return self.data

    def initial(self):
        return self.data["first_name"][0] + self.data["last_name"][0]
    
    # function that returns the birth year of a profile

    def profile_BMI(self):
        # self.data["height"] == hgt and self.data["weight"] == wgt
        # bmi = wgt / (hgt**2)
        # return bmi

        bmi = self.data["height"] / self.data["weight"]**2
        return bmi

    def get_birth_month(self):
        return self.data["birthday"]["month"]

    def get_birth_day(self):
        return self.data["birthday"]["day"]

    def get_birth_year(self, year):
        self.data["year"] = year - self.data["age"] 
        return self.data["year"]

    def average_age(self):
        total = 0
        total = total + self.data["age"]
        average = total / len(self.data)
        return average

    @staticmethod
    def minimum_age():
        v = []
        for i in profilelist:
            v.append(profilelist[i]["age"])
        print(v)
        s = sorted(v)
        print(s)
        print(s[0])
    
    
    def maximum_age():
        v = []
        for i in profilelist:
            v.append(profilelist[i]["age"])
        print(v)
        s = sorted(v)
        print(s[-1])


c = Profile("n1")
c2 = Profile("n2")
print(c.inc_att(1))
print(c.update_fullname(22, "Adeola", "Bakare"))
print(c2.f_and_l_title())
print(c.initial())
print(c2.profile_BMI())
print(c.average_age())
print(c.length_of_data)
print(c2.remove_profile())
Profile.minimum_age()
Profile.maximum_age()
print(c.get_birth_month())
print(c2.get_birth_day())
print(c2.get_birth_year(2022))




    

























    
