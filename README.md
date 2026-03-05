# Credit Application Governance Audit — NovaCred

## Executive Summary

This project conducts a governance audit of NovaCred’s automated credit application pipeline. The objective of the audit is to evaluate whether the data used in the credit decision process, as well as the resulting approval outcomes, meet key standards of **data integrity, algorithmic fairness, and data protection**.

Automated decision systems are increasingly used in financial services to assess loan applications and determine credit approval outcomes. Because these systems directly influence individuals’ access to financial resources, it is essential that they operate on reliable data, produce fair outcomes across demographic groups, and ensure that sensitive personal information is adequately protected.

The analysis conducted in this project reveals three key governance observations:

First, the raw dataset contained several data integrity issues, including duplicate identifiers, identity conflicts, missing critical attributes, and logically inconsistent financial values. These issues required a structured data quality remediation process before reliable analysis could be conducted.

Second, once the dataset was validated, the analysis of approval outcomes revealed disparities between demographic groups, particularly in relation to gender and age. These disparities indicate potential fairness risks that would require monitoring and governance oversight in a production decision system.

Third, the dataset contains multiple attributes that qualify as personally identifiable information, including direct identifiers and quasi-identifiers. Without appropriate safeguards, these attributes create re-identification risks. The project therefore demonstrates privacy-by-design techniques, including pseudonymisation and data minimisation, to reduce the exposure of sensitive personal data.

Overall, the project illustrates that effective governance of automated credit decision systems requires coordinated controls across **data quality management, fairness monitoring, and privacy protection mechanisms**.

---

# Project Context

Credit approval systems represent a high-impact application of data-driven decision making. These systems evaluate applicants based on demographic and financial attributes and produce outcomes that determine whether a loan is approved or rejected.

Because these decisions influence individuals’ economic opportunities, automated credit systems must be subject to robust governance practices. Poor data quality can lead to incorrect risk assessments, algorithmic models may unintentionally produce discriminatory outcomes, and the processing of personal data introduces significant privacy risks.

The objective of this project is therefore not to develop a predictive model but to perform a **governance audit of an existing credit decision dataset**. The analysis evaluates whether the dataset and approval outcomes exhibit risks related to data integrity, fairness, and privacy exposure.

The audit is structured around three analytical pillars:

- **Data Quality Assessment**
- **Algorithmic Fairness Analysis**
- **Privacy and Data Protection Evaluation**

Each component corresponds to one of the notebooks included in the repository.

---

# Data Quality Assessment

## Objective

The first stage of the project focused on validating the reliability of the dataset used in the credit decision pipeline. Data quality is a fundamental requirement for any analytical system, particularly when automated decisions affect individuals’ access to financial services.

If datasets contain inconsistencies, missing values, or logically invalid records, any subsequent analysis may produce misleading results. Therefore, before evaluating fairness or privacy concerns, it was necessary to audit the dataset and remove records that did not meet basic integrity standards.

The raw dataset initially contained **502 credit application records** with approximately **35 attributes describing each application**. These attributes included demographic information, financial variables, credit history indicators, and the final loan approval decision.

The goal of this stage was to identify integrity issues and produce a cleaned analytical dataset that could be reliably used in the fairness and privacy analyses.

---

## Data Integrity Checks

Several types of data integrity checks were applied during the cleaning process.

The first step was to identify **duplicate application identifiers**. Duplicate records can occur when the same application is submitted multiple times or when ingestion processes accidentally replicate entries. Duplicate IDs were detected and the redundant records were removed to ensure that each credit application was represented only once in the dataset.

The dataset was also examined for **identity collisions involving Social Security Numbers (SSNs)**. In a small number of cases, the same SSN appeared associated with different individuals. Because SSNs are intended to uniquely identify individuals, such collisions indicate severe data integrity issues. Records involved in these identity conflicts were removed from the dataset to preserve consistency.

Another critical validation step involved identifying **records missing key underwriting attributes**. Variables such as age and annual income are essential for evaluating credit risk. Applications missing these attributes cannot be meaningfully analysed and were therefore excluded from the cleaned dataset.

Finally, the dataset was examined for **logically inconsistent financial values**. Certain records contained financial attributes that were unrealistic or contradictory. Examples included negative savings balances, credit history durations inconsistent with applicant age, and financial behaviour that exceeded plausible income levels. These records were removed because they likely reflect data entry errors or corrupted entries.

---

## Data Standardisation

In addition to removing invalid records, several attributes required standardisation.

Categorical variables such as gender appeared under multiple formats and were normalised to a consistent representation. Date variables such as date of birth were also converted into a standardised date format to ensure consistency in downstream analyses.

These transformations ensured that the dataset had a consistent structure across all records.

---

## Cleaning Results

After applying the validation and remediation steps described above, the dataset was reduced from **502 records to 482 records**, meaning that **20 records were removed due to integrity issues**.

The removed records corresponded to several categories of problems:

- duplicate application identifiers  
- SSN identity collisions  
- missing key attributes such as age or income  
- logically inconsistent financial values  

The resulting dataset, referred to as **df_clean**, represents a validated analytical dataset that satisfies the defined quality standards. This dataset was then used as the input for the fairness and privacy analyses conducted in the subsequent stages of the project.

---

# Algorithmic Fairness Analysis

## Objective

Once a reliable dataset had been established, the next stage of the project focused on evaluating whether the credit approval outcomes exhibited patterns that may indicate algorithmic bias.

Algorithmic bias occurs when automated decision systems produce systematically different outcomes for different demographic groups. In credit approval contexts, such disparities can have significant social implications because they may restrict access to financial services for certain populations.

The fairness analysis therefore examined approval outcomes across demographic attributes contained within the dataset.

---

## Gender-Based Approval Analysis

The first stage of the fairness analysis examined approval rates across gender groups. The objective was to determine whether male and female applicants experienced different approval outcomes.

The analysis revealed a measurable difference in approval rates between the two groups. Female applicants were approved at a lower rate than male applicants. To quantify this difference, the analysis calculated **disparate impact**, a commonly used fairness metric that compares approval rates between demographic groups.

The results indicated that the ratio of approval rates fell below commonly used fairness thresholds, suggesting that female applicants experienced lower approval rates relative to male applicants.

Statistical testing confirmed that the relationship between gender and approval outcomes was statistically significant, indicating that the observed disparity is unlikely to be due to random variation in the dataset.

---

## Age-Based Approval Patterns

In addition to gender, the fairness analysis evaluated approval outcomes across different age groups. Applicants were grouped into age ranges to determine whether certain age segments systematically received higher or lower approval rates.

The analysis revealed variation across age groups, with some segments receiving substantially lower approval rates than others. This stage of the analysis helps identify whether certain demographic groups may be disproportionately affected by the credit decision process.

---

## Proxy Discrimination Analysis

Beyond direct demographic attributes, the analysis also investigated whether certain variables could function as **proxy variables** for demographic characteristics.

Proxy discrimination occurs when variables that appear neutral indirectly encode demographic information. Geographic attributes such as ZIP codes are a common example because they often correlate strongly with demographic composition.

The analysis examined the relationship between geographic variables, demographic composition, and approval outcomes. The results showed that certain geographic regions exhibited distinct demographic distributions and also displayed different approval rates.

These findings suggest that geographic variables could potentially act as proxy variables for demographic attributes, meaning that bias could persist even if demographic attributes were removed from the decision process.

---

## Financial Profile Comparison

To determine whether demographic disparities could be explained by differences in financial characteristics, the analysis compared financial attributes across demographic groups.

Variables such as income, savings balances, credit history length, and debt-to-income ratios were analysed to determine whether one group consistently displayed stronger financial profiles than another.

The analysis found that financial attributes alone did not fully explain the observed differences in approval outcomes. This suggests that demographic disparities may not simply reflect financial risk differences but may instead reflect patterns embedded in historical decision processes or correlations within the dataset.

---

# Privacy and Data Protection Assessment

## Objective

The final stage of the project evaluated the dataset from a privacy and data protection perspective.

The dataset contains several attributes that qualify as **personally identifiable information (PII)**. These attributes include direct identifiers such as Social Security Numbers, names, and email addresses, as well as quasi-identifiers such as date of birth, IP addresses, and ZIP codes.

The presence of these attributes introduces the risk that individuals could be re-identified if the dataset were shared or combined with external information.

---

## Identification of Sensitive Attributes

The first step of the privacy analysis involved identifying which variables represent direct identifiers and which represent quasi-identifiers.

Direct identifiers uniquely identify individuals on their own and therefore require the strongest protection. In this dataset, Social Security Numbers represent the most sensitive direct identifier.

Quasi-identifiers, such as birth date and geographic location, may not uniquely identify individuals individually but can enable re-identification when combined with other attributes.

Understanding these distinctions is essential for determining how the dataset should be protected.

---

## Pseudonymisation

To reduce the exposure of direct identifiers, the project demonstrates the use of **pseudonymisation**. Pseudonymisation replaces sensitive identifiers with cryptographic representations that cannot easily be reversed.

In the privacy notebook, Social Security Numbers are replaced with cryptographic hashes. This transformation allows the dataset to retain a consistent identifier for linking records while removing the original SSN values from the dataset.

After generating the pseudonymised identifier, the original SSN attribute is removed from the dataset.

---

## Data Minimisation

In addition to pseudonymisation, several **data minimisation techniques** were implemented.

Data minimisation is a key principle of modern data protection frameworks and involves limiting the amount of personal data processed to only what is necessary for the intended purpose.

Several attributes in the dataset contained more detailed information than required for analytical use. Exact birth dates were therefore converted into broader age ranges, IP addresses were partially masked to remove device-level precision, and ZIP codes were truncated to represent only coarse geographic regions.

These transformations reduce the risk of re-identification while preserving the analytical value of the dataset.

---

# Governance Implications

The findings of this audit highlight several governance challenges associated with automated credit decision systems.

First, the data quality analysis demonstrates that operational datasets frequently contain inconsistencies that must be addressed before reliable analysis can be performed. Automated validation mechanisms should therefore be implemented to ensure that only high-quality data enters analytical pipelines.

Second, the fairness analysis illustrates how automated decision systems may produce outcomes that disproportionately affect certain demographic groups. Organisations deploying such systems should implement monitoring mechanisms that regularly evaluate decision outcomes across demographic segments.

Third, the privacy assessment highlights the importance of protecting personal data within analytical datasets. Privacy-by-design principles should be applied throughout the data lifecycle to minimise exposure of sensitive identifiers.

Together, these findings demonstrate that responsible governance of automated decision systems requires coordinated controls addressing **data integrity, fairness monitoring, and privacy protection**.

---

# Conclusion

This project demonstrates how governance auditing techniques can be applied to evaluate automated decision systems used in credit approval contexts.

By examining NovaCred’s credit application dataset through the lenses of data quality, fairness, and privacy protection, the project provides a structured assessment of the governance risks associated with automated credit decision pipelines.

Ensuring responsible algorithmic decision systems requires reliable data, fair decision outcomes, and strong privacy protections. Integrating these elements into governance frameworks enables organisations to deploy automated decision systems in a responsible and trustworthy manner.

