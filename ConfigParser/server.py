
from script import my_dict
import configparser

config = configparser.ConfigParser()

class Server():
    def __init__(self, environment):
        self.environment = environment

def get_client(environment='prod'):
    config.read('environments.properties')
    server = config['ENV']
    if environment.lower() not in server:
        raise ValueError("The specified environment doesn't exist.", environment)
    return Server(server[environment.upper()])