from validateemail import validate_email
from Users import User
from datetime import datetime, date
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from database import Database

db = Database('store.db')
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
user_label = Label(app,text="")


users = db.fetch()

def Login():
    for user in users:
        if email_entry.get() == user[2] and password_entry.get() == user[3]:
            user_label['text'] = user[0]
            email_entry.pack_forget()
            password_entry.pack_forget()
            button_login2.pack_forget()
            #name_label['text'] = "Name Surname" 
            name_label.pack()
            name_entry.insert(0,user[1])
            name_entry.pack()
            email_label['text'] = "Email"
            #email_entry.insert(0,user[2])
            email_label.pack()
            email_entry.pack()
            #password_label['text'] = "Password"
            #password_entry.insert(0,user[3])
            password_entry.pack()
            password_label.pack()
            confirm_label.pack()
            confirm_entry.insert(0,user[4])
            confirm_entry.pack()
            age = CalculateAge(int(user[5]))
            birthyear_label['text'] = f"Age: {age}"
            birthyear_entry.insert(0,user[5])
            birthyear_entry.pack()
            birthyear_label.pack()
            button_update.pack()
            break
        elif email_entry.get() != user[2] or password_entry.get() != user[3]:
            messagebox.showerror('Sorry!','email or password incorrect')
            break
        else:
            continue


def Update():
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
        db.update(int(user_label['text']) ,name_entry.get(), email_entry.get(), password_entry.get(), confirm_entry.get(),birthyear_entry.get())
        messagebox.showinfo('Success','Your profile has been updated!')
        return


def SignUp():
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
        for user in users:
            if email_entry.get() == user[2]:
                messagebox.showerror("Sorry!","This email already taken!")
                return
            else:
                db.insert(name_entry.get(),email_entry.get(),password_entry.get(),confirm_entry.get(),birthyear_entry.get())
                messagebox.showinfo("Success","Your profile has been created! You can enter with email and password!")
                break
        return


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

#update button
button_update = Button(app, text="Update Profile", command=Update)

# sign up button
button_signup = Button(app, text="Sign Up", command=SignUp)
button_signup.pack(pady = 25)

# information label
info_label = Label(app, text="Do you have an account? Click the button below to Login!")
info_label.pack(pady=20)

# changing from signup to login 
button_login = Button(app, text="Login", command=ClearElements)
button_login.pack(pady = 25)

app.mainloop()