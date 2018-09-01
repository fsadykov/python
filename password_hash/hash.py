from werkzeug.security import generate_password_hash, check_password_hash

class fscoding():
    def __init__(self, fname, lname, username, password, status):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = generate_password_hash(password, method='sha256')
        self.status = False

    def changeName(self):
        self.fname = input("Enter First Name :")
        self.lname = input("Enter Last Name :")

    def login(self):
        print(""" Welcome to FS Coding Class """)
        userName = input("Please enter the Username :")
        passWord = input("Please enter the Password :")
        if userName == self.username:
            check_pass = check_password_hash(self.password, passWord)
            if check_pass == True:
                print("You are login to our System")
            else:
                print("Username or password invalid")
        else:
            print("Username or password invalid")
    def changePasswd(self):
        print("Change the password")
        new_password = input("Enter the password :")
        new_generated = generate_password_hash(new_password, method='sha256')
        self.password = new_generated

    def fullInfo(self):
        print("FirstName :" + self.fname + ' LastName :' + self.lname + ' Password :'+ self.password + " Status :" + self.status)
