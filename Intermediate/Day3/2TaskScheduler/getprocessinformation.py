import subprocess
import json
from pprint import pprint as pp
import datetime


subprocess.Popen
pl = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE).communicate()[0]
print(pl.decode('utf-8'))


today = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
print( today)
outputfilepath = f"./datastore/process_{today}.log"

with open(outputfilepath, 'a') as outputfile:
    outputfile.write(pl.decode('utf-8'))
    

"""
inputfilepath = "./datastore/input.json"
outputfilepath = "./datastore/output.txt"

with open(inputfilepath, 'r') as input:
	json_content = json.load(input)

print(json_content["name"], ' | ', json_content["job"])
for hobby in json_content["hobbies"]:
    print(f'\t{hobby}')

print(json_content)

pp(json_content)
"""