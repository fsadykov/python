import csv
import json

with open('fruits.csv', 'r') as f:
    reader = csv.reader(f)
    fruits = list(reader)

dinctionary = {}
count = 0.0
for item in fruits:
    if item[0] in dinctionary:
        count += float(item[2])
    dinctionary[item[0]] = {item[1]:count}


def checkItem(arg):
    countFriuts = len(arg)
    typeFriuts = []
    for typeOfFriuts in arg:
        if typeOfFriuts not in typeFriuts:
            typeFriuts.append(typeOfFriuts)
    totalType = len(typeOfFriuts)
    print("Total fruits {}, Type of the fruits {}".format(countFriuts, totalType))


print(json.dumps(dinctionary, indent=2))
checkItem(fruits)
