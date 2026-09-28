Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 1 of 32 
 
STATISTICAL ANALYSIS PLAN 
 
 
Study Title: A Randomized, Double-Blinded, Placebo-Controlled Study 
of the Effect of XmAb®5871 on Systemic Lupus 
Erythematosus Disease Activity 
  
Sponsor Xencor, Inc. 
 111 West Lemon Avenue 
 Monrovia, CA 91016 
  
  
Name of Test Drug: XmAb5871 
  
Protocol Number: XmAb5871-04 
  
Phase: Phase 2 
  
  
  
  
  
Analysis Plan Version Version 1.0 
  
Analysis Plan Date May 2, 2018 
  
 

Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 3 of 32 
TABLE OF CONTENTS 
Section Page 
1. INTRODUCTION ...............................................................................................................7 
2. OVERVIEW OF STUDY DESIGN ....................................................................................7 
2.1 Primary Objective ......................................................................................................10 
2.2 Secondary Objectives ................................................................................................10 
2.3 Exploratory Objectives ..............................................................................................10 
3. SAMPLE SIZE JUSTIFICATION ....................................................................................11 
4. RANDOMIZATION, BLINDING AND DROP OUTS ...................................................11 
5. DEFINITIONS OF PATIENT POPULATIONS TO BE 
ANALYZED ......................................................................................................................12 
5.1 Enrolled Population ...................................................................................................12 
5.2 Intent-to-Treat (ITT) Population ...............................................................................12 
5.3 Safety Population .......................................................................................................12 
5.4 Efficacy Evaluable Population ..................................................................................12 
5.5 Pharmacokinetic/Immunogenicity Population ..........................................................13 
5.6 Pharmacodynamic Population: ..................................................................................13 
6. DEFINITIONS, COMPUTATIONS, DATA CONVENTIONS .......................................13 
6.1 Definitions and Computations ...................................................................................13 
6.2 Conventions ...............................................................................................................14 
7. MISSING DATA AND DROPOUTS ...............................................................................15 
7.1 Partial/Missing Dates for Study-Related Visits or Procedures: ................................15 
7.2 Partial/Missing Dates for Adverse Events .................................................................15 
8. DESCRIPTION OF STATISTICAL ANALYSES ...........................................................16 
8.1 General Principles .....................................................................................................16 
8.2 Patient Enrollment, Disposition, Protocol Deviations ...............................................16 
8.3 Demographics and Baseline Characteristics .............................................................17 
8.4 Additional Baseline Characteristics ..........................................................................17 
8.5 Physical Examination and Medical History/Concurrent Illness ................................17 
8.6 Prior and Concomitant Therapy ................................................................................17 
8.7 Study Treatment Administration, Exposure and Procedure ......................................17 
8.8 Efficacy and Exploratory Analysis ............................................................................18 
8.8.1 Primary Efficacy Endpoint (Loss of Improvement at Day 225) .......................18 
8.8.2 Secondary Efficacy Endpoints ..........................................................................19 
8.8.3 Exploratory Efficacy Endpoints ........................................................................21 
8.9 Safety Analysis ..........................................................................................................21 
8.9.1 Treatment Emergent Adverse Events................................................................21 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 4 of 32 
8.9.2 Serious Adverse Events.....................................................................................22 
8.9.3 Adverse Events Leading to Discontinuation from Study ..................................22 
8.9.4 Deaths ................................................................................................................22 
8.9.5 Clinical Laboratory Tests ..................................................................................22 
8.9.6 Vital Signs .........................................................................................................24 
8.9.7 12-Lead Electrocardiogram ...............................................................................25 
8.10 Pharmacokinetics (PK) ..............................................................................................25 
8.11 Pharmacodynamics (PD) ...........................................................................................26 
8.12 Pharmacokinetic/Pharmacodynamic Analyses ..........................................................26 
8.13 Immunogenicity: Human Anti-Human Antibodies (AHA) .......................................26 
8.14 Pharmacogenomics ....................................................................................................26 
9. INTERIM ANALYSIS ......................................................................................................27 
10. TESTING/VALIDATION PLAN AND SOFTWARE SYSTEM ....................................27 
11. STATISTICAL ANALYSIS CHANGES FROM THE 
PROTOCOL ......................................................................................................................27 
12. REFERENCES ..................................................................................................................28 
13. SCHEDULE OF ASSESSMENTS ....................................................................................29 
APPENDIX 1.     IMPUTATION OF PARTIAL AND MISSING 
DATES ...............................................................................................................................31 
 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 5 of 32 
ABBREVIATIONS AND DEFINITIONS 
Ab Antibody 
ABC Absolute B cell count 
AE Adverse event 
ALT Alanine aminotransferase 
AP Alkaline phosphatase 
ATC Anatomical therapeutic chemical 
BILAG British Isles Lupus Activity Group (version BILAG2004) 
BMI Body Mass Index 
bpm Beats per minute 
BP Blood pressure 
BUN Blood urea nitrogen 
CI Confidence interval 
CPK Creatine phosphokinase 
CS Clinically significant 
CTCAE Common Terminology Criteria for Adverse Events 
CV Coefficient of variation 
DBP Diastolic blood pressure 
ECG Electrocardiogram 
eCRF Electronic Case Report Form  
EOI End of infusion 
EOS End-of-study 
FDA Food and Drug Administration 
FSH Follicle stimulating hormone 
Fv Antibody variable 
GCP Good Clinical Practices 
GGT Gamma-glutamyl transferase 
GI Gastrointestinal 
HAHA Human anti-human antibodies 
HBcAb Hepatitis B core antibody 
HBsAg Hepatitis B surface antigen 
HCV Hepatitis C virus 
HIV Human immunodeficiency virus 
HR Heart rate 
ICH International Committee for Harmonization 
Ig Immunoglobulin 
IP Investigational Product 
IQR Interquartile Range 
ITT Intent to Treat 
IU International units 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 6 of 32 
IV Intravenous 
K-M Kaplan-Meier 
LDH Lactate dehydrogenase 
mAb Monoclonal antibody 
mmHg Millimeters of mercury 
MedDRA Medical Dictionary for Regulatory Activities 
MTD Maximum tolerated dose 
NCS Not clinically significant 
PD Pharmacodynamic 
PGA Physician’s Global Assessment 
PK Pharmacokinetic 
PT Prothrombin time 
PPD Pharmaceutical Product Development (clinical research organization) 
PPT Partial Prothrombin time 
RI Responder Index 
RR Respiratory rate 
SAE Serious adverse event 
SAP Statistical Analysis Plan 
SAS Statistical Analysis Software 
SBP Systolic blood pressure 
SD Standard deviation  
SDS System Documentation Specifications  
SE Standard error of the mean 
SELENA 
SLEDAI 
SLE disease activity index as modified in the SELENA study 
SLE Systemic Lupus Erythematosus  
SOC System Organ Class 
TEAE Treatment-emergent adverse event 
ULN Upper limit of normal 
UNK Unknown 
VAS Visual Activity Scale 
WHO-DD World Health Organization - Drug Dictionary 
 
 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 7 of 32 
1. INTRODUCTION 
The Statistical Analysis Plan (SAP) describes the data analysis specifications for Xencor, Inc. 
protocol XmAb5871-04 titled: “A Randomized, Double-Blinded, Placebo-Controlled Study 
of the Effect of XmAb®5871 on Systemic Lupus Erythematosus Disease Activity”. It details 
the inferential statistical methodology to be used in analyzing study data and outlines the 
statistical programming specifications, tables, figures, and listings. It describes the variables 
and populations, anticipated data transformations and manipulations, and other details of the 
analyses not provided in the clinical study protocol. Additional purposes of the SAP are to 
serve as a communication tool between Vantage Data Designs, Inc. and Xencor, Inc. with 
respect to expected statistical data outputs after database lock and to allow SAS 
Programming of the tables, listings, figures to commence as early in the process as possible. 
This version of the statistical analysis plan was prepared in accordance with the protocol 
XmAb5871-04 Version 2.0 dated July 29, 2016. Other related documents are the electronic 
case report forms (eCRFs), eCRF completion guidelines (with screenshots) from PPD, and 
System Documentation Specifications (SDS) document from Medidata RAVE.  
This SAP supersedes the statistical considerations identified in the protocol. The SAP will be 
finalized prior to database lock and describes the statistical analysis as it is foreseen when the 
study is being planned. If circumstances should arise during the study rendering this analysis 
inappropriate, or if in the meantime improved methods of analysis should come to light, 
different analyses may be made. Any deviations from the SAP after database lock, reasons 
for such deviations and all alternatives or additional statistical analyses that may be 
performed, will be described in a SAP Addendum. 
2. OVERVIEW OF STUDY DESIGN 
Experimental Design: Phase 2, randomized, double-blind, placebo-controlled, multi-center 
study in patients with Systemic Lupus Erythematosus (SLE) Disease. 
Allocation of treatment: Two randomized treatment arms. Participants will receive either 5 
mg/kg XmAb5871 or placebo (1:1 treatment allocation) by IV infusion every other week for 
up to a total of 16 infusions. 
Number of patients planned: A total of approximately 90 patients will be enrolled in up to 25 
sites. Patients who are lost to follow up or withdraw consent for study participation prior to 
randomization and study drug administration may be replaced, at sponsor’s discretion. 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 8 of 32 
Treatment and Study Duration: After up to a 4-week screening period, participants will 
receive XmAb5871 or placebo by IV infusion every other week for up to a total of 16 doses 
(30 weeks) and will be followed for 6 weeks following the last dose for a total study period 
of up to 40 weeks. 
Study Procedures: Eligible patients must have moderate to severe, non-organ threatening, 
SLE activity defined as a SELENA SLEDAI of ≥6 (≥4 points of which must come from non-
serological findings) OR ≥1 BILAG B score OR ≥1 BILAG A score. Patients must be able 
and willing to discontinue background immunosuppressive medications and to receive a brief 
course of IM steroid therapy to enter screening. 
After obtaining informed consent, 160 mg of IM depomedrol will be administered and 
screening studies will be performed. Over the 2-4 week period following the initial IM 
depomedrol, per investigator discretion, patients may receive additional IM depomedrol (up 
to an additional 320 mg during screening) to treat their SLE symptoms to a target of disease 
activity improvement defined as a SELENA SLEDAI decrease of ≥4 points OR a decrease in 
BILAG of ≥1 severity grade in at least one organ system that began with A or B (clinical 
criteria without requiring temporal criteria). Immunosuppressive therapy will be stopped or 
tapered off over the 2-4 week screening period and must be discontinued by randomization 
on Day 1. Patients on anti-malarial therapy may continue on their usual dose. Patients 
entering the study on oral doses of ≤15 mg of prednisone per day (or the equivalent) will 
taper their oral steroids to 10 mg per day or less by randomization (Day 1) and then may 
continue on a ≤10 mg daily dose through the study. Patients who do not meet the disease 
activity improvement criteria during the 2-4 week screening period will not be randomized 
into the study and their participation will end. 
Patients must have documented disease activity improvement following the brief course of 
IM steroid therapy during the screening period to be randomized into the study on Day 1. 
Those patients who achieve the required disease activity improvement from the screening 
baseline will be randomized to receive either XmAb5871 (5 mg/kg) or matching placebo by 
IV administration (double-blinded) over 1-2 hours every 2 weeks from Day 1 through Day 
211 for a total of up to 16 infusions. Disease activity (SELENA SLEDAI, BILAG) on Day 1 
will be considered the baseline disease activity for determination of the efficacy endpoints. 
On Day 1, 80 mg of IM depomedrol will be administered and baseline procedures including 
physical exam, blood and urine samples for laboratory assessments, PK and PD samples will 
be performed. The first infusion of XmAb5871 or placebo will be given IV over a period of 2 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 9 of 32 
hours. Patients will be observed for at least 2 hours after completion of the first study drug 
administration during which time safety assessments will be performed. 
All patients will return to the research facility on Day 8 for safety, PK and PD assessments. 
On study Day 15, patients will receive 80 mg of IM depomedrol in addition to the procedures 
scheduled for that day and will receive the second IV infusion of XmAb5871 or placebo. 
Patients will return on study Days 29, 43, 57, 71, 85, 99, 113, 127, 141, 155, 169, 183, 197, 
and Day 211 for XmAb5871 or placebo administration IV over 1-2 hours and for safety, PK 
and PD assessments. Patients will be required to remain at the study site for observation for 
at least 1 hour after the completion of each infusion. 
Patients will be followed for the loss of disease activity improvement (LOI) as defined by: 
I. The assessment by the investigator that SLE disease activity is appropriate for an 
increase in therapy (including addition of another lupus therapy, except for 
adjustments in NSAIDs) AND 
II. There has been one of the following compared to baseline (Day 1): 
1) a SELENA SLEDAI increase of ≥4 points from maximal improvement OR 
2) a worsening of at least 1 BILAG A or B score OR 
3) the appearance of a new BILAG A or B score. 
Patients who meet the criteria for loss of disease activity improvement at any timepoint up to 
and including Day 211 will not receive further infusions of XmAb5871 or placebo and may 
receive any appropriate SLE therapy at the discretion of the principal investigator. 
The effect of XmAb5871 on loss of improvement of SLE disease activity will be evaluated 
as the percentage of patients without loss of disease activity improvement at Day 225 
(primary endpoint) and Day 169 (secondary endpoint). Patients with loss of disease activity 
improvement at any time-point up to and including Day 225 will be considered non-
responders for the primary endpoint. Patients who discontinue the study early either because 
of loss of improvement or for other reasons will be followed for a further period of 6 weeks 
after their last dose of XmAb5871 or placebo. 
All patients completing the treatment period should be followed through Day 253 (EOS). 
Patient participation is complete once EOS study procedures are performed. All AE(s) 
(including serious AEs and deaths) and use of concomitant medication information will be 
collected throughout the study from screening through the EOS visit. Patients developing 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 10 of 32 
treatment-emergent AEs (TEAEs) or clinically significant safety lab abnormalities will be 
followed until resolution or until the TEAEs/abnormalities are stabilized. 
Schedule of Assessments: The study consists of a Screening visit (Day -28 to Day -1) 
followed by sixteen infusions of XmAb5871 given every two weeks (Days 1, 15, 29, 43, 57, 
71, 85, 99, 113, 127, 141 155, 169, 183, 197, and Day 211) with collection of disease activity 
assessments, safety data, PK, and PD. Patients will be seen on Day 8 for safety monitoring, 
PK and PD and will be followed for 6 weeks after the final infusion (Days 225 and 253 
[EOS]). Patients who experience loss of disease activity improvement will have their study 
drug infusions discontinued and will receive appropriate SLE rescue therapy at the discretion 
of the principal investigator. The patient should be followed for an additional 6 weeks from 
the time of the last study drug infusion. Assessments listed for the Day 225 visit should be 
performed at the time of loss of disease activity improvement (LOI). Assessments listed for 
the Day 253 (EOS) visit should be performed at the follow-up visit 6 weeks from the time of 
the last study drug infusion. The maximal study duration for an individual patient will be 253 
days after the first infusion. 
Please see Section 13 of this SAP for the Schedule of Assessments. 
 Data collection: Electronic Case Report Form (eCRF) using Medidata RAVE platform and 
administered by PPD. 
2.1 Primary Objective 
To determine the ability of XmAb5871 to maintain SLE disease activity improvement 
achieved by a brief course of disease-suppressing intramuscular (IM) steroid therapy in SLE 
patients. 
2.2 Secondary Objectives 
• To evaluate time to loss of SLE disease activity improvement achieved by a brief 
course of disease-suppressing IM steroid therapy in SLE patients 
• To evaluate the safety and tolerability of every other week intravenous (IV) 
administration of XmAb5871 in patients with SLE 
• To evaluate the pharmacokinetics (PK) and immunogenicity of every other week IV 
administration of XmAb5871 in patients with SLE 
2.3 Exploratory Objectives 
To characterize the pharmacodynamics (PD) of every other week IV administration of 
XmAb5871 in patients with SLE as follows: 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 11 of 32 
• To evaluate the effect of XmAb5871 on changes in the absolute B Cell count (ABC) 
• To characterize the effect of XmAb5871 on SLE disease activity over time 
• To evaluate the effect of XmAb5871 on autoantibody, complement and cytokine 
levels 
3. SAMPLE SIZE JUSTIFICATION 
It is anticipated that approximately 90 patients will be enrolled in the study. Sample size is 
based on a previously completed study of SLE patients treated with IM depomedrol for 2 
weeks following cessation of background immunosuppressant therapy. In that study, by 
month 6, 40/41 patients lost the disease activity improvement achieved following IM steroid 
therapy; a 2.4% placebo response.  
Assuming a 10% placebo response (defined as no loss of disease activity improvement from 
Day 1 to Day 169) and a 38% response in the XmAb5871 treatment arm (i.e., a 28% delta 
between treatment arms), 40 patients per treatment arm will provide 80% power to detect this 
difference at alpha=0.05 (two-sided) by use of the Fishers exact test. Adding 10% for 
unevaluable patients, the total number per arm is calculated as 45. 
4. RANDOMIZATION, BLINDING AND DROP OUTS  
Approximately 90 patients will be randomized in a 1:1 treatment allocation scheme; 
therefore, 45 patients will be assigned to the XmAb5871 arm and 45 patients assigned to the 
placebo arm. There are no stratification factors planned for this randomization. A clinical 
research organization independent of the clinical trial team will develop the randomization 
schedule and the actual randomization assignment will be made through a secure Interactive 
Web-Based System (IWRS). 
After obtaining oral and written informed consent, patients will be screened according to the 
inclusion and exclusion criteria. The screening number will be used throughout the screening 
period. Patients who meet all selection criteria will then be randomized and receive a patient 
number on Day 1. The patient number will ensure identification throughout the study. 
The study will be conducted in a double-blind manner. All patients, investigators, and study 
staff/clinicians will be blinded to the study treatment assignment (XmAb5871 or Placebo) 
until the study is formally unblinded for data analysis purposes. The Sponsor’s team 
members responsible for study conduct and safety monitoring will also be blinded to study 
treatment. The randomization schedule will be held at an independent clinical research 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 12 of 32 
organization not affiliated with the study conduct and will only release the full randomization 
schedule after the database is formally locked for data analysis purposes.  
However, individual patient treatment assignment may be revealed due to the occurrence of a 
medical emergency requiring medical intervention or if the Medical Monitor for the study 
determines that patient safety requires knowledge of the study drug assignment. 
Documentation of the breaking of the randomization code, including the date and reason for 
such unblinding, must be documented in the EDC system. 
Patients dropping-out or withdrawing, for any reason, without completing all screening 
evaluations successfully, will be considered as “screening failures “. Such patients will not 
receive a patient number; however, screening data will be collected in the electronic Case 
Report Forms (eCRFs). The Investigator will keep a screening log of all patients screened to 
assess the numbers and characteristics of the excluded patients, and the reasons for their 
exclusion. 
5. DEFINITIONS OF PATIENT POPULATIONS TO BE ANALYZED 
5.1 Enrolled Population 
Defined as all patients who were enrolled in the study (signed informed consent, met 
inclusion and exclusion criteria and were randomized), whether or not the study drug was 
administered. 
5.2 Intent-to-Treat (ITT) Population 
Defined as all patients randomized and who have received at least a partial dose of 
XmAb5871 or placebo. 
5.3 Safety Population 
Defined as all patients who received at least a partial dose of XmAb5871 or placebo.  In this 
study, this is equivalent to the ITT population. 
5.4 Efficacy Evaluable Population 
Defined as all patients who: 
• Complete study through Day 225 assessments 
• Discontinue due to reaching the protocol specified LOI endpoint (and have not 
missed 2 or more consecutive doses prior to the LOI visit) 
• Discontinue due to drug-related adverse event (nonresponder) 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 13 of 32 
5.5 Pharmacokinetic/Immunogenicity Population 
The Pharmacokinetic population will include all patients with at least one pre-dose and one 
post-dose evaluable result reported.  All patients who received XmAb5871 and have at least 
1 post-IMP dosing ADA sample drawn will be included in the immunogenicity population. 
5.6 Pharmacodynamic Population:  
Defined as all patients who have received XmAb5871 and for whom the PD data are 
considered to be sufficient and interpretable will be analyzed in the PD analyses.   
6. DEFINITIONS, COMPUTATIONS, DATA CONVENTIONS 
6.1 Definitions and Computations 
Screening 
Screening is defined as Day -1 (Visit 1) prior to the first study drug administration.  
Baseline 
Baseline represents the procedures or assessments done prior to the first administration of 
XmAB5871 or placebo. Baseline could possibly be the screening visit under this definition.   
Visit Dates  
For ease of data analysis and summary table presentations, the nominal visit day 
nomenclature (see chart below) will be used. See Appendix 13 for more details.  
 
Study Phase Day 
  
Screening -1 
Treatment 1, 8, 15, 29, 43, 57, 71, 85, 99, 113, 127, 141, 155, 169, 
183, 197, 211 (last study drug administration) and 225 
End of Study 253 
  
 
Adverse Event (AE) 
AEs will be collected and recorded for each patient from the date the informed consent form 
(ICF) was signed (Screening) until the end of their participation in the study, i.e., the patient 
has discontinued or completed the study.  
The definitions of AE terms are guided by the United States Code of Federal Regulations (21 
CFR 312.32) and are included in Section 6.1.2.1 of the study protocol. Please use the study 
protocol if further information is needed.  
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 14 of 32 
Treatment Emergent Adverse Event (TEAE) 
Adverse medical events occurring after the Date of Informed Consent but before the first 
dose of study drug will be recorded as non-treatment emergent AEs on the AE case report 
form. AEs are considered “treatment-emergent” if the start date for a new event or a grade 
increase for an existing AE starts on or after the date of the first dose. 
Efficacy Endpoints 
The type, definition, and calculation of each of the efficacy endpoint are described in detail 
within Section 8.8 of this SAP.  
Safety Endpoints 
The type, variables collected, timepoints collected, and calculation of each of the safety 
endpoint are described in detail within Section 8.9 of this SAP.  
6.2 Conventions 
• 1 year = 365.25 days. Year is calculated as (days / 365.25) and will be rounded to 1 
digit after the decimal point (tenths) for presentation purposes. 
• 1 month = 30.4375 days. Month is calculated as (days / 30.4375) and will be rounded 
to 1 digit after the decimal point (tenths) for presentation purposes. 
• 1 pound = 0.454 kg and 1 kg = 2.2 pounds 
• 1 inch = 2.54 cm and 1 cm = 0.3937 inches 
• Body mass index (BMI) calculated as [weight (lbs) / height (in)2] x 703 
• BMI using metric system: [weight (kg) / [height (m)]2 
• Age will be calculated in years relative to the date of study consent based on the 
following SAS statement: Age = ([Consent Date - Date of Birth] / 365.25) and will be 
rounded down to the nearest integer for presentation purposes. 
• Investigational Product (Study Drug) is XmAb5871 and Comparator Product is 
Placebo. 
• Unless otherwise specified, percentages will be calculated based on the number of 
patients specified by the appropriate population definition. 
• The software used for all summary statistics and statistical analyses will be SAS 
Version 9.4 or later. 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 15 of 32 
• All tables, listings, figures will be produced in landscape orientation using Times 
New Roman 9-point font. Output files will be created in rich text file (RTF) format.  
• Missing or invalid data will be generally treated as missing, not imputed, unless 
otherwise stated (see Section 7).  
7. MISSING DATA AND DROPOUTS 
The issue of how to handle missing data caused by dropouts in clinical studies is a research 
topic that is still under development in the statistical literature. As has been noted in the ICH-
E9 guideline, “no universally applicable method of handling missing values can be 
recommended”. The best approach is to minimize the chance of missing data / dropouts at the 
design stage of the clinical study and during study monitoring.  
In general, data will be analyzed as received from the clinical database. Hence, missing 
values will not be imputed except for the following situations: 
7.1 Partial/Missing Dates for Study-Related Visits or Procedures: 
It is anticipated that all study-related visit and procedure dates entered into the clinical study 
database will be complete (i.e. day, month, year are all recorded) and accurate. Any missing 
or partially missing date of this type will be queried before statistical analyses are performed. 
If the day, month, and/or year are still unknown, then the dates will be imputed as follows for 
purposes of analysis: 
•  If the day of the visit or procedure date is missing, then take the previous visit and 
add the number of days to the next visit according to the visit schedule.  
•  If the month of the visit or procedure date is missing then take the previous visit and 
add the number of months to the next visit according to the visit schedule. 
•  If the year of the visit or procedure date is missing, then the year will be queried. If 
the year is unknown, no imputation of year will take place.  
 Imputed dates will be noted in the patient data listings.   
7.2 Partial/Missing Dates for Adverse Events 
Rules for imputing partial/Missing dates are detailed in Appendix 1.  
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 16 of 32 
8. DESCRIPTION OF STATISTICAL ANALYSES 
8.1 General Principles 
Unless otherwise noted, data will be summarized in tabular format by XmAb5871 or Placebo 
treatment group using summary tables and data listings. For this Phase 2 study, a patient who 
is enrolled but does not receive study drug will be excluded from the data summary tables. 
Data summaries will only include patients that receive study drug. All study data documented 
on the eCRFs will be included in the study data listings. 
Given this is a randomized placebo-control study; inferential statistical methodologies are 
planned and any statistical tests are utilized they will be two-sided, with type 1 error rate of 
5%.  All confidence intervals (if constructed) will be constructed at the 95% confidence 
level. No p-value adjustments on the secondary efficacy endpoints for multiplicity analyses 
will be made. 
Data will be summarized with respect to enrollment and disposition summaries, 
demographics and baseline characteristics, concomitant medications, efficacy, and safety 
measures. Summary (i.e. descriptive) statistics will include N, mean, standard deviation, 
median, range (minimum, maximum) values for continuous variables and frequencies, and 
percentages for categorical variables.  Time-to-event analyses will be summarized using 
Kaplan-Meier survival analysis and figures for the estimated median time. 
Missing or invalid data will be generally treated as missing, not imputed, unless otherwise 
stated (see Section 7).  
8.2 Patient Enrollment, Disposition, Protocol Deviations  
• Patient enrollment by site along with number of patients evaluable for safety, ITT, 
evaluable for efficacy populations will be tabulated.  
• The number of patients completing the study and number withdrawing the study with 
the primary reason for withdrawal (Loss of Improvement, AE, physician 
recommendation, withdrew consent, lost to follow-up, or other reasons) will be 
tabulated. 
• A protocol deviation is any noncompliance with the clinical trial protocol or Good 
Clinical Practice (GCP). The noncompliance may be either on the part of the patient, 
the investigator, or the study site staff. Since protocol deviations are not part of the 
eCRF database, they will be identified and documented by Xencor study 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 17 of 32 
monitors/project manager based on a review of data listings prior to database lock. 
Protocol deviations will be listed.  
8.3 Demographics and Baseline Characteristics 
A summary of age, gender, race, ethnicity, height, weight, and BMI will be presented using 
appropriate descriptive statistics. 
The categorical (discrete) variables will be summarized using counts and percentages. The 
continuous variables will be summarized using mean, median, standard deviation, and range 
(maximum, minimum). These summaries will include patients in the ITT population. 
8.4 Additional Baseline Characteristics 
The time (months) from date of diagnosis of Lupus disease to randomization date and 
depomedrol administration / dose amount will be summarized using descriptive statistics. 
SLE associated symptoms will be recorded in SLEDAI and BILAG worksheets and these 
baseline characteristics will be presented in the corresponding efficacy tables. 
Pharmacogenomics and FSH will also be summarized with baseline characteristics. 
8.5 Physical Examination and Medical History/Concurrent Illness  
All Physical Exam and Medical History/Concurrent Illnesses data will be presented in patient 
listings. 
8.6 Prior and Concomitant Therapy  
All medications taken before a patient’s first dose will be reported as prior medications in 
patient listings. All medications taken since the time of first dose until the end of the study 
will be classified as concomitant medications. These medications will be coded using WHO 
Drug Dictionary (WHODD), version 201509.  The number and proportion of patients in the 
Safety population using concomitant medications will be tabulated and summarized in a table 
by WHODrug anatomical class (ATC) and preferred drug name. These data will also be 
presented in patient listings.  
8.7 Study Treatment Administration, Exposure and Procedure 
There are sixteen infusions of XmAb5871 (or placebo) planned every two weeks (Days 1, 15, 
29, 43, 57, 71, 85, 99, 113, 127, 141, 155, 169, 183, 197, and 211).  
Exposure to study treatment (XmAB5871 or placebo) will be demonstrated by calculating the 
days of exposure (date of first dose of study drug to the last dose date of study treatment) and 
the number of infusions. These will be tabulated using descriptive statistics. 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 18 of 32 
Study treatment administration procedure will be described by “Was Study Drug 
Administered” (Yes/No), “Was Infusion Completed” (Yes/No), and “Was Study Drug 
Administration Interrupted” (Yes/No) for each visit study treatment was administered.  
Patient listings will be prepared showing the patient number, whether or not drug was 
administered at that specific visit, reasons why not, lot number, date and time of dose 
administration, planned volume/dose, actual total volume/dose administered, dose 
interruptions, dose restart, and reason for dose interruption. 
8.8 Efficacy and Exploratory Analysis 
Efficacy analyses will be performed on the Efficacy Evaluable and ITT Populations. The 
Efficacy Evaluable will serve as the primary population for all efficacy analyses and the ITT 
will be conducted for sensitivity analysis purposes.  
Efficacy parameters: SELENA SLEDAI, BILAG 2004, and Physician’s Global Assessment 
(PGA) will be collected at Screening, Days 1, 29, 57, 85, 113, 141, 169, 197, 225 and 253. 
8.8.1 Primary Efficacy Endpoint (Loss of Improvement at Day 225) 
The primary endpoint will be evaluated as the percentage of SLE patients without loss of 
disease activity improvement from Day 1 to Day 225 (i.e., responders). Loss of improvement 
will be  defined as worsening of dis ease activity that in the opinion of the principal 
investigator requires a change in treatment (exclusive of a decrease in oral steroids) AND one 
of: 
1) SELENA- SLEDAI increase of ≥4 points from maximal improvement OR 
2) Worsening of at least 1 BILAG A or B score OR 
3) New BILAG A or B score. 
The LOI parameter will be taken directly from the eCRF (Form Name: Loss of Improvement, 
Variable Name: LOIMPR, where LOIMPR=Yes, and LOI date variable = LOIMDAT. 
The number of “responders” will be presented as frequenc y counts and percentages by 
treatment arm. The primary efficacy analysis will test the hypothesis of equal response rates 
using Barnard’s Unconditional Exact Test as implemented in the EXACT statement of PROC 
FREQ in SAS 9.4, with rows corresponding to tre atment arms and columns corresponding to 
binomial response indicators . An exact confidence interval for the difference in response 
rates will be computed using the RISKDIFF(METHOD=SCORE) option . In addition, e xact 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 19 of 32 
confidence intervals will be provided for each treatment’s response rate based on the 
Clopper-Pearson method. 
Similar analysis will be conducted on the ITT population as a sensitivity analysis.  
8.8.2 Secondary Efficacy Endpoints  
• The percentage of SLE patients without loss of disease activity improveme nt from Day 1 
to Day 169 (i.e., res ponders) will be evaluated as described in the primary endpoint 
analysis (above) on both the efficacy evaluable and ITT populations (sensitivity).  
• The time to loss of SLE disease activity improvement achieved by a short period of IM 
steroid therapy in SLE patients. The time to loss of SLE disease activity improvement 
will be calculated from date of randomization to the date loss of improvement is first 
achieved. This endpoint will be summarized by treatment arm using Kaplan -Meier 
methods (median, 95% CI, number of events, number censored, etc.) and Kaplan- Meier 
plots. The log -rank test will be used to test for treatment group differences.  Similar 
analysis will be conducted on the ITT population as a sensitivity analysis.  
Patients who discontinue treatment early will be censored at their last assessment date 
that occured within 4 weeks of their final dose , whichever comes first . Patients who 
complete the study with no observed LOI will be censored at day 225. 
• Multivariate a nalysis: Cox proportional hazards regression will be used to explore the 
potential effects of pre -specified prognostic factors on time to loss of SLE disease 
activity improvement. The adjusted hazard ratios for treatment versus placebo and 
covariates will be estimated, together with 95% CIs. A pre-specified analysis will employ 
a forward, then backward stepwise approach. In the forward step, prognostic factors will 
be added in the order specified below  in Section 8.8.2.1 (excepting those for which other 
handling is described for the factor) , with retention of those factors for which the Wald 
test P ≤ 0.10.  After  all factors have been tested in dividually in sequential  order, the 
resulting multivariate model will be evaluated with a backwards s tepwise procedu re. 
Those factors with P > 0.20 in the full model will be removed in order of largest p- value 
until all final factors have P ≤ 0.20.  This final model will be summarized in a table and a 
forest plot. The analysis will be performed on the ITT population only. Patients who 
discontinue treatment early will be censored at their last assessment date that occured 
within 4 weeks of their final dose. Patients who complete the study with no observed LOI 
will be censored at D ay 225. Additional exploratory multivariat e proportional hazards 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 20 of 32 
analyses may be performed , for example,  to assess treatment effect modification by 
subgroups (i.e. modeled either as post-hoc stratifications or interactions).  
8.8.2.1 Pre-specified Prognostic Factors 
1) BILAG Total Score at screening and change in BILAG total score from Screening 
visit to Day 1 dosing visit. Stepwise procedures will test these two factors together 
using a likelihood ratio test instead of individually using Wald tests. 
2) BILAG number of A and B scores at screening and change in number of A and B 
scores from Screening visit to Day 1 dosing visit. Stepwise procedures will test these 
two factors together using a likelihood ratio test instead of individually using Wald 
tests. 
3) SELENA SLEDAI Score at screening and change in SELENA SLEDAI Score from 
Screening visit to Day 1 dosing visit. Stepwise procedures will test these two factors 
together using a likelihood ratio test instead of individually using Wald tests. 
4) Physician’s Global Disease activity VAS at screening and change in the VAS from 
Screening visit to Day 1 dosing visit. Stepwise procedures will test these two factors 
together using a likelihood ratio test instead of individually using Wald tests. 
5) Total Depomedrol dose, including screening doses and Day 1 and 15 doses 
6) Daily Prednisone dose at Day 1 
7) FcγRIIa R131H Polymorphism 
8) FcγRIIb I232T Polymorphism 
9) BMI at baseline 
10) Study day of first noncompliant steroid use at any time on study prior to LOI (i.e. 
time-varying covariate), as assessed by the Sponsor’s medical monitor. Patients in 
this group may also be excluded from an exploratory sensitivity analysis or, 
alternatively, censored at the date of first noncompliant steroid use. 
11) Study day of any non-protocol SLE therapy in the absence of an earlier LOI 
determination. Patients with non-missing values for this factor will be evaluated for 
informative censoring in a sensitivity analysis using a proportional hazards model 
with censoring times replaced by LOI events at the start of non-protocol therapy. This 
analysis may not be reported in the CSR if the treatment effect estimate changes less 
than 10% and statistical significance conclusions are unaffected.  
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 21 of 32 
8.8.3 Exploratory Efficacy Endpoints  
The following disease assessment indices will be used for exploratory analyses of disease 
activity over time: 
• Physician’s Global Assessment (PGA) VAS 
• SELENA SLEDAI hybrid version with SELENA SLEDAI Flare index 
• BILAG 2004 
The PGA, SLEDAI, and BILAG will be summarized by treatment arm at each visit using 
descriptive statistics (N, mean, standard deviation, median, minimum/maximum). Change 
from baseline will also be tabulated at each visit using the same descriptive statistics. 
Categorical variables will be presented as frequency counts and percentages. These 
exploratory endpoints will be evaluated on both the efficacy evaluable and ITT populations 
(sensitivity). 
8.9 Safety Analysis 
Safety Population is defined as all patients who received at least a partial dose of XmAb5871 
or Placebo and will be utilized for all safety analyses. In this study the Safety Population is 
equivalent to the ITT population. 
8.9.1 Treatment Emergent Adverse Events  
All AEs reported before a patient’s first dose will be reported as non-treatment adverse 
events in patient listings. All medications taken since the time of first dose until the end of 
the study will be classified as TEAEs.  
All Treatment Emergent Adverse Events (TEAEs) will be listed, documenting all 
information collected on the eCRF.   
Verbatim terms of TEAEs will be mapped to preferred terms and related system organ 
classes (SOC) using the Medical Dictionary for Regulatory Activities (MedDRA) Version 
19.0. 
Tables will summarize the number and percentage of patients having a TEAE in each system 
organ class and preferred term. Further tables will summarize the number and percentage of 
patients having TEAE, classified according event intensity (severity graded 1-5 according to 
CTCAE v4.03) and the number and percentage of patients with” related” events.  
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 22 of 32 
• ‘Related’ includes events where the relationship to the study drug was reported as 
‘Possibly Related’, ‘Probably Related’, and ‘Definitively Related’ or where the 
relationship was not reported on the CRF.  
• ‘Not Related’ are events reported as ‘Not Related ‘and ‘Unlikely Related’ on the 
CRF. 
The order of SOCs presented in tables will be according to the internationally agreed order of 
SOCs according to MedDRA. Within each SOC, the preferred terms will be shown in 
alphabetic order. 
Note: Patients who have multiple events in the same SOC and/or preferred term will be 
counted only once at each level of summation (overall, by SOC, and by preferred term) in the 
tables. For summaries of AEs by severity, only the highest severity of AE will be counted at 
each level of summation (overall, by SOC, and by preferred term) in the tables. For 
summaries of related AEs, patients with more than one related AE will be counted only once 
at each level of summation (overall, by SOC, and by preferred term) in the tables.  
8.9.2 Serious Adverse Events  
A listing of patients who reported a serious adverse event will be included. The data will be 
obtained from the AE dataset where the AESAE=Yes for that specific adverse event. 
8.9.3 Adverse Events Leading to Discontinuation from Study 
A listing of patients and the adverse events which led to study discontinuation from the study 
will be included.  The data will be obtained from the AE dataset where AEDISC=Yes.  
Additionally, AEs will be identified from the EOS dataset where the primary reason for 
treatment termination is checked as an Adverse Event.  These two datasets will be reconciled 
prior to database lock.  
8.9.4 Deaths  
A listing of patients who died on study will be included. Any associated AE will be identified 
from the AE dataset where AEDEATH box is checked.  
8.9.5 Clinical Laboratory Tests  
Hematology: The following hematology parameters will be assessed at Screening and at 
Days 1, 8, 15, 29, 43, 57, 71, 85, 99, 113, 127, 141, 155, 169, 183, 197, 211, 225 and 253 
(EOS): hemoglobin, hematocrit, red blood cell count, white blood cell count with differential 
(% and derived absolute values), mean corpuscular volume, mean corpuscular hemoglobin, 
mean corpuscular hemoglobin concentration, and absolute platelet count. 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 23 of 32 
Clinical chemistry: The following clinical chemistry parameters will be assessed at Screening 
and at Days 1, 8, 29, 57, 85, 113, 141, 169, 197, 225 and 253 (EOS): total protein, sodium, 
potassium, calcium, chloride, bicarbonate (HCO3), inorganic phosphate, albumin, glucose, 
blood urea nitrogen (BUN), creatinine, uric acid, bilirubin, alkaline phosphatase (AP), 
aspartate aminotransferase (AST), alanine aminotransferase (ALT), gamma-glutamyl 
transferase (GGT), lactate dehydrogenase (LDH), creatine phosphokinase (CPK), amylase, 
and lipase. 
Urinalysis: The following urinalysis parameters will be assessed at Screening, and on Days 1, 
29, 57, 85, 113, 141, 169, 197, 225, and 253 (EOS): pH, glucose, ketones, specific gravity, 
nitrite, protein, bilirubin, urobilinogen, leukocytes and blood. Microscopic urinalysis will be 
performed if urinalysis results are abnormal. A spot urine protein/creatinine ratio will be 
performed for urine dipstick of 2+ or greater protein. 
Coagulation: The following coagulation parameters will be assessed on Screening, and Days 
1, 29, 85, 141,197, and 253 (EOS): international normalized ratio (INR), prothrombin time 
(PT), and activated partial thromboplastin time (aPTT). 
Immunoglobulin: Serum IgG, IgE, and IgM will be assessed at Screening and on Days 1, 15, 
71, 127, 155, 183, 211, and 253 (EOS).  
Complement levels: C3 and C4 levels will be assessed at Screening and on Days 1, 29, 57, 
85, 113, 141, 169, 197, 225, and 253 (EOS).  
Shift tables (shift from baseline grade to maximum (and minimum) post-dose grade) will be 
presented for chemistry, hematology, and coagulation tests.  
Summary statistics (n, mean, SD, min, max) will be utilized to characterize immunoglobulins 
and complement levels and will be presented by Visit and Timepoint.  Corresponding change 
from baseline and percent change from baseline will also be presented for immunoglobulins 
and complement levels 
Urinalysis parameters will be presented in patient listings.  
The results from urine Pregnancy tests (Screening, Days 1, 15, 43, 71, 99, 127, 155, 183, 
211, and 253), Follicle Stimulating Hormone (assessed at Screening only), and Serology 
(assessed at Screening only: HBsAg, HBcAb, and HCV Ab) will be presented in patient 
listings.  
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 24 of 32 
Individual patient data listings of all chemistry, hematology, coagulation, urinalysis, serum 
immunoglobulins and complement (C3 and C4) results will be presented by patient and time 
point.   
All values outside the clinical reference ranges will be flagged in the data listings.  The 
abnormal values will be flagged with ‘Low’ for values below the lower limit of the clinical 
reference range and ‘High’ for values above the upper limit of the clinical reference range 
and included in the listings.  The investigator or designee will assess whether the values 
outside the clinical reference range are clinically significant and these will be reported as 
abnormal not clinically significant (NCS) or abnormal clinically significant (CS).  Clinically 
significant laboratory and that are not explained by the patient’s underlying disease or 
medications should be entered as AEs and the relationship to study drug assigned. Additional 
testing during the study may be done if medically indicated. The study patient will be 
followed until the test(s) has (have) normalized or stabilized. 
8.9.6 Vital Signs  
Vital signs will be assessed at Screening and on Days 1, 8, 15, 29, 43, 57, 71, 85, 99, 113, 
127, 141, 155, 169, 183, 197, 211, 225, and 253 (EOS). On Day 1, vital sign assessments will 
be made immediately prior to infusion, 15, 30, 60, and 120 minutes after the start of the 
infusion (±5 minutes), immediately before the EOI (if different than 120 minutes from start 
of infusion), and at 15, 30, 60 and 120 minutes after EOI. During subsequent infusions, vital 
signs will be measured immediately prior to infusion, 30 and 60 minutes after the start of the 
infusion (±5 minutes), immediately before the EOI (if different than 60 minutes from start of 
infusion), and at 30 and 60 minutes after EOI. On non-dosing days vital signs should be 
measured prior to blood sampling. During the infusion of XmAb5871, vital signs will be 
obtained in the semi-supine siting position. The following vital signs will be measured:  
• Blood pressure (systolic and diastolic [mmHg]);  
• Heart rate (beats per minute [bpm]);  
• Oral body temperature (°C);  
• Respiratory rate (breaths per minute).  
• Supine BP and heart rate recordings will be made after the study patient has been 
recumbent and at rest >= 5 minutes. 
Vital sign variables will be summarized in a descriptive manner by calculating the observed 
mean, standard deviation, median, and range at baseline and at each post-baseline 
measurement. Mean change and mean percent change from baseline will also be presented. 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 25 of 32 
All vital sign tests will be included in by-patient listings for further medical review. 
8.9.7 12-Lead Electrocardiogram 
Standard safety 12-lead ECGs will be performed at Screening and on Days 1, 29, 127, 183, 
and 253 (EOS). On Day 1, supine ECGs will be performed immediately prior to the infusion 
and 2 hours after EOI. On all other visit days, ECGs will be performed only pre-dose.  
The 12-lead ECGs will be performed after the patient has been resting supine for ≥ 5 
minutes. The following ECG parameters will be collected: PR interval, QRS interval, RR 
interval, QT interval, and QTc interval (QTcB and QTcF).  
Each ECG parameter will be summarized in a descriptive manner by calculating the observed 
mean, standard deviation, median, and range at baseline and at each post-baseline 
measurement. Mean change and mean percent change from baseline will also be presented.  
QTcB and QTcF values will be categorized according to their values into the categories 
• ≤ 430 ms 
• 430 – 450 ms 
• 450 – 480 ms 
• 480 – 500 ms 
• 500 ms  
and categorized according to their change from baseline into the categories 
• ≤ 30 ms, 
• 30 – 60 ms  
• 60 ms  
The categories described above will be summarized in frequency tables using number of 
patients (n) and percentages. 
All ECGs must be evaluated by a qualified physician for the presence of abnormalities.   
8.10 Pharmacokinetics (PK) 
XmAb5871 pharmacokinetic visit, scheduled time point, sampling dates/times will be listed 
by patient. The individual patient pre -dose (trough) and end -of-infusion (peak) 
concentration-time data will be listed and displayed graphically on the linear and log scales. 
The concentration -time data will be summarized descriptively in tabular and graphical 
formats (linear and log scales). 
PK data analysis will be undertaken by a PK consultant.  
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 26 of 32 
8.11 Pharmacodynamics (PD) 
All observed Pharmacodynamics data collection date/times will be provided in patient listings.  
PD of XmAb5871 will be evaluated by absolute B cell counts (ABC) and B cell subsets, and 
CD19 receptor occupancy (RO).   
Flow Cytometry B Cell and T Cell Assessment:  
• CD20+ B cells and T cells will be quantified at Screening and on Days 1, 8, 15, 29, 
57, 85, 113, 141, 169, 197, 225, and 253 (EOS).  
• CD19 RO (as CD19+ geometric mean of all  CD20+ [MFI]) and B cell subsets 
(CD20+, CD20+/IgD+CD27- , CD20+/IgD+CD27+, CD20+/IgD -CD27+-, 
CD20+/IgD-CD27-) will be quantified at Screening and on Days 1, 8, 15,  29, 57, 85, 
113, 141, 169, 197, 225, and 253 (EOS). 
All observed PD data and change from bas eline data will be summarized using descriptive 
statistics and will be listed and summarized in tabular and/or graphical form. Descriptive 
statistics on continuous data will include mean, median, standard deviation, and range, while 
categorical data may be summarized using frequency counts and percentages. 
PD data will be analyzed by an appropriate expert consultant in this field. 
8.12 Pharmacokinetic/Pharmacodynamic Analyses 
Individual and mean peak and trough serum concentrations of XmAb5871 will be 
summarized in tabular form and  plotted versus time on dual y -axis plots along with 
biomarkers CD19 RO and ABC % change from baseline.  
The peak and trough serum concentrations of XmAb5871 will be examined by FcγRIIa 
R131H and FcγRIIb I232T polymorphisms to determine if these genetic characteristics affect 
pharmacokinetics. 
8.13 Immunogenicity: Human Anti-Human Antibodies (AHA) 
The presence of human anti-human antibodies (ADA) will be assessed on Days 1, 15, 43, 85, 
127, 183, 225, and 253 (EOS). Frequency and titer of anti-XmAb5871 antibodies (ADA) will 
be listed. 
8.14 Pharmacogenomics  
The date/time (if not done, reason why) and result of the pharmacoge nomics evaluation 
(FcγR genotype testing: FcγRIIa R131H and FcγRIIb I232T polymorphisms) will be listed 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 27 of 32 
by patient. Polymorphism frequencies will be tabulated along with the baseline 
characteristics.   
Where patients provided informed consent, the residual FcγR polymorphism sample was 
retained by Xencor or Xencor’s designee for future exploratory genotyping research. 
Samples are to be maintained for no more than 15 years before destruction. Samples are to be 
stored at Cancer Genetics Inc. 
9. INTERIM ANALYSIS 
No formal efficacy interim analyses are planned; however aggregate blinded interim safety 
reviews will be performed for submission to regulatory authorities. The blinded aggregate safety 
information will be reviewed by a Safety Review Committee (SRC) after 15 patients have 
completed the study, after 45 patients have completed the study, and after 75 patients have 
completed the study. The SRC will consist of, at a minimum, the coordinating investigator and 
the medical representatives of the Sponsor (Xencor) and the CRO (PPD). The principal 
investigators and/or their delegates from each actively enrolling investigational site will be 
allowed to participate. All patients in the study will receive appropriate SLE rescue therapy at the 
discretion of the principal investigator and discontinue study drug infusions at the time of loss of 
disease activity improvement, however the SRC may request an unblinded review of safety data 
by an independent review committee should there be a trend in either an increase frequency of 
early SLE disease flares or the occurrence of organ-threatening SLE disease flares.  
A Safety Review Charter will be developed and implemented prior to the first safety review 
meeting. 
10. TESTING/VALIDATION PLAN AND SOFTWARE SYSTEM 
Statistical Analysis Software (SAS) version 9.4 or later will be used to analyze the data, 
create summary tables, patient data listings, and graphical representation of the data. All SAS 
programs will be validated using industry standard validation procedures. 
11. STATISTICAL ANALYSIS CHANGES FROM THE PROTOCOL 
The analyses described are based on the final clinical study protocol XmAb5871-04 Version 
2.0 dated July 29, 2016.  This SAP supersedes the statistical considerations identified in the 
protocol. Note the following differences between this SAP version and the Protocol: 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 28 of 32 
1) Since PK sampling is limited to peak and trough samples, PK reporting will be 
limited to serum concentration listings, summary descriptive statistics over time and 
mean peak and trough figures over time, as specified in this SAP. Expert analysis of 
PK data, such as non-compartmental analyses, will not be performed due to the 
limited peak and trough sampling scheme. 
2) Since PK sampling is limited to peak and trough samples, the PK population will be 
defined more simply to include ‘all patients with at least one pre-dose and one post-
dose evaluable result reported.’ 
3) PK/PD comparisons will be limited figures comparing mean peak and trough 
concentrations to CD19RO and ABC % change from baseline. 
4) Components of the mechanistic studies exploratory endpoints and all mechanistic 
study analyses may be reported separately from the main clinical study report. These 
analyses are not detailed in this SAP.  
12. REFERENCES 
1. Protocol XmAb5871-04: A Randomized, Double-Blinded, Placebo-Controlled Study of 
the Effect of XmAb®5871 on Systemic Lupus Erythematosus Disease Activity. Version 
2.0, July 29, 2016.  
2. International Federation of Pharmaceutical Manufacturers and Associations. Medical 
Dictionary for Regulatory Activities (MedDRA). Version 19.0 Reston, Virginia, USA; 
2008. 
3. WHO Collaborating Center for International Drug Monitoring. WHO Drug Dictionary. 
WHO Drug version 201509. Uppsala, Sweden; 2008.  
4. SAS Institute Inc. SAS Version 9.3. Cary, NC, USA; 2002-2003. 
5. International Conference on Harmonisation of Technical Requirements for Registration 
of Pharmaceuticals for Human Use, ICH Harmonised Tripartite Guideline, Statistical 
Principles for Clinical Trials (E9), 5 February 1998. 
6. International Conference on Harmonisation of Technical Requirements for Registration 
of Pharmaceuticals for Human Use, ICH Harmonised Tripartite Guideline, Structure and 
Content of Clinical Study Reports (E3), 30 November 1995. 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 29 of 32 
13.  SCHEDULE OF ASSESSMENTS 
 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 30 of 32 
 
 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 31 of 32 
APPENDIX 1.     IMPUTATION OF PARTIAL AND MISSING DATES 
 
Adverse Event  
All AE onset dates must be entered on the eCRF as complete dates.  In the rare case that all 
or part of an AE onset date is missing but an AE resolution date is present and after first dose 
date then the AE onset date will be imputed as follows: 
Year of onset Month of 
onset 
Day of 
onset 
Onset date to be imputed as 
Missing Missing Missing Date of first dose 
year = year of first dose Missing Non-
missing 
Set month to month of first dose 
year = year of first dose Missing Missing Set month and day to those of 
first dose 
year < year of first dose Missing Non-
missing 
set month to December 
year < year of first dose Missing Missing set month and day to December 
31 
year > year of first dose Missing Non-
missing 
set month to January 
year > year of first dose Missing Missing set month and day to January 1 
year = year of first dose Month = month 
of first dose 
Missing Set day as day of 1st dose 
year = year of first dose Month < month 
of first dose 
Missing Set day as last day of onset month 
year = year of first dose Month > month 
of first dose 
Missing Set day as first day of onset 
month 
year < year of first dose Non-missing Missing Set day as last day of onset month 
year > year of first dose Non-missing Missing Set day as first day of onset 
month 
 
Xencor, Inc.   Statistical Analysis Plan  
Protocol: XmAb5871-04  Version: 1.0 (Dated 02MAY2018) 
 
Confidential/Proprietary Property of Xencor, Inc.  
Page 32 of 32 
If AE resolution date is present and prior to first dose date, then there is no need to impute 
incomplete AE start date, as the AE is not treatment emergent and the event should be in the 
medical history. 
Concomitant Medications 
• If year and month are present and day is missing then set day to first day of month for 
start date, and set day to last day of month for end date 
• If year and day are present and month is missing then set month to January for start 
date, and set month to December for end date 
• If year is present and month and day are missing then set month and day to January 1 
for start date, and set month and day to December 31 for end date 
• Completely missing dates will not be imputed 
• If start date is completely missing and end date is on or after the first dose, then the 
medication will be classified as concomitant; if the end date is missing, then the 
medication will be classified as ongoing.  Medications for which the start and end 
dates are completely missing will be classified as concomitant. 
Medical History and Diagnosis Dates 
• If day is missing and month is non-missing, day will be set to 15th of the month. 
• If month is missing and day is non-missing, then month will be set to July.  
• If month and day are both missing, month and day will be set to July 1st. 
• If complete date is missing, then impute it as the date of informed consent -1. 
 
 