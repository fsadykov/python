# importing the module logging
import logging

# Log format will follow this
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

# Create logger config file
logging.basicConfig(filename = './warning.log', level=logging.DEBUG, format=LOG_FORMAT)

# Geting all logs and assing to the logger variable 
logger = logging.getLogger()

# Test the warning message
logger.warning('You hit WARNING log!')
