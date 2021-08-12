# Digital-Ocean python Api Module
#dev/Python

Connect manager module 
```
manager = digitalocean.Manager(token="you token")
```

`manager.end_point` To see where goes all data
`manager.get_all_droplets()` See all droplets 
`manager.get_account()` Get account information 
`manager.get_all_sshkeys()` Get all your ssh keys in DC


## Creating a droplet (instance) to Digital-Ocean
``` This code will create droplet existing ssh-key
import 
manager = digitalocean.Manager(token="yourtoken")
keys = manager.get_all_sshkeys()
droplet = digitalocean.Droplet(token="yourtoken", name='PythonDroplet', region = "nyc3", size_slug='512mb', image='centos-7-x64', ssh_keys=keys, backups=False)
droplet.create()

```

## Manage a droplet drom digitaal-oceaan 
```
droplet = manager.get_droplet(droplet_id=105189062)

```

`droplet.status` See the status 
`droplet.memory` To see memory of the droplet 



 |  Args:
 |      name (str): name
 |      size_slug (str): droplet size
 |      image (str): image name to use to create droplet
 |      region (str): region
 |      ssh_keys: (:obj:`str`, optional): list of ssh keys
 |      backups (bool): True if backups enabled
 |      ipv6 (bool): True if ipv6 enabled
 |      private_networking (bool): True if private networking enabled
 |      user_data (str): arbitrary data to pass to droplet
 |      volumes (:obj:`str`, optional): list of blockstorage volumes
 |      monitoring: (bool) - True if installing the DigitalOcean monitoring agent