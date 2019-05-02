from urllib.request import urlopen


def get_content(request_url):
    webcontent = []

    with urlopen(request_url) as content:
        for line in content:
            webcontent.append(line.decode('utf-8').split())

    return webcontent


def main():
    remote_url = 'http://sixty-north.com/c/t.txt'
    contents = get_content(remote_url)
    print(contents)

    remote_url = 'https://www.python.org/'
    contents = get_content(remote_url)
    print(contents)

    remote_url = 'http://go.codeschool.com/spamvanmenu'
    contents = get_content(remote_url)
    print(contents)


if __name__ == "__main__":
    main()
