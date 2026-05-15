import re


def extract_fields(text):

    data = {}

    patterns = {
        "policy_number": r"Policy Number[:\-]?\s*(.+)",
        "policyholder_name": r"Policyholder Name[:\-]?\s*(.+)",
        "incident_date": r"Incident Date[:\-]?\s*(.+)",
        "incident_time": r"Incident Time[:\-]?\s*(.+)",
        "incident_location": r"Location[:\-]?\s*(.+)",
        "claim_type": r"Claim Type[:\-]?\s*(.+)",
        "estimated_damage": r"Estimated Damage[:\-]?\s*₹?([\d,]+)"
    }

    for field, pattern in patterns.items():

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            value = match.group(1).strip()

            if field == "estimated_damage":
                value = float(value.replace(",", ""))

            data[field] = value

        else:
            data[field] = None

    return data