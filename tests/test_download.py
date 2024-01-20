import requests

url = 'http://localhost:4000/download'

s = requests.Session()
r = requests.post(url, params={"upload_id": "2228b058-b7eb-11ee-8350-96efd1126c2e"})
for line in r.iter_lines():
    if line:
        print(line)
