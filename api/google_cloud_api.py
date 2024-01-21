import logging

from google.cloud import vision
from fastapi import UploadFile


def detect_text_in_image(file: UploadFile) -> str:
    """Detects text in the file.
    DOCUMENT_TEXT_DETECTION"""

    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=file.file.read())

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    result = ""
    for text in texts:
        result += f' "{text.description}"'
    logging.debug("Receiving OCR result from Google API: " + str(result))
    return result
