import json
from pprint import pprint as pp
from utilitiesmodule import *

filepath = './datastore/movies.json'

with open(filepath, mode='r', encoding='utf-8') as jsonfile:
    json_content = json.load(jsonfile)

banner("Simple Print", 100)
print(json_content)    
banner_v2(100)

banner("Pretty Print", 100)
pp(json_content)    
banner_v2(100)

banner("Movie Titles", 100)
for movie in json_content:
    print(movie['title'], ' | ', movie['year'])
banner_v2(100)