import fitz

def extract_pdf_text(pdf_path):

    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    return text


def extract_txt_text(txt_path):

    with open(txt_path, "r", encoding="utf-8") as f:
        return f.read()