import configparser

config = configparser.ConfigParser()
config.read('config.properties')


my_dict = {}
my_dict['ENVIRONMENT'] = config['PROJECT']['ENVIRONMENT']

