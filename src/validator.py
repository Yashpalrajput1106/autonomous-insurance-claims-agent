MANDATORY_FIELDS = [
    "policy_number",
    "policyholder_name",
    "incident_date",
    "incident_location",
    "claim_type",
    "estimated_damage"
]


def find_missing_fields(data):

    missing = []

    for field in MANDATORY_FIELDS:

        value = data.get(field)

        if value in [None, "", []]:
            missing.append(field)

    return missing