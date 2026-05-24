def classify_document(text):

    text = text.lower()

    if "invoice" in text or "total amount" in text:
        return "Invoice"

    elif "resume" in text or "experience" in text:
        return "Resume"

    elif "kwh" in text or "amount due" in text:
        return "Utility Bill"

    elif len(text.strip()) < 20:
        return "Unclassifiable"

    return "Other"