from pathlib import Path
import json

from extract_text import extract_pdf_text, extract_txt_text
from classifier import classify_document
from entity_extractor import (
    extract_invoice,
    extract_resume,
    extract_utility_bill
)

from retrieval import build_index, search


DATA_FOLDER = "data"


documents = []

results = {}


files = list(Path(DATA_FOLDER).glob("*"))


for file in files:

    print(f"Processing: {file.name}")

    if file.suffix.lower() == ".pdf":
        text = extract_pdf_text(file)

    elif file.suffix.lower() == ".txt":
        text = extract_txt_text(file)

    else:
        continue

    doc_class = classify_document(text)

    extracted_data = {"class": doc_class}

    if doc_class == "Invoice":
        extracted_data.update(extract_invoice(text))

    elif doc_class == "Resume":
        extracted_data.update(extract_resume(text))

    elif doc_class == "Utility Bill":
        extracted_data.update(extract_utility_bill(text))

    results[file.name] = extracted_data

    documents.append({
        "filename": file.name,
        "text": text
    })


with open("output/output.json", "w") as f:
    json.dump(results, f, indent=4)


print("\noutput.json created successfully")


# Semantic Search

index, embeddings = build_index(documents)


while True:

    query = input("\nEnter search query (or type exit): ")

    if query.lower() == "exit":
        break

    search_results = search(query, index, documents)

    print("\nRelevant Documents:")

    for result in search_results:
        print(result)