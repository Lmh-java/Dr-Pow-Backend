import json
import logging
from typing import List

from PIL import Image
from pptx import Presentation


from template.history_template import HistoryTemplate
from template.pastel_template import PastelTemplate
from template.plain_template import PlainTemplate
from template.minimalistic_template import MinimalisticTemplate
from template.school_template import SchoolTemplate
from template.portfolio_template import PortfolioTemplate

from api.openai_api import query_chatgpt3_5
from api.unsplash_api import search_photo, download_photo

# FIXME: If this flag is true, it will save the api call chances.
DEBUG_FLAG = True


# Core PPT Generator
class PPTGenerator:
    def __init__(self, content: str, prompt: str, template: str = '', file_type: str = ''):
        self.content = content
        self.prompt = prompt
        # templates mapping
        if template == 'History':
            self.template = HistoryTemplate()
        elif template == 'Minimalistic':
            self.template = MinimalisticTemplate()
        elif template == 'Pastel':
            self.template = PastelTemplate()
        elif template == 'Portfolio':
            self.template = PortfolioTemplate()
        elif template == 'School':
            self.template = SchoolTemplate()
        else:
            self.template = PlainTemplate()
        self.file_type = file_type

    def generate(self) -> Presentation:
        # convert UploadFile to Document obj
        logging.debug("received doc content: {}".format(self.content[:50]))

        # call chatgpt api to fetch json
        if DEBUG_FLAG:
            with open("tests/example_json_response.json", 'r') as _:
                json_result = json.loads(_.read())
        else:
            logging.debug("123192310239102931923012:" + self.content[:1000])
            json_result = json.loads(query_chatgpt3_5(self.content, self.prompt)
                                     .model_dump_json().replace("\n", ""))['content']
            json_result = json.loads(json_result)
        logging.debug("received json from chatgpt3.5: {}".format(json_result))

        self.template.create_title_slide(json_result['presentation theme'])
        presentation_slides: List[dict] = json_result['presentation slides']
        count = 0
        for slide in presentation_slides:
            count += 1
            if count > 10:
                break
            try:
                if DEBUG_FLAG:
                    self.template.create_pic_slide(slide['title'], slide['body'], Image.open("tests/test_image.png"))
                else:
                    photo_id = search_photo(slide["title"])
                    self.template.create_pic_slide(slide['title'], slide['body'], download_photo(photo_id))
            except Exception as e:
                logging.error("Skip due to error when creating slide #{}, {}".format(count, e))
        logging.debug("Successfully created pptx")
        # self.template.get_ppt().save("tests/test_outcome.pptx")
        return self.template.get_ppt()
