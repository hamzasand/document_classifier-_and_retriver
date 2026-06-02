import fitz

def extract_pdf_text(pdf_path):
    try:
        text = ""

        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text()

        return text

    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""


def extract_txt_text(txt_path):
    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        print(f"Error reading {txt_path}: {e}")
        return ""