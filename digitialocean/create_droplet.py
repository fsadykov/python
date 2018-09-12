from digitalocean import SSHKey
import digitalocean
user_ssh_key = open('/Users/fsadykov/.ssh/id_rsa.pub').read()
key = SSHKey(token='6636374f68fc47bb1fbbf4bfd2a1f946a8e07409a8d097fff506a484bc50e7a4',
             name='My Mac',
             public_key=user_ssh_key)
key.create()


droplet = digitalocean.Droplet(token="6636374f68fc47bb1fbbf4bfd2a1f946a8e07409a8d097fff506a484bc50e7a4",
                               name='DropletWithSSHKeys',
                               region='ams3', # Amster
                               image='centos-7-x64', # Ubuntu 14.04 x64
                               size_slug='512mb',  # 512MB
                               ssh_keys=keys, #Automatic conversion
                               backups=False)
droplet.create()
