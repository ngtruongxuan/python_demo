import requests
from json_encoder import json

import mysql.connector
# config = {
#   'user': 'pldm_user_rw',
#   'password': 'WZaFNDujzUWNUKKB',
#   'host': 'db-dev.seldatdirect.com',
#   'database': 'pldm_dev',
#   'raise_on_warnings': True,
#   'use_pure': False
# }

config = {
  'user': 'pldm_nganha_rw',
  'password': 'tX7VCgP9FrSnNSsT',
  'host': 'db-live2.seldatdirect.com',
  'database': 'pldm_live',
  'raise_on_warnings': True,
  'use_pure': False
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
lsCode = '15013-0000049'
type = 'trim'
lsCode = lsCode.split(',')
for cd in lsCode:
    query = """
        set @cd = '"""+cd+"""';
        set @unit = (select """+type+"""_variation_unit_id from """+type+"""_variation_units where cd = @cd limit 1);
    
        UPDATE inventories
        set allocated = available
        where """+type+"""_variation_unit_id = @unit and warehouse_id = 2 and available>0;
        
        UPDATE inventories
        set available = 0
        where """+type+"""_variation_unit_id = @unit and warehouse_id = 2 and available>0;
    """
    print query
    cursor.execute(query,multi=True)
# cnx.commit()
cursor.close()
cnx.close()
