import json
from pprint import pprint as pp

inputfilepath = "./datastore/input.json"
outputfilepath = "./datastore/output.txt"

with open(inputfilepath, 'r') as input:
	json_content = json.load(input)

print(json_content["name"], ' | ', json_content["job"])
for hobby in json_content["hobbies"]:
    print(f'\t{hobby}')

print(json_content)

pp(json_content)

