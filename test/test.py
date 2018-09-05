import requests
from json_encoder import json

import mysql.connector
config = {
  'user': 'pldm_user_rw',
  'password': 'WZaFNDujzUWNUKKB',
  'host': 'db-dev.seldatdirect.com',
  'database': 'pldm_dev',
  'raise_on_warnings': True,
  'use_pure': False,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
url = 'http://api.timezonedb.com/v2/list-time-zone?key=BWYLPCYMUJIZ&format=json'

response = requests.get(url)

data=json.loads(response.text)
zones = data['zones']
for zone in zones:
    utc = zone['gmtOffset']/60/60
    time = zone['zoneName'].replace("/",' - ') 
    du = zone['gmtOffset']%3600
    if utc>0 :
        utc = '+'+str(utc).zfill(2)
    else:
        utc = abs(utc)
        utc = '-'+str(utc).zfill(2)
    timeName = '(' + 'UTC ' + utc +":"+str(du/60).zfill(2)+ ') '+time
      
    add_employee = ("INSERT INTO timezones (cd, name) VALUES (%s, %s)")
    data_employee = (zone['zoneName'],timeName)
    cursor.execute(add_employee, data_employee)
    print timeName
     
    
    
zone = {
    'Africa':'Africa',
    'America':'America',
    'Antarctica':'Antarctica',
    'Asia':'Asia',
    'Atlantic':'Atlantic',
    'Australia':'Australia',
    'Europe':'Europe',
    'Indian':'Indian',
    'Pacific':'Pacific'
}
for k,v in zone.items():
    zoneQuery = ("INSERT INTO areas (cd, name) VALUES (%s, %s)")
    zoneData = (k,v)
    cursor.execute(zoneQuery, zoneData)
    print k,v
cnx.commit()

cursor.close()
cnx.close()
print(response.text)