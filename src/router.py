FRAUD_KEYWORDS = [
    "fraud",
    "inconsistent",
    "staged"
]


def determine_route(data, missing_fields):

    description = (
        data.get("incident_description") or ""
    ).lower()

    claim_type = (
        data.get("claim_type") or ""
    ).lower()

    estimated_damage = data.get("estimated_damage")

    if any(word in description for word in FRAUD_KEYWORDS):

        return (
            "Investigation Flag",
            "Suspicious keywords found"
        )

    if missing_fields:

        return (
            "Manual Review",
            "Mandatory fields missing"
        )

    if claim_type == "injury":

        return (
            "Specialist Queue",
            "Injury claim detected"
        )

    if estimated_damage and estimated_damage < 25000:

        return (
            "Fast-track",
            "Damage below ₹25,000"
        )

    return (
        "Standard Processing",
        "No special conditions triggered"
    )