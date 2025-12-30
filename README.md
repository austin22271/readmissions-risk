# Hospital Readmissions Risk Tool

## Overview
This project is a rule-based Python tool designed to identify patients at higher risk of hospital readmission.  
It uses simple, explainable clinical and utilization factors to assign risk levels and provide transparent reasoning.

The goal of this tool is to support clinical decision-making and care coordination, not replace clinician judgment.

---

## How It Works
The model evaluates patients using the following factors:
- Age
- Prior hospital admissions
- Length of stay

Each factor contributes to a numeric risk score, which is then classified into:
- Low Risk
- Medium Risk
- High Risk

The tool also provides explanations for why a patient was flagged as higher risk.

---

## Example Output
For each patient, the tool prints:
- Risk classification
- Reasons for risk designation

It also produces summary metrics showing the distribution of risk across the patient population.

---

## How to Run
1. Ensure Python 3 is installed
2. Clone this repository
3. Run the script:

```bash
python readmissions_risk.py

Use Case

Hospitals can use this tool to:

Prioritize follow-up outreach for high-risk patients
