import requests

url = 'http://localhost:4000/download'

s = requests.Session()
r = requests.post(url, params={"upload_id": "c755b8ba-b7f4-11ee-8b4a-96efd1126c2e"})

with open('test_outcome.pptx', 'wb+') as ppt:
    for chunk in r.iter_content():
        ppt.write(chunk)

