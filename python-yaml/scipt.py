import yaml
import os

with open('playbook.yml') as file:
    data = yaml.load(file)

print(data)

with open('test.yml', 'w') as file:
    yaml.dump(data, file)
