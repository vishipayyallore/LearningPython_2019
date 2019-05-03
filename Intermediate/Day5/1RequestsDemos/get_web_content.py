from urllib.request import urlopen
import csv
import datetime

def get_configuration(csv_file_name):
    remote_urls = []

    with open(csv_file_name, 'r') as file:
        csvfile = csv.reader(file)

        for row in csvfile:
            remote_urls.append(row)

    return remote_urls

def get_web_content(request_url):
    webcontent = []

    with urlopen(request_url) as content:
        for line in content:
            webcontent.append(line.decode('utf-8'))

    return webcontent

def save_content_locally(filename, content):
    today = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    outputfilepath = f"./Logs/{filename}_{today}.log"

    with open(outputfilepath, 'a') as outputfile:
        for line in content:
            outputfile.write(line)

def main():
    csvfilename = './Data/config.csv'

    remote_urls = get_configuration(csvfilename)
    
    for remoteurl in remote_urls:
        # Getting the content from Web
        file_content = get_web_content(remoteurl[1])

        # Storing the content locally
        save_content_locally(remoteurl[0], file_content)

if __name__ == "__main__":
    main()
