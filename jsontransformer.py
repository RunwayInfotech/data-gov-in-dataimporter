import sys
import json


'''
usage:

1. Download data from data.gov.in in json format and save it as a file
2. Update the field 'id' inside 'fields' in the json per your wish. If you want to remove any field, set its label to empty string
3. python jsontransformer.py <INPUT_JSON_FILE> <OUTPUT_JSON_FILE>

 
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
			if fields[i]:
				temp[fields[i]] = entry[i]
		output_dict['data'].append(temp)

	output_json = json.dumps(output_dict)

	with open(OUTPUT_JSON_FILE, 'w') as outfile:
		outfile.write(str(output_json))




def get_field_names(data):
	fieldList = list()
	fields = data['fields']
	
	for field in fields:
		fieldList.append(field['id'])

	return fieldList


if __name__ == "__main__":
	main(sys.argv)
