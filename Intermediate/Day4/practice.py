"""This File is used for practice the programs daily
"""

from urllib.request import urlopen

remote_url = 'http://sixty-north.com/c/t.txt'
# remote_url = 'http://go.codeschool.com/spamvanmenu'
# remote_url = 'https://www.python.org/'

with urlopen(remote_url) as content:
    for line in content:
        print(line.decode('utf-8').split())

