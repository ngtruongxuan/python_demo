import requests
import random
from json_encoder import json

import mysql.connector
config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'test',
  'raise_on_warnings': True,
  'use_pure': False,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
i=0
cursor.execute('TRUNCATE TABLE `order`')
query = ("INSERT INTO `order`(cd,type) VALUES(%s,%s);")
# for i in range(0,1000000):
#     data = (i,random.choice('ABC'))
#     cursor.execute(query, data)
# while i < 100000:
#     i = i+1
#     data = (i,random.choice('ABC'))
#     cursor.execute(query, data)
cnx.commit()
cursor.close()
cnx.close()

