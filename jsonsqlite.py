import sys
import json
import sqlite3
from itertools import repeat


'''
usage:

1. Download data from data.gov.in in json format and save it as a file
2. Update the field 'label' inside 'fields' in the json to reflect your column names.
3. python jsonsqlite.py <JSON_FILENAME> <DB_FILENAME>  <TABLE_NAME> 

 
'''
 
def main(argv):
	JSON_FILE = argv[1]
	DB_FILE = argv[2]
	TABLE_NAME = argv[3]

	
	jsondata = json.load(open(JSON_FILE))
	columns = get_column_names(jsondata)
	columnstr = ",".join(columns)
	values = list(repeat('?', len(columns)))
	valuestr = ",".join(values)
	
	conn = sqlite3.connect(DB_FILE)
	c = conn.cursor()
		
	create_query = 'create table ' +  TABLE_NAME + ' (' + columnstr + ')'
	c.execute(create_query)


	data = jsondata['data']	
	insert_query = 'insert into ' + TABLE_NAME + ' values(' + valuestr + ')'
	values = list(repeat('?', len(columns)))
	for entry in data:
		c.execute(insert_query,entry)
	
	conn.commit()
	c.close()	
	


def get_column_names(data):
	fieldList = list()
	fields = data['fields']
	for field in fields:
		fieldList.append(field['label'])
	return fieldList


if __name__ == "__main__":
	main(sys.argv)
