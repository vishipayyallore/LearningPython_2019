import json

inputfilepath = "./datastore/input.json"
outputfilepath = "./datastore/output.txt"

with open(inputfilepath, 'r') as input:
	obj = json.load(input)
	with open(outputfilepath, 'w') as output:
		output.write(obj['name'] + "'s Hobbies:\n")
		for hobby in obj['hobbies']:
			output.write(hobby + "\n")
