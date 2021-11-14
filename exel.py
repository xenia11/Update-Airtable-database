import csv
import json
import openpyxl
from pathlib import Path
import os
import pandas as pd

# df = pd.read_csv('airtable.csv',error_bad_lines=False)

from pyairtable import Api, Base, Table
import requests
import airtable

at = airtable.Airtable('base_id', 'api_key')

table = Table('api_key', 'base_id', 'Table 2')

#ubaci u set sve iz airtable

items_dict = set()
email_dict= set()
for item in table.all():
		fields = item['fields']
		item_key = fields['First Name'] + fields['Last Name']
		# item_email = fields['Work Email']
		items_dict.add(item_key)
		# email_dict.add(item_email)
		# print(item_email)

excel_jobadder = pd.read_excel('jobadder.xlsx')
for index, row in excel_jobadder.iterrows():
    excel_row_key = row['First Name'] + row['Last Name']
    email = row['Email']
    if excel_row_key in items_dict:
        print('ima')
        # if email in email_dict:
        # 	print('ima telefon')
        # else:
        # 	print("nema telefon")
        # 	addEmail = {}
        # 	addEmail['Work Email'] = row['Email']

        # 	table.create(data)

    else:
        print('nema')
        data = {}
        data['First Name'] = row['First Name']
        data['Last Name'] = row['Last Name']
        
        table.create(data)

for index, row in excel_jobadder.iterrows():
    excel_row_key = row['First Name'] + row['Last Name']
    if excel_row_key in items_dict:
        print('ima')
    else:
        print('nema')
        data = {}
        data['First Name'] = row['First Name']
        data['Last Name'] = row['Last Name']



#prodji kroz sve iz excel-a 
	# za svaki uzmi FirstName + LastName i provjeri da li postoji u setu
	# ako ne postoji mapiraj u dictionary i table.create(taj objekat)




# result = at.get('Table 2')
# print(result)
# examp = { "records": []}


# for r in at.iterate('Table 2'):
#     examp["records"].append(r)
    
# print(examp)
   
		



# set_at = set()
# for index, row in df.iterrows():
#     airtable_row_key = str(row['First Name']) + str(row['Last Name'])
#     if airtable_row_key in set_at:
#         continue
#     set_at.add(airtable_row_key)








        # call rest api, and create new rows directly in airtable
        # https://pyairtable.readthedocs.io/en/latest/api.html


        # data = [
	       #  [
	       #  	row['First Name'], 
	       #  	row['Last Name']
	       #  ]
        # ]
        # dataFrame = pd.DataFrame(data)

        # with open('airtable.csv', 'a', newline = '\n') as f:
        #     dataFrame.to_csv(f, index = False, header=False)
