from digitalocean import SSHKey
import digitalocean
import os
import time
# myToken='6636374f68fc47bb1fbbf4bfd2a1f946a8e07409a8d097fff506a484bc50e7a4'
print('Creating Digital-Ocean Droplet')
myToken = input("Enter token :")
nameDroplet='MYSQL'


debianList = {'Debian','debian', '1',}
centos6List = {'Centos6','Centos 6', '2', 'centos6'}
centos7List = {'Centos7','Centos 7', '3', 'centos7'}
ubuntulist = {'Ubuntu','ubuntu ', '4', 'ubuntu'}
while True:
    os.system('clear')
    print("""
    1. Debian
    2. Centos 6
    3. Centos 7
    4. Ubuntu
    """)
    distributionDroplet = input("Choose the option :")
    if distributionDroplet in debianList:
        chosenImage = 'debian-9-x64'
        break
    elif distributionDroplet in centos6List:
        chosenImage = 'centos-6-x64'
        break
    elif distributionDroplet in centos7List:
        chosenImage = 'debian-7-x64'
        break
    elif distributionDroplet in ubuntulist:
        chosenImage = 'ubuntu-18-04-x64'
        break
    else:
        print('Wrong option')
        time.sleep(2)


answer = input("Do you have ssh-key on your remote machine? :")
yesAnswers = {'yes','y', 'ye', ''}
noAnswers = {'no','n', 'noo'}
if answer in yesAnswers:
    try:
        manager = digitalocean.Manager(token=myToken)
        keys = manager.get_all_sshkeys()
        newDroplet = digitalocean.Droplet(token=myToken, name=nameDroplet, region="nyc1", \
        size_slug='1gb', image=chosenImage, ssh_keys=keys, backups=False)
        newDroplet.create()

        while True:
            existDroplet = manager.get_droplet(droplet_id=newDroplet.id)
            if existDroplet.ip_address != None:
                with open('hosts', 'w') as file:
                    file.write("""[mysql-server]\n""" + existDroplet.ip_address)
                break

    except NameError as error:
        print("You hit an error ", error)

elif answer in noAnswers:
    print("Example: /Users/yoiurname/.ssh/id_rsa.pub")
    path = input("Please enter path to ssh-public_key :")
    try:
        user_ssh_key = open(path).read()
        key = SSHKey(token=myToken, name='newsshkey', public_key=user_ssh_key)
        key.create()

        manager = digitalocean.Manager(token=myToken)
        keys = manager.get_all_sshkeys()
        newDroplet = digitalocean.Droplet(token=myToken, name=nameDroplet, region="nyc1", \
        size_slug='1gb', image='centos-7-x64', ssh_keys=keys, backups=False)
        newDroplet.create()

        while True:
            existDroplet = manager.get_droplet(droplet_id=newDroplet.id)
            if existDroplet.ip_address != None:
                with open('hosts', 'w') as file:
                    file.write("""[mysql-server]\n""" + existDroplet.ip_address)
                break
        print("Make sure you can login to this server :" + existDroplet.ip_address)
        print("Then you can start ansible-playbook")

    except Exception as e:
        print("Something wrong please check path and make sure you token do not exist" , e)
