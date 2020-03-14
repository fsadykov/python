#!/usr/bin/python
import sys
import os 
import mysql.connector
from mysql.connector.constants import ClientFlag

# Please update this following cinfigurations
ssl_paths = {
    "ssl_ca"   : "/Users/fsadykov/Projects/python/Company/Task_5/client-certs/ca.pem",
    "ssl_cert" : "/Users/fsadykov/Projects/python/Company/Task_5/client-certs/client-cert.pem",
    "ssl_key"  : "/Users/fsadykov/Projects/python/Company/Task_5/client-certs/client-key.pem"
}

# all these environment variables are should be set export DB_HOST='192.168.3.1'
if os.environ.get("DB_HOST") and os.environ.get("DB_USER") and os.environ.get("DB_PASSWORD"):
    db_host = os.environ.get("DB_HOST")
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    config = {
        'user': str(db_user),
        'password': str(db_password),
        'host': str(db_host),
        'ssl_ca': ssl_paths['ssl_ca'],
        'ssl_cert': ssl_paths['ssl_cert'],
        'ssl_key': ssl_paths['ssl_key'],
        'client_flags': [ClientFlag.SSL],
    }
else:
    print("Please set following environemnt variables. <DB_HOST>, <DB_USER>, <DB_PASSWORD>")
    exit()

cnx = mysql.connector.connect(**config)
cur = cnx.cursor(buffered=True)
cur.execute("SHOW STATUS LIKE 'Ssl_cipher'")
print(cur.fetchone())
cur.close()
cnx.close()