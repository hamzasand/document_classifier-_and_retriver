import re

def extract_invoice(text):

    invoice_number = re.search(
        r'(?:Invoice\s*#?|INV[- ]?)([A-Za-z0-9-]+)',
        text,
        re.IGNORECASE
    )

    date = re.search(
        r'(\d{4}-\d{2}-\d{2})',
        text
    )

    company = re.search(
        r'Company:\s*(.+)',
        text,
        re.IGNORECASE
    )

    total_amount = re.search(
        r'Total(?:\s+Amount)?\s*:\s*\$?([\d,.]+)',
        text,
        re.IGNORECASE
    )

    return {
        "invoice_number": invoice_number.group(1) if invoice_number else None,
        "date": date.group(1) if date else None,
        "company": company.group(1).strip() if company else None,
        "total_amount": float(total_amount.group(1).replace(",", ""))
                        if total_amount else None
    }

def extract_resume(text):

    name = text.split('\n')[0]

    email = re.search(r'[\w\.-]+@[\w\.-]+', text)

    phone = re.search(r'(\+?\d[\d -]{8,}\d)', text)

    experience = re.search(r'(\d+)\+?\s+years', text.lower())

    return {
        "name": name,
        "email": email.group() if email else None,
        "phone": phone.group() if phone else None,
        "experience_years": experience.group(1) if experience else None
    }


def extract_utility_bill(text):

    account_number = re.search(r'Account Number[: ]+(\w+)', text)

    date = re.search(r'\d{4}-\d{2}-\d{2}', text)

    usage = re.search(r'(\d+)\s*kwh', text.lower())

    amount_due = re.search(r'Amount Due[: ]+\$?(\d+\.?\d*)', text)

    return {
        "account_number": account_number.group(1) if account_number else None,
        "date": date.group() if date else None,
        "usage_kwh": usage.group(1) if usage else None,
        "amount_due": amount_due.group(1) if amount_due else None
    }