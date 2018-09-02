import json


# This dictionary conent user data
User = dict(fname='Nazira', lname='Sadykova', username='nazirasadykov', password="redhat", status=False)
with open('user.json', 'w') as file:
    json.dump(User, file, indent=2)

listUser = [{'fname': 'Farkhod', 'lname': 'Sadykov', 'username': 'farkhodsadykov', 'password': 'Redhat2018', 'status': True}, {'fname': 'Nazira', 'lname': 'Sadykova', 'username': 'nazirasadykov', 'password': 'redhat', 'status': False}]
with open('list.json', 'w') as file:
    json.dump(listUser, file, indent=2)
