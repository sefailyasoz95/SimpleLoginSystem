from validateemail import validate_email
from Users import User
from datetime import datetime, date

def Greeting():
        today = date.today()
        bugun = today.strftime("%d.%m.%Y")
        print(f"Welcome to Python Login & Sign Up System - {bugun}")
        print("1) Login")
        print("2) Sign Up")

Greeting()

def SignUp():
    new_user = User()
    users_file = open('users_file.txt', 'a')
    new_user.users['name_surname'] = input("Enter your name and surname: ")
    users_file.write(new_user.users['name_surname']+'\n')
    new_user.users['email'] = input("Enter your email: ")
    if validate_email(new_user.users['email']):
        users_file.write(new_user.users['email']+'\n')
    else:
        print("The email you entered is not valid.")
        new_user.users['email'] = input("Enter your email: ")
        users_file.write(new_user.users['email']+'\n')

    new_user.users['password'] = input("Enter a password: ")
    users_file.write(new_user.users['password']+'\n')
    new_user.users['confirm_password'] = input("Confirm your password: ")
    if new_user.users['password'] != new_user.users['confirm_password']:
        print("Passwords do not match")
        new_user.users['confirm_password'] = input("Confirm your password: ")
        users_file.write(new_user.users['confirm_password']+'\n')
    else:
        users_file.write(new_user.users['confirm_password']+'\n')
    new_user.users['birth_year'] = input("Enter your birth year: ")
    users_file.write(new_user.users['birth_year']+'\n')
    #age = int(new_user.birth_year)
    new_user.PersonCreated()
    users_file.close()

def Login():
    my_user = User()
    users_file = open('users_file.txt','r')
    lines = users_file.readlines()
    my_user.email = input("Email: ")
    my_user.password = input("Password: ")
    i = 0
    while lines != None :
        if my_user.email == lines[i].strip() and my_user.password == lines[i+1].strip():
            print(f'Welcome {my_user.email}')
            print("Your age is ",CalculateAge(lines[i+3]))
            break
        else:
            i += 1
            if i == len(lines):
                print("This email does not exist.")
                break

    users_file.close()

def CalculateAge(birth_date):
    today = date.today()
    age = int(today.year) - int(birth_date)
    return age

def SelectOption():
    input_result = input()
    if int(input_result) == 1:
        Login()
    elif int(input_result) == 2:
        SignUp()
    else:
        print("Invalid input. Try again")
        return SelectOption()
        
SelectOption()