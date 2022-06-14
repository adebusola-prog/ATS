first_name = input("what is your first_name?")
last_name = input("what is your last_name?")
user_name = input("what is your user_name?")
pass_word = input("what is your pass_word?")
print("")
print("your credentials have been saved")
print("")


confirm_username =input("kindly input your username")
confirm_password =input("kindly input your password")
if (user_name==confirm_username) and (pass_word==confirm_password):
    print("login successful!")
else:
    print("incorrect credentials")
