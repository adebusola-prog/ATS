def number(num):
    f = {0:"zero", 1:"one", 2: "two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
        10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14: "fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 
        18:"eighteen", 19: "nineteen", 20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80: "eighty",
        90:"ninety"}

    thousand = 1000


    if num in f:
        return (f[num])
    else:
        if num < 100:
            return(f[num//10*10] + " " + f[num%10])
        elif 100 < num < thousand:
            if num % 100 == 0:
                return (f[num//100] + " " + "hundred")
            else:
                return (f[num//100] + " hundred and " + number(num%100))
        elif num < thousand * 1000:
            if num % 100 == 0:
                return number(num//1000) + ' thousand '
            else:
                return number(num//1000) + ' thousand ' + number(num % 1000)
              

# n = int(input("enter a number"))
# print(number(n))
def get_password():
    password = input("Enter an 8-digit password: (Passwords must be alphanumeric!): ")
    if password.isalnum() and len(password) >= 8:
        return password
    print("ERROR: Incorrect format. Re-enter password again!")
    return get_password()

get_password()


class Authentication(object):
    def __init__(self, username = ''):
        self.username = username

    def __lower(self):
        lower = any(c.islower() for c in self.username)
        return lower

    def __upper(self):
        upper = any(c.isupper() for c in self.username)
        return upper

    def __digit(self):
        digit = any(c.isdigit() for c in  self.username)
        return digit

    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()

        length = len(self.username)

        report =  lower and upper and digit and length >= 6

        if report:
            print("Username passed all checks ")
            return True

        elif not lower:
            print("You didnt use Lower case letter")
            return False

        elif not upper:
            print("You didnt use Upper Case letter")
            return False

        elif length <6:
            print("username should Atleast have 6 character")
            return False

        elif not digit:
            print("You didnt use Digit")
            return False
        else:
            pass

C = Authentication("abdul12")
print(C.validate())






# def number(num):
#     f = {0 : "zero", 1:"one", 2:"two", 3:"three", 4: "four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
#         11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15: "fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty",
#         30: "thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
        
#     thousand = 1000
#     if num in f:
#         return f[num]
#     else:
#         if num < 100:
#             return (f[num//10 *10] + f[num % 10])
#         elif 100 < num < thousand:
#             if num % 10 == 0:
#                 return (f[num//100] + "hundred")
#             else:
#                 return (f[num//100] + "hundred and" + number(num % 100))
#         elif num > thousand * 1000:
#             if num % 1000 == 0:
#                 return (f[num//1000] + " thousand")
#             else:
#                 return (f[num//1000]) + " thousand" + number(num % 1000)


# print(number(9999))


import pickle
def deposite_account():
    depo = int(input("Enter amount to Deposit"))
    return depo


def generate_account_no():
    acc_no = (input("Enter Account Number"))
    return acc_no

def check_balance(acc_no):
    
    dbfile = open('ussd','rb')
    header = pickle.load(dbfile)
    print(header.items())
    


    
    # result = [acc for acc in header.items() if acc['acc_no'] == acc_no]
    # print(result)

    # contents = []
    # f= open("ussd.txt","r")
    # f1= f.read()
    # contents.append(f1)

    # print(type(contents[0]))
    #return [acc for acc in contents if acc['acc_no'] == acc_no]

def get_details():
    contents = []
    f= open("ussd.txt","r")
    f1= f.read()
    contents.append(f1)
    print(contents)
    return contents

def make_transfer():
    get_details()



def Register_ussd():
    header = {}

    header['firstname'] = input("Enter Firstname: ")
    header['lastname']= input("Enter Lastname: ")
    header['account_b'] = 0.0 + deposite_account()
    header['pin']= '0000'
    header['acc_no']=generate_account_no()

    print(type(header))

    dbfile =open('ussd', 'ab')

    pickle.dump(header, dbfile)

    dbfile.close()

    # f = open("ussd.txt","a+")
    # f.write(f"{header},\n")
    # f.close()

def collect_ussd_option():
    print('Enter Option ')
    print('1. Register')
    print('2. Check Balance')
    print('3. Make Transfer')
    print('4. Buy Airtime')
    option = int(input('Enter: '))

    if option == 1:
        Register_ussd()
    elif option == 2:
        acc_no = input("Enter account number: ")
        check_balance(acc_no)
    elif option == 3:
        make_transfer()
    elif option == 4:
        get_details()
    else:
        print("Only positive integer are allowed")
        collect_ussd_option()

if __name__ == '__main__':
    collect_ussd_option()














































def ger(a, b):
    '''returns arg 1 raisd'''
    return a ** b   

# print(ger.__doc__)

# ger(3, 4)






