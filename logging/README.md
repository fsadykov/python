# Using logging module on python
Loggin allow you to write status messages to a file or other output stings. These messages contents which part go the code has executed and what problems may arisen. Each log has level you can see following status.

Levels: Debug, Info, Warning, Error, Critical

In this example infoSctipt.py  will create info.log on current directory and will write the info message 'You hit info log! '.  Message will appended on the file for example you will run again you will se two message. 

``` infoSctipt.py
import logging

# Create logger config file
logging.basicConfig(filename = './info.log', level=logging.DEBUG)
logger = logging.getLogger()

# Test the info meassage
logger.info('You hit info log!')
```


In this example script will create warning.log file and format will changed. Format will follow the name of the log,  data of the log  and message 'You hit WARNING log!'
```
import logging

# Log format will follow this
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

# Create logger config file
logging.basicConfig(filename = './warning.log', level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()

# Test the warning message
logger.warning('You hit WARNING log!')
```

If you would like to not append the file write the actual time log you can change log mode to writemode
example: 

```
import logging

# Log format will follow this
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

# Create logger config file
logging.basicConfig(filename = './warning.log', level=logging.DEBUG, format=LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()

# Test the warning message
logger.warning('You hit WARNING log!')
```

Use you log module on your code to be more professionally :) 