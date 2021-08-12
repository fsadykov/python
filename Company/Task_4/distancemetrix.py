import csv
import json
import requests
import time
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='
beginDest = '1385 W Lake St, Chicago, IL 60607, USA'
with open('Kiosk Coords.csv', 'r') as f:
    reader = csv.reader(f)
    kiosks = list(reader)
    kiosks.pop(0)


address = []
address.append(beginDest)
for item in kiosks:
    address.append(item[1])



def nextStop(addresslist, curentLocation):
    allAddress = []
    for addres in addresslist:
        response = requests.get(url + curentLocation + ',DC&destinations=' + addres + ' &key=AIzaSyCGvB2cNSP1Lhj6LiXtq13DtUagbHSvry8')
        responseDict = response.json()
        mile = str(responseDict['rows'][0]['elements'][0]['distance']['text'])
        addres = responseDict['destination_addresses'][0]
        allAddress.append([mile, addres])
        allAddress.sort()
        result = allAddress[0]
    return result


for item in address:
    nextAddress = nextStop(address, address[0])
    print("Your next stop is :", nextAddress)
    address.pop(address.count(nextStop))



if __name__ == '__main__':
    main()
