import requests

# remote_url = 'https://www.python.org/'
remote_url = 'https://github.com/timeline.json'
http_request = requests.get(remote_url)

print(f'Status Code: {http_request.status_code}')
print(f'Output\n {http_request.text}')
    

