import sys
import json


'''
usage:

1. Download data from data.gov.in in json format and save it as a file
2. Update the field 'label' inside 'fields' in the json to reflect your column names.
3. python jsontransformer.py <INPUT_JSON_FILE> <OUTPUT_JSON_FILE>  <COMMA SEPARATED NEW FIELDS> 

 
'''
 
def main(argv):
	INPUT_JSON_FILE = argv[1]
	OUTPUT_JSON_FILE = argv[2]

	jsondata = json.load(open(INPUT_JSON_FILE))
	fields = get_field_names(jsondata)
	output_dict = {'data' : []}

	data = jsondata['data']	
	for entry in data:
		temp = dict()
		for i in range(len(entry)):
			temp[fields[i]] = entry[i]
		output_dict['data'].append(temp)

	output_json = json.dumps(output_dict)
	with open(OUTPUT_JSON_FILE, 'w') as outfile:
  		json.dump(output_json, outfile, sort_keys = True, indent = 4,)



def get_field_names(data):
	fieldList = list()
	fields = data['fields']
	
	for field in fields:
		fieldList.append(field['label'])

	return fieldList


if __name__ == "__main__":
	main(sys.argv)
