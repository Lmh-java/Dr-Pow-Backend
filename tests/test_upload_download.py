import requests

url = 'http://localhost:4000/upload'

r = requests.post(url, files={
    "file": ("test_txt.txt", open('test_txt.txt', "rb"),
             "application/vnd.openxmlformats-officedocument.presentationml.presentation")},
                  params={"prompt": "",
                          "template": "Minimalistic",
                          "file_type": "application/vnd.openxmlformats-officedocument"})
print(r.json())
upload_id = r.json()['upload_id']

url = 'http://localhost:4000/download'

s = requests.Session()
r = requests.get(url, params={"upload_id": upload_id})

with open('test_outcome.pptx', 'wb+') as ppt:
    for chunk in r.iter_content():
        ppt.write(chunk)