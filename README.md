# Data Quality Findings

## Dataset Overview

The original dataset contained **502 credit application records**.

Following a structured validation and cleaning process, **20 records were removed**, resulting in a curated dataset (`df_clean`) containing **482 validated observations**.

All removed observations were isolated into a separate dataset (`df_flagged`). Each flagged record includes a documented reason for exclusion to ensure auditability and transparency.

All subsequent fairness and compliance analysis is conducted exclusively on `df_clean`.

---

## Validation Framework Applied

The cleaning process followed a structured validation framework covering three primary dimensions:

1. Completeness  
2. Consistency  
3. Validity  

Each removed record failed at least one of these validation criteria.

---

## 1️⃣ Completeness Issues

Several records contained missing or empty mandatory fields required for credit decision assessment. These included:

- Missing email addresses  
- Missing gender values  
- Missing date of birth  
- Incomplete nested financial attributes  

Records with critical missing attributes were excluded because they compromise both analytical integrity and regulatory defensibility.

In a production credit system, incomplete personal or financial data would invalidate automated decision logic.

---

## 2️⃣ Consistency Issues

The dataset contained structural inconsistencies that required normalization.

Examples include:

- Gender encoded inconsistently ("Male", "M", "Female", "F")
- Multiple date format representations (YYYY-MM-DD, DD/MM/YYYY, etc.)
- Optional fields inconsistently present across records
- Schema irregularities in nested financial structures

While most consistency issues were corrected through standardization, records with irreparable structural inconsistencies were removed.

Inconsistent encoding poses risks for bias analysis, as fragmented categories can distort fairness metrics.

---

## 3️⃣ Validity Issues

Certain records contained values that violated logical or financial plausibility rules.

Examples include:

- Extreme Debt-to-Income (DTI) ratios (e.g., 1.85)
- Edge cases in credit history duration
- Financial ratios inconsistent with declared income levels

While extreme DTI values may occur under rare circumstances, the absence of formally defined validation thresholds represents a governance gap.

Records deemed financially invalid or logically inconsistent were removed to protect downstream analytical integrity.

---

## Governance Implications of Data Quality Findings

The data quality assessment revealed several governance concerns:

- Absence of formal validation thresholds for financial ratios  
- Lack of standardized categorical encoding rules  
- No documented data quality control framework  
- No automated anomaly detection process  

Although the dataset was remediated manually for analytical purposes, a production-grade credit approval system should include:

- Automated validation pipelines  
- Defined business rule boundaries  
- Structured exception handling  
- Continuous data quality monitoring  

Failure to implement such controls may expose NovaCred to operational and regulatory risk.

---

## Cleaning Outcome Summary

- 502 original records  
- 20 removed due to validation failures  
- 482 validated records retained  

The separation between `df_clean` and `df_flagged` ensures transparency, traceability, and reproducibility of the cleaning process.
