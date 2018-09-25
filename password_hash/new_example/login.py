from werkzeug.security import generate_password_hash, check_password_hash
import json

with open('user.json') as file:
    data = json.load(file)

class myapp():
    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = generate_password_hash(password, method='sha256')
        
    def login(self):
        username = input('Please enter the username :')
        password = input('Please enter the password :')
        if username == self.username:
            check_pass = check_password_hash(self.password, password)
            if check_pass == True:
                print('You are welcome back')
            else:
                print('Username or password invalid')
        else:
            print('Username or password invalid')

    def fullInfo(self):
        return "Firstname {}, Lastnaem {}, Username {}, Secured password {}".format(self.fname, self.lname, self.username, self.password)

user = myapp(data['fname'], data['lname'], data['username'], data['password'])
