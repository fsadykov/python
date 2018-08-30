class person():
    def __init__(self, name, year, gender, password):
            self.name = name
            self.year = year
            self.gender = gender
            self.password = password

    def fullinfo(self):
        print ("Persons name is:{} born in {} Gender is {}".format(self.name, self.year, self.gender))

    def entry(self):
        var = input("Enter your password :")
        if var == self.password:
            print("You are able to login")
        else:
            print("You are not able to login")

    def changeName(self):
        newname = input("Please enter your new name :")
        self.name = newname

user_1 = person("Farkhod Sadykov", 1996, "Male", "redhat")
user_2 = person("Bakulya Alymbek", 1994, "Female", "noredhat")

# user_1.fullinfo()
# user_2.fullinfo()
# user_1.entry()
# user_1.changeName()
# user_1.fullinfo()
