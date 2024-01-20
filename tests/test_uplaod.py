import requests

url = 'http://localhost:3000/upload'

r = requests.post(url, files={
    "file": ("filename", open('test_doc.docx', "rb"),
             "application/vnd.openxmlformats-officedocument.presentationml.presentation"),
    "prompt": "test prompt",
    "template": "test template",
    "file_type": "application/vnd.openxmlformats-officedocument"})
