password = ''
user_name = ''

first_name=input("what is your first_name?")
last_name=input("what is your last_name?")
user_name=input("what is your user_name?")
password=input("what is your password?")

print('')

print('Your details has been saved')
print('')

Confirm_username = ''
Confirm_password = ''

while user_name != Confirm_username and password != Confirm_password:
    Confirm_username = input('Kindly re-enter your username')
    Confirm_password = input('Kindly re-enter your password')
    if password == Confirm_password and user_name == Confirm_username:
        print('Login Successful!')
    else:
        print('Incorrect Login Credentials')

