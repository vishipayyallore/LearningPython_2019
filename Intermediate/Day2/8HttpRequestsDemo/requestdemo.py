import requests
from pprint import pprint

remote_url = 'http://go.codeschool.com/spamvanmenu'
http_request = requests.get(remote_url)

output = http_request.json()
print(output)
pprint(output)


print('Today\' Menu')
for item in output:
    print(item['name'],    ': ', item['desc'].title(), ', $', item['price'], sep='')
