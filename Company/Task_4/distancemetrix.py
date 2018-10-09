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
for item in kiosks:
    address.append([item[0], item[1]])
# I have now name of the building and address of the building
# ['600 W Chicago', '600 W Chicago Ave, Chicago, IL 60654']

def nextStop(addreslist, curentLocation):
    global allAddress
    allAddress = []
    for addres in addreslist:
        response = requests.get(url + curentLocation + ',DC&destinations=' + addres[1] + ' &key=AIzaSyCGvB2cNSP1Lhj6LiXtq13DtUagbHSvry8')
        responseDict = response.json()
        mile = str(responseDict['rows'][0]['elements'][0]['distance']['text'])
        addres = responseDict['origin_addresses'][0]
        allAddress.append([mile, addres])
        allAddress.sort()
        driverGo = allAddress.pop(0)
    return driverGo

def driver():
    for address in allAddress:
        nextStop(allAddress, driverGo)

if __name__ == '__main__':
    driver()
