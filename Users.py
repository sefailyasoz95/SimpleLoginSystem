from camelcase import CamelCase

class User:
   # name_surname = ""
    #email = ""
    #password = ""
    #confirm_password = ""
    #birth_year = 0
    users = {'name_surname': '','email':'', 'password': '', 'confirm_password': '', 'birth_year': 0}
    
    def PersonCreated(self):
        c = CamelCase()
        username = self.users['name_surname']
        print("Dear "+ c.hump(username) +" your profile has been created")
