# data-ecosystems-project
DEGO 2606 Group Project – Credit Application Governance Analysis


# Credit Application Governance Analysis  
DEGO 2606 – Data Ecosystems and Governance in Organizations  

## Executive Summary

This project evaluates the data governance, fairness, and regulatory compliance of NovaCred’s credit approval system.

Our team conducted a structured audit of the credit application dataset to assess:

- Data quality and integrity  
- Potential algorithmic bias  
- Privacy and GDPR compliance risks  
- Governance control gaps  

From an original dataset of **502 credit applications**, 20 corrupted or invalid observations were removed. The validated dataset (`df_clean`) contains **482 observations** and is used for all subsequent analysis.

Preliminary findings indicate structural inconsistencies, sensitive data exposure risks, and potential regulatory concerns depending on fairness outcomes.

---

## Data Quality Assessment

### Dataset Overview

- Original dataset: 502 rows  
- Removed due to corruption/invalidity: 20 rows  
- Final validated dataset (`df_clean`): 482 rows  

All excluded records were isolated into a separate dataset (`df_flagged`), including a column specifying the reason for exclusion.

---

### Identified Issues

The following data quality issues were identified:

- Missing or empty fields (email, gender, date_of_birth)
- Inconsistent categorical encoding ("Male" vs "M", "Female" vs "F")
- Inconsistent date formats
- Structural inconsistencies in optional fields
- Extreme financial ratios (e.g., Debt-to-Income ratio of 1.85)

---

### Remediation Approach

The cleaning process included:

- Standardization of categorical variables  
- Date normalization  
- Validation rules for financial metrics  
- Removal of corrupt or incomplete records  
- Creation of:
  - `df_clean` → validated dataset for analysis  
  - `df_flagged` → excluded records with documented reasons  

All bias and compliance analysis is conducted using `df_clean`.

---

## Bias & Fairness Analysis

(Section to be completed after bias analysis.)

This section evaluates potential disparate impact in credit approval decisions.

The analysis includes:

- Approval rates by gender  
- Disparate Impact (DI) ratio calculation  
- Age-based approval patterns  
- Investigation of proxy variables (e.g., ZIP code)  

According to the four-fifths rule, a DI ratio below 0.8 indicates potential disparate impact and regulatory concern.

---

## Privacy & GDPR Assessment

The dataset contains multiple categories of Personally Identifiable Information (PII), including:

- Full name  
- Email address  
- Social Security Number (SSN)  
- IP address  
- Date of birth  
- ZIP code  

Key privacy risks identified:

- SSN stored in plaintext  
- No visible pseudonymization or encryption  
- No documented retention policy  
- No explicit consent tracking  
- No audit trail for automated decision logic  

Mapping to GDPR principles will be finalized after completion of the privacy analysis.

---

## Governance Recommendations

Preliminary governance recommendations include:

### Data Controls
- Standardized data dictionary  
- Automated validation rules  
- Defined financial threshold boundaries  

### Fairness Controls
- Ongoing disparate impact monitoring  
- Periodic fairness audits  
- Model transparency documentation  

### Privacy Controls
- Pseudonymization or tokenization of SSN  
- Encryption of sensitive PII  
- Defined data retention and deletion policies  
- Audit logging for decision explainability  

These measures would significantly reduce regulatory, reputational, and operational risk.