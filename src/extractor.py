import re


def extract_fields(text):

    data = {}

    patterns = {
        "policy_number": r"Policy Number[:\-]?\s*(.+)",
        "policyholder_name": r"Policyholder Name[:\-]?\s*(.+)",
        "effective_dates": r"Effective Dates[:\-]?\s*(.+)",
        "incident_date": r"Incident Date[:\-]?\s*(.+)",
        "incident_time": r"Incident Time[:\-]?\s*(.+)",
        "incident_location": r"Location[:\-]?\s*(.+)",
        "incident_description": r"Incident Description[:\-]?\s*(.+)",
        "claimant": r"Claimant[:\-]?\s*(.+)",
        "third_parties": r"Third Parties[:\-]?\s*(.+)",
        "contact_details": r"Contact Details[:\-]?\s*(.+)",
        "asset_type": r"Asset Type[:\-]?\s*(.+)",
        "asset_id": r"Asset ID[:\-]?\s*(.+)",
        "claim_type": r"Claim Type[:\-]?\s*(.+)",
        "attachments": r"Attachments[:\-]?\s*(.+)",
        "initial_estimate": r"Initial Estimate[:\-]?\s*₹?([\d,]+)",
        "estimated_damage": r"Estimated Damage[:\-]?\s*₹?([\d,]+)"
    }

    for field, pattern in patterns.items():

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            value = match.group(1).strip()

            if field in ["estimated_damage", "initial_estimate"]:
                value = float(value.replace(",", ""))

            data[field] = value

        else:
            data[field] = None

    return data