import requests

# Authentication information
url = 'https://api.digitalocean.com/v2/droplets'
token = 'YourToken'

# Get list of all droplets
droplets = requests.get(url=url, headers={'Authorization': 'Bearer {}'.format(token)})

listDroplets = droplets.json()
for droplet in listDroplets['droplets']:
    print('Id: ' + str(droplet['id']) + ' Name: ' + droplet['name'] + 'Ipaddres:' + listDroplets['droplets'][0]['networks']['v4'][0]['ip_address'])
