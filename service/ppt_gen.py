from docx import Document
from fastapi import UploadFile

from service.doc_parser import extract_doc_content
from template.plain_template import PlainTemplate


# Core PPT Generator
class PPTGenerator:
    def __init__(self, file: UploadFile, prompt: str, template: str = '', file_type: str = ''):
        self.doc_file = Document(self.doc_file.file)
        self.prompt = prompt
        self.template = PlainTemplate()
        self.file_type = file_type

    def generate(self):
        # convert UploadFile to Document obj
        doc_content = extract_doc_content(self.doc_file)
        print(doc_content)
