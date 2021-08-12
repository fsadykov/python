import yaml
import os

with open('playbook.yml') as file:
    data = yaml.load(file)

def pingHost(IPHOST):
     with open('hosts', 'w') as file:
         file.write('[test]\n{}'.format(IPHOST))

os.system('ansible all -u root -i hosts -m ping ')

def buildthemysql():
    with open('test.yml', 'w') as file:
        yaml.dump(data, file)
    os.system('ansible-playbook -i hosts -u root test.yml')
