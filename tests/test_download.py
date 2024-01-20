import requests

url = 'http://localhost:4000/download'

s = requests.Session()
r = requests.post(url, params={"upload_id": "b69b4524-b7e7-11ee-8a9a-96efd1126c2e"})
for line in r.iter_lines():
    if line:
        print(line)
