Biostatistics & Statistical Programming / 
Novartis Institutes for BioMedical Research
LLG783
CLLG783X2201
A Patient and Investigator-blinded, randomized, placebo-
controlled study of LLG783 in subjects with peripheral 
artery disease (PAD) and intermittent claudication
Statistical Analysis Plan (SAP)
Author(s):
Document type: SAP Documentation – NIBR 
Document status: Amendment 1/Final
Release date: 08-Feb-2019
Number of pages: 22
Property of Novartis
For business use only
May not be used, divulged, published or otherwise disclosed
without the consent of Novartis
Personal Protected Data
Novartis For business use only Page 2
SAP Amendment 1 CLLG783X2201
Corporate Confidential Information
Novartis For business use only Page 3
SAP Amendment 1 CLLG783X2201
Table of contents
Table of contents .................................................................................................................3
List of tables ........................................................................................................................4
List of figures ......................................................................................................................4
1 Introduction..............................................................................................................5
1.1 Scope of document ..................................................................................................5
1.2 Study reference documentation ...............................................................................5
1.3 Study objectives.......................................................................................................5
1.3.1 Primary objective(s) ................................................................................5
1.3.2 Secondary objective(s) ............................................................................5
1.4 Study design and treatment......................................................................................7
2 First interpretable results (FIR) ...............................................................................8
3 Interim analyses .......................................................................................................8
4 Statistical methods: Analysis sets............................................................................9
5 Statistical methods for Pharmacokinetic (PK) parameters .................................... 10
5.1 Variables................................................................
................................................11
5.2 Descriptive analyses ..............................................................................................11
6 Statistical methods for Efficacy/Pharmacodynamic (PD) parameters...................11
6.1 Primary objective...................................................................................................11
6.1.1 Variables ...............................................................................................12
6.1.2 Descriptive analyses..............................................................................12
6.1.3 Statistical model, assumptions and hypotheses.....................................12
6.2 Secondary objectives .............................................................................................13
6.2.1 Variables ...............................................................................................14
6.2.2 Descriptive analyses..............................................................................14
6.2.3 Statistical model, assumptions and hypotheses.....................................14
7 Statistical methods for safety and tolerability data................................................17
7.1 Variables................................
................................................................................17
7.2 Descriptive analyses ..............................................................................................18
7.3 Graphical presentation...........................................................................................19
8 Pharmacokinetic / pharmacodynamic relationships ..............................................19
9 Statistical methods for biomarker data .................................................................. 20
Corporate Confidential Information
Corporate Confidential Information
Novartis For business use only Page 4
SAP Amendment 1 CLLG783X2201
10 Reference list .........................................................................................................22
List of tables
Table 4-1 Protocol deviation codes and analysis sets............................................10
List of 
figures
Figure 1-1 Study design ............................................................................................ 7
Novartis For business use only Page 5
SAP Amendment 1 CLLG783X2201
1 Introduction 
1.1 Scope of document
The RAP documents contain detailed information to aid the production of Statistics & 
Programming input into the Clinical Study Report (CSR) for trial “CLLG783X2201”.
The Statistical analysis plan (SAP) describes the implementation of the statistical analysis 
planned in the protocol.
Tables, Figures, Listings (TFL) details the presentation of the data, including shells of summary 
tables, figures and listings, and Programming Datasets Specification (PDS) contains 
programming specifications e.g. for derived variables and derived datasets, to support the 
creation of CSR and IA outputs.
1.2 Study reference documentation
Final study protocol (version v00) is available at the time of finalization of Statistical Analysis 
Plan.
1.3 Study objectives
1.3.1 Primary objective(s)
Primary objective(s) Endpoints related to primary objectives
 To	evaluate	the	safety	and	tolerability
of	 LLG783 in subjects with PAD and
intermittent claudication after 16 weeks
of exposure to LLG783.
 AEs (including observations made
during physical examinations as
appropriate)
 Incidence
 Severity
 Vital signs including:
 Pulse rate
 Blood pressure (BP)
 Respiratory rate
 Body temperature
 Laboratory evaluations
 Hematology
 Clinical chemistry
 Urinalysis
 Electrocardiogram (ECG) intervals
 To evaluate the effect of LLG783 on
functional capacity a fter 3 months of
treatment in subjects with PAD and
intermittent claudication.
 Maximum walking distance assessed by
6-minute walk test (6MWT)
1.3.2 Secondary objective(s)
Secondary objective(s) Endpoints related to secondary objectives
Novartis For business use only Page 6
SAP Amendment 1 CLLG783X2201
 To investigate the PK of LLG783 in
subjects with PAD and intermittent
claudication.
 PK parameters will be determined,
including: AUCinf, AUClast, AUC0-t,
AUC0tau, Cmax and Tmax
 To evaluate the effect of LLG783 on
symptomatic functional capacity after 3
months of treatment in subjects with
PAD and intermittent claudication.
 Pain-free walking distance assessed by
6MWT
Corporate Confidential Information
Novartis For business use only Page 7
SAP Amendment 1 CLLG783X2201
1.4 Study design and treatment
This is a non-confirmatory, randomized, subject and investigator-blinded, placebo-controlled, 
parallel-group study in subjects with PAD and intermittent claudication. 
Approximately 4 0 randomized subjects will be treated in a 1:1 ratio to receive LLG783 or 
placebo as an i.v. infusion of  i.v. dosing once ev ery 4 weeks for a total of 4 doses over 
a period of 12 weeks/3 months. 
The dose may be altered based on review of data from the 1st interim analysis (IA). 
. 
Figure 1-1 Study design
It is intended that the s.c. study participants would maintain the same assessment visit schedule 
as the i.v. dosed study participants.
Subjects who discontinue the study for reasons other than safety prior to the week 16 visit may
be replaced to ensure ability to assess 40 subjects with a functional assessment after 16 weeks 
of exposure.
Corporate Confidential Information
CCI
CCI
Corporate Confidential Information
Novartis For business use only Page 8
SAP Amendment 1 CLLG783X2201
2 First interpretable results (FIR)
FIR  will focus on the following analyses:
1. Subject disposition
2. Demographics and baseline characteristics
3. Safety results
o Number and percentage of subjects with adverse events by preferred term.
o Overall incidence of AEs.
4. Efficacy results
o Arithmetic mean (80% CI) of 6MWT parameters vs time profile by treatment.
o MMRM model analysis of 6MWT parameters.
o Model estimated means of 6MWT parameters over time.
5. Pharmacokinetic results for Plasma
o Arithmetic mean (SD) concentration-time plot.
o Summary statistics for PK parameters.
6. Immunogenicity Data
3 I nterim analyses 
There are 2 planned IAs in this study. It is planned to conduct the first IA (IA1) once 
approximately 12 subjects reach 8 weeks following the first dose. The purpose of IA1 will be 
to assess the PK of LLG783 to make a dose adjustment should the exposure be significantly 
lower or higher than expected. 
Corporate Confidential Information
Corporate Confidential Information
Corporate Confidential Information
Corporate Confidential Information
Corporate Confidential Information
Corporate Confidential Information
Corporate Confidential Information
Corporate Confidential Information
Corporate Confidential Information

Novartis For business use only Page 9
SAP Amendment 1 CLLG783X2201
.
Unblinded IA results will be reviewed by the clinical team. The clinical team may communicate 
interim results (e.g. evaluation of efficacy c riteria or information needed for 
planning/modifying another study) to relevant Novartis teams for information, consulting 
and/or decision purposes.
Additional interim analyses may b e conducted to support decision making concerning the 
current clinical study, the sponsor’s clinical development projects in general or in case of any 
safety concerns. In this case, the analyses as described in the sections below are conducted for 
the relevant endpoints.
4 Statistical methods: Analysis sets
For subjects whose actual treatment received does not match the randomized treatment, the 
treatment actually received will be used for the analysis.
The safety analysis set will include all subjects that received any study drug.
The PK analysis set will include all subjects with at least one available valid (i.e. not flagged 
for exclusion) PK concentration measurement, who received any study drug and experienced 
no protocol deviations with relevant impact on PK data.
The PD analysis set will include all subjects with any available PD data, who received any study 
drug and experienced no protocol deviations with relevant impact on PD data.
The analysis sets and protocol deviation codes are related as follows:
Corporate Confidential Information
Corporate Confidential Information
Corporate Confidential Information
Novartis For business use only Page 10
SAP Amendment 1 CLLG783X2201
Table 4-1 Protocol deviation codes and analysis sets
Category
Deviation code
Text description of deviation Data exclusion
Subjects are excluded from PD analysis in case of these PDs: Exclude subject from PD
analysis set
COMD03 Change in type or dosage of narcotic pain 
relievers; OR Change in type or dosage of 
PAD specific symptom-relief drugs prior to 
week 16 of study.
Inc05 Deviation from inclusion criterion 5 –
Moderately impaired ambulatory function due 
primarily to PAD and maximum walk distance 
between 50 and 400 meters.
Exc02 Deviation from exclusion criterion 2 –
Pregnant or nursing (lactating) women.
Exc05b Deviation from exclusion criterion 05b –
Chronic heart failure New York Heart 
Association Class III or IV.
Exc14 Deviation from exclusion criterion 14 –
Patients unable to hold all narcotic pain 
relievers for 24 hours prior to performance of 
the 6MWT.
Inc03 Deviation from inclusion criterion 3 - On stable 
medical therapy for at least 4 weeks prior to 
the screening visit.
Exc03 Deviation from exclusion criterion 3 – Patients 
who meet the specific PAD related exclusion 
criteria.
If updates to this table are needed, an amendment to the SAP needs to be implemented prior to
DBL.
Dose adjustment might occur as part of the IA1 safety and tolerability conclusions. In case of 
dose adjustment occurring during the study, subjects will be analyzed under first dose received, 
censoring any observations post dose adjustment (if any) in statistical models and descriptive 
summaries. Further updates on the SAP analysis strategy d escribed below may be needed, 
depending on the findings of the IA1 and the proposed changes to the dosing strategy.
5 Statistical methods for Pharmacokinetic (PK) parameters
All subjects within the PK analysis set will be included in the PK data analysis.
In case of dose adjustment occurring during the study, subjects will be analyzed under first 
doses received, censoring any observations post dose adjustment (if any) in descriptive 
summaries. 
Novartis For business use only Page 11
SAP Amendment 1 CLLG783X2201
5.1 Variables 
If data permit and as applicable, the following pharmacokinetic parameters for the parent 
LLG783 will be determined using the actual recorded sampling times and non-compartmental 
method(s) with Phoenix WinNonlin (Version 6.4 or higher) from the serum concentration data.
 PK parameters related to secondary objectives:
- AUCinf, AUClast, AUC0-t, AUC0tau, Cmax, Tmax.
5.2 Descriptive analyses
LLG783 serum concentrations will be listed by treatment, subject, and visit/sampling time point. 
Descriptive summary statistics will be provided by treatment and visit/sampling time point, 
including the frequency (n, %) of concentrations below the LLOQ (and above the ULOQ) and 
reported as zero. Pharmacokinetic parameters will be listed by t reatment and subject and 
summarized by t reatment and visit. Summary s tatistics will include mean (arithmetic and 
geometric), SD, CV (arithmetic and geometric), median, minimum and maximum. An 
exception to this is Tmax where median, minimum and maximum will be presented.
Concentrations below LLOQ will be treated as zero in summary statistics and for PK parameter 
calculations. A geometric mean will not be reported if the dataset includes zero values.
Arithmetic mean (SD) serum concentration by time will be plotted on linear-linear and log-
linear scale (all treatment groups in the same graph).
Overlaying individual serum concentration by time profile, by treatment will be plotted (one 
graph per treatment group, all subjects in the same graph) on linear-linear and log-linear scale.
Individual serum concentration by time profile, by subject will be plotted on linear-linear and 
log-linear scale (one graph per treatment group and subject).
6 Statistical methods for Efficacy/P
harmacodynamic (PD) 
parameters
All subjects within the PD analysis set will be included in the PD data analysis.
In case of dose adjustment occurring during the study, subjects will be analyzed under first 
doses received, censoring any observations post dose adjustment (if any) in statistical models 
and descriptive summaries. 
6.1 Primary objective
To evaluate the effect of LLG783 on functional capacity after 3 months of treatment in subjects 
with PAD and intermittent claudication.
Corporate Confidential Information
Corporate Confidential Information
Novartis For business use only Page 12
SAP Amendment 1 CLLG783X2201
6.1.1 Variables 
The primary efficacy endpoint is the Maximum walking distance (MWD) defined as the total 
distance walked in 6 minutes as assessed by the 6MWT and will be used to evaluate functional 
capacity of PAD subjects participating in this study.
Change from baseline in MWD will also be derived. Baseline will be taken from the screening 
6-minute walk test.
6MWT data will be excluded from primary and secondary analyses under below conditions:
 within 24 hours after narcotic pain medication
 the very first 6MWT after the adverse event of COPD exacerbation
 all tests after post baseline stent or angioplasty procedures
 Lap distance for the 6
MWT significantly shorter than the recommended length of
50-70m
6.1.2 Descriptive analyses
Maximum walking distance (MWD) and change from baseline in MWD will be listed by 
treatment, subject and visit. Summary s tatistics will be provided for raw and change from 
baseline by t reatment and visit/time and will include sample size, mean (arithmetic), SD,
median, minimum, maximum. 
6.1.2.1 Graphical presentation of results
Arithmetic mean (80% CI) of raw MWD and change from baseline in MWD will be plotted by 
visit and treatment. Spaghetti plots of raw MWD and change from baseline in MWD of all 
individuals will be given by treatment.  
6.1.3 Statistical model, assumptions and hypotheses
The change from baseline in MWD will be analyzed in a repeated measure mixed effects model 
with treatment, visit and the treatment-by-visit interaction as fixed effects and baseline MWD 
as a covariate. The visit-by-baseline MWD interaction may be included in the model as an 
additional covariate. An unstructured residual covariance structure will be used, if possible, 
otherwise 
if an unstructured covariance cannot be fitted, simpler structures will be explored. 
The Least-Squares Mean (LSM) change from baseline in MWD for each visit will be estimated 
from the model for each treatment along with the treatment difference and the associated p-
value and two-sided 80% confidence interval (CI).
From the Week 16 quantities, the following criteria will be assessed:
1. The lower confidence limit of the 80% CI f or the treatment difference (LLG783 –
placebo) is greater than 0.
2. The estimated treatment difference is greater than or equal to 50 meters.
The first criterion will address whether, with high certainty, LLG783 is superior to placebo in
improvement in MWD. The second criterion will address whether the observed mean
Novartis For business use only Page 13
SAP Amendment 1 CLLG783X2201
improvement in MWD over placebo is at least 50 meters, a threshold that is considered to
represent highly competitive efficacy in this subject population.
6.1.3.1 Model checking procedures
Handling of missing values/censoring/discontinuations
The primary analysis will be based on all subjects with a baseline MWD and at least one post 
baseline MWD. Subjects who undergo any lower extremity vascular interventions (angioplasty, 
stenting, or bypass surgery) before the Week 16 efficacy assessment or subjects who drop out 
for other reasons before this assessment may be replaced to ensure 40 subjects complete this 
primary endpoint assessment. Data from such subjects will be included in the model for the 
primary analysis until the time of dropout or intervention; no imputation of the missing data 
will be performed for the primary analysis.
6.1.3.2 Graphical presentation of results
Model estimated treatment means and difference in change from baseline in MWD will be 
plotted over time, by visit (all treatment groups in the same graph).
6.1.3.3 Sensitivity analyses
As sensitivity analyses, the same analysis described for the primary analysis will be performed 
using the last observation carried forward (LOCF) and worst observation carried forward 
(WOCF) approaches of imputation for missing MWD data.
Baseline maximum walk distance will be summarized separately for subjects who complete the 
6MWT at week 16 and those who drop out of the study prior to this assessment. Summary
statistics will include n, mean, SD, minimum, median, and maximum. The p-value from a two-
sample t
-test comparing the baseline maximum walk distance between the two groups will be 
reported together with the summary.
The relationship between the maximum change in maximum walk distance and baseline
maximum walk distance will be explored using a graphical and modeling approach. A simple
linear regression line and the Pearson correlation, both for each treatment, will be overlaidonto 
a scatterplot. Additionally, a linear regression model for the maximum change in maximum 
walk distance with effects of treatment, baseline, and the treatment-by-baseline interaction will 
be fitted, and the p-value for the test of the interaction effect will be reported.
The relationship between change in maximum walk distance and change in ABI at week 16 will
be explored in a similar fashion.
Depending on the assessment of the PK profiles and dose response of subjects on different dose 
levels (if any after IA1), it might be reasonable to assume same mean response for both doses 
(providing similar AUC in the PAD population as observed in healthy volunteers). In that case 
different dose levels can be combined in one treatment arm regardless of different dose level.
6.2 Secondary objectives
To evaluate the effect of LLG783 on symptomatic functional capacity a fter 3 months of 
treatment in subjects with PAD and intermittent claudication.
Novartis For business use only Page 14
SAP Amendment 1 CLLG783X2201
6.2.1 Variables 
The secondary e fficacy e ndpoint is the pain- free walking distance defined as the distance 
walked up to the point of onset of claudication symptoms as assessed by the 6MWT and will 
be used to evaluate symptomatic functional capacity of PAD subjects participating in this study.  
Change from baseline in pain-free walking distance will also be derived. Baseline will be taken 
from the screening 6-minute walk test.
The exclusion rule of 6MWT defined in Section 6.1.1 will also apply to pain-free walking 
distance.
6.2.2 Descriptive analyses
Secondary endpoint will be listed and summarized in an equivalent way as described in Section 
6.1.2.
6.2.3 Statistical model, assumptions and hypotheses
Secondary endpoint will be analyzed in an equivalent way as described in Section 6.1.3.
6.2.3.1 Model checking procedures
Model checking procedures for pain-free walking distance will be the same as for primary 
analysis, refer to Section 6.1.3.1.
6.2.3.2 Graphical presentation of results
Graphical presentation of results for pain-free walking distance will be the same as for primary 
analysis, refer to Section 6.1.3.2.
6.2.3.3 Sensitivity analyses
As sensitivity analyses, the same analysis described for the secondary analysis in Section 6.2.3, 
will be performed using the last observation carried forward (LOCF) and worst observation 
carried forward (WOCF) approaches of imputation for missing pain-free walking distance. 
Corporate Confidential Information
Novartis For business use only Page 15
SAP Amendment 1 CLLG783X2201
Corporate Confidential Information
Novartis For business use only Page 16
SAP Amendment 1 CLLG783X2201
Corporate Confidential Information
Novartis For business use only Page 17
SAP Amendment 1 CLLG783X2201
7 Statistical methods for safety and tolerability data
All subjects within the Safety analysis set will be included in the safety data analysis.
In case of dose adjustment occurring during the study, safety analyses will be performed by two
analysis periods: pre-dose adjustment period and post-dose adjustment period. All subjects will 
be summarized by dose received during each period. 
7.1 Variables
Safety variables include adverse events, vital signs (body temperature, blood pressure, pulse 
rate, respiratory rate), height and weight, ECG intervals, laboratory measurements (hematology, 
clinical chemistry, urinalysis, coagulation panel), as well as subject demographics, baseline 
characteristics, and treatment information.
Corporate Confidential Information
Novartis For business use only Page 18
SAP Amendment 1 CLLG783X2201
7.2 Descriptive analyses
Subject demographics and other baseline characteristics
All data for background and demographic variables will be listed by treatment group and subject. 
Summary statistics will be provided by treatment group.
Relevant medical history, current medical conditions, results of laboratory screens, drug tests 
and any other relevant information will be listed by treatment group and subject.
Treatment
Data for study drug administration and concomitant therapies will be listed by treatment group 
and subject.
Vital signs
All vital signs data will be listed by treatment, subject, and visit/time and if ranges are available 
abnormalities (and relevant orthostatic changes) will be flagged. Summary statistics will be 
provided by treatment and visit/time.
Height and weight
All height and weight and BMI data will be listed by treatment, subject, and visit, as part of the 
vital signs panel.
ECG evaluations
All ECG data will be listed by treatment, subject and visit/time, abnormalities will be flagged. 
Summary statistics will be provided by treatment and visit/time.
Clinical laboratory evaluations
All laboratory data will be listed by treatment, subject, and visit/time and if normal ranges are 
available abnormalities will be flagged. A separate listing is provided presenting all parameters 
in a subject with any abnormal values. Summary statistics will be provided by treatment and 
visit/time.
Adverse events
All information obtained on adverse events will be displayed by treatment and subject.
The number and percentage of subjects with adverse events will be tabulated by body system 
and preferred term with a breakdown by t reatment. A subject with multiple adverse events 
within a body system is only counted once towards the total of this body system and treatment.
The number and percentage of subjects with adverse events by maximum severity of adverse 
events will be tabulated by body system and preferred term with a breakdown by treatment.
The number and percentage of subjects with adverse events classified as related to study drug 
will be tabulated by body system and preferred term with a breakdown by treatment.
Novartis For business use only Page 19
SAP Amendment 1 CLLG783X2201
ClinicalTrials.gov and EudraCT
For the legal requirements of ClinicalTrials.gov and EudraCT, two required tables on treatment 
emergent adverse events which are not serious adverse events with an incidence greater than 
5% and on treatment emergent serious adverse events and SAE suspected to be related to study 
treatment will be provided by system organ class and preferred term on the safety set population
and prepared internally by Novartis.
If for a same subject, several consecutive AEs (irrespective of study t reatment causality, 
seriousness and severity) occurred with the same SOC and PT:
 a single occurrence will be counted if there is ≤ 1 day gap between the end date of the
preceding AE and the start date of the consecutive AE
 more than one occurrence will be counted if there is > 1 day gap between the end date
of the preceding AE and the start date of the consecutive AE.
For occurrence, the presence of at least one SAE / SAE suspected to be related to study 
treatment / non-SAE has to be checked in a block e.g., among AE's in a ≤ 1 day gap block, if at 
least one SAE is occurring, then one occurrence is calculated for that SAE.
The number of deaths resulting from SAEs suspected to be related to study treatment and SAEs 
irrespective of study treatment relationship will be provided by SOC and PT. 
Other safety evaluations
Immunogenicity
All immunogenicity results will be listed by subject and visit/time. Summary statistics will be 
provided by treatment and visit/time.
7.3 Graphical presentation 
Boxplots to visualize trends in longitudinal safety d ata (vitals, ECG, lab parameter) will be 
created.
8 Pharmacokinetic / pharmacodynamic relationships
All subjects within the PK/PD analy
sis set will be included in the PK/PD data analysis.
In case of dose adjustment occurring during the study, PK/PD analyses may be performed by 
two analysis periods: pre-dose adjustment period and post-dose adjustment period. All subjects 
will be summarized by dose received during each period. 
In addition, relationship between LLG783 concentration or an appropriate PK parameter and 
MWD may be explored in a graphical and/or modeling approach.
Corporate Confidential Information
Novartis For business use only Page 20
SAP Amendment 1 CLLG783X2201
9 Statistical methods for biomarker data
Corporate Confidential Information
Novartis For business use only Page 21
SAP Amendment 1 CLLG783X2201
Handling of LLOQ and ULOQ
Biomarker data are reported as concentration results, measured using a specific assay with a
working range defined by the two limits: Lower limit of quantification (LLOQ) and Upper limit 
of quantification (ULOQ). Values which fall below the LLOQ or above the ULOQ are reported 
as < LLOQ * dilution factor (dilution factor: if sample diluted and concentration measured still 
below LLOQ) and > ULOQ * dilution factor, respectively.
Corporate Confidential Information
Novartis For business use only Page 22
SAP Amendment 1 CLLG783X2201
To ensure that biomarkers only h ave numerical values, censored values will be imputed as 
follows
 Values below the LLOQ are replaced by LLOQ/2.
 Values above the ULOQ are replaced by ULOQ.
Imputed values are used for summary statistics, inferential analyses and plots (with a special 
symbol). Values below LLOQ and values above ULOQ are shown as such in the listings. In the 
summary t able, the frequency ( n, %) of values below the LLOQ and above the ULOQ, 
respectively, will be included. 
If the proportion of imputed data is more than 20% for any treatment group at any timepoint, a 
footnote is added to the summary statistics table stating that the proportion of values outside the 
limits of quantification is more than 20% for some treatment groups at some time points and 
that in such cases summary statistics may be heavily biased.
If the proportion of imputed data for a given biomarker, across all treatment groups and time 
points, is more than 50%, no summary statistics are provided and the data are only listed.
If the proportion of imputed data for a given biomarker, across all treatment groups and time 
points, is more than 30%, no inferential analysis will be performed.
10 Reference list
1.
Clinical Trial Protocol, CLLG783X2201
2. Site Operations Manual for Protocol No. CLLG783X2201
3. Investigator’s Brochure for Protocol No. CLLG783X2201
Corporate Confidential Information
Corporate Confidential Information
Corporate Confidential Information