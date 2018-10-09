def nextStop(addreslist, curentLocation):
    allAddress = []
    for addres in addreslist:
        response = requests.get(url + curentLocation + ',DC&destinations=' + addres[1] + ' &key=AIzaSyCGvB2cNSP1Lhj6LiXtq13DtUagbHSvry8')
        responseDict = response.json()
        mile = str(responseDict['rows'][0]['elements'][0]['distance']['text'])
        addres = responseDict['origin_addresses'][0]
        allAddress.append([mile, addres])
        allAddress.sort()
    return allAddress[0]
