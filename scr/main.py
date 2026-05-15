import json

from parser import parse_document
from extractor import extract_fields
from validator import find_missing_fields
from router import determine_route


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

    file_path = "../data/claim1.txt"

    result = process_claim(file_path)

    print(json.dumps(result, indent=4))