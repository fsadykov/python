
person = {'name': 'Ahmed', 'lastname': 'Ali', 'password': 'redhat'}

class evolvecyber():
    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password

    def login(self):
        username = input("Please enter your username :")
        password = input("Please enter your password :")
        if username == self.username:
            if password == self.password:
                print("You are login to system")
            else:
                print("Your password is wrong")
        else:
            print("Your username is wrong")

user_1 = evolvecyber('Ahmed', 'Ali', 'ahmedali', 'redhat')
