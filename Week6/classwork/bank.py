bank = {}
def import_and_create_bank(filename):
    with open("bank.txt", "r") as f:
        lines = f.readlines()
        for line in lines: 
            lst = line.strip().split(":")
            print(lst)
            if len(lst) <=1:
                continue

            key = lst[0].strip()
            value = lst[1].strip()
            try:
                value = float(value)
                bank[key] = bank.get(key, 0) + value
            except:
                continue

    return bank


# print(bannk(bank))

# user_account = {}
# def sign_up(user_account):
#     user_account = {}
#     with open("user.txt", "r") as f:
#         lines = f.readlines()
#         for line in lines:
#             lst = line.strip().split("-")
#             key = lst[0].strip()
#             value = lst[1].strip()
#             if len(lst) <= 1:
#                 continue
#             user_account[key] = user_account.get(key) + value
#             return user_account

# print(sign_up(user_account))



def signup(user_accounts, log_in, username, password):
    if username not in user_accounts.keys():
        # If password is not valid, return False
        if valid(password)== True:
            if password != username:
                # If both user credentials are valid and continue
                user_accounts[username] = password
                log_in[username] = False
                return True
    else:
                return False


def valid(password):
    if len(password) < 8:
        return False
    elif not any(x.islower() for x in password):
        return False
    elif not any(x.isupper() for x in password):
        return False
    elif not any(x.isdigit() for x in password):
        return False
    else:
        return True

def import_and_create_accounts(user_accounts, log_in):
    user_accounts = {}
    log_in = {}

    user = open("user.txt", 'r')
    lines = user.readlines()
    for line in lines:
        if '-' not in line:
            continue
        lst = line.strip().split("-")
        username = lst[0].strip()
        password = lst[1].strip()
        
        if username == "":
            continue
        elif password == "":
            continue
        signup(user_accounts, log_in, username, password)
    return user_accounts,log_in

def login(user_accounts, log_in, username, password):
    if username in user_accounts:
        if user_accounts[username]==password:
            log_in[username]=True
            return True
        else:
            return False
    else:
        return False



def update(bank, log_in, username, amount):
    if username in bank:
        if log_in[username] == True:
            if amount + bank[username] >= 0:
                bank[username] = bank[username] + amount
                return True
            else:
                return False
        else:
            return False
    else:
        bank[username] = amount 
        return True

def transfer(bank, log_in, userA, userB, amount):
    if userA in bank:
        if log_in[userA] == True:
            if userB in log_in:
                if userB in bank:
                    if bank[userA] - amount >= 0:
                        bank[userA] = bank[userA] - amount
                        bank[userB] = bank[userB] + amount
                        return True
                else:
                    bank[userB] = 0
                    if bank[userA] - amount >= 0:
                        bank[userA] = bank[userA] - amount
                        bank[userB] = bank[userB] + amount
                        return True
                    else:
                        return False
                        
            else:
                return False
        else:
            return False
    else:
        return False




def change_password(user_accounts, log_in, username, old_password, new_password):
    if username in user_accounts:
        if log_in[username]==True:
            if user_accounts[username]==old_password:
                if old_password!=new_password:
                    if(valid(new_password)==True):
                        user_accounts[username]=new_password
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def delete_account(user_accounts, log_in, bank, username, password):
    if username in user_accounts:
        if log_in[username]==True:
            if user_accounts[username]==password:
                    del log_in[username]
                    del user_accounts[username]
                    del bank[username]
            return True
    else:
        return False






def main():
    '''
    The main function is a skeleton for you to test if your overall programming is working.
    Note we will not test your main function. It is only for you to run and interact with your program.
    '''

    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password);
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break;
        else:
            print("The option is not valid. Please re-enter the option.\n")

#This will automatically run the main function in your program
#Don't change this
if __name__ == '__main__':
    main()



















