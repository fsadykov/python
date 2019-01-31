## import module requests
import requests

## You have to change to your token
# token = 'changetoyourtoken'
token = input('Please enter the token :')

## This is your object
data = {
    'ssh_keys': None,
    'tags': ['web'],
    'region': 'nyc3',
    'user_data': None,
    'volumes': None,
    'ipv6': True,
    'private_networking': None,
    'backups': False,
    'size': 's-1vcpu-1gb',
    'image': 'ubuntu-16-04-x64',
    'name': 'example.com'
    }

## Endpoint to create object
url = 'https://api.digitalocean.com/v2/droplets'

## Posting the object to create on the digitalocean
resp = requests.post(url, json=data,
        headers={'Authorization': 'Bearer {}'.format(token)})

## Show the object created on digitalocean
print(resp.json())
