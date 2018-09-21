import mysql.connector
from __builtin__ import file




config = {
    'host': '127.0.0.1',
    'database': 'av_carlos_live',
    'user': 'root',
    'password': '',
    'raise_on_warnings': True,
    'use_pure': False
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

cursor.close()
cnx.close()

file ='../file/oli_sku_name.xlsx'

import openpyxl as opxl
wb = opxl.load_workbook(file)
# sheet = wb.get_sheet_by_name('Sheet1')
# print data.sheetnames

ws = wb['Sheet1']
query = "";
for row in ws.rows:
    sku = row[1].value.strip()
    oldName = row[3].value.strip()
    newName = row[4].value.strip()
    query = query + '''
        update product p
        join product_detail pd on pd.product_id = p.id
        set name = "'''+newName+'''"
        where pd.sku = "'''+sku+'''" and p.name = "'''+oldName+'''";
    '''
#     print sku,oldName,newName
#     for cell in row:
#         vl = cell.value
#         print cell.value
resQuery = open('../file/update_name.sql','w')
resQuery.write(query)
resQuery.close()
print query
# sheet = wb.get_sheet_by_name('Sheet3')
# for cellObj in sheet['A1':'C3']:
#       for cell in cellObj:
#               print(cell.coordinate, cell.value)
#       print('--- END ---')
