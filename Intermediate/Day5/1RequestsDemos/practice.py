"""This File is used for practice the programs daily
"""

import datetime
import csv
from urllib.request import urlopen

def get_content(request_url):
    webcontent = []

    with urlopen(request_url) as content:
        for line in content:
            webcontent.append(line.decode('utf-8'))

    return webcontent


remote_urls = []

with open('./Data/config.csv', 'r') as file:
    csvfile = csv.reader(file)

    for row in csvfile:
        print(row)
        remote_urls.append(row)

print(remote_urls)

print(dict(remote_urls))

content = get_content(remote_urls[0][1])

today = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
outputfilepath = f"./Logs/{remote_urls[0][0]}_{today}.log"


with open(outputfilepath, 'a') as outputfile:
    outputfile.write(str(content))


content = get_content(remote_urls[1][1])

today = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
outputfilepath = f"./Logs/{remote_urls[1][0]}_{today}.log"


with open(outputfilepath, 'a') as outputfile:
    for line in content:
        outputfile.write(line)
