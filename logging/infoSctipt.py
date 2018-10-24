import logging

# Create logger config file
logging.basicConfig(filename = './info.log', level=logging.DEBUG)
logger = logging.getLogger()

# Test the info meassage
logger.info('You hit info log!')
