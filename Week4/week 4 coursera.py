# # # def import_and_create_bank (filename):
# # #     expenses = {}
# # #     f = open(filename, "r")
# # #     lines = f.readlines()
# # #     for line in lines:
# # #        lst = line.strip().split(':')
# # #        if len(lst) <= 1:
# # #             continue
# # #     key = lst[0].strip()
# # #     value = lst[1].strip()

# # #     try:
# # #     value = float(value)
# # #     expenses[0] = expenses.get(key, 0) + value 

# # #     except:
# # #         cotinue

# # # f.close()
# # # return expenses 


# # # def main():
# # #     expenses = import_and_create_bank ("bank.txt")
# # #     print('expenses:', expenses)

# # # if __name__ == '__main__':
# # #     main()
    
# # from winreg import ExpandEnvironmentStrings


# # def bank_update_dict(bank.txt):
# #     expenses = {}                                     #creating an empty dictionary
# #     with open("bank.txt", "r") as file:               #reading from the file/openinng the file
# #         for line in file:
# #             try:
# #                 (dictkey, dictvalue) =(line.split(":")[0], line.split(":")[1])
# #             except IndexError as i:
# #                 continue
# #             (dictkey, dictvalue) = (dictkey.strip(),dictvalue.strip())
            
    
# #             try:
# #                 value = float(value)
# #                 expenses[dictkey] = expenses.get(dictkey, 0) + value
# #             except:
# #                 continue

# #     return expenses
# # print(bank_update_dict("bank.txt"))
# # #return bank


# def online_bank_dict(bank.txt):
#     expenses = {}
#     with open("bank.txt", "r") as file:
#         for line in file:
#             try:
#                 (key, value) = (line.split(":")[0], line.split(":")[1])
#             except IndexError as i:
#                 continue
#             (key, value) = (key.strip(), value.strip())


#             try:
#                 value = float(value)
#                 expenses [key] = expenses.get(key, 0) + value
#             except:
#                 continue

#         return expenses
# print(online_bank_dict("bank.txt"))
# return bank

# def signup(user_accounts, log_in, username, password):
#     if(username==password):
#         return False
#     else:
#         if (username in user_accounts):
#             return True
#         else:
#             if valid(password)==True:
#                 user_accounts[username]=password
#                 log_in[username]=False
#             else:
#                 return False










    