Property of Novartis
For business use only
May not be used, divulged, published or otherwise disclosed
without the consent of Novartis
Biostatistics & Statistical Programming / 
Novartis Institutes for BioMedical Research
KAE609
CKAE609X2111 / NCT04321252
A randomized, subject and investigator-blinded, placebo 
controlled, single and multiple ascending dose study to 
assess the safety
, tolerability, and pharmacokinetics of 
KAE609 administered intravenously in healthy subjects
Statistical Analysis Plan (SAP)
Author(s):
Document type: SAP Documentation – NIBR
Document status: Final
Release date: 29-Apr-2021
Number of pages: 12
Personal Protected Data
Novartis For business use only Page 2
SAP Amendment 1 CKAE609X2111
Commercially Confidential Information
Novartis For business use only Page 3
SAP Amendment 1 CKAE609X2111
Table of contents
Table of contents .................................................................................................................3
List of tables ........................................................................................................................3
1 Introduction .........................................................................................................................4
1.1 Scope of document ..................................................................................................4
1.2 Study reference documentation ...............................................................................4
1.3 Study objectives.......................................................................................................4
1.4 Study design and treatment......................................................................................5
2 First interpretable results (FIR) ...........................................................................................7
3 Interim analyses...................................................................................................................7
4 Statistical methods: Analysis sets........................................................................................7
5 Statistical methods for Pharmacokinetic (PK) parameters
..................................................8
5.1 Variables..................................................................................................................8
5.2 Descriptive analyses ................................................................................................8
5.3 Statistical model, assumptions and hypotheses .......................................................9
5.3.1 Model checking procedures ....................................................................9
5.3.2 Graphical presentation of results.............................................................9
6 Statistical methods for Pharmacodynamic (PD) parameters ...............................................9
7 Statistical methods for safety and tolerability data..............................................................9
7.1 Variables................................
..................................................................................9
7.2 Descriptive analyses ..............................................................................................10
7.3 Graphical presentation...........................................................................................12
8 Statistical methods for biomarker data
..............................................................................12
9 Exploratory objectives.......................................................................................................12
List of tables
Table 4
-1 Protocol deviation codes and analysis sets..............................................8
Commercially Confidential Information
Novartis For business use only Page 4
SAP Amendment 1 CKAE609X2111
1 Introduction
1.1 Scope of document
The RAP documents contain detailed information to aid the production of Statistics & 
Programming input into the Clinical Study Report (CSR) for trial “CKAE609X2111”.
The Statistical analysis plan (SAP) 
describes the implementation of the statistical analysis 
planned in the protocol.
1.2 Study reference documentation
Final study protocol (v02) and site operation manual (SOM v01) are available at the time of 
finalization of the original Statistical Analysis Plan.
1.3 Study objectives
Objective(s) Endpoint(s)
Primary objective(s) Endpoint(s) for primary objective(s)
 To assess the safety and tolerability of single
and multiple iv doses of KAE609 in healthy
subjects
 Adverse events, physical examination
findings, vital signs, ECG
findings (including QTcF), safety
laboratory assessments including
chemistry, hematology, and urinalysis
results
Secondary objective(s) Endpoint(s) for secondary objective(s)
 To assess the pharmacokinetics (PK) of single
and multiple iv doses of KAE609 in healthy
subjects
 AUC, Tmax, Cmax, CL, Vz, and T1/2
 To assess local tolerance at infusion site of
KAE609 iv administration
 Findings of physical examination of
infusion site
Commercially Confidential Information
Novartis For business use only Page 5
SAP Amendment 1 CKAE609X2111
1.4 Study design and treatment
This is a randomized, subject and investigator-blinded, placebo-controlled, single and multiple 
ascending iv dose study in healthy subjects. The study consists of two parts and the study 
scheme is shown in Figure 1-1:
 Part A is a single ascending dose (SAD) study with 5 cohorts of 8 subjects each
 Part B is a multiple ascending dose (MAD) study with 2 cohorts of 9 subjects each
For both parts of the study, each subject will participate in an up to 28- day screening period 
during which a full physical examination, medical history, drug screening, vital signs, ECG 
evaluation and safety laboratory tests evaluation will be performed.
A review of safety and PK data will be conducted at the completion of each cohort prior to 
dosing of the next subsequent cohort.  Safety assessments will include physical examinations, 
ECGs, vital signs, standard clinical laboratory evaluations (hematology, blood chemistry, 
urinalysis) adverse event and serious adverse event monitoring.
Part A: Single-ascending dose study
In Part A sequential cohorts of 8 healthy subjects per cohort will be randomized to receive 
successively higher single iv doses of KAE609 or matching placebo. In each cohort, subjects 
will be randomized in a 3:1 ratio to KAE609 (6 subjects/cohort) or matching placebo (2 
subjects/cohort). Four planned dose cohorts will be included in Part A (A1, A2, A3 and A4).  
Commercially Confidential Information
Commercially Confidential Information
Novartis For business use only Page 6
SAP Amendment 1 CKAE609X2111
Figure 1-2 Study design - SAD
Part B: Multiple-ascending dose study
In Part B sequential cohorts of 9 healthy subjects per cohort will be randomized to receive 
successively higher iv doses of KAE609 or matching placebo. Two planned dose cohorts will 
be included in Part B (B1 and B2). For Cohort B1, healthy subjects will receive a 60 mg dose 
of KAE609 or matching placebo iv q24h for 5 days. . For Cohort B2, healthy subjects will 
receive a 120 mg dose of KAE609 or matching placebo iv q24h for 5 days. In each cohort, 
subjects will be randomized in a 2:1 ratio to KAE609 (6 subjects/cohort) or matching placebo 
(3 subjects/cohort).
Commercially Confidential Information
Commercially Confidential Information
Commercially Confidential Information
Novartis For business use only Page 7
SAP Amendment 1 CKAE609X2111
Figure 1-3 Study design - MAD
2 First interpretable results (FIR)
3 I nterim analyses
4 Statistical methods: Analysis sets
For subjects for which the actual treatment received does not match the randomized treatment,
the treatment actually received will be used for the analysis.
Commercially Confidential Information
Commercially Confidential Information
Commercially Confidential Information
Commercially Confidential Information
Novartis For business use only Page 8
SAP Amendment 1 CKAE609X2111
The safety analysis set will include all subjects who received at least one dose of any study drug.
The PK analysis set will include all subjects with at least one available valid (i.e. not flagged 
for exclusion) PK concentration measurement, who received any study drug and experienced 
no protocol deviations with relevant impact on PK data.
The analysis sets and protocol deviation codes are related as follows:
Table 4-1 Protocol deviation codes and analysis sets
Category
Deviation code
Text description of deviation Data exclusion
Subjects are excluded from PK analysis in case of these PDs: 
TRT01 Incorrect dose administered Exclude subject from PK 
analysis set at 
pharmacokineticist 
discretion
If updates to this table are needed, an amendment to the SAP needs to be implemented prior to 
DBL.
5 Statistical methods for Pharmacokinetic (PK) parameters
The secondary objective is to evaluate the pharmacokinetics of single and multiple ascending 
iv doses of KAE609 in healthy subjects.
5.1 Variables
The pharmacokinetic parameters are described as follows and will be calculated separately from 
the KAE609 concentration data:
 Part A (SAD): Cmax, Tmax, AUClast, AUCinf, AUC0-t (AUC0-24), T1/2, Vss and CL
 Part B (MAD): Cmax, Tmax, AUC0-24h, T1/2 Day 1  and Cmax, Tmax, AUCtau
(AUC0-24), AUClast, , T1/2, Vss and CL
5.2 Descriptive analyses
For each part, KAE609 plasma concentration data will be listed by subject, and visit/sampling 
time point. Descriptive summary statistics will be provided by treatment and visit/sampling 
time point, 
Summary s tatistics will include mean (arithmetic and geometric), SD, CV (arithmetic and 
geometric), median, minimum and maximum. 
PK parameters will be listed by s ubject. Descriptive summary s tatistics will include mean 
(arithmetic and geometric), SD, and CV (arithmetic and geometric), median, minimum and 
Commercially Confidential Information
Commercially Confidential Information
Commercially Confidential Information
Novartis For business use only Page 9
SAP Amendment 1 CKAE609X2111
maximum. An exception to this is Tmax where median, minimum and maximum will be 
presented.
5.3 Statistical model, assumptions and hypotheses
5.3.1 Model checking procedures
Graphical check will be performed.
5.3.2 Graphical presentation of results
Arithmetic mean (SD) plasma concentration data will be plotted across time, with separate line
types for each treatment.
Overlaying individual plasma concentration-time profiles will be generated.
Scatterplots of Cmax and AUC parameters versus dose will be created with the estimated power 
model curve overlaid.
6 Statistical methods for Pharmacodynamic (PD) parameters
Not applicable.
7 Statistical methods for safety and tolerability data
The primary objective of this study is to assess the safety and tolerability of single and multiple 
ascending iv doses of KAE609 in healthy subjects.
7.1 Variables
The primary safety and tolerability variables are adverse events, vital signs (blood pressure, 
pulse rate, body t emperature), ECG intervals, laboratory m easurements, as well as subject 
demographics, baseline characteristics, and treatment information.
Commercially Confidential Information
Novartis For business use only Page 10
SAP Amendment 1 CKAE609X2111
7.2 Descriptive analyses
Subject demographics and other baseline characteristics
All data for background and demographic variables will be listed by  part, treatment group and 
subject. Summary statistics will be provided by part and treatment group.
Relevant medical history, current medical conditions, results of laboratory screens, drug tests 
and any other relevant information will be listed by part, treatment group and subject.
Treatment
Data for study drug administration (rescue medication) and concomitant therapies will be listed 
by part, treatment group and subject.
Vital signs
All vital signs data will be listed by treatment, subject, and visit/time and if ranges are available 
abnormalities (and relevant orthostatic changes) will be flagged. Summary statistics will be 
provided by part, treatment and visit/time.
ECG evaluations
All ECG data will be listed by treatment, subject and visit/time, abnormalities will be flagged. 
Summary statistics will be provided by part, treatment and visit/time.
Clinical laboratory evaluations
All laboratory data will be listed by treatment, subject, and visit/time and if normal ranges are 
available abnormalities will be flagged. A separate listing is provided presenting all parameters 
in a subject with any abnormal values. Summary statistics will be provided by part, treatment 
and visit/time.
Local tolerance at infusion site
Local tolerance at infusion site will be summarized by part and treatment group. 
Adverse events
All information obtained on adverse events will be displayed by part, treatment and subject.
The number and percentage of subjects with adverse events will be tabulated by system organ 
class and preferred term with a breakdown by treatment, and separately by preferred term and 
treatment. A subject with multiple adverse events within a system organ class is only counted 
once towards the total of this system organ class and treatment.
The number and percentage of subjects with adverse events by maximum severity of adverse 
events will be tabulated by s ystem organ class and preferred term with a breakdown by 
treatment.
The number and percentage of subjects with adverse events classified as related to study drug 
will be tabulated by system organ class and preferred term with a breakdown by treatment.
For the legal requirements of ClinicalTrials.gov and EudraCT, two required tables on all <on -
treatment/treatment emergent> adverse events which are not serious adverse events and on all 
<on-
treatment/treatment emergent> serious adverse events and SAE suspected to be related to 
Novartis For business use only Page 11
SAP Amendment 1 CKAE609X2111
study treatment will be provided by system organ class and preferred term on the safety set 
population.
If for a same subject, several consecutive AEs (irrespective of study t reatment causality, 
seriousness and severity) occurred with the same SOC and PT:
 a single occurrence will be counted if there is  ≤ 1 day gap between the end date of the
preceding AE and the start date of the consecutive AE
 more than one occurrence will be counted if there is > 1 day gap between the end date
of the preceding AE and the start date of the consecutive AE.
For occurrence, the presence of at least one SAE / SAE suspected to be related to study 
treatment / non SAE has to be checked in a block e.g., among AE's in a ≤ 1 day gap block, if at 
least one SAE is occurring, then one occurrence is calculated for that SAE.
The number of deaths resulting from SAEs suspected to be related to study treatment and SAEs 
irrespective of study treatment relationship will be provided by SOC and PT.
Holter ECG data analysis
The relationship between change from baseline in time-matched QTcF and KAE609 plasma 
concentration will be explored using linear mixed effects modeling. Other ECG parameters (QT, 
QTcB, HR, PR interval and QRS) will be summarized. Data from the SAD and MAD parts of 
the study will be pooled for this assessment. The change from baseline in QTcF will be the 
dependent variable in the model, KAE609 plasma concentration will be a covariate, and time a 
categorical variable. A random intercept for each subject will be specified. Placebo subjects 
will be included in the analysis with a plasma concentration of 0. The placebo-corrected change 
from baseline in QTcF and the two-sided 90% confidence interval will be extracted from the 
model at the geometric mean maximum plasma concentration for each treatment.
A plot of raw QTcF  change vs KAE609 plasma concentration will be presented together with 
the estimated slope and 90% Confidence Interval (CI) from the statistical model.
The analysis results for categorical outliers and T-
wave morphology will be summarized in 
frequency t ables with counts and percentages for both number of subjects and number of 
timepoints. For categorical outliers, the number of subjects (%) and timepoints will be 
determined by treatment group for the following:
 increase in QTcF from baseline of > 30 ms and > 60 ms
 absolute QTcF values  > 500 ms
 PR change from baseline > 25% increase resulting in PR > 220 ms
 QRS change from baseline > 25% increase resulting in QRS > 120 ms
 heart rate change from baseline > 25% decrease resulting in heart rate < 50 beats per
minute
 heart rate change from baseline > 25% increase resulting in a heart rate > 100 beats per
minute
For T-wave morphology, the analysis will be focused on the treatment emergent changes.
A cardiac safet
y report will be prepared separately.
Novartis For business use only Page 12
SAP Amendment 1 CKAE609X2111
7.3 Graphical presentation 
Boxplots to visualize trends in longitudinal safety d ata (vitals, ECG, lab parameter) will be 
created.
8 Statistical methods for biomarker data
Not applicable.
9 Exploratory objectives
Commercially Confidential Information