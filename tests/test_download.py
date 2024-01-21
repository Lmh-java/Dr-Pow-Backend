import requests

url = 'http://localhost:4000/download'

s = requests.Session()
r = requests.get(url, params={"upload_id": "528ed57c-b81a-11ee-8d3f-96efd1126c2e"})

with open('test_outcome.pptx', 'wb+') as ppt:
    for chunk in r.iter_content():
        ppt.write(chunk)

