from validateemail import validate_email
from Users import User
from datetime import datetime, date
from tkinter import *
from tkinter import messagebox
import tkinter as tk

app = Tk()
windowWidth = app.winfo_reqwidth()
windowHeight = app.winfo_reqheight()
positionDown = int(app.winfo_screenheight()/2 - windowHeight/2)
positionRight = int(app.winfo_screenwidth()/2 - windowWidth/2)

today = date.today()
bugun = today.strftime("%d.%m.%Y")
app.title(f'Welcome to Python Login and Sign Up System. {bugun}')
app.geometry('425x750+{}+{}'.format(positionRight,positionDown))

date_label = Label(app, font=('bold',15),bg='lightblue', pady=10)
date_label.pack(fill=tk.X)
date_label.place()

entered_name = StringVar()
entered_email = StringVar()
entered_password = StringVar()
entered_confirm = StringVar()
entered_birthyear = StringVar()

# creating an empty dictionary variable to display logged user info
user_info = {'name_surname': '', 'email':'', 'password':'','age':''}

def Login():
    my_user = User()
    users_file = open('users_file.txt','r')
    lines = users_file.readlines()
    my_user.email = email_entry.get()
    my_user.password = password_entry.get()
    i = 0
    while lines != None :
        if my_user.email == lines[i].strip() and my_user.password == lines[i+1].strip():
            #print(f'Welcome {my_user.email}')
            #print("Your age is ",CalculateAge(lines[i+3]))
            user_info['name_surname'] = lines[i-1].strip()
            user_info['email'] = lines[i].strip()
            user_info['password'] = lines[i+1].strip()
            user_info['age'] = CalculateAge(lines[i+3].strip())
            email_entry.pack_forget()
            password_entry.pack_forget()
            button_login2.pack_forget()
            name_label['text'] = "Name Surname" 
            name_label.pack()
            name_entry.insert(0,user_info['name_surname'])
            name_entry.pack()
            email_label['text'] = f"Email: {user_info['email']}"
            email_label.pack()
            password_label['text'] = f"Password: {user_info['password']}"
            password_label.pack()
            birthyear_label['text'] = f"Age: {user_info['age']}"
            birthyear_label.pack()
            break
        else:
            i += 1
            if i == len(lines):
                messagebox.showerror('ERROR','This email does not exist')
                return

    users_file.close()

# creating neccessary elements to display logged in user
'''
logged_in_namesurname = Label(app, text = user_info['name_surname'])
logged_in_namesurname.pack()

logged_in_email = Label(app, text = user_info['email'])
logged_in_email.pack()

logged_in_password = Label(app, text = user_info['password'])
logged_in_password.pack()

logged_in_age = Label(app, text = user_info['age'])
logged_in_age.pack()
'''

def SignUp():
    new_user = User()
    users_file = open('users_file.txt', 'a')
    if name_entry.get() == '' or email_entry.get() == '' or password_entry.get() == '' or confirm_entry.get() == '' or birthyear_entry.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    elif password_entry.get() != confirm_entry.get():
        messagebox.showerror('Try Again', 'Passwords do not match')
        return
    elif not validate_email(email_entry.get()):
        messagebox.showerror('Try Again', 'Please enter a valid email')
        return
    else:
        new_user.users['name_surname'] = name_entry.get()
        users_file.write(new_user.users['name_surname']+'\n')
        new_user.users['email'] = email_entry.get()
        users_file.write(new_user.users['email']+'\n')
        new_user.users['password'] = password_entry.get()
        users_file.write(new_user.users['password']+'\n')
        new_user.users['confirm_password'] = confirm_entry.get()
        users_file.write(new_user.users['confirm_password']+'\n')
        new_user.users['birth_year'] = birthyear_entry.get()
        users_file.write(new_user.users['birth_year']+'\n')
        messagebox.showinfo('Success','Your account has been created succesfully!')
        users_file.close()


def ClearElements():
    # change visibility of the unneccessary elements
    name_entry.pack_forget()
    name_label.pack_forget()
    confirm_entry.pack_forget()
    confirm_label.pack_forget()
    birthyear_entry.pack_forget()
    birthyear_label.pack_forget()
    button_login.pack_forget()
    button_login2.pack(pady=20)
    info_label.pack_forget()
    button_signup.pack_forget()



def CalculateAge(birth_date):
    today = date.today()
    age = int(today.year) - int(birth_date)
    return age



# GET NAME AND SURNAME
name_label = Label(app, text='Name Surname', font=('bold',12), pady=10)
name_label.pack()

name_entry = Entry(app, textvariable=entered_name)
name_entry.pack()

# GET EMAIL
email_label = Label(app, text='Email', font=('bold',12), pady=10)
email_label.pack()

email_entry = Entry(app, textvariable=entered_email)
email_entry.pack()

# GET PASSWORD
password_label = Label(app, text='Password', font=('bold',12), pady=10)
password_label.pack()

password_entry = Entry(app, textvariable=entered_password)
password_entry.pack()
# CONFIRM PASSWORD
confirm_label = Label(app, text='Confirm Password', font=('bold',12), pady=10)
confirm_label.pack()

confirm_entry = Entry(app, textvariable=entered_confirm)
confirm_entry.pack()

# GET BIRTH YEAR
birthyear_label = Label(app, text='Birth Year', font=('bold',12), pady=10)
birthyear_label.pack()

birthyear_entry = Entry(app, textvariable=entered_birthyear)
birthyear_entry.pack()

# second login button
button_login2 = Button(app, text="Login", command=Login)

# sign up button
button_signup = Button(app, text="Sign Up", command=SignUp)
button_signup.pack(pady = 25)

# information label
info_label = Label(app, text="Do you have an account? Click the button below to Login!")
info_label.pack(pady=20)

# changing from signup to login 
button_login = Button(app, text="Login", command=ClearElements)
button_login.pack(pady = 25)


# def Greeting():
#   print("1) Login")
#    print("2) Sign Up")

#Greeting()

'''
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
'''

'''
def SelectOption():
    input_result = input()
    if int(input_result) == 1:
        Login()
    elif int(input_result) == 2:
        SignUp()
    elif int(input_result) == 0:
        exit()
    else:
        print("Invalid input. Try again")
        return SelectOption()
        
SelectOption()
'''
app.mainloop()