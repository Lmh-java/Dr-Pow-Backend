import requests

url = 'http://localhost:4000/upload'

r = requests.post(url, files={
    "file": ("filename", open('test_doc.docx', "rb"),
             "application/vnd.openxmlformats-officedocument.presentationml.presentation")},
                  params={"prompt": "Use Spanish to return",
                          "template": "History",
                          "file_type": "application/vnd.openxmlformats-officedocument"})
print(r.json())
