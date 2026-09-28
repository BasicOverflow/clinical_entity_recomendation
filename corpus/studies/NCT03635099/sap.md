TITLE PAGE
TRIAL STATISTICAL ANALYSIS PLAN c25658163-02
BI Trial No.: 1407-0030
Title: Phase II evaluation of safety, tolerability, and efficacy of BI 730357 
in patients with moderate-to-severe plaque psoriasis
BI Investigational
Product(s):   BI 730357
Responsible trial 
statistician(s):
Phone: 
Fax: 
Date of statistical 
analysis plan:
06 SEPT 2019 SIGNED 
Version: Final
Page 1 of 34
Proprietary confidential information
 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies. All rights reserved.
This document may not - in full or in part - be passed on, reproduced, published or otherwise used without prior written permission.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 2 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
1. TABLE OF CONTENTS
TITLE PAGE ...........................................................................................................................1
1. TABLE OF CONTENTS......................................................................................2
LIST OF TABLES ...................................................................................................................4
2. LIST OF ABBREVIATIONS ..............................................................................5
3. INTRODUCTION.................................................................................................7
4.
CHANGES IN THE PLANNED ANALYSIS OF THE STUDY......................8
5. ENDPOINTS .........................................................................................................8
5.1
PRIMARY ENDPOINTS.....................................................................................8
5.2 SECONDARY ENDPOINTS...............................................................................8
5.2.1 Key secondary endpoints......................................................................................8
5.2.2 Secondary endpoints.............................................................................................8
6. GENERAL ANALYSIS DEFINITIONS ..........................................................10
6.1 TREATMENTS...................................................................................................10
6.2 IMPORTANT PROTOCOL DEVIATION......................................................11
6.3 SUBJECT SETS ANALYSED
...........................................................................13
6.5
POOLING OF CENTRES .................................................................................15
6.6 HANDLING OF MISSING 
DATA AND OUTLIERS ....................................15
6.6.1 Efficacy data ........................................................................................................15
6.6.2 Safety data and other data .................................................................................16
6.7 BASELINE, TIME WINDOWS AND CALCULATED VISITS ...................
16
7. PLANNED ANALYSIS ......................................................................................18
7.1 DEMOGRAPHIC AND OTHER BASELINE CHARACTERISTICS .........
19
7.2 CONCOMITANT DISEASES AND MEDICATION .....................................19
7.3 TREATMENT COMPLIANCE ........................................................................20
7.4
PRIMARY ENDPOINTS...................................................................................20
7.4.1 Primary Analysis.................................................................................................20
7.4.2 Secondary analyses .............................................................................................21
7.5 SECONDARY ENDPOINTS.............................................................................22
7.5.1 Key secondary endpoints....................................................................................22
7.5.2 (Other) Secondary endpoints .............................................................................22

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 3 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
7.7 EXTENT OF EXPOSURE.................................................................................26
7.8 SAFETY ANALYSIS..........................................................................................26
7.8.1 Adverse events.....................................................................................................26
7.8.2 Laboratory data ..................................................................................................28
7.8.3 Vital signs.............................................................................................................29
7.8.4 ECG......................................................................................................................30
7.8.5 Others...................................................................................................................30
8. REFERENCES....................................................................................................31
10. HISTORY TABLE..............................................................................................34

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 4 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
LIST OF TABLES
Table 6.1: 1 Definition of treatment periods.........................................................................10
Table 6.2: 1 Important protocol deviations...........................................................................11
Table 6.7: 1 Time windows for assignment of on
-treatment efficacy, safety lab, vital 
signs, and biomarker measurements to visits for statistical analysis................17
Table 7.4: 1 MCPMod contrast coefficient (design stage) ...................................................21
Table 7.8.1: 1 Other special groupings of adverse events .......................................................27
Table 10: 1 History table .....................................................................................................34
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 5 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
2. LIST OF ABBREVIATIONS
Include a list of all abbreviations used in the TSAP
Term Definition / description
AE Adverse Event
BRPM Blinded Report Planning Meeting
BES Biopsy Evaluable Set
CTC Common Terminology Criteria
CTP Clinical Trial Protocol
CTR Clinical Trial Report
DM&SM Boehringer Ingelheim Data Management And Statistics Manual
DRA Drug Regulatory Affairs
DMG Dictionary Maintenance Group
EDC Electronic Data Capture
EMEA European Agency For The Evaluation Of Medicinal Products
FAS Full Analysis Set
ICH International Conference On Harmonisation
IPD Important Protocol Deviation
LOCF Last Observation Carried Forward
MedDRA Medical Dictionary For Regulatory Activities
MCPMod Multiple Comparison Procedure and Modelling
MQRM Medical Quality Review Meeting
MMRM Mixed Effect Model Repeated Measurement
PASI Psoriasis Area Severity Index
PK Pharmacokinetics
PKS Pharmacokinetics Set
PPS Per Protocol Set
PSTAT Project Statistician
PT Preferred Term
PV Protocol Violation
Q1 Lower Quartile
Q3 Upper Quartile
REP Residual Effect Period
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 6 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
Term Definition / description
SA Statistical Analysis
SD Standard Deviation
SMQ Standardised MedDRA Query
SOC System Organ Class
sPGA Static Physician’s Global Assessment
TOM Trial Oversight Meeting
ToC Table of Contents
TS Treated Set
TMW Trial Medical Writer
TSAP Trial Statistical Analysis Plan
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 7 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
3. INTRODUCTION
As per ICH E9, the purpose of this document is to provide a more technical and detailed 
elaboration of the principal features of the analysis described in the protocol, and to include 
detailed procedures for executing the statistical analysis of the primary and secondary 
variables and other data.
This TSAP assumes familiarity with the Clinical Trial Protocol (CTP), including Protocol 
Amendments. In particular, the TSAP is based on the planned analysis specification as written 
in CTP Section 7 “Statistical Methods and Determination of Sample Size”. Therefore, TSAP 
readers may consult the CTP for more background information on the study, e.g., on study 
objectives, study design and population, treatments, definition of measurements and variables, 
planning of sample size, randomization.
The trial data is stored in the BI Rave (BRAVE) database system.
SAS® Version 9.4 will be used for analyses.
R version 3.3.2 or later with “DoseFinding” package (9) will be used for MCPMod analysis.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 8 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
4. CHANGES IN THE PLANNED ANALYSIS OF THE STUDY
5. ENDPOINTS
5.1 PRIMARY ENDPOINTS
The co-primary endpoints are:
 Achievement of ≥75% reduction from baseline PASI score (PASI 75) at Week 12
 Achievement of a sPGA score 0 or 1 at Week 12
The co-primary endpoints are the proportion of patients achieving PASI 75 and sPGA 0/1 at 
Week 12 by treatment group.
Details for scoring Psoriasis Area and Severity Index (PASI) and static Physician Global 
Assessment (sPGA) are described in Section 10.1 and 10.2 of the CTP. 
5.2 SECONDARY ENDPOINTS
5.2.1 Key secondary endpoints
This section is not applicable as no key secondary endpoint has been specified in the protocol
5.2.2 Secondary endpoints
 Achievement of ≥50% reduction from baseline in PASI score (PASI 50) at Week 12 
 Achievement of ≥90% reduction from baseline in PASI score (PASI 90) at Week 12 
 Achievement of 100% reduction from baseline in PASI score (PASI 100) at Week 12
 Achievement of sPGA score 0 at Week 12
 Achievement of ≥75% reduction from baseline in PASI score (PASI 75) at Week 16, 
20, 24
 Achievement of an sPGA score 0 or 1 at Weeks 16, 20, and 24 
 Change from baseline in psoriasis symptoms evaluated using the total score on the 
Psoriasis Symptoms Scale (PSS) at Week 12 
 Achievement of a Dermatology Life Quality Index (DLQI) score of 0 or 1 at Week 12 

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 9 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 10 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
6. GENERAL ANALYSIS DEFINITIONS
6.1 TREATMENTS
Patients will be randomised 2:2:2:2:1 to one of 4 BI 730357 treatment groups A to E, of
which A will receive the lowest and D the highest dose of BI 730357; treatment group E will
receive placebo.
At Week 12, patients will remain in their treatment group or be reassigned depending on the 
primary efficacy endpoint result:
 Non-responders will be reassigned to the next higher dose level or to the highest dose 
level 
based on the original treatment assignment at randomization.
 Placebo recipients (group E) who achieve a PASI 75 response will remain on placebo 
through Week 24. Otherwise, they will be assigned with the highest dose level starting 
from Week 12. 
 200 mg recipients will not be titrated at week 12.
For example, patients from dose groups A to C who fail to achieve a PASI 50 response will 
be switched to the next higher respective dose. Patients who have achieved a PASI 50 
response will continue on their initial dose of BI 730357. Patients from dose group D will 
remain on the dose group D through Week 24.
Patients will be analyzed according to the treatment to which they were randomized. The 
following study periods based on actual start and stop dates of study treatment administration 
are defined: 
Table 6.1: 1 Definition of treatment periods
Analysing Treatment 
Period
Start Date (including) Stop Date (excluding)
Screening Date of informed consent  Date of medication 
randomization -1 day
On-treatment period Date of medication 
randomization
 Date of last study 
medication intake + 7 days
Follow-up Date of last study medication 
intake +8 days
 Last contact date
For the main safety analyses, Adverse Events (AEs) will be classified to one of the following 
time periods: “screening”, “on-treatment”, or “follow-up”. Section 7.3.4 of the protocol 
specifies that, all AEs and laboratory assessments with an onset between start of treatment and 
end of the residual effect period (REP), a period of 7 days after the last dose of trial 
medication for this trial, will be assigned to the “on-treatment” period for evaluation.
Detailed rules for assigning AEs to these time periods are listed below:
 If date of informed consent ≤AE onset date and <date of first drug administration, then 
the AE is assigned to “screening”
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 11 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
 If date of first drug administration ≤AE onset date ≤date of last intake +7 days, then 
the AE is assigned to “on-treatment”
 If AE onset date > date of last drug administration+7 days, then the AE is assigned to 
“follow-up”
AE will be reported for first and second 12 weeks separately. If an AE onsets on the day of 
week 12 visit, actual time of AE and time of drug administration on week 12 visit will be 
compared to determine under which period such AE will be reported.
6.2 IMPORTANT PROTOCOL DEVIATION
A protocol deviation (PD) is important if it affects the rights or safety of the study subjects, or 
if it can potentially influence the primary outcome measurement(s) in a non-negligible way. 
Patients with important PDs that could potentially impact the evaluation of the primary 
endpoint(s) will be excluded from PPS, if applicable).
A list of important PDs (IPDs) is given in Table 6.2: 1. Important PDs will be reviewed at 
Medical Quality Review Meetings (MQRMs) conducted periodically during the trial. A list of 
protocol deviation will be discussed at the Blinded Report Planning Meetings (BRPMs).
If the data show other important PDs, this table will be supplemented accordingly at BRPMs 
or through team review of the manual PD log. The decision whether a subject will be 
excluded from the analysis will be made at the final BRPM prior to Database Lock (DBL).
Table 6.2: 1 Important protocol deviations
Category / 
Code
Description Requirements Excluded from
(if applicable)
Automatic/
Manual
A
A1 Entrance criteria not met Inclusion criteria not met 
as specified in the protocol
A1.1 Demographic or pregnancy 
testing inclusion criterion
not met
Inclusion criteria 1,2,3 not 
met
None Automatic
A1.2 Psoriasis inclusion criterion 
not met
Inclusion criteria 4 not met PPS Automatic
A1.3 Patient does not meet
the specified moderate to 
severe plaque-type psoriasis
Inclusion criteria 5 not met PPS Automatic 
and Manual
A2 Exclusion criteria not met Exclusion criteria not met 
as specified in the protocol
A 2.1 Patient has active/past 
clinically important 
diseases, has significant 
laboratory values, or 
pregnancy-related
exclusion criteria met
Exclusion criteria 1, 
9,10,11,12,13 not met
None Automatic 
A 2.2 Patient has participated in
another clinical trial
within 30 days before
the randomization or 
previously enrolled in trial
Exclusion criteria 2,3 not 
met
PPS Automatic
and Manual
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 12 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
Table 6.2: 1 (Cont’d) Important protocol deviations 
Category / 
Code
Description Requirements Excluded from
(if applicable)
Automatic/
Manual
A 2.3 Patient has not sufficient 
wait time since last intake 
of restricted medication or 
must or wish to continue the 
intake of restricted 
medications
Exclusion criteria 4,6 not 
met
PPS Automatic 
and Manual
A 2.4 Patient has received
a live vaccine
Exclusion criteria 5 not 
met
None Automatic/
Manual
A 2.5 Patient has chronic 
alcohol/drug abuse 
Exclusion criteria 8 not 
met
None Automatic
A 2.6 Patient has suicidal ideation Exclusion criteria 14 not 
met
None Automatic
B Informed consent
B1 Informed consent missing Informed consent not 
available/not done
All
B2 Date of informed consent 
was after the date of any 
study related procedure, or 
the patient signed the wrong 
version of ICF
Informed consent late PPS if ICF after 
procedure (A). 
None if wrong 
version. (M)
Automatic 
and Manual
C Trial medication and 
randomisation
C1.1 Incorrect trial medication 
taken prior to week 12 
Medication kit assigned 
not matching treatment 
patient was randomised to 
(cross-treatment1) and/or 
not matching IVRS 
assignment
PPS Automatic 
and manual
C1.2 Incorrect trial medication 
taken after week 12
Medication kit assigned 
not matching treatment 
patient was randomised to 
(cross-treatment1) and/or 
not matching IVRS 
assignment
None Automatic 
and manual
C2 Non-compliance Overall compliance <80% 
or >120%
Non-compliance caused by 
treatment cessation due to 
a cardiovascular procedure 
should not be classified as 
a protocol violation.
PPS Automatic
C3 PASI score entered in IRT 
entry error at week 12
PASI score entered in IRT 
not the same as entered in 
CRF page at 
randomization and week 
12
None Automatic 
and Manual
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 13 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
Table 6.2: 1 (Cont’d) Important protocol deviations 
Category / 
Code
Description Requirements Excluded from
(if applicable)
Automatic/
Manual
C4 Medication code broken 
inappropriately
Medication code broken 
inappropriately - reason for 
medication code break 
None
D Concomitant medication
D 1.1 Prohibited medication use 
potential impact patient 
safety2 in first 12 weeks
Prohibited medication used 
may impact patient safety 
profile in first 12 weeks of 
treatment
None Manual
D 1.2 Prohibited medication use 
potential impact patient 
safety2 in second 12 weeks 
Prohibited medication used 
may impact patient safety 
profile in second 12 weeks 
of treatment
None Manual
D 1.3 Prohibited medication use 
potential impact patient 
efficacy3 in first 12 weeks
Prohibited medication used 
may impact patient efficacy 
profile in first 12 weeks of 
treatment
PPS Manual
D 1.4 Prohibited medication use 
potential impact patient 
efficacy3 in second 12 weeks
Prohibited medication used 
may impact patient efficacy 
profile in second 12 weeks 
of treatment
None Manual
E Study Specific
E 1 Dispense expired drug None
1 cross-treatment means actual treatment received is different from randomized or IRT assigned treatment type.
2 Prohibited medication use potential impact patient safety are manually reviewed in MQRM or TOM. Decision 
are documented in related meeting minutes and final BRPM minutes.
3 Prohibited medication use potential impact patient efficacy includes all pre-treatment PsO therapy not meet 
washout period or concomitant use during study conduct specificied in CTP table 4.2.2.1:1.
6.3 SUBJECT SETS ANALYSED
There are five patient sets defined in this trial:
 Randomised Set (RS)
The RS includes all patients who signed the informed consent form and were also 
randomised, regardless whether the patient was treated with trial medication or not.
 Treated Set (TS)
The TS includes all patients in the RS who received at least 1 dose of trial medication and 
is based on the actual treatment received at randomization visit and week 12 visit, if 
applicable.
 Full Analysis Set (FAS)
The FAS includes all patients in the RS who received at least 1 dose of trial medication 
and provided baseline and at least 1 post-randomisation measurement of PASI. 
 Per Protocol Set (PPS)
The PPS, a subset of FAS, includes all patients who did not have an IPD affecting the 
primary efficacy endpoint or patients safety (see Table 6.2: 1 for details).
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 14 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
Patient disposition will be based on randomized set. 
The FAS will be used for the analyses of demographics, baseline characteristics and all 
efficacy endpoints. The efficacy analyses will follow the intention-to-treat (ITT) principle in 
assigning patients to treatment groups, i.e., efficacy analyses will be analysed as randomised 
using the FAS. 
The TS will be used for the analyses of concomitant medication use, medical history, PsO
therapy history, treatment exposure, compliance, and safety (including adverse events, 
laboratory measurements, vital signs, and ECG). Safety analyses will assign patients to the 
treatment group based on the actual treatment received. 
PPS for sensitivity analysis will be considered if necessary. Decision will be documented in 
BRPM minutes.
If a patient erroneously receives the wrong dose of trial drug, the patient’s efficacy data will 
be analysed in the randomized treatment group and the patient’s safety data will be analysed 
in the actual treatment group. If a patient receives placebo instead of  randomized BI730357 
study medication, this will be noted as an IPD.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 15 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
6.5 POOLING OF CENTRES
This section is not applicable because centre/country is not included in the statistical model.
6.6 HANDLING OF MISSING DATA AND OUTLIERS
General imputation rules for continuous and binary endpoints are described in protocol 
section 7.5. 
Missing data imputations at the interim analysis at completion of both week 4 and week 12, 
will be performed using all available on-treatment data observed up to the respective analysis 
cut-off date.
6.6.1 Efficacy data
If at any time a patient uses an inappropriate concomitant medication, then all future data will 
be treated as failure for binary variables and LOCF (using the last on-treatment observation 
prior to inappropriate concomitant medication use) for continuous variables. As part of the 
LOCF technique, baseline values will be carried forward if no post-baseline value is available.
If a patient is missing items from a questionnaire measured at a visit, these will be handled 
according to the instructions given in Section 10.11 of the protocol specific to each 
questionnaire.
For the NAPSI, PSSI, and PPASI assessment, if the CRF is marked as “No” indicating that 
the patient does not have nail, scalp, palmo-plantar disease, then the total score will be set as 
zero (0) for that assessment in the analysis dataset.
For efficacy endpoints which are continuous in nature, a restricted maximum likelihood 
(REML)-based mixed model repeated measures (MMRM) approach will be used for 
inferential analysis, if applicable. No imputation will be performed for data used in MMRM.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 16 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
6.6.2 Safety data and other data
In general, missing data will not be imputed and only observed values will be analyzed. 
Missing or incomplete AE dates will be imputed according to BI standards (see DM&SM) 
“Handling of missing and incomplete AE dates”). (1)
6.7 BASELINE, TIME WINDOWS AND CALCULATED VISITS
For efficacy endpoints, baseline is defined as the pre-treatment observation at Visit 2. If Visit 
2 is missing, then Visit 1 will be used for baseline.
For laboratory safety measurements, the last measurements taken prior to the treatment start 
will be considered as baseline.
In general, measurements reported with a date only (and no time) and taken on the day of first 
administration of trial treatment will also be considered pre-treatment values.
The visit schedule with accompanying details can be found in Flow Chart 1. Measurements 
taken after start of treatment will be considered either on- or off-treatment values based on 
definition in Table 6.1: 1.
On-treatment measurements for EOT and EOS visit for early discontinued patients will be 
allocated to visits by means of time windows with the limit between adjacent windows half-
way between the planned dates for the visits; the middle day is counted to the window of the 
later visit. Mutually exclusive relative day windows are defined below to provide derived 
visits that correspond to the post-baseline time points. For example, Visit 6 is planned on Day 
29 and Visit 7 is planned on Day 57. Therefore, the window of Visit 6 reaches until Day 42 
while the window of Visit 7 starts on Day 43. The visit schedule with corresponding windows 
is given in Table 6.7: 1.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 17 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
Table 6.7: 1 Time windows for assignment of on-treatment efficacy, safety lab, vital signs, 
and biomarker measurements to visits for statistical analysis
Window No. Window label Nominal visit Nominal day Interval
0 Baseline VISIT 2 1 N/A
1 Week 1 VISIT 3 4 [2,4]
2 Week 1 VISIT 4 8 [5,11]
3 Week 2 VISIT 5 15 [12,21]
4 Week 4 VISIT 6 29 [22,42]
5 Week 8 VISIT 7 57 [43,70]
6 Week 12 VISIT 8 85 [71,98]
7 Week 16 VISIT 9 113 [99,126]
8 Week 20 VISIT 10 141 [127,154]
9 Week 24 EOT 169 [155,182]
10 Week 28 EOS 197 [183,∞]
If there are multiple values for an efficacy endpoint in one window (visit), use the one from 
scheduled visit. If value from scheduled visit is not present, the visit closest to the nominal 
day will be selected for assessing endpoints at a particular visit and for by-visit displays. If the 
visits are equidistant from the nominal day, then the earlier visit will be selected. All 
measured values will be stored in analysis datasets. 
The same visit windows will be used for safety laboratory and vital sign assessments. If there 
are multiple safety or laboratory values in one time window on treatment, the worst value will 
be selected for the by-visit analyses.
Analysis of AE data, concomitant medication or non-drug therapies, as well as use of rescue 
medication will not be based on visits. Frequency tables for these data will be using on-
treatment data only. Therefore, no assignment to time windows will be necessary for such 
data.
While the nominal times listed in this section should be adhered to as closely as possible, the 
actual sampling times will be recorded and used for determination of pharmacokinetic 
parameters.
For visits without an assigned value based on time windows, a value will thereafter be 
imputed as defined in Section 6.6. LOCF imputation of efficacy endpoints, when applicable, 
will be performed based on all available observations obtained during the on-treatment period, 
irrespective of whether the observation was selected in any time window.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 18 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
7. PLANNED ANALYSIS
According to CTP Section 7.4, there are two interim analyses planned for this study. 
1) An administrative interim analysis for the purpose of internal planning other 
indications of BI 730357 will be performed when the last patient completes the 4 
week follow-up visit
a. Output will comprise only baseline summaries, key efficacy endpoints( i.e. 
PASI, sPGA) and key adverse events tables
b. No separate report is planned to be written for this analysis
2) The interim for the primary analysis (at an interim time point) will be performed 
when the last patient completes the 12 week follow-up visit
For each interim analysis, the trial team will perform a blinded analysis and an independent 
team will perform unblinded analyses. In order to support the further double-blinded conduct 
of the trial until the week 24 visit, the trial team are kept blinded on the individual patients’ 
treatment group assignment. Details of each interim analysis are specified in the trial interim 
analysis logistic and access plan for week 4 and week 12 separately.
The analysis of the entire efficacy, safety, and biomarker data collected through the full 28 
weeks of follow-up will be performed once all entered patients have completed the trial (up to
EOT/Week 28 Visit); at that time point, a final database lock will be done and all on-
treatment data through week 28 will be reported.
General remarks:
The format of the listings and tables will follow the standards defined in the BI corporate 
guideline “Reporting of clinical trials and project summaries” (6).
For EoT tables, the set of summary statistics is: N / Mean / SD / Min / Median / Max.
For appendix tables, the set of summary statistics is: N / Mean / SD / Min / Q1 (lower
quartile) / Median / Q3 (upper quartile) / Max.
Tabulations of frequencies for categorical data will include all possible categories and will 
display the number of observations in a category as well as the percentage (%) relative to the 
respective treatment group. Percentages will be rounded to one decimal place. The category 
“missing” will be displayed only if there are actually missing values. Percentages will be 
based on all patients in the respective patient set no matter whether they have non-missing 
values or not.
Planned treatment for first 12 weeks of treatment is defined as treatment patient assigned from 
IVRS at randomization visit (visit2). Planned treatment for second 12 weeks of treatment is 
defined as the treatment patient assigned from IVRS at week 12 visit (V8).
Subject data listings of data used in the analyses (i.e. demographic and baseline characteristics 
and key efficacy endpoints) will also be provided and included in Appendix 16.2 of the CTR.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 19 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
Disposition of the patient population participating in the trial will be summarised by 
presentation of the frequency of patients screened, entered, screened but not entered, treated, 
entered but not treated. Within treated patients, data will be summarized by treatment periods 
(period 1 - first 12 weeks of treatment and period 2 – second 12 weeks of treatment) for 
treatment ongoing patients, patients complete planned treatment period and patients who are 
prematurely discontinued, by reason. Disposition will be listed by country.
7.1 DEMOGRAPHIC AND OTHER BASELINE CHARACTERISTICS
Only descriptive statistics are planned for this section of the report. Demographic parameters 
collected and to be presented include, but are not limited to, the following:
 Gender (Male, Female)
 Race and ethnicity (as defined in the eCRF)
 Age [years]
 Height [cm]
 Weight [kg] (continuous)
 Weight Group (>100kg vs. < 100 kg)
 Body mass index [kg/m2] (defined as weight [kg]/(height [cm]/100)2)
 Body mass index [kg/m2] (>30 vs. <30)
 Smoking history (Never-smoked, Ex-smoker, Currently smokes)
 Alcohol History (Non-drinker, drinks – no interference, drinks – possible interference)
 Region
 PsA history (diagnosed, suspected, no PsA)
 Prior biologic use for psoriasis (Yes/No)
Baseline disease characteristic to be presented include, but are not limited to, the following: 
 BSA (Visit 1)
 PASI score
 sPGA
 NAPSI, PPASI, PSSI
 Pain VAS
 PSS total score
 DLQI
For NAPSI, PPASI, PSSI and pain-VAS, report is only based on patients are applicable to the 
measurement per protocol, e.g. pain VAS only for patients with psoriatic arthritis.
7.2 CONCOMITANT DISEASES AND MEDICATION
Only descriptive statistics are planned for this section of the report.
A table of the number (%) of patients with concomitant diagnoses from baseline condition by 
system organ class (SOC) and preferred term (PT) will be included along with a supporting 
listing. Concomitant diagnoses will be coded with the most recent version of MedDRA in 
effect at database lock.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 20 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
Concomitant medication will be described as a table of number (%) of patients with on-
treatment medication use. On-treatment is defined as medication with a stop date after or on 
the day of first trial drug intake and before last trial drug intake + 7 days.
Number (%) of patients with psoriasis therapy history will be summarized, including both 
non-topical drug therapy and non -drug therapy.
7.3 TREATMENT COMPLIANCE
Treatment compliance will be reported from baseline to Week 24 based on calculation as 
described in CTP section 4.3. Only descriptive statistics are planned for this section of the 
report. Treatment non-compliance is defined as any randomized patients having taken at least 
one dose of study medication with an overall compliance rate not between 80% and 120% 
inclusive. Overall compliance is calculated based on unweighted average of study drug 
compliance rate at each visit during the treatment period. For the patients who discontinued 
the study treatment prematurely only the visits on or before premature discontinuation will be 
used for the calculation of overall compliance.
Only descriptive statistics are planned for this section of the report. Summary statistics of 
compliance in the treated set will be given for the number of subjects as well as the 
corresponding percentage with compliance in the categories <80%, 80% - 120%, >120%, 
missing.
7.4 PRIMARY ENDPOINT
S
7.4.1 Primary Analysis
After the last patient reaches Week 12, the primary analyses of the primary endpoints will be 
performed in all randomized patients who receive at least one dose of treatment based on 
randomised treatment (FAS) using the Multiple Comparison Procedures and Modelling 
(MCP-Mod) approach (7, 8). 
First, the response rate for co-primary endpoints at week 12 of each dose group will be 
estimated using a logistic regression model. The model will include the fixed effect of 
treatment (categorical dose) and baseline PASI score as covariate. SAS procedure “proc 
logistic” will be used to fit the logistic regression model. 
           =      +   
i ~  subject, j ~  treatment
    = the response variable for primary endpoints
   = the baseline measurement of subject i (=1,2,…)
  = coefficient of baseline effect
   = the effect of treatment j (= 1, ..,Y)
The adjusted mean estimates of response at logit scale for each dose groups, as well as the 
estimated variance-covariance matrix will then be analysed using MCPMod for dose-response 
analysis. 
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 21 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
The multiple comparison procedure will be implemented using of optimal contrast tests which 
control the family-wise type I error rate at one- sided α = 0.05. The optimal contrasts 
corresponding to the candidate models are calculated as in the trial design stage and shown in 
Table 7.4:1. The actual analysis contrast coefficients will be based on using the estimated 
variance-covariance matrix from the data.
Table 7.4: 1 MCPMod contrast coefficient (design stage)
Contract coefficients for dose
Model 0 25 mg 50 mg 100 mg 200 mg
Linear -0.179 -0.350 -0.301 -0.037 0.868
Emax1 -0.248 -0.467 -0.272 0.214 0.774
Emax2 -0.553 -0.458 0.048 0.388 0.575
Logistic -0.210 -0.429 -0.403 0.341 0.702
Exponential model -0.133 -0.264 -0.261 -0.231 0.889
If at least one dose-response model is statistically significant, rejecting the null hypothesis of 
a flat dose-response curve indicates a benefit of BI 730357 over placebo. Test statistics and p-
values will be displayed for different dose response models.
Once the significance of a dose-response signal is established, the selected dose-response 
model(s) will be re-fitted to the data without any parameter assumptions to generate a set of 
new estimates of the model parameters from the data. The final dose-response model will be 
estimated by averaging significant model(s) based on their Akaike Information Criterion 
(AIC) (the smaller the AIC value the better model fit). Fitted response rate and difference to 
placebo for all investigated dose-response models will be tabulated at each dose along with 
logistic regression estimate and the weighted AIC estimate.
Fitted dose-response curve(s) for significant model(s) will be graphically presented with 95% 
confidence band across investigated dose range (0 to 200mg).
The adjusted mean estimates from the logistic regression and fitted MCPMod estimates of 
response rate are both on the logit scale. The absolute and difference in proportions will be 
calculated by transforming the estimate back to the probability scale. More details please refer 
to Section 9.4.
7.4.2 Secondary analyses
For both co-primary endpoints, the point estimate and two -sided 90% and 95% exact
confidence intervals for proportion of responder will be displayed for each treatment group. 
The unadjusted absolute difference in proportion between active groups and placebo group 
regarding the co-primary endpoints will be estimated with 90% and 95% Pearson-Clopper 
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 22 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
exact confidence intervals and p-value calculated by Chi-square test. This is considered the 
secondary analysis for the primary endpoint(s). 
7.5 SECONDARY ENDPOINTS
7.5.1 Key secondary endpoints
This section is not applicable as no key secondary endpoint has been specified in the protocol.
7.5.2 (Other) Secondary e ndpoints
If considered necessary, a MCPMod approach will also be applied to selected secondary 
endpoints.
 PASI 75 at week 16
The same methods as discussed for the secondary analysis for the primary endpoint will be 
used to analyse clinical binary secondary and further endpoints for each treatment group as 
well as treatment comparison.
For the convenience of writing and reviewing, all PASI and sPGA endpoints at different time 
points (secondary and further clinical endpoints) are described in this section.
For the analysis of binary efficacy endpoints after week 12 based on non
-responder 
imputation, patients switch treatment at week 12 will be imputed as failure for records after 
week 12, under original randomized treatment arm. 
Psoriasis Area and Severity Index (PASI)
Treatment comparison for unadjusted absolute difference in proportion between active groups 
and placebo group will be performed for achievement of 50% (PASI50), 75% (PASI75), 
100% (PASI 100) at week 12 and 75% (PASI 75) at Week 16, 20 and 24.
Descriptive statistics of total PASI score and PASI total score change from baseline, PASI 
total score percentage change from baseline and the percentage of patients who achieve a 
PASI score of at least 50% (PASI 50), 75% (PASI 75), 90% (PASI90) and 100% (PASI100) 
reductions from baseline will be tabulated by treatment over time. Additionally, these will be 
graphically represented by line plots over time.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 23 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
Static Physician's Global Assessment (sPGA)
The sPGA is scored using the following levels of assessment:
0 - clear 1 - almost clear 2 - mild 3 - moderate 4 - marked 5 - severe
Details for scoring sPGA and its components are described in Section 10.2 of the CTP.
Treatment comparison for unadjusted absolute difference in proportion between active groups 
and placebo group will be performed for sPGA equals to 0 at week 12 and sPGA clear or 
almost clear at week 12, 16, 20 and 24.
The number and proportion of patients who achieve a sPGA score of 1 (clear) or 2(almost 
clear) over time will be tabulated for each treatment group. 
Additionally, the proportion of patients shifting from their baseline sPGA values to different 
values over time will be tabulated for each treatment group.
PSS total score change from baseline at week 12
For change from baseline in PSS total score at Week 12 and treatment comparison, a 
restricted maximum likelihood (REML)-based mixed model repeated measures (MMRM) 
approach will be used. The analyses will include the fixed, categorical effects of treatment, 
visit, and treatment-by-visit interaction, as well as the continuous, fixed covariates of baseline 
PSS total score and baseline PASI score-by-visit interaction. Patient will be considered as a 
random effect.  An unstructured covariance structure for within subject variation will be used.
The number and proportion of patients who PSS total score 0 over time will be tabulated for 
each treatment group. 
Additionally, the proportions of patients shifting from their baseline PSS values to different 
values over time will be tabulated for each treatment group for each individual domain (pain, 
redness, itching, burning).
DLQI score of 0 or 1 at week 12
Achievement of a Dermatology Life Quality Index (DLQI) score of 0 or 1 at week 12 will 
analysed by treatment comparison of unadjusted absolute difference in proportion between 
active groups and placebo group with 90% and 95% exact confidence intervals. This is 
considered the secondary analysis for the primary endpoint(s).
For DLQI, if one question is left unanswered this is scored 0 and the total score is summed 
and expressed as usual out of a maximum of 30;

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 24 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 25 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 26 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
7.7 EXTENT OF EXPOSURE
Exposure will be presented as categorized period of “1-28”, “29-56”, “57-84” and 
“>85” days based on dose received for total study medication intake. Exposure will be 
summarized and presented separately for first 12 weeks and second 12 weeks of 
treatment. 
7.8 SAFETY ANALYSIS
All safety analyses will be performed on the treated set. 
7.8.1 Adverse events
The analyses of adverse events will be descriptive in nature. All analyses of AEs will be based 
on the number of patients with AEs (not the number of AEs).
Multiple overlapping or adjacent recordings (AE occurrences) of the same AE are collapsed 
into one AE event if all AE attributes are identical as defined in (3, 4).
Two AE occurrences are considered to be time-overlapping if the start date of the second, 
later occurrence is earlier or equal to the end date of the first occurrence.
Two AE occurrences are considered to be time-adjacent if the start date of the second, later 
occurrence is one day later than the end date of the first occurrence. The default definition for 
the gap of one day may be changed on the project level.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 27 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
If multiple overlapping (AE occurrences) of the same AE have different attributes, the AEs 
will be queried to confirm whether they are in fact one occurrence or to correct the end date of 
the first occurrence to match the start date of the second occurrence.
After this process of collapsing the events to remove duplication and clarify any 
inconsistencies, the resulting data will form the basis for all reporting of AEs in the listings, 
tables, and figures.
For further details on summarization of AE data, please refer to the guideline 'Handling and 
summarization of adverse event data for clinical trial r
eports and integrated summaries' (3, 4).
The analysis of adverse events will be based on the concept of treatment emergent adverse 
events. That means that all adverse events occurring between first drug administration and 
within 7 days of last drug administration will be assigned to the assigned treatment. All 
adverse events occurring before first drug intake will be assigned to ‘screening’.
The severity of AEs will be summarised by the maximum intensity of the events each patient had 
(as indicated by the recorded RCTC version 2 grade). This will show the number and percent of 
patients who had at most mild, moderate, severe, and life threatening events. Severe adverse 
event is defined as an AE with RCTC grade equals to 3 (severe) or 4 (life threatening).
Groupings of adverse events and adverse events of special interest (AESI)
The AESI have been defined in the protocols as hepatic injury defin ed by the following 
alterations of liver parameters:
 For patients with normal liver func tion at Baseline: an elevation of AST and/or 
ALT >3 fold ULN combined with an elevation of total bilirubin >2 fold ULN 
measured in the same blood draw samp le .
See Section 7.3.2 for a description of the assessment of potential Hy’s Law cases.
Other user-defined special adverse event grouped term for BI 730357 specified in Table 
7.8.1:1 will be reported.
Table 7.8.1: 1 Other special groupings of adverse events
N AESI Term Definition#
1 Yes Drug Induced 
Liver Injury* 
SMQ Drug related hepatic disorders –
comprehensive search (20000006)
2 Yes Opportunistic 
infections*
BIcMQ “Opportunistic infections” BIcMQ 
(30000108)
3 Yes Tuberculosis* BIcMQ “Tuberculosis” BIcMQ (30000107)
4 Yes Severe 
infections*
SOC “Infections and infestations” with CRF 
grade >=3
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 28 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
Table 7.8.1:1 Other special groupings of adverse events
5 No Cardiovascular, 
Cerebrovascular, 
events (including 
MACE)
 SOC ‘cardiac disorders’ (fatal cases only)
 SOC ‘vascular disorders’ (fatal cases only)
 SMQ Myocardial Infarction (20000047)
 SMQ Haemorrhagic central nervous 
system vascular conditions (20000064)
 SMQ Ischaemic central nervous system 
vascular conditions (20000063)
PTs: cardiac death, sudden cardiac death, 
sudden death
*: adverse event of special interest (AESI). AESI will be collected according to eCRF
The following periods will be defined for assessing adverse events:
 First 12 weeks of treatment
 Second 12 weeks of treatment
For AE occurs on day of week 12 visit, actual AE onset time will be compared with first drug 
administration time to determine AE period. The treatment label for second 12 weeks will be 
a combination of actual treatment in first 12 weeks of treatment and second 12 weeks of 
treatment.  
AE summaries
An overall summary of adverse events will be presented. The frequency of patients with 
adverse events will be summarized by treatment, primary system organ class and preferred 
term according to MedDRA. Separate tables will be provided for patients with:
 Drug-related AEs
 AESIs
 AEs leading to discontinuation
 Serious AEs
 Severe AEs (RCTC grade 3 or 4)
 Investigator defined drug related SAE
 Other significant AEs 
 AE by worst RCTC intensity
 Investigator defined drug-related serious AEs
 Special AE grouped term
7.8.2 Laboratory data
The analyses of laboratory data will be descriptive in nature and will be based on BI 
standards.  For lab descriptive, two separate tables for first 12 weeks of treatment and entire 
study period will be provided. For the entire period table, a new treatment label for each 
patient: start with treatment received at randomization and be updated if the patient have 
switched the treatment during the course of trial (by concatenating the second treatment after 
the first treatment) will be derived.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 29 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
The number and perce nt of patients with possibly clinically significant on-trea tment
abnormalities as identified by useof c lin ically significant ranges for each laboratory
paramet e r collected will be presented. Thepatients with possibl y clinicallysignificant
abnormalities will be identified within the initial on-treatm e nt period by study treatment.
Each laboratory value will be grad ed using the RCTC (version 2.0) grading of laboratory 
abnormalities. A summary table of the Baseline grade compared with the last available on -
treatment grade will display thenumber and percent of each type of transition in grade by
lab
oratory parameter within each treatment period, and treatment group. A second table will 
show the number and perce nt of patients with each type of transition from Baseline to their 
w
orst on-trea tment grade p a rameter within each treatment period, and treatment group. For 
these shift tables, only the double blind period will be considered. Parameters using
categorised values, such as the urinalysis parameters, will show the shift tableamong those 
values in a simil ar manner to the RCTC graded values. Last and worst value will be 
considered with respect to each period. For example, if patient have entered the second 12 
weeks of treatment, then the last value for first 12 weeks table is considered as the last value 
measured before week 12 reassignment.
A gra
phical summary highlighting potential cases of Hy’s Law within each treatment
group will be presented. The maximum on-trea tment values of total bilirubin and ALT 
will be plotted each on a s cale as multiples of the upper limit of normal. The figure will
show areas that meet the criteria of cholestasis (total bilirubin > 2x ULN), Templ e ’s 
corollary (ALT > 3 x ULN) and Hy’s L a w as the combination of these two fact o rs. A 
similar figure using maximum AST values in place of ALT will be constructed. An 
accompanying listing will show by sample date and study day thefull course of the total 
bilirubin, ALT, AST and alkaline phosphatase values for patients whose tot al bilirubin 
are > 2xULN or AST or A LT values > 3 x ULN at any time during the study (all
treatment periods). The listing will indicate where the value meets the criteria, either
falling in the cholestasis range, that for Temple’s corollary or where the combination 
meets that for Hy’s Law itself.
Laboratory measurements taken up to the residual effect period of 7 days after the last 
administration of randomized study drug will be considered as on-treatment.
Study visits will be presented by the Visit labels in Table 6.7.1.
7.8.3 Vital signs
The analyses of laboratory data will be descriptive in nature and will be based on BI standards 
(see DM&SM: Display and Analysis of Laboratory Data) (5).
Listing and descriptive statistics of laboratory values over time as well as median and 
interquartile range (IQR) of changes between baseline and extreme abnormal value on 
treatment will be provided. Baseline is understood as the last available measurement before 
study drug administration. Extreme abnormal value on treatment is understood as the on 
treatment laboratory value which is most significantly away from the reference range.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 30 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
Frequency of patients with transitions relative to reference range and listing of patients with 
significant abnormal laboratory values will be presented as well.
In cases of repeated measurements performed for the same visit the last observation will be 
used for tabulations.
7.8.4 ECG
Not applicable.
7.8.5 Others
CSS-R
The individual items and categories of suicidal ideation and behavior from the C-SSRS will 
be summarized through descriptive statistics.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 31 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
8. REFERENCES
1. CPMP/ICH/363/96: "Statistical Principles for Clinical Trials", ICH Guideline Topic E9, 
Note For Guidance on Statistical Principles for Clinical Trials, current version.
5. CPMP/ICH/137/95: “Structure and Content of Clinical Study Reports”, ICH Guideline 
Topic E3; Note For Guidance on Structure and Content of Clinical Study Reports, current 
version.
7. Pinheiro J, Bornkamp B, Bretz F. Design and analysis of dose-finding studies combining 
multiple comparisons and modeling procedures. J Biopharm Stat. 2006; 16:5. 639-
656.[R10-1424]
8. Pinheiro J, Bomkamp B, Glimm E, et al. Model-based dose finding under model 
uncertainty using general parametric models. Stat Med 2014; 33 (10): 1646-1661 [R15-
4293]
9. Bornkamp B, Pinheiro J, Bretz F. Package 'DoseFinding' (February 19, 2015).
Comprehensive R Archive Network. 2015 [R15-2001]

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 32 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 33 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Page 34 of 34
Proprietary confidential information © 2019 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
10. HISTORY TABLE
Table 10: 1 History table
Version Date
(DD-MMM-YY)
Author Sections 
changed
Brief description of change
Initial 08-Nov -2018 None This is the initial TSAP with necessary 
information for trial conduct
Final 06-Sept-2019 None This is the final TSAP, approved
before unblinding of the week 4 interim 
analysis. It is also intended to
be the TSAP for primary analysis at 
week 12 and final database lock.

   
 
APPROVAL / SIGNATURE PAGE 
 
Document Number:  Technical Version Number:  
Document Name:  
 
 
                                                                                                                  
Title:  
 
 
 
                                                                                                                    
Signatures (obtained electronically) 
 
Meaning of Signature  Signed by Date Signed 
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
 
 
 
 
 
   
 
 
 
 
 
   
 
 
 
 
 
 
c25658163 2.0
8-01-tsap-core
Phase II evaluation of safety, tolerability, and efficacy of BI 730357 in patients with
moderate-to-severe plaque psoriasis
Approval-Biostatistics 06 Sep 2019 20:08 CEST
Approval-Biostatistics 06 Sep 2019 20:28 CEST
Approval-Medical Writer 09 Sep 2019 07:55 CEST
Approval-Clinical Trial Leader 09 Sep 2019 11:14 CEST
Approval-Team Member Medicine 09 Sep 2019 22:02 CEST

Boehringer Ingelheim Page 2 of 2
Document Number:  Technical Version Number:  
 
 
(Continued) Signatures (obtained electronically) 
 
Meaning of Signature  Signed by Date Signed 
 
 
  
 
 
 
 
 
 
  
 
 
 
  
 
 
   
   
 
 
  
   
 
 
  
   
 
 
  
   
 
 
  
   
 
 
  
   
 
 
  
   
 
 
  
   
 
 
  
   
 
 
  
 
c25658163 2.0
001-MCS-50-415_RD-01 (3.0) / Saved on: 18 Jan 2021
TITLE PAGE
TRIAL STATISTICAL ANALYSIS PLAN
c35536779-01
BI Trial No.: 1407-
0030 Part 2
Title:   Phase II evaluation of safety, tolerability, and efficacy of BI    
730357 in patients with moderate-to-severe plaque psoriasis
Including revised protocol amendment (c20414608-
08)
Investigational
Product(s):
BI 730357
Responsible trial 
statistician(s):   
  
  Phone: 
Fax: 
Date of statistical 
analysis plan:
12 May 2021 SIGNED 
Version: 1
Page 1 of 43
Proprietary confidential information
 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies. All rights 
reserved.
This document may not - in full or in part - be passed on, reproduced, published or otherwise used without prior written permission.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 2 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
1. TABLE OF CONTENTS
TITLE PAGE............................................................................................................................1
1. TABLE OF CONTENTS......................................................................................2
LIST OF TABLES ...................................................................................................................4
2.
LIST OF ABBREVIATIONS...............................................................................5
3. INTRODUCTION.................................................................................................7
4.
CHANGES IN THE PLANNED ANALYSIS OF THE STUDY ......................8
5. ENDPOINTS(S).....................................................................................................8
5.1 PRIMARY ENDPOINT(S)...................................................................................8
5.2 SECONDARY ENDPOINT(S)
.............................................................................8
5.2.1 Key secondary endpoint(s) ...................................................................................8
5.2.2 Secondary endpoint(s)...........................................................................................8
5.4.5 Variables related to safety
..................................................................................11
6. GENERAL ANALYSIS DEF
INITIONS...........................................................12
6.1 TREATMENT(S) ................................................................................................12
6.2 IMPORTANT PROTOCOL DEVIATIONS....................................................13
6.3 SUBJECT SETS ANALYSED
...........................................................................13
6.5 POOLING OF CENTRES
..................................................................................14
6.6 HANDLING OF MISSING DATA AND OUTLIERS ....................................15
6.6.1 Efficacy data ........................................................................................................15
6.6.2 Safety data and other data..................................................................................15
6.7 BASELINE, TIME WINDOWS AND CALCULATED VISITS....................16
7. PLANNED ANALYSIS ......................................................................................19
7.1 DEMOGRAPHIC AND OTHER BASELINE CHARACTERISTICS .........
19
7.2 CONCOMITANT DISEASES AND MEDICATION......................................20
7.3 TREATMENT COMPLIANCE ........................................................................21
7.4
PRIMARY ENDPOINT(S).................................................................................21
7.4.1 Primary analysis of the primary endpoint(s)....................................................21
7.4.2 Secondary analyses for the co
-primary endpoints ...........................................22
7.4.4 Sensitivity analyses for the co-primary endpoints............................................23
7.5 SECONDARY ENDPOINT(S)...........................................................................25
7.5.1 Key secondary endpoint(s) .................................................................................25

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 3 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
7.5.2 (Other) Secondary endpoint(s)...........................................................................25
7.7 EXTENT OF EXPOSURE
.................................................................................29
7.8 SAFETY ANALYSIS..........................................................................................29
7.8.1 Adverse Events
....................................................................................................29
7.8.2 Laboratory data...................................................................................................31
7.8.3 Vital signs .............................................................................................................32
7.8.4 ECG ......................................................................................................................32
7.8.5 Others ...................................................................................................................32
8. TIMEPOINT OF RELEASE OF TREATMENT INFORMATION .............
33
9. REFERENCES ....................................................................................................34
11. HISTORY TABLE..............................................................................................43

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 4 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
LIST OF TABLES
Table 6.1: 1 Definition of treatment periods.........................................................................12
Table 6.7: 1 Time windows for assignment of on-treatment efficacy, safety lab, vital 
signs, and biomarker measurements to visits for statistical analysis................17
Table 7.8.1:1 Other user-defined special groupings of adverse events....................................30
Table 11: 1 History table .....................................................................................................43
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 5 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
2. LIST OF ABBREVIATIONS
A list of all abbreviations used in this TSAP
Term Definition / description
AE Adverse Event
BRPM Blinded Report Planning Meeting
BES Biopsy Evaluable Set
CTC Common Terminology Criteria
CTP Clinical Trial Protocol
CTR Clinical Trial Report
DM&SM Boehringer Ingelheim Data Management And Statistics Manual
DRA Drug Regulatory Affairs
DMG Dictionary Maintenance Group
EDC Electronic Data Capture
EMEA European Agency For The Evaluation Of Medicinal Products
FAS Full Analysis Set
ICH International Conference On Harmonisation
IPD Important Protocol Deviation
LOCF Last Observation Carried Forward
MedDRA Medical Dictionary For Regulatory Activities
MQRM Medical Quality Review Meeting
MMRM Mixed Effect Model Repeated Measurement
PASI Psoriasis Area Severity Index
PK Pharmacokinetics
PKS Pharmacokinetics Set
PPS Per Protocol Set
PSTAT Project Statistician
PT Preferred Term
PV Protocol Violation
Q1 Lower Quartile
Q3 Upper Quartile
REP Residual Effect Period
SA Statistical Analysis
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 6 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
Term Definition / description
SD Standard Deviation
SMQ Standardised MedDRA Query
SOC System Organ Class
sPGA Static Physician’s Global Assessment
TOM Trial Oversight Meeting
ToC Table of Contents
TS Treated Set
TMW Trial Medical Writer
TSAP Trial Statistical Analysis Plan
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 7 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
3. I NTRODUCTION
As per ICH E9 (1), the purpose of this document is to provide a more technical and detailed 
elaboration of the principal features of the analysis described in the protocol, and to include 
detailed procedures for executing the statistical analysis of the primary and secondary 
variables and other data. To be precise, this trial statistical analysis plan intends to describe 
the statistical analysis strategy for the part 2 of study 1407-0030 in detail.
This TSAP assumes familiarity with the Clinical Trial Protocol (CTP), including Protocol 
Amendments. In particular, the TSAP is based on the planned analysis specification as written 
in CTP Section 7 “Statistical Methods and Determination of Sample Size”. Therefore, TSAP 
readers may consult the CTP for more background information on the study, e.g., on study 
objectives, study design and population, treatments, definition of measurements and variables, 
planning of sample size, randomization.
SAS® Version 9.4 will 
be used for analyses.
R Version 4.0.1 (2020-06-06) with “RBesT” package (Version 1.6.1) will be used for the 
Bayesian analysis.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 8 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
4. C HANGES IN THE PLANNED ANALYSIS OF THE STUDY
A fast-track approach will be taken in order to expedite decision making and for preparation 
of the planned phase III trials, see more details in Section 8.
Details surrounding the assessment of the impact of the COVID-19 pandemic on the
trial, are specified in Section 10.1.
5. ENDPOINTS(S)
5.1 P RIMARY ENDPOINT(S)
The co-primary endpoints are:
 Achievement of ≥75% reduction from baseline PASI score (PASI 75) at Week 12
 Achievement of a sPGA score 0 or 1 at Week 12
The summary measures for the co-primary endpoints are the proportion of patients achieving 
PASI 75 at Week 12 and achieving sPGA 0/1 at Week 12, respectively, by treatment group.
Details for scoring Psoriasis Area and Severity Index (PASI) and static Physician Global 
Assessment (sPGA) are described in Section 10.1 and 10.2 of the CTP. 
5.2 S ECONDARY ENDPOINT(S)
5.2.1 Key secondary endpoint(s)
This section is not applicable as no key secondary endpoint has been specified in the protocol.
5.2.2 Secondary endpoint(
s)
 Achievement of ≥50% reduction from baseline in PASI score (PASI 50) at Week 12 
 Achievement of ≥90% reduction from baseline in PASI score (PASI 90) at Week 12 
 Achievement of 100% reduction from baseline in PASI score (PASI 100) at Week 12
 Achievement of sPGA score 0 at Week 12
 Change from baseline in psoriasis symptoms evaluated using the total score on the 
Psoriasis Symptoms Scale (PSS) at Week 12 
 Achievement of a Dermatology Life Quality Index (DLQI) score of 0 or 1 at Week 12
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 9 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 10 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 11 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
5.4.5 Variables related to safety
In this trial, no endpoint of safety will be analyzed. However, safety and tolerability will be
assessed in a descriptive way based on:
 Vital signs (blood pressure (BP), pulse rate (PR), body weight)
 Clinical laboratory tests (hematology, clinical chemistry and urinalysis)
 Suicidality (as captured in the Columbia-Suicide Severity Rating Scale(C-SSRS) )
 Adjudicated cerebrocardiovascular events 
 Adverse events (note that clinically significant physical examinations and 
pathological ECG findings are reported as AE/SAE)

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 12 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
6. GENERAL ANALYSIS DEFI NITIONS
6.1 T REATMENT(S)
Patients will be randomised 4:4:1 to one of two BI 730357 treatment groups V (200 mg
b.i.d.) or U (400 mg q.d.); treatment group W will receive placebo. In Part 2, the trial
medication should be taken with a meal.
Patients will be analyzed according to the treatment to which they were randomized. The 
following study periods based on actual start and stop dates of study treatment administration 
are defined: 
Table 6.1: 1 Definition of treatment periods
Analysing Treatment 
Period
Start Date (including) Stop Date (excluding)
Screening Date of informed consent Date of medication 
randomization -1 day
On-treatment period Date of medication 
randomization
Date of last study 
medication intake + 7 days
Follow-up Date of last study medication 
intake +8 days
Last contact date
For the main safety analyses, Adverse Events (AEs) will be classified to one of the following 
time periods: “screening”, “on-treatment”, or “follow-up”. Section 7.3.4 of the protocol 
specifies that, all AEs and laboratory assessments with an onset between start of treatment and 
end of the residual effect period (REP), a period of 7 days after the last dose of trial 
medication for this trial, will be assigned to the “on-treatment” period for evaluation.
Detailed rules for assigning AEs to these time periods are listed below:
 If date of informed consent ≤AE onset date  <date of first drug administration, then the 
AE is assigned to “screening”;
 If date of first drug administration ≤AE onset date ≤date of last intake +7 days, then 
the AE is assigned to “on-treatment”;
 If AE onset date > date of last drug administration+7 days, then the AE is assigned to 
“follow-up”.
Section 7.3.4 of the protocol specifies that adverse events that start before first drug intake 
and deteriorate under treatment will also be considered as ‘treatment emergent’. Worsening 
will be determined by a more severe grade according to Rheumatology Common Toxicity 
Criteria (RCTC) Version 2.0.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 13 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
6.2 I MPORTANT PROTOCOL DEVIATIONS
A protocol deviation (PD) is important if it affects the rights or safety of the study subjects, 
or if it can potentially influence the primary outcome measurement(s) in a non-negligible 
way. Handling of iPDs in analysis is included in the DV domain specifications and stored 
within the Trial Master File (TMF) in the electronic Document Management System (eDMS). 
6.3 S UBJECT SETS ANALYSED
The following patient analysis sets are defined:
 Screened set:
   This screened set includes all patients who signed the informed consent form.
 Randomised set (RS):
The RS includes all patients who signed the informed consent form and were also 
randomised, regardless whether the patient was treated with trial medication or not.
 Treated set(TS)
:
The TS includes all patients in the RS who were documented to have taken at least 1 
dose of trial medication. Patients will be grouped based on the actual treatment 
received at the randomization visit and week 12 visit, if applicable.
 Full analysis set (FAS):
The FAS includes all patients in the RS who received at least 1 dose of trial 
medication and provided baseline and at least 1 post-randomisation measurement of 
PASI. Patients will be grouped according to the treatment to which they were 
randomized by IRT at the start of the trial.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 14 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
The FAS will be used for the analyses of demographics, baseline characteristics and all 
efficacy endpoints. The efficacy analyses will follow the intention-to-treat (ITT) principle in 
assigning patients to treatment groups, i.e., efficacy analyses will be analysed as randomised 
using the FAS. 
The TS will be used for the analyses of concomitant medication use, medical history, PsO 
therapy history, treatment exposure, compliance, and safety (including adverse events, 
laboratory measurements, vital signs, and ECG). Safety analyses will assign patients to the 
treatment group based on the actual treatment received. 
If a patient erroneously receives the wrong dose of trial drug, the patient’s efficacy data will 
be analysed using the randomized treatment group and the patient’s safety data will be 
analysed using the actual treatment group.
6.5 P OOLING OF CENTRES
This section is not applicable because centre/country is not included in the statistical model.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 15 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
6.6 H ANDLING OF MISSING DATA AND OUTLIERS
6.6.1 Efficacy data
General imputation rules for continuous and binary endpoints are described in protocol 
section 7.5. Every effort should be made to collect complete data at all visits.
The following rules will be used to impute for missing data:
 For all non-binary endpoints, LOCF (Last Observation Carried Forward) will be 
used to impute missing values.
 For all binary endpoints (i.e., endpoints that are either 1 (patient responded) or 0 
(patient did not respond)):
                - If no data after that visit*, then impute as failure (NRI [No Response 
Imputation])
                - If data at visits* before and after, only impute as success if both visits are 
successes; else impute as failure.
* Patients that take prohibited medications to treat PsO will be treated the same as those 
that discontinued from the trial, i.e., subsequent visits following start of prohibited 
medication will be considered as failure for binary endpoints.
If at any time a patient uses an inappropriate concomitant medication, then all future data will 
be treated as failure for binary variables and LOCF (using the last on-treatment observation 
prior to inappropriate concomitant medication use) for continuous variables. As part of the 
LOCF technique, baseline values will be carried forward if no post-baseline value is available.
If a patient is missing items from a questionnaire measured at a visit, these will be handled 
according to the instructions given in Section 10 of the protocol specific to each 
questionnaire. Missing items from the Quality of Life questionnaires will be handled 
according to the measure instructions (cf. CTP Appendix 10.6). If there is no data for a 
particular visit, then it will be imputed following the same rules as described in the protocol.
For the NAPSI, PSSI, and PPASI assessment, if the CRF is marked as “No” indicating that 
the patient does not have nail, scalp, palmo-plantar disease, then exclude such patients from 
the analysis for 
NAPSI, PSSI, and PPASI.
For efficacy endpoints which are continuous in nature, a restricted maximum likelihood 
(REML)-based mixed model repeated measures (MMRM) approach will be used for 
inferential analysis, if applicable. No imputation will be performed for data used in MMRM.
6.6.2 Safety data and other data
With respect to safety evaluations, it is not planned to impute missing values; and only 
observed values will be analysed.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 16 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
Missing or incomplete AE dates will be imputed according to BI standards “Handling of 
missing and incomplete AE dates” (2).
6.7 B ASELI
NE, TIME WINDOWS AND CALCULATED VISITS
For efficacy endpoints, baseline is defined as the pre-treatment observation at Visit 2. If Visit 
2 is missing, then Visit 1 will be used for baseline.
For laboratory safety measurements, the last measurements taken prior to the treatment start 
will be considered as baseline.
In general, measurements reported with a date only (and no time) and taken on the day of first 
administration of trial treatment will also be considered pre-treatment values.
The visit schedule with accompanying details can be found in Flow Chart 1 in the protocol. 
Measurements taken after start of treatment will be considered either on- or off-treatment 
values based on definition in Table 6.1: 1.
On-treatment measurements for EOT and EOS visit for early discontinued patients will be 
allocated to visits by means of time windows with the limit between adjacent windows half-
way between the planned dates for the visits; the middle day is counted to the window of the 
later visit. Mutually exclusive relative day windows are defined below to provide derived 
visits that correspond to the post-baseline time points. For example, Visit 6 is planned on Day 

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 17 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
29 and Visit 7 is planned on Day 57. Therefore, the window of Visit 6 reaches until Day 42 
while the window of Visit 7 starts on Day 43. The visit schedule with corresponding windows 
is given in Table 6.7: 1.
Table 6.7: 1 Time windows for assignment of on-treatment efficacy, safety lab, vital signs, 
and biomarker measurements to visits for statistical analysis
Window No. Window label Nominal visit Nominal day Interval
0 Baseline VISIT 2 1 N/A
1 Week 1 VISIT 3 4 [2,5]
2 Week 1 VISIT 4 8 [6,11]
3 Week 2 VISIT 5 15 [12,21]
4 Week 4 VISIT 6 29 [22,42]
5 Week 8 VISIT 7 57 [43,70]
6 Week 12 VISIT 8/EOT 
visit
84 [71,98]
7 Week 16 EOS 113 [99,∞]
If there are multiple values for an efficacy endpoint in one window (visit), use the one from 
scheduled visit. If value from scheduled visit is not present, the visit closest to the nominal 
day will be selected for assessing endpoints at a particular visit and for by-visit displays. If the 
visits are equidistant from the nominal day, then the earlier visit will be selected. All
measured values will be stored in analysis datasets. 
The same visit windows will be used for safety laboratory and vital sign assessments. If there 
are multiple safety or laboratory values in one time window on treatment, the worst value will 
be selected for the by-visit analyses.
Analysis of AE data, concomitant medication or non-drug therapies, as well as use of rescue 
medication will not be based on visits. Frequency tables for these data will be using on-
treatment data only. Therefore, no assignment to time windows will be necessary for such 
data.
While the nominal times listed in this section should be adhered to as closely as possible, the 
actual sampling times will be recorded and used for determination of pharmacokinetic 
parameters.
For visits without an assigned value based on time windows, a value will thereafter be 
imputed as defined in Section 6.6. LOCF imputation of efficacy endpoints, when applicable, 
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 18 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
will be performed based on all available observations obtained during the on-treatment period, 
irrespective of whether the observation was selected in any time window.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 19 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
7. P LANNED ANALYSIS
For End-Of-Text (EoT ) tables, the set of summary statistics is: N / Mean / SD / Min / Median 
/ Max. For appendix tables, the set of summary statistics is: N / Mean / SD / Min / Q1 (lower
quartile) / Median / Q3 (upper quartile) / Max.
Tabulations of frequencies for categorical data will include all possible categories and will 
display the number of observations in a category as well as the percentage (%) relative to the 
respective treatment group. Percentages will be rounded to one decimal place. The category 
“missing” will be displayed only if there are actually missing values. Percentages will be 
based on all patients in the respective patient set no matter whether they have non-missing 
values or not.
Planned treatment is defined as the treatment to which one patient has been assigned by IVRS 
at randomization visit (visit2). 
Subject data listings of data used in the analyses (i.e. demographic and baseline characteristics 
and key efficacy endpoints) will also be provided and included in Appendix 16.2 of the CTR.
Disposition of the patient population participating in the trial will be summarised by 
presentation of the frequency of patients screened, entered, screened but not entered, treated, 
entered but not treated. Within treated patients, data will be summarized by treatment ongoing 
patients, patients complete planned treatment period and patients who are prematurely 
discontinued, by reason. Disposition will be listed by country.
7.1 D EMOGRAPHIC AND OTHER BASELINE CHARACTERISTICS
Only descriptive statistics are planned for this section of the report. Demographic parameters 
collected and to be presented include, but are not limited to, the following:
 Gender (Male, Female)
 Race and ethnicity (as defined in the eCRF)
 Age [years]
 Height [cm]
 Weight [kg] (continuous)
 Weight Group (>100kg vs. < 100 kg)
 Body mass index [kg/m2] (defined as weight [kg]/(height [cm]/100)2)
 Body mass index category (>30 kg/m2 vs. <30 kg/m2)
 Smoking history (Never-smoked, Former-smoker, Currently smokes)
 Alcohol History (Never-drinker, Former-drinker, Current-drinker)
 Region and country
 Prior biologic use for psoriasis (Yes/No)
Baseline disease characteristic to be presented include, but are not limited to, the following: 
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 20 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
 BSA (Visit 1)
 PASI score
 sPGA
 NAPSI, PPASI, PSSI
 Pain VAS
 PSS total score
 DLQI
 Duration of Psoriasis [years]
 PsA history (diagnosed, suspected, no PsA)
For NAPSI, PPASI, PSSI and pain-VAS, report is only based on patients who have such 
applicable measurements per protocol, e.g. pain VAS is reported only among patients with 
psoriatic arthritis.
Number (%) of patients with psoriasis therapy history will be summarized, including both 
non-topical drug therapy and non -drug therapy.
7.2 C ONCOMITANT DISEASES AND MEDICATION
Only descriptive statistics are planned for this section of the report, based on the treated set.
A table of the number (%) of patients with concomitant diagnoses from baseline condition by 
system organ class (SOC) and preferred term (PT) will be included. Concomitant diagnoses 
will be coded with the most recent version of MedDRA in effect at database lock.
Concomitant medication will be described as a table of number (%) of patients. Depending on 
if concomitant medication stops before trial treatment starts or not, medication information
collected from eCRF pages will be classified as historical medication or on-treatment 
concomitant medication, and a summary table will be provided for each of the two categories.
Historical medication is defined as medication taken prior to the start of trial treatment and 
stopped before trial treatment starts. There are two scenarios for on-treatment concomitant 
medications:
 Scenario 1: 
medication start date or stop date is between first dose of trial treatment 
and last dose of trial treatment plus 7-day REP;
or
 Scenario 2: medication stop date is after ‘last dose of trial treatment plus 7-day REP’, 
and medication start date is before ‘last dose of trial treatment plus 7-day REP’.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 21 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
7.3 T REATMENT COMPLIANCE
Treatment non-compliance, as one type of important protocol deviations (iPDs), is defined as 
any randomized patients having taken at least one dose of study medication with an overall 
compliance rate not between 80% and 120% inclusive. Overall compliance rate is calculated 
based on unweighted average of study drug compliance rate across all visits during the 
treatment period. For patients who discontinued the study treatment prematurely, only the 
visits on or before premature discontinuation will be used for the calculation of overall 
compliance rate.
Treatment compliance will be reported from baseline to Week 12 based on calculation as 
described in CTP section 4.3. When presenting the compliance rate of study medication by 
visit, if patients discontinue treatment prematurely, then their compliance data collected at 
EOT visit is mapped to the next originally planned visit per protocol for reporting. For 
example, if one patient prematurely discontinues the study treatment at Week 10 and comes to 
site for EOT visit, then his/her compliance data collected at EOT visit is mapped to Week 12 
for reporting purpose. That compliance rate should be interpreted as the compliance rate for 
his
/her participation days in the window between planned Week 8 and Week 12.
Only descriptive statistics are planned for this section of the report. Summary statistics of 
compliance in the treated set will be given for the number of subjects as well as the 
corresponding percentage with compliance in the categories <80%, 80% - 120%, >120%, 
missing.
7.4 P RIMARY ENDPOINT(S)
7.4.1 Primary analysis of the primary endpoint(s)
The co-primary endpoint ‘achievement of PASI 75 at Week 12’ will be summarized in the 
form of proportion of patients achieving PASI 75 at Week 12 as an outcome measure so as to 
perform the primary analysis.
For Part 2 of 1407-0030, the primary analysis on PASI 75 at week 12 will be based on a 
Bayesian borrowing approach. An informative prior is derived for the placebo control group 
based on historical placebo data. The derivation of the informative prior is based on a meta-
analytic predictive (MAP) prior approach which is additionally robustified against prior-data 
conflicts by adding a vaguely informative component to the prior.
A Bayesian approach with an informative mixture beta prior for the placebo group will be
used. The prior is a combination of a mixture of informative beta priors derived from
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 22 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
historical trials and a vaguely informative beta prior. The weight on the vaguely informative
beta prior is 50%. The prior mentioned in the protocol is now updated based on additional 
historical information being available to: 
Non-informative beta prior Beta(1, 1) is used for BI 730357 active treatment arms. 
The proportions of 200 mg b.i.d. and 400 mg q.d. recipients who achieve PASI 75
improvement criteria at Week 12, will be respectively compared with that of placebo
recipients. For that purpose, the posterior probability distribution for the risk difference will
be evaluated and compared to specific boundary values. The dual criteria will be assessed to
evaluate the effect of BI 730357: (1) significance: a posterior probability of at least 90% that
the PASI 75 response rate for patients on BI 730357 arm is higher than that for patients on
placebo arm
; and (2) relevance: a posterior probability of at least 50% that the PASI 75 
response rate for patients on BI 730357 arm is higher than that for patients on placebo arm by 
various boundary values. If at least one dose satisfies both criteria based on PASI 75 response 
rate, it is considered as “pass”. If neither doses have significance or relevance criteria been 
met, it is considered as “not pass”. Otherwise it is in the “consider” zone. When falling in 
‘consider zone’ based on PASI 75 response rate, sPGA 0/1 at week 12 will be jointly 
evaluated.
The calculations for the Bayesian posterior probability calculation are based on R-package
RBesT Version 1.6.1 and R version 4.0.1(2020-06-06).
The primary analysis for sPGA clear or almost clear at week 12 will be summarizing the 
proportion of responders in each arm together with 90% and 95% exact confidence intervals.
7.4.2 S econdary analyses for the co-primary endpoints
The secondary analyses for PASI 75 at week 12 include:
 summarizing the proportion of responders in each arm 
together with 90% and 95% 
exact confidence intervals.
 Calculating the unadjusted absolute difference in proportion between active treatment 
group and placebo group
, 90% and 95% confidence intervals together with a 
corresponding p-value to investigate if the active treatment group has a different
response rate from the placebo group based on Chi-square distribution;
The secondary analysis for sPGA clear or almost clear at week 12 is calculating the 
unadjusted absolute difference in proportion between active treatment group and placebo 
group, 90% and 95% confidence intervals together with a corresponding p-value to 
investigate if the active treatment group has a different response rate from the placebo group 
based on Chi-square distribution.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 23 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 24 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 25 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
7.5 S ECONDARY ENDPOINT(S)
7.5.1 Key secondary endpoint(s)
This section is not applicable as no key secondary endpoint has been specified in the protocol.
7.5.2 (Other) Secondary endpoint(s)
The same methods as discussed previously for the secondary analyses for the summary 
measure of the co-primary endpoint ‘PASI 75 at week 12’ will be used to analyse clinical 
binary secondary endpoints for each treatment group as well as treatment comparison.
Psoriasis Area and Severity Index (PASI)
Treatment comparison for unadjusted absolute difference in proportion between active groups 
and placebo group will be performed for achievement of 50% (PASI50), 90% (PASI90), 
100% (PASI 100) at week 12.
Static Physician's Global Assessment (sPGA)
The sPGA is scored using the following levels of assessment:
0 – clear;
1 - almost clear;
2 – mild;
3 – moderate;
4 -  severe
Details for scoring sPGA and its components are described in Section 10.2 of the CTP.
Treatment comparison for unadjusted absolute difference in proportion between active groups 
and placebo group will be performed for sPGA equals to 0 
at week 12.
PSS total score change from baseline at week 12
For change from baseline in PSS total score at Week 12 and treatment comparison, a 
restricted maximum likelihood (REML)-based mixed model repeated measures (MMRM) 
approach will be used. The analyses will include the fixed, categorical effects of treatment,
visit, and treatment-by-visit interaction, as well as the continuous, fixed covariates of baseline 
PSS total score and baseline PSS score-by-visit interaction. Patient will be considered as a 
random effect.  An unstructured covariance structure for within subject variation will be used.
DLQI score of 0 or 1 at week 12

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 26 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
For DLQI, if one question is left unanswered, this is scored 0 and then the total score is 
summed and expressed as usual out of a maximum of 30.
Achievement of a Dermatology Life Quality Index (DLQI) score of 0 or 1 at week 12 will be 
analysed by treatment comparison of unadjusted absolute difference in proportion between 
active groups and placebo group with 90% and 95% confidence intervals.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 27 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 28 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 29 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
7.7 E XTENT OF EXPOSURE
Exposure will be presented as categorized period of “1-28”, “29-56”, “57-84” and 
“>85” days based on dose received for total study medication intake. Exposure will be 
summarized and presented for first 12 weeks of treatment. 
7.8 S AFETY ANALYSIS
All safety analyses will be performed on the treated set.
7.8.1 Adverse Events
The analyses of adverse events will be descriptive in nature. All analyses of AEs will be based 
on the number of patients with AEs (not the number of AEs).
The analysis of adverse events will be based on the concept of treatment emergent adverse 
events. That means that all adverse events occurring between first drug administration and 
within 7 days after last drug administration will be assigned to the assign
ed treatment. Section 
7.3.4 of the protocol specifies that adverse events that start before first drug intake and 
deteriorate under treatment will also be considered as ‘treatment emergent’. Worsening will 
be determined by a more severe grade according to Rheumatology Common Toxicity Criteria 
(RCTC) Version 2.0.
All adverse events occurring before first drug intake will be assigned to ‘screening’ and all 
AEs occurring after last drug intake + 7 days will be assigned to ‘follow-up’ (for listings 
only).
According to ICH E3 (6), in addition to Deaths and serious adverse events, ‘other significant’ 
AEs need to be listed in the clinical trial report. These will be any non-serious
adverse event that led to an action taken with study drug (e.g. discontinuation or dose
reduced or interrupted). An overall summary of adverse events will be presented.
The frequency of subjects with AEs will be summarised by treatment, primary system organ
class and PT using the version of MedDRA at the database lock. Separate tables will be
provided for subjects with SAEs, AEs leading to treatment discontinuation and related AEs.
The system organ classes will be sorted by default by decreasing frequency and PTs will be

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 30 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
sorted by decreasing frequency within SOC.
For further details on summarization of AE data, please refer to the guideline 'Handling and 
summarization of adverse event data for clinical trial reports and integrated summaries' (7).
The severity of AEs will be summarised by the maximum intensity of the events each patient had 
(as indicated by the recorded RCTC version 2 grade). This will show the number and percent of 
patients who had at most mild, moderate, severe, and life-threatening events. “Severe adverse 
event” is defined as an AE with RCTC grade equals to 3 (severe) or 4 (life threatening).
Groupings of adverse events and adverse events of special interest (AESI)
The term “adverse events of special interest (AESI)” relates to any specific AE that has 
been identified at the project level as being of particular concern for prospective safety 
monitoring and safety assessment within this trial, e.g., the potential for AEs based on 
knowledge from other compounds in the same class.
AESIs need to be reported to the sponsor’s Pharmacovigilance Department within the 
same timeframe that applies to SAEs.
The AESI have bee n defined in section 5.2.6.1 of the protocol.
Other user-defined special adverse event grouped term for BI 730357 specified in Table 
7.8.1:1 will be reported.
Table 7.8.1:1 Other user-defined special groupings of adverse events
N Term Definition #
1 SMQ Drug Related Hepatic 
Disorders
SMQ Drug related hepatic disorders –
comprehensive search (20000006)
2 SMQ Opportunistic infections MedDRA SMQ Opportunistic Infections (narrow -
20000235)
3 Tuberculosis related terms BIcMQ “Tuberculosis related terms” BIcMQ 
(30000107)(broad)
4 Severe infections SOC “Infections and infestations” with eCRF 
severity grade >= Rheumatology Common Toxicity 
Criteria (RCTC) Grade 3 – MedDRA (soc code 
10021881 mppath=1)
5 Gastritis related terms 
• BIcMQ Gastritis (broad) [32008061]
6 Malignancies including all sub-
SMQs
- SMQ broad (20000090)
Merge medbase by mptcd to all HLT terms
# This column indicates whether the Term(s) provided in the first column are MedDRA 
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 31 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
preferred terms (PT), Standardised MedDRA Queries (SMQ) or BI customised 
MedDRA Queries (BIcMQ).
In addition, the adjudication outcome of Cerebro-cardiovascular events from the vendor, 
, will be summarized by indication,  treatment, primary system organ class and 
preferred term.
  
AE summaries
An overall summary of adverse events will be presented. The frequency of patients with 
adverse events will be summarized by treatment, primary system organ class and preferred 
term according to MedDRA. Separate tables will be provided for patients with:
 Investigator defined drug-related AEs
 Investigator defined drug-related serious AEs
 AESIs
 AEs leading to discontinuation
 Serious AEs
 Other significant AEs 
 AE by worst RCTC intensity
 Special AE grouped term (or called “user-defined AE category”) specified in Table 
7.8.1:1
7.8.2 Laboratory data
The analyses of laboratory data will be descriptive in nature and will be based on BI 
standards.  
The number and perce nt of patients with possibly clinically significant on-trea tment
abnormalities as identified by use of c lin ically significant ranges for each laboratory
paramet e r collected will be presented. The patients with possibl y clinically significant
abnormalities will be identified within the initial on-treatm e nt period by study treatment.
Each laboratory value will be grad ed using the RCTC (version 2.0) grading of laboratory 
abnormalities. A summary table of the Baseline grade compared with the last available on -
treatment grade will display the number and percent of each type of transition in grade by
lab
oratory parameter within each treatment period, and treatment group. A second table will 
show the number and perce nt of patients with each type of transition from Baseline to their 
w
orst on-trea tment grade p a rameter within each treatment period, and treatment group. For 
these shift tables, only the double blind period will be considered. Parameters using
categorised values, such as the urinalysis parameters, will show the shift table among those 
values in a similar manner to the RCTC g raded values. 
A gra
phical summary highlighting potential cases of Hy’s Law within each treatment

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 32 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
group will be presented. The maximum on-treatment values of total bilirubin and ALT 
will be plotted each on a s cale as multiples of the upper limit of normal. The figure will
show areas that meet the criteria of cholestasis (total bilirubin > 2x ULN), Templ e ’s 
corollary (ALT > 3 x ULN) and Hy’s L a w as the combination of these two fact o rs. A 
similar figure using maximum AST values in place of ALT will be constructed. An 
accompanying listing will show by sample date and study day thefull course of the total 
bilirubin, ALT, AST and alkaline phosphatase values for patients whose tot al bilirubin 
are > 2xULN or AST or A LT values > 3 x ULN at any time during the study (all
treatment periods). The listing will indicate where the value meets the criteria, either
falling in the cholestasis range, that for T emple’s corollary or where the combination 
mee
ts that for Hy’s Law itself.
Laboratory measurements taken up to the residual effect period of 7 days after the last 
administration of randomized study drug will be considered as on-treatment.
Study visits will be presented by the Visit labels in Table 6.7 :1.
Listing and descriptive statistics of laboratory values over time as well as median and 
interquartile range (IQR) of changes between baseline and extreme abnormal value on 
treatment will be provided. Baseline is understood as the last available measurement before 
study drug administration. Extreme abnormal value on treatment is understood as the on 
treatment laboratory value which is most significantly away from the reference range.
Frequency of patients with transitions relative to reference range and listing of patients with 
significant abnormal laboratory values will be presented as well.
In cases of repeated measurements performed for the same visit the last observation will be 
used for tabulations.
7.8.3 Vital signs
Only descriptive statistics are planned for this section of the report.
7.8.4 ECG
Relevant findings at baseline were reported as baseline conditions, and other findings on 
ECGs were reported as AEs and analyzed accordingly.
7.8.5 Others
C
-SSRS
The individual items and categories of suicidal ideation and behaviour from the C-SSRS will 
be summarized through descriptive statistics.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 33 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
8. TIMEPOINT OF RELEASE OF TREATMENT 
INFORMATION
Fast-track approach:
Once the last patient has completed their End-of-Treatment (EOT) visit and all corresponding 
data has been entered and cleaned to the level documented in the “Data Delivery Request” 
(DDR) form, the data will be declared ready to be unblinded via the “Data Ready to be 
Unblinded and/or Final Trial Cl
osure Notification” (RUN) form. Then the treatment 
information will be released for analysis.
The data collection for the off-treatment residual effect period until the End-of-Study (EoS)/ 
Follow-Up visit will continue into the unblinded trial database. Once trial data collection has 
been completed and all data has been entered and cleaned as documented on the RUN form, a 
final data lock will be performed.
After the release of treatment information, it is expected that only trial data related to the off-
treatment residual effect period will be entered and changed. Therefore, after the timepoint of 
release of treatment information, all changes affecting trial data up to the End-of-Treatment 
(EoT) visit will be documented and summarized in the CTR.
Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 34 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
9. REFERENCES
1. CPMP/ICH/363/96: "Statistical Principles for Clinical Trials", ICH Guideline Topic E9, 
Note For Guidance on Statistical Principles for Clinical Trials, current version.
4. Bias reduction of maximum likelihood estimates. Firth, D. Biometrika.
1993; 80 (1): 27-38. [R20-2291]      
5. Ge, M., Durham, L. K., Meyer, R. D., Xie, W., & Thomas, N. (2011). Covariate-
adjusted difference in proportions from clinical trials using logistic regression and 
weighted risk differences. Drug information journal: DIJ/Drug Information Association, 
45(4), 481-493  [R16-5360]
6. CPMP/ICH/137/95: “Structure and Content of Clinical Study Reports”, ICH Guideline 
Topic E3; Note For Guidance on Structure and Content of Clinical Study Reports, 
current version, EMA webpage.

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 35 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 36 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 37 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 38 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 39 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 40 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 41 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 42 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021

Boehringer Ingelheim
TSAP for BI Trial No: 1407-0030 Part 2
c35536779
-01
Page 43 of 43
Proprietary confidential information © 2021 Boehringer Ingelheim International GmbH or one or more of its affiliated companies
001-MCS-50-415_RD-01 (3.0) / Saved on 18 Jan 2021
11. HISTORY TABLE
Table 11: 1 History table
Version Date Author Sections 
changed
Brief description of change
1 12-May-2021 None This is the final TSAP 
