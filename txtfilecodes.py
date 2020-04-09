
# creating an empty dictionary variable to display logged user info
user_info = {'name_surname': '', 'email':'', 'password':'','age':''}

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
'''

'''
READING FROM A TEXT FILE

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
'''

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


# def Greeting():
#   print("1) Login")
#    print("2) Sign Up")

#Greeting()
