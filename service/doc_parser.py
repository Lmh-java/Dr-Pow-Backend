from docx import Document


# extract document content and return the string
def extract_doc_content(doc: Document) -> str:
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
