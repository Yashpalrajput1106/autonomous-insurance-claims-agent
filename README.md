# Autonomous Insurance Claims Processing Agent

## Overview

This project is a lightweight AI-assisted insurance claims processing system designed to automate First Notice of Loss (FNOL) document handling.

The system:

- Extracts structured information from FNOL documents
- Detects missing mandatory fields
- Routes claims based on business rules
- Provides explainable routing decisions
- Outputs standardized JSON responses

Supported formats:
- TXT


---

# Features

## Document Parsing
- TXT document support
- PDF document support using `pdfplumber`

## Field Extraction

### Policy Information
- Policy Number
- Policyholder Name
- Effective Dates

### Incident Information
- Incident Date
- Incident Time
- Incident Location
- Incident Description

### Involved Parties
- Claimant
- Third Parties
- Contact Details

### Asset Details
- Asset Type
- Asset ID
- Estimated Damage

### Other Fields
- Claim Type
- Attachments
- Initial Estimate

---

# Routing Rules

| Condition | Route |
|---|---|
| Estimated damage < ₹25,000 | Fast-track |
| Missing mandatory fields | Manual Review |
| Description contains fraud keywords | Investigation Flag |
| Claim type = Injury | Specialist Queue |
| Otherwise | Standard Processing |

Fraud keywords:
- fraud
- inconsistent
- staged

---


# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd autonomous-insurance-claims-agent
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Project

Update the file path inside `src/main.py`:

```python
file_path = "data/claim_fasttrack.txt"
```

Run:

```bash
python -m src.main
```

---




# Technologies Used

- Python 3
- pdfplumber
- Regex
- JSON

---

# Design Approach

The project uses a hybrid rule-based architecture:

- Regex extraction for deterministic field extraction
- Validation layer for mandatory field checking
- Rule-based routing engine for explainable claim processing

This approach ensures:
- Simplicity
- Explainability
- Reliability
- Easy extensibility

---

# Future Improvements

Potential enhancements:

- OCR support for scanned PDFs
- OpenAI/LLM-powered extraction
- FastAPI REST API
- Streamlit dashboard
- Confidence scoring
- Database integration

---

# Author

Developed as part of an Autonomous Insurance Claims Processing Agent assessment project.