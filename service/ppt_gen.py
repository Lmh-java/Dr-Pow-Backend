import io
import json
import logging
from typing import List

from PIL import Image
from docx import Document
from fastapi import UploadFile
from pptx import Presentation

from service.doc_parser import extract_doc_content
from template.plain_template import PlainTemplate

from api.openai_api import query_chatgpt3_5


# Core PPT Generator
class PPTGenerator:
    def __init__(self, file: UploadFile, prompt: str, template: str = '', file_type: str = ''):
        with io.BytesIO() as io_b:
            io_b.write(file.file.read())
            self.doc_file = Document(io_b)
        self.prompt = prompt
        self.template = PlainTemplate()
        self.file_type = file_type

    def generate(self) -> Presentation:
        # convert UploadFile to Document obj
        doc_content = extract_doc_content(self.doc_file)
        logging.debug("received doc content: {}".format(doc_content[:50]))

        # call chatgpt api to fetch json
        # json_result = json.loads(query_chatgpt3_5(doc_content, self.prompt).model_dump_json())
        # use dummy json file now instead
        with open("tests/example_json_response.json", 'r') as _:
            json_result = json.loads(_.read())
        logging.debug("received json from chatgpt3.5: {}".format(json_result))

        self.template.create_title_slide(json_result['presentation theme'])
        presentation_slides: List[dict] = json_result['presentation slides']
        for slide in presentation_slides:
            self.template.create_pic_slide(slide['title'], slide['body'], Image.open('tests/test_image.png'))
        logging.debug("Successfully created pptx")
        return self.template.get_ppt()
