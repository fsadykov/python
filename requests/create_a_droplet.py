import requests

# Connect to DigitalOcean
url = 'https://api.digitalocean.com/v2/droplets'
token = 'c4524635b2484d4baf4d8b8af1e680ed6ae8f9b829e1556c71970dd5a0c58e85'

# Get list of all droplet

droplets = requests.post(url=url, headers={'Authorization': 'Bearer {}'.format(token)}, body=machine)
