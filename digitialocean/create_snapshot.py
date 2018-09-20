import digitalocean
token = input("Please enter your token :")
droplet = digitalocean.Droplet(token=token, id=110599324)
droplet.take_snapshot(snapshot_name='example_snapshot')
