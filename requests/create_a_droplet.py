import requests

# Connect to DigitalOcean
url = 'https://api.digitalocean.com/v2/droplets'
token = input("Please enter your token")

dicDroplet = {
'name': 'example.com',
'region': 'nyc3',
'size': 's-1vcpu-1gb',
'image': 'ubuntu-16-04-x64',
'ssh_keys': None,
'backups': False,
'ipv6': True,
'user_data': None,
'private_networking': None,
'volumes': None,
'tags': ['web']}

# Get list of all droplet
createDroplet = requests.post(url=url, headers={"Authorization": "Bearer {}".format(token)}, json=dicDroplet)
