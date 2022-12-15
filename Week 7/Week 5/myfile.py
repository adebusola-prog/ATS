# def get_account(filename):
#     d = {}
#     bank ={}
#     with open(filename, "r") as file:
#         for line in file:
#             try:
#                 (dictkey, dictval) = (line.split(":")[0], line.split(":")[1])
#             except IndexError as i:
#                 continue
#             (dictkey, dictval)= (dictkey.strip(), dictval.strip())
#             fval = 0.0

#             try:
#                 fval = float(d.val)
#             except ValueError as v:
#                 continue

#             if dictkey in d.keys:
#                 d[dictkey] += fval
#             else:
#                 d[dictkey] = fval


#     return d
# print(get_account('filename'))

# return bank
             


from dataclasses import dataclass


def create_bank_account(useraccount, login, username, password):
    
    if(username == password):
        return False
    else:
        if username in useraccount:
            return True
        else:
            if valid[password] == True:
                username[useraccount] = password
                login[username] = False
            else:
                return False


def valid(password):
    if len(password) < 8:
        return False
    elif not any(x.islower()for x in password):
        return False
    elif not any (x.isupper()for x in password):
        return False
    elif not any (x.isdigit()for x in password):
        return False
    else:
        return True

def create_password(filename):
    user_accounts = {}
    login = {}
    with open(filename, "r") as data:
        lines = data.readlines()
        for i in lines:
            new = i.strip(),split("-")
            if len (new) <= 1:
                continue
            key = new[0].strip()
            value = new[1].strip()
            try:
                signup(user_accounts,login,key,value)
            except:
                continue
        return user_accounts, login



def login(user_accounts, log_in, username, password):
    if username in user_accounts:
        if user_accounts[username]==password:
            log_in[username]= True
            return True
        else:
            return False

    else:
        return False





































