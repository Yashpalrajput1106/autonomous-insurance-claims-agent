import json

from src.parser import parse_document
from src.extractor import extract_fields
from src.validator import find_missing_fields
from src.router import determine_route

def process_claim(file_path):

    text = parse_document(file_path)

    extracted = extract_fields(text)

    missing = find_missing_fields(extracted)

    route, reason = determine_route(
        extracted,
        missing
    )

    result = {
        "extractedFields": extracted,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }

    return result


if __name__ == "__main__":

    file_path = "data/claim1.pdf"
    # file_path = "data/claim_fraud.txt"
    # file_path = "data/claim_injury.txt"
    # file_path = "data/claim_missing.txt"


    result = process_claim(file_path)

    print(json.dumps(result, indent=4))

    # SAVE OUTPUT JSON
    with open("output/result.json", "w") as f:
        json.dump(result, f, indent=4)