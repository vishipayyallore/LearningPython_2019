import requests
import sys
from urllib.request import urlopen

# remote_url = 'https://www.python.org/'
# remote_url = 'http://sixty-north.com/c/t.txt'
remote_url = 'http://go.codeschool.com/spamvanmenu'

with urlopen(remote_url) as content:
    for line in content:
        print(line)
