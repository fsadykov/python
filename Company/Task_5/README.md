# Script to connect DB using ssl
#interview

## Versions 
pip 20.0.2
Python 3.7.4


## Steps to Run the script
Please follow bellow steps to run the script 
```
git clone git@github.com:fsadykov/python.git
cd python/Company/Task_5
```

After you go to the folder Task_5 you will need install some packages run following command to install all necessary packages

```
pip install -r requirements.txt
```

After all packages are installed please update script to right values
you will need to update dictionary call `ssl_paths`

```
ssl_paths = {
    "ssl_ca"   : "/Users/fsadykov/Projects/python/Company/Task_5/client-certs/ca.pem",
    "ssl_cert" : "/Users/fsadykov/Projects/python/Company/Task_5/client-certs/client-cert.pem",
    "ssl_key"  : "/Users/fsadykov/Projects/python/Company/Task_5/client-certs/client-key.pem"
}
```

make sure you put right location 
```
ls /Users/fsadykov/Projects/python/Company/Task_5/client-certs/ca.pem
ls /Users/fsadykov/Projects/python/Company/Task_5/client-certs/client-cert.pem
ls /Users/fsadykov/Projects/python/Company/Task_5/client-certs/client-key.pem
```

After that you will need to set some other environment variables please follow 
```
export DB_HOST='134.122.26.220'
export DB_USER='RemoteSslUser'
export DB_PASSWORD='DB_PASSWORD'
```

After that you should be able to run the script
```
(db-connect) ╭─ fsadykov ~/Projects/python/Company/Task_5 
╰─(‹master*› ) python script.py 
('Ssl_cipher', 'DHE-RSA-AES256-SHA')
```
