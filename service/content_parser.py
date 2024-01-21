import io
import logging

from docx import Document
from fastapi import UploadFile

from api.google_cloud_api import detect_text_in_image
from service.doc_parser import extract_doc_content


def parse_content(file: UploadFile) -> str:
    filename = file.filename
    if filename.endswith("docx"):
        with io.BytesIO() as io_b:
            io_b.write(file.file.read())
            doc_content = extract_doc_content(Document(io_b))
            return doc_content
    elif filename.endswith("txt"):
        return file.file.read().decode("utf-8")
    elif filename.endswith("md"):
        pass
    elif filename.endswith("png"):
        return detect_text_in_image(file)
    elif filename.endswith("jpg"):
        return detect_text_in_image(file)
    elif filename.endswith("jpeg"):
        return detect_text_in_image(file)
    else:
        raise ValueError("Unsupported file")
