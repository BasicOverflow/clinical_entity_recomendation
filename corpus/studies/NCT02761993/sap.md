ST266-PERIO-201 
A RANDOMIZED, DOUBLE-BLIND, PLACEBO 
CONTROLLED STUDY TO EVALUATE THE SAFETY, 
EFFICACY, AND TREATMENT REGIMEN OF ST266 IN 
SUBJECTS WITH MODERATE TO SEVERE 
PERIODONTITIS 
NCT2761993 
Stemnion, Inc.  CONFIDENTIAL                  Statistical Analysis Plan 
Protocol No. ST266-PERIO-201                                   02 October 2017 
 
 
STATISTICAL ANALYSIS PLAN 
02 October 2017 
VERSION 4.0 
 
 
 
 
 A RANDOMIZED, DOUBLE-BLIND, PLACEBO-
CONTROLLED STUDY TO EVALUATE THE SAFETY, 
EFFICACY, AND TREATMENT REGIMEN OF ST266 IN 
SUBJECTS WITH MODERATE TO SEVERE 
PERIODONTITIS 
 
 
 
 
PROTOCOL NUMBER ST266-PERIO-201 
 
 
 
 
 
 
 
SPONSORED BY 
 
Noveome Biotherapeutics, Inc 
100 Technology Dr. Ste 200 
Pittsburgh, PA 15219 
 
 
 
  
 
PREPARED BY 
 
Rho, Inc. 
6330 Quadrangle Drive, Suite 500 
Chapel Hill, NC  27517 
Telephone:  (919) 408-8000 
Fax:  (919) 408-0999 
 
 
             
Version:  ST266-Perio-201_SAP_v4.0  Page 1 of 35 
 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
This document is confidential and proprietary to Stemnion, Inc .  Acceptance of this document constitutes 
agreement by the recipient that no  unpublished information contained herein will be reproduced, 
published, or otherwise disclosed without the prior written approval of Stemnion, Inc , except that this 
document may be disclosed to appropriate Institutional Review Boards under the condition that they keep 
the information confidential. 
DOCUMENT VERSION CONTROL 
Version Number Date Comments/Changes 
0.1 08 August  2016 Original Version 
0.2 08 November 2016 Updated per sponsor comments 
0.3 26 December 2016 Updated per sponsor comments 
0.4 09 January 2016 Updated per sponsor comments.  Includes 
options for managing the analysis of rescue 
therapy. 
0.5 31 January 2017 Updated per teleconference with team on 
26Jan17 
0.6 10 February 2017 Updated per teleconference with team on 
03Feb17 and continuing discussion among 
statisticians from Forsyth and Rho and the 
team at Stemnion/Noveome 
1.0 20 March  2017 Finalize per phone call on 2/28/2017 
2.0 05 April 2017 Updated primary endpoint analysis to be 
only on tooth-sites with baseline PD 
>=6mm. 
Re-organization of endpoints into secondary 
versus exploratory analyses 
3.0 10 April 2017 Updated missing data imputation section for 
clarity and method 
3.1 14 September 2017 Updated the SAP to fully characterize the 
statistical model.  Added site and smoker 
status as covariates in the primary analysis. 
Changed the Primary Endpoint from change 
from baseline PD at 90 days to the change 
from baseline PD at 270 days. 
Removed Amended Per Protocol (APP) 
population 
3.2 29 September 2017 Added smoking status and treatment group 
in model as an interaction term. 
Added exploratory endpoints % of patients 
Version:  ST266-Perio-201_SAP_v4.0  Page 2 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
with pockets a) < 5mm, b) decreasing by 2 
mm or more that at baseline were ≥5mm, 
and c) 75% of pockets < 5 mm that at 
baseline were ≥5mm 
4.0 02 October 2017 Final 
 
 
Version:  ST266-Perio-201_SAP_v4.0  Page 3 of 35 

Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
APPROVALS 
Approved:  Date:  
 Jan Lessem, MD, PhD 
On behalf of Noveome 
  
    
  Date:  
 John Hall 
Director, Clinical Operations, Stemnion 
  
    
  Date:  
 Marcus Herman-Giddens 
Biostatistician, Rho, Inc. 
  
    
Version:  ST266-Perio-201_SAP_v4.0  Page 4 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
TABLE OF CONTENTS 
LIST OF ABBREVIATIONS ............................................................................................  7 
LIST OF IN-TEXT TABLES ............................................................................................. 8 
1. PURPOSE OF THE ANALYSES .............................................................................. 9 
2. PROTOCOL SUMMARY ........................................................................................ 10 
2.1 Study Objectives ......................................................................................... 13 
2.2 Overall Study Design and Plan ...................................................................  13 
2.3 Study Population ......................................................................................... 15 
2.4 Treatment Regimens................................................................................... 15 
2.5 Treatment Group Assignments or Randomization ....................................... 15 
2.6 Sample Size Determination ......................................................................... 16 
3. GENERAL ANALYSIS AND REPORTING CONVENTIONS.................................. 17 
4. ANALYSIS POPULATIONS ................................................................................... 18 
5. STUDY SUBJECTS ............................................................................................... 19 
5.1 Disposition of Subjects ................................................................................ 19 
5.2 Protocol Deviations ..................................................................................... 19 
6. DEMOGRAPHIC AND OTHER BASELINE CHARACTERISTICS ......................... 20 
7. MEASUREMENTS OF TREATMENT COMPLIANCE ............................................ 21 
8. EFFICACY EVALUATION ..................................................................................... 22 
8.1 Overview of Efficacy Analysis Issues .......................................................... 22 
8.1.1 Handling of Dropouts or Missing Data ................................................ 22 
8.1.2 Rescue Therapy ................................................................................ 22 
8.1.2.1 Amendment to Protocol Rescue Criteria ............................... 22 
8.1.3 Multicenter Studies ............................................................................ 22 
8.1.4 Assessment Time Windows ............................................................... 23 
8.2 Efficacy Variables ....................................................................................... 23 
8.3 Analysis Methods ........................................................................................ 23 
8.3.1 Primary Efficacy Analyses .................................................................  23 
8.3.2 Secondary Efficacy Analyses ............................................................. 24 
8.3.3 Efficacy Analyses at Other Time Points ............................................. 25 
8.3.4 Exploratory Efficacy Analyses ............................................................ 25 
8.4 Examination of Subgroups .......................................................................... 26 
8.5 Exploratory Categorical Analysis of PD ....................................................... 26 
8.6 Pooled comparisons ................................................................................... 27 
9. SAFETY EVALUATION ......................................................................................... 28 
9.1 Overview of Safety Analysis Methods ......................................................... 28 
9.2 Extent of Exposure ...................................................................................... 28 
9.3 Adverse Events ........................................................................................... 28 
9.4 Deaths, Serious Adverse Events, and Other Significant Adverse Events .... 29 
9.5 Clinical Laboratory Evaluation ..................................................................... 29 
9.6 Vital Signs, Physical Findings, and Other Observations Related to Safety .. 29 
9.6.1 Vital Signs .......................................................................................... 29 
9.6.2 Physical Examinations ....................................................................... 30 
9.6.3 Other Safety Measures ...................................................................... 30 
Version:  ST266-Perio-201_SAP_v4.0  Page 5 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
10. TIMING OF DATA COLLECTION AND ANALYSES ............................................. 31 
11. REFERENCES ....................................................................................................... 32 
12. APPENDICES ........................................................................................................ 33 
12.1 Study Flow Chart ........................................................................................ 33 
12.2 Schedule of Events ..................................................................................... 34 
THIS PAGE HAS BEEN INTENTIONALLY LEFT BLANK ........................................... 35 
 
Version:  ST266-Perio-201_SAP_v4.0  Page 6 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
LIST OF ABBREVIATIONS 
Abbreviation or Specialist Term Explanation 
AAP American Academy of Periodontists 
AE Adverse event 
AMP Amnion-derived multi-potent progenitor cells 
BOP Bleeding on probing 
CAL Clinical attachment level 
CEJ Cemento-enamel junction 
eCRF Electronic case report form 
FDA Food and Drug Administration 
FMPI Full-mouth plaque index 
GCF Gingival crevicular fluid 
GCP Good Clinical Practice 
GEE Generalized estimating equation 
HbA1c Glycated hemoglobin 
ICH International Council for Harmonisation 
IEC Independent ethics committee 
IL Interleukin 
IMDM Iscove’s Modified Dulbecco’s Medium 
IND Investigational New Drug Application 
IRB Institutional review board 
IWRS Interactive web response system 
MMP Matrix metalloproteinase 
PD Pocket depth 
PGE2 Prostaglandin E2 
RBL Radiographic bone level 
SAE Serious adverse event 
SAR Suspected adverse reaction 
SRP Scaling and root planing 
ST266 Study drug: amnion-derived cellular cytokine solution 
 
Version:  ST266-Perio-201_SAP_v4.0  Page 7 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
LIST OF IN-TEXT TABLES 
Table 8-1 Efficacy Variables and Analysis Methods ...................................... 23 
 
 
Version:  ST266-Perio-201_SAP_v4.0  Page 8 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
1. PURPOSE OF THE ANALYSES 
This study is a randomized, double-blind, placebo-controlled study to evaluate the safety, 
efficacy, and treatment regimen of ST266 in subjects with moderate to severe 
periodontitis.  The purpose of the analysis is to estimate both the safety and efficacy of 
two regimens of ST266 at 270 days following scaling and root planing.  Analysis of the 
primary and secondary endpoints will be conducted after all subjects have completed the 
Day 270 visit (“Primary Completion Date”).  
The statistical analysis plan (SAP) for protocol ST266-PERIO-201 is being developed 
before database lock and any analyses of the primary endpoint.  The SAP contains 
detailed information of the planned statistical analyses and reporting of the study data for 
use in the final clinical study report (CSR).  It is written with due consideration of the 
recommendations outlined in the most recent International Conference on Harmonization 
(ICH) E9 Guideline entitled Guidance for Industry: Statistical Principles for Clinical 
Trials [1] and the most recent ICH E3 Guideline, entitled Guidance for Industry: 
Structure and Content of Clinical Study Reports [2]. 
Separate statistical analysis plans are being developed for exploratory endpoints: 
cytokines in gingival crevicular fluid (GCF) and serum, periodontal microbial flora as 
determined from microbial analyses, and radiographic bone level (RBL). These analyses 
will be appended to this SAP upon completion. 
The SAP describes the populations that will be analyzed and the efficacy and safety 
assessments that will be evaluated.  It also provides details of the specific statistical 
methods that will be used.  If additional analyses are required to supplement the planned 
analyses described in this SAP, they will be identified as post-hoc analyses in the CSR. 
Version:  ST266-Perio-201_SAP_v4.0  Page 9 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
2. PROTOCOL SUMMARY 
Name of Sponsor/Company: 
Stemnion, Inc. 
Name of Investigational Product: 
ST266 [Amnion-derived Cellular Cytokine Solution (ACCS)] 
Title of Study:  
A randomized, double-blind, placebo-controlled study to evaluate the safety, efficacy, and 
treatment regimen of ST266 in subjects with moderate to severe periodontitis. 
Study Center(s): Multi-center (6 clinical sites in the United States) 
Phase of Development: Phase 2a 
Objectives:  
Primary: 
To determine the efficacy of ST266 to reduce pocket depth (PD) adjunctive to scaling and root 
planing 270 days after initiation of treatment. 
Secondary: 
To determine safety and changes in: 
• Clinical attachment level (CAL) 
• Bleeding on probing (BOP) 
Study Design: 
The study is a 9-month, randomized, double-blind, parallel-design study of subjects with 
existing moderate to severe periodontal disease randomly assigned to one of three groups. The 
primary endpoint of PD change will be evaluated following 270 days on study.  Subjects will be 
followed for 9 months for safety and radiographic evaluations. 
Subjects who meet inclusion and exclusion criteria will be randomized to one of three treatment 
groups. Randomization will be stratified by site and smoker status (never smoked or quit 
smoking more than two years ago vs. has smoked within the last two years). Randomization will 
be blocked such that assignment to treatment groups both within sites and within smoker status 
will be approximately even (1:1:1). Treatment will be initiated after scaling and root planing 
(SRP). 
All subjects will be evaluated at baseline and Days 1, 15, 30, 60, 90, 180, and 270. 
Number of Subjects (Planned): A total of 150 subjects will be enrolled in the study, 50 per 
group. 
Study Duration per Subject: Each subject will be enrolled in the study for 9 months. 
Diagnosis and main criteria for inclusion:  
Moderate to severe periodontal disease according to American Academy of Periodontists (AAP) 
definition (at least 6 teeth with 6mm or greater pocket depth and 3 mm or greater CAL at 
baseline). 
 
Inclusion Criteria: 
1. Provision of signed, written informed consent prior to participation in any study-related 
Version:  ST266-Perio-201_SAP_v4.0  Page 10 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
procedures. 
2. Good general health as evidenced by medical history. 
3. Between 18 and 85 years of age at time of informed consent signature. 
4. Male or female. 
5. Minimum of 18 teeth, excluding third molars. 
6. Having moderate to severe periodontal disease according to AAP definition (at least 6 
teeth ≥6 mm PD and ≥3 mm CAL at baseline). 
7. Having >30 percent bleeding sites upon probing. 
8. Willing to abstain from chewing gums and other mouth rinses for the study duration. 
9. Ability and willingness to attend all study visits and comply with all study visits and 
comply with all study procedures and requirements. 
10. Willingness to abstain from routine dental care. 
11. For women with reproductive potential, willingness to use highly effective 
contraception (e.g. licensed hormonal contraception, intrauterine device, abstinence, or 
vasectomy in partner). 
 
Exclusion Criteria: 
1. Presence of orthodontic appliances. 
2. A soft or hard tissue tumor of the oral cavity. 
3. Carious lesions requiring immediate treatment. 
4. Participation in any other clinical study within 30 days of screening or during the study. 
5. Pregnancy or lactation. If a subject meets this criterion, she may be rescreened for study 
participation when she no longer meets this criterion. 
6. Antibiotic therapy within the last 30 days. 
7. Chronic use (≥3 times/week) of anti-inflammatory medications (e.g., non-steroidal 
anti-inflammatory drugs, steroids). Low-dose aspirin (less than 325 mg daily) is 
allowed. 
8. Immunocompromised subjects. 
9. Subjects with cancer or a history of cancer within the last 5 years of screening. 
10. Any medical history or any concomitant medication that might affect the assessment of 
the study treatment or periodontal tissues, such as diabetes, nifedipine, phenytoin 
(Dilantin), or anticoagulant medications (e.g., warfarin [Coumadin] etc.). 
11. Involvement in the planning or conduct of the study. 
12. History of any clinically significant disease or disorder which, in the opinion of the 
investigator, may either put the subject at risk because of participation in the study, or 
interfere with interpretation of the subject’s study results. 
13. Previous randomization for treatment in the present study. 
Investigational product, dosage and mode of administration: 1X ST266 applied in a dose of 
20 microliters per tooth. Total daily dose will be less than 1 milliliter. ST266 will be applied 
directly to the marginal gingiva around each tooth (buccal and lingual) using sterile packaged 
pipette tips compatible with the Eppendorf Repeater M4 device. 
 
Version:  ST266-Perio-201_SAP_v4.0  Page 11 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
Duration of Treatment:  
Group 1: ST266 dosed daily on Days 1-5, 8-12, 22, and 30, and then monthly for 7 months 
(Days 60, 90, 120, 150, 180, 210, and 240). 
Group 2: ST266 dosed 2x/week (with at least one day between treatments) for the first 3 
months and monthly for 5 months thereafter (Days 120, 150, 180, 210, and 240). 
Group 3: Placebo dosed at the same frequency as Group 1. 
Placebo, Dosage, and Mode of Administration: Sterile saline (0.9% NaCl) will be applied in 
the same manner and in the same volume as the investigational product, ST266. 
Criteria for Evaluation: 
Efficacy:  
The primary efficacy endpoint of this study is the change from baseline in the PD for each 
patient at 9 months (Day 270) for those pockets ≥6mm at baseline. 
Secondary efficacy endpoints of this study are: 
 (1) Change from baseline in CAL at 9 months and (2) change from baseline in BOP at 9 months 
for those pockets ≥6mm at baseline. 
Exploratory endpoints of this study are:  
(1) Pro-inflammatory mediators, enzymes and bone markers will be measured in gingival 
crevicular fluid (GCF) and serum at the baseline, Days 15, 90, 180, and 270; 
 (2) Microbial analysis of periodontal flora will be performed at baseline and at Days 15, 90, 
180, and 270; and  
(3) Change from baseline in radiographic bone levels (RBL) at Days 90 and 270.  PD, CAL, 
BOP, and FMPI will also be summarized at Days 90, 180 and 270. 
(4) Smoker/treatment interaction will be summarized for PD and CAL at Days 90, 180, and 270.  
(5) Percent of patients with all pockets < 5mm will be summarized at Days 90, 180 and 270. 
(6) Percent of patients with pockets decreasing by 2mm or more that at baseline were ≥5mm will 
be summarized at Days 90, 180 and 270.  
(7) Percent of patients with 75% of pockets < 5mm that at baseline were ≥5mm will be  
summarized at Days 90, 180 and 270. 
Safety: The safety endpoints are frequency and pattern of adverse events (AEs) and serious 
adverse events (SAEs). 
Planned Sample Size: 
The sample size for the study is based on the sample size required to compare treatment with 
ST266 versus placebo for the primary efficacy endpoint. 
The number of subjects was estimated based on two meta-analysis studies that reviewed 50 and 
72 articles respectively (Bonito, 2005). 
Using the normal approximation for sample size determination for an independent sample t-test, 
and assuming a PD reduction of 0.5 mm on average (difference in means) with a standard 
deviation of 0.7 mm, alpha=0.05 (0.025 per comparison, Bonferroni correction), and 85% 
power, a sample size of 44 per group will be required. The expected dropout rate is 
approximately 10% based on previous experiments; hence 50 subjects will be enrolled per 
group.   
Statistical methods: 
Analysis of the clinical efficacy data will consist of modeling endpoints, including change from 
Version:  ST266-Perio-201_SAP_v4.0  Page 12 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
baseline in PD, CAL, BOP, and FMPI, with treatment group, smoking status, and investigational 
site as main effects and the interaction of smoking status and treatment group.  Post-baseline 
treatment comparisons will be modeled through a GEE method (with a linear link and within-
patient exchangeable covariance matrix), adjusting for the baseline value. Methods of analysis 
for periodontal flora, inflammatory cytokine levels in GCF and in serum, and RBL will be 
described in separate statistical analysis plans. 
 
2.1 Study Objectives 
The primary objective is to estimate the efficacy of ST266 to reduce pocket depth (PD) as 
an adjunctive to scaling and root planing (SRP). 
The secondary objectives of this study are to determine: (1) safety as established by 
assessment of AEs and SAEs, and (2) changes in the following clinical parameters: 
• Clinical attachment level (CAL) 
• Bleeding on probing (BOP) 
Additional exploratory objectives are to compare the effects of the treatments and dosing 
schedules in the following: 
• Proinflammatory mediators, enzymes, and bone markers in gingival crevicular 
fluid (GCF) and serum 
• Periodontal flora as determined from microbial analyses  
• Radiographic bone level (RBL) 
• Full-mouth plaque index (FMPI)   
• Percent of patients with all pockets < 5mm  
• Percent of patients with pockets decreasing by 2mm or more that at baseline 
were ≥5mm 
• Percent of patients with 75% of pockets < 5mm that at baseline were ≥5mm 
2.2 Overall Study Design and Plan 
The study is a 9-month, randomized, double-blind, placebo controlled, parallel design 
study of subjects with existing moderate to severe periodontal disease. All subjects will 
be treated by a dental professional at the study site. The dental professional will be a 
qualified and trained licensed periodontist, dentist, or dental hygienist skilled in 
periodontal clinical research. All investigators will be trained in grading clinical 
parameters in the same manner for consistency. Subjects will be recruited at multiple 
treatment sites. After signing informed consent, subjects will be screened with a medical 
and dental history and full mouth dental examination. Clinical parameters will be 
recorded including PD, CAL, and BOP. Subjects will have urinalysis in addition to blood 
Version:  ST266-Perio-201_SAP_v4.0  Page 13 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
tests including hematology and chemistry (liver and kidney function) panels. Women of 
child-bearing potential will be administered a pregnancy test. 
If inclusion/exclusion criteria are met, subjects will undergo a baseline visit with 
measurements of FMPI, collection of gingival crevicular fluid (GCF) and blood samples. 
Subgingival plaque samples will be collected for microbial analysis. Vertical bitewing X-
rays will be collected to assess RBL. Subjects will undergo SRP procedure(s) prior to 
being randomly assigned to one of three treatment groups as described in section 2.5.  
Local anesthesia must be used for SRP.  All treatments of ST266 or placebo will be 
administered in office by a dental professional.  
All subjects will be evaluated at screening, baseline, and Days 1, 15, 30, 60, 90, 180, and 
270. Evaluations will be performed by a blinded dental professional to mask the group as 
all groups do not have the same study schedule. The blinded examiners will be 
independent from the dental professionals who apply the study drug to the subjects, 
thereby ensuring that the treatment assignment cannot be inferred based on the treatment 
schedule. 
At each evaluation, medical and dental history will be updated, an oral exam will be 
performed, and AEs and SAEs will be assessed and recorded. PD, CAL, and BOP will be 
evaluated at screening and on Days 15, 30, 60, 90, 180, and 270. Subjects will have 
urinalysis in addition to blood tests including hematology and chemistry (liver and kidney 
function) panels done at screening and repeated at Days 90 and 270. FMPI will be 
recorded at baseline and on Days 15, 30, 60, 90, 180, and 270. Inflammatory cytokines in 
serum will be measured at baseline and on Days 15, 90, 180, and 270. GCF will be 
collected and analyzed at baseline and on Days 15, 90, 180, and 270. Microbial analysis 
of periodontal flora will be performed at baseline and on Days 15, 90, 180, and 270. 
At each treatment visit, in addition to administration of ST266 or placebo, medical and 
dental history will be updated, AEs and SAEs will be assessed and recorded, concomitant 
medications will be recorded, and oral hygiene instruction will be provided. 
Randomization will be stratified by site and smoker status (never smoked or quit smoking 
more than two years ago vs. has smoked within the last two years). Randomization will 
be blocked such that assignment to treatment groups both within sites and within smoker 
status will be approximately even (1:1:1). ST266 will be supplied to the study site and 
prepared for use by trained clinical staff, who will not be the same as the dental 
professionals evaluating the subjects. 
Primary Endpoint: The primary endpoint of this study is the average change from 
baseline in tooth site PD for each patient at 9 months (Day 270) in tooth sites with 
baseline PD ≥ 6mm.  The change in pocket depth at each tooth site will be the dependent 
variable with the average over all tooth-sites for each patient being estimated by the 
statistical model.   
 
Version:  ST266-Perio-201_SAP_v4.0  Page 14 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
Secondary Endpoints: The secondary endpoints of this study are:  
• change from baseline in CAL at 270 days in tooth sites with baseline PD ≥ 
6mm 
• change from baseline in BOP for each patient at 270 days.  BOP for each 
patient is calculated as the percent of tooth sites in the whole mouth with 
bleeding on probing. 
Baseline refers to the initial measurement of the endpoint, which may occur at the 
screening or baseline visit according to the schedule of assessments. 
 
Safety Endpoints: The safety endpoints are the frequency and pattern of AEs and SAEs. 
Exploratory Endpoints: Pro-inflammatory mediators, enzymes, and bone markers will 
be measured in GCF and serum at baseline and Days 15, 90, 180, and 270. Microbial 
analysis of periodontal flora will be performed at baseline and at Days 15, 90, 180, and 
270.  Change from baseline in RBL will be measured at Days 90 and 270.  PD, CAL, 
BOP, will also be analyzed at Days 180 and 270.  FMPI will also be analyzed at Days 90, 
180 and 270. Percent of patients with all pockets < 5mm, percent of patients with pockets 
decreasing by 2mm or more that at baseline were ≥5mm, and percent of patients with 
75% of pockets < 5mm that at baseline were ≥5mm will be shown at Days 90, 180 and 
270.  
2.3 Study Population 
The population of this study comprises adults with moderate to severe periodontitis who 
meet the inclusion/exclusion criteria as described in the protocol synopsis in Section 2 of 
the SAP. Approximately 150 subjects will be enrolled with 50 subjects per treatment 
group.  Subjects may be re-screened if they do not fail inclusion criteria #6 (having 
moderate to severe periodontal disease according to the AAP definition [at least 6 teeth 
with ≥6 mm PD and ≥3 mm CAL at baseline). 
2.4 Treatment Regimens 
Group 1: ST266 dosed daily on Days 1-5, 8-12, 22, and 30 and then monthly for 7 
months (Days 60, 90, 120, 150, 180, 210, and 240). 
Group 2: ST266 dosed 2x/week (with at least one day between treatments) for the first 3 
months and monthly for 5 months thereafter (Days 120, 150, 180, 210, and 
240). 
Group 3: Placebo dosed at the same frequency as Group 1. 
2.5 Treatment Group Assignments or Randomization 
Randomization will be stratified by site and smoker status (never smoked or quit smoking 
more than two years ago versus has smoked within the last two years). Randomization 
will be blocked such that assignment to treatment groups both within sites and within 
Version:  ST266-Perio-201_SAP_v4.0  Page 15 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
smoker status will be approximately even (1:1:1). ST266 will be supplied to the study site 
and prepared for use by trained clinical staff, who will not be the same as the dental 
professionals evaluating the subjects. 
At the 90-Day analysis, one statistician and one programmer will be unblinded in order to 
generate the unblinded 90-day analysis.  Another team of statisticians and programmers 
will remain blinded until the 270-day analysis at the end of the study. 
2.6 Sample Size Determination 
One hundred and fifty (150) subjects will be enrolled.  The sample size for the study is 
based on the sample size required to compare treatment with ST266 versus placebo for 
the primary efficacy endpoint. 
The number of subjects was estimated based on two meta-analysis studies that reviewed 
50 and 72 articles respectively (Bonito, 2005). 
Using the normal approximation for sample size determination for an independent sample 
t-test, and assuming a PD reduction of 0.5 mm on average (difference in means) with a 
standard deviation of 0.7 mm, alpha=0.05 (0.025 per comparison, Bonferroni correction), 
and 85% power, a sample size of 44 per group will be required. The expected dropout 
rate is approximately 10% based on previous experiments; hence 50 subjects will be 
enrolled per group.   
Version:  ST266-Perio-201_SAP_v4.0  Page 16 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
3. GENERAL ANALYSIS AND REPORTING CONVENTIONS 
For continuous endpoints, the summary statistics will generally include number of 
subjects with data (n), mean, standard deviation, median, minimum and maximum. No 
preliminary rounding will be performed; rounding will only occur after analysis.  To 
round, the digit to right of last significant digit will be considered:  if < 5 then round 
down, if ≥ 5 then round up.  Means and medians will be presented with one more decimal 
place than the precision of the data.  Standard deviations will be presented with two more 
decimal places than the precision of the data.  Percentages will be presented with one 
decimal place.  Minimums and maximums will be presented with the same precision as 
the original data. 
 For categorical endpoints, the summary statistics will generally include:  number of 
subjects randomized and/or dosed, number of subjects with data, and the percentage of 
those with data in each category.  Frequency distributions will be presented as 
appropriate.  
Analysis of the clinical efficacy data will consist of modeling endpoints, including 
change from baseline in PD, CAL, BOP, and FMPI, with treatment group, patients, 
smoking status, and investigational site as  main effects and adjusting for baseline values 
of a given endpoint. Post-baseline treatment comparisons will be modeled through a GEE 
method (with a linear link and exchangeable covariance matrix), adjusting for the 
baseline value. Methods of analysis for periodontal flora, inflammatory cytokine levels in 
GCF and in serum, and RBL will be described in separate statistical analysis plans. 
Hypothesis testing, unless otherwise indicated, will be two-sided.  When confidence 
intervals are presented, they will be two-sided with a confidence coefficient of 95%.   
Actual P-values will be reported to 3 decimal places if greater than 0.001.  If less than 
0.001, the value ‘<0.001’ will be reported.  
The statistical software, SAS® version 9.3 or above, will be used for all summaries and 
statistical analyses. 
Version:  ST266-Perio-201_SAP_v4.0  Page 17 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
4. ANALYSIS POPULATIONS 
Statistical analyses will be based on the analysis populations as defined below: 
• Safety population: All randomized subjects who use at least one dose of study 
drug, regardless of whether or not they undergo any study assessments. 
• Intention-to-Treat (ITT) population: All randomized subjects. 
• Per Protocol (PP) population: All subjects who use at least one dose of study 
drug and do not have major protocol deviations as defined in § 5.2.  
 
Version:  ST266-Perio-201_SAP_v4.0  Page 18 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
5. STUDY SUBJECTS 
5.1 Disposition of Subjects 
Subject disposition will be summarized in tables and listings: overall, by treatment, by 
smoking status at baseline, and by site.   
• The number of subjects screened (overall) 
• The number of subjects enrolled and randomized 
• The number of subjects treated 
• The number of subjects who have completed each visit 
• The number of subjects who discontinued study treatment; overall and by 
discontinuation reason: 
• Adverse Event 
• Death 
• Lack of Efficacy 
• Lost to Follow-up 
• Non-Compliance with Study Duration 
• Physician Decision 
• Pregnancy 
• Progressive Disease 
• Protocol Violation 
• Recovery 
• Screen Failure 
• Study Terminated by Sponsor 
• Technical Problems 
• Withdrawal by Subject 
• Other 
5.2 Protocol Deviations 
Major protocol deviation information will be maintained separately from the electronic 
CRF, and exports of these data will be delivered separately from the clinical datasets.  A 
major deviation is one that may affect the outcome, analysis, or interpretation of the 
study.  These deviations may include, but are not limited to, the following: 
Inclusion/exclusion criteria deviations, randomization deviations, and terminations for 
lack of compliance. Major protocol deviations will be identified by an expert committee 
prior to unblinding the study.  Protocol deviations can be self-reported, recorded 
following interim monitoring visits, or following remote monitoring.  For the per protocol 
analysis all subjects with minor deviations will be included.  All subjects with major 
deviations will be reviewed as described above and will not be included in the per 
protocol analysis. 
Subjects who miss 20% or more of their prescribed treatments will be considered non-
compliant and will be excluded from the per-protocol statistical analysis. 
Version:  ST266-Perio-201_SAP_v4.0  Page 19 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
6. DEMOGRAPHIC AND OTHER BASELINE CHARACTERISTICS 
Baseline data (demography, medical history, dental history, and baseline disease 
characteristics) will be summarized. 
Demography includes age, sex, race, and ethnicity. Sex, race, and ethnicity will be 
tabulated in frequencies and continuous summary statistics will be presented for age at 
screening.  Data will also be presented in a listing. 
The number and percentage of subjects with each medical history event will be presented 
by body system and event term.  A listing will also be created which will include the 
body system, event term, whether the medical history event is ongoing and controlled, as 
well as the start and end dates of the event and any associated comments.  
The number and percentage of subjects who have been diagnosed with periodontitis, 
abscesses, or who have had any oral surgeries or root canals, or are currently 
experiencing dental pain will be presented.  A listing will also be created which will 
include the above events as well as their associated dates, the date the subject last visited 
a dentist or hygienist, frequency of flossing and mouth rinse, and interdental irrigation 
devices. 
Results of the baseline oral exam will be listing by area examined and will denote an 
abnormal or normal result; and, if abnormal, the associated description of the abnormality 
will be listed.  The presence of periodontal abscess or endodontic abscess will also be 
presented. 
Tooth status at baseline will be presented in a listing by subject and tooth, and will denote 
whether the tooth is missing, sound, decayed, filled, fractured, has a crown, and/or is an 
implanted tooth. 
Quadrants completed during the scaling the root planing procedure at visit 3 will be 
presented in a listing. 
Demographic and baseline disease characteristics will be presented for the safety 
population. 
Version:  ST266-Perio-201_SAP_v4.0  Page 20 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
7. MEASUREMENTS OF TREATMENT COMPLIANCE 
Every treatment application of study drug will be performed in the dental clinic by the 
clinician/investigator (dental professional); therefore, the investigator can assess non-
compliance based on subject attendance of scheduled treatments. 
Missed treatments may be completed if done within the treatment windows described in 
the protocol. 
Subjects who miss 20% or more of their prescribed treatments will be considered non-
compliant and excluded from the per-protocol statistical analysis. 
Treatment compliance will be calculated as: 
[(# doses completed within X days (with “X” as defined above) from original 
scheduled dose date)/ (# planned doses)]*100 
Treatment compliance will be presented by group at each visit and overall using both 
continuous summary statistics and the following frequency cut-offs: <50%, 50 - 80%, 
>80% for the ITT population.   
Treatment compliance will also be presented in a listing presenting subject, dosing 
schedule/treatment group, planned dosing day, whether the subject was dosed within “X” 
days (with “X” as defined above”), actual dosing day, and treatment compliance. 
Version:  ST266-Perio-201_SAP_v4.0  Page 21 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
8. EFFICACY EVALUATION 
8.1 Overview of Efficacy Analysis Issues 
8.1.1 Handling of Dropouts or Missing Data 
All reasonable efforts will be made to minimize missing data.  However, there are two 
possibilities for data being missing.  In one case, the measurement associated with an 
individual pocket may be missing at an evaluation.  In this case, the worst previous value 
for this variable will be imputed for that tooth/pocket.  Furthermore, the data from an 
entire patient may be missing because they withdrew before completing the study.   For 
this imputation, an approach similar to that for each site will be employed.  For visits that 
would follow a patient’s premature discontinuation from the study, the worst observation 
associated with each individual pocket will be imputed for all subsequent visits for that 
patient and will thus also be carried forward for the 270-day evaluation.  Subjects who 
drop out of the study will not be replaced. 
8.1.2 Rescue Therapy 
The need for rescue therapy including the site requiring therapy, the date and study day, 
the pocket depth (PD), whether SRP was performed, the protocol version under which the 
subject was enrolled, and any associated comments will be presented in a listing. 
Additionally, a table will be created to summarize and compare the need for and timing 
of rescue therapy across the three treatment groups. 
Further ad-hoc exploratory analyses to examine the characteristics of subjects receiving 
rescue therapy and the circumstances surrounding the need for rescue therapy may be 
conducted. 
8.1.2.1 Amendment to Protocol Rescue Criteria 
In this study, rescue therapy was intended to occur only after the Day 90 evaluation. 
However, under early versions of the protocol, the timing of rescue therapy was not 
explicitly stated, and rescue therapy was permitted at any time after the initial SRP 
treatment if indicated by clinical parameters (PD or CAL). A subsequent amendment to 
the protocol (Amendment 2) was made to correct this issue, but some subjects enrolled 
under the earlier versions of the protocol received “premature” rescue therapy prior to 
Day 90.  
Pockets/teeth that are “rescued” should be considered treatment failures after rescue.  For 
this reason, rescued teeth/pockets will be assigned a value equal to the worst score 
observed at any previous visit for that pocket/tooth in the primary and secondary 
analyses..  
8.1.3 Multicenter Studies 
This is a multi-center study and randomization has been stratified by site.   
Version:  ST266-Perio-201_SAP_v4.0  Page 22 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
8.1.4 Assessment Time Windows 
See Section 15.2 for the Schedule of Assessments.  Assessments within the stated visit 
windows will be considered for analysis of the given time point.  If multiple assessments 
occur within a visit window, the assessment occurring closest to the target day for the 
assessment will be used in the analysis. In the case of a tie, the worst record will be used. 
8.2 Efficacy Variables 
Table 8-1 Efficacy Variables and Analysis Methods 
Efficacy Variables Method 1 a 
Primary  
Pocket Depth Δ from baseline at Day 270 in tooth-sites with 
baseline PD ≥6mm a 
Secondary  
Clinical Attachment Level Δ from baseline at Day 270 in tooth-sites with 
baseline PD ≥6mm a 
Bleeding on Probing Δ from baseline at Day 270 using whole mouth 
average percentage of site with bleeding on probing b 
  
a Generalized Estimating Equations will be used as the primary analytical method.  The dependent variable will be 
change from baseline to Day 270 and the model will include treatment group, patients, smoking status, and 
investigational site for a given endpoint.  A linear link and exchangeable covariance matrix will be employed. Only 
treatment comparisons at Day 270 will report a p-value.  Comparisons at other time points will only present the point 
estimate and 95% confidence interval.  The analyses will incorporate all data from individual tooth sites within         
each subject.  
b ANCOVA will be used for the analysis of this variable.  The dependent variable will be change from baseline to Day 
270 and the model will include treatment group, patients, smoking status, and investigational site for this endpoint.  
Only treatment comparisons at Day 270 will report a p-value.  Comparisons at other time points will only present the 
point estimate and 95% confidence interval.   
8.3 Analysis Methods 
The Day 270 analyses will be independent of the Day 90 analyses.  All primary and 
secondary efficacy analyses unless otherwise stated will be performed on the ITT 
population.  Unblinding will be performed for the Primary and secondary analyses at Day 
270. 
8.3.1 Primary Efficacy Analyses 
The generalized estimating equations (GEE) method with a linear link and exchangeable 
covariance matrix (within subject correlation structure) will be used to estimate the 
treatment group effects with respect to change from baseline PD at 270 days, adjusted for 
baseline PD in tooth-sites with baseline PD ≥6 mm.  The two primary hypotheses to be 
tested are:  
1) The change in PD from baseline (PD ≥6 mm) (Screening Visit) at the 270 Day 
Visit differs between the Group 1 (see section 2.4) and Group 3 (placebo) 
treatments. Point estimates and 95% confidence intervals will be presented for the 
Version:  ST266-Perio-201_SAP_v4.0  Page 23 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
treatment group differences in PD change from baseline at Day 270 by baseline 
smoker status.;   
2) The change in PD from baseline (PD ≥6 mm) (Screening Visit) at the 270 Day 
Visit differs between the Group 2 (see section 2.4) and Group 3 (placebo) 
treatments. Point estimates and 95% confidence intervals will be presented for the 
treatment group differences in PD change from baseline at Day 270 by baseline 
smoker status.    
SAS code for the GEE model is as follows: 
 
proc gee data=Day270dataset   
   where (base>=6 and ITT Set=’Y’  and paramcd='PDEPTH'); 
   class subjid trt01a site smoker_status; 
   model chg = trt01a base site smoker_status smoker_status*trt01a; 
   repeated  sub=subjid /type=exch; 
   lsmeans trt01a/pdiff; 
run; 
 
Where: 
1) The Day270dataset only includes records for Day 270visit) 
2) chg = change from baseline of each individual toot site 
3) (base>=6 and ittfl='Y' and paramcd='PDEPTH'):  subsets the dataset to include only 
PD outcomes, the ITT population, and tooth sites with baseline PD greater or equal 
to 6mm.    
4) chg= change in PD from baseline 
5) trt01a = treatment group 
6) site=investigator institution rather than tooth site 
7) base = baseline PD 
The 15-, 30-, and 60-Day visits were not included in the primary statistical model since 
the tooth-sites at the earlier visits may still be healing from the effects of the SRP 
procedure with possible SRP-related gingival swelling affecting the PD measures.  
Since there are two primary hypotheses, Bonferroni corrections will control for 
multiplicity with p<0.025 considered significant.  Point estimates and 95% confidence 
intervals will be presented for the treatment group differences in change from baseline at 
each assessment time point.  These analyses will be performed once all the subjects 
(excluding those withdrawn) have been unblinded and completed their 270-Day Visit.  
8.3.2 Secondary Efficacy Analyses 
Additional secondary efficacy analyses will be performed  to test the effects of treatment 
group and their interactions on the secondary endpoints of the change from baseline in 
CAL and BOP at Day 270.  For the CAL analysis, the GEE analyses will be performed 
with the same statistical model as described in the primary PD  efficacy analysis  but with 
the change from baseline in CAL of tooth-sites with baseline PD ≥6 mm as the dependent 
Version:  ST266-Perio-201_SAP_v4.0  Page 24 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
variable.  Separate hypotheses will be performed for testing the treatment effects of group 
1 versus group 3 (placebo) and group 2 versus group 3 (placebo).  As described above, 
this model will include the baseline smoker status (smoker or non-smoker) by treatment 
group interaction.   For the secondary efficacy analyses of the BOP change from baseline, 
ANCOVA will be performed with treatment group as the main effect, and covariates for 
baseline PD, site, patients, smoker status, and the baseline smoker status (smoker or non-
smoker) by treatment group interaction .   Point estimates and 95% confidence intervals 
will be presented for the treatment group differences in CAL and BOP change from 
baseline at Day 270 and by baseline smoker status.    
The CAL and BOP secondary analyses described above will be tested hierarchically in 
the order of: CAL change from baseline at Day 270, and BOP (presented as a whole 
mouth average percentage) change from baseline at Day 270.  The treatment effects for 
the CAL or BOP change from baseline at the Day 270 Visit will be compared between 
Treatment Group 1 and Placebo, and between Treatment Group 2 and Placebo.  The 
alpha will be set at 0.025 to allow for the Bonferroni correction for 2 multiple 
comparisons for secondary endpoints.  Since the smoker status by treatment group 
interaction is acting as a gatekeeper for further inference testing by smoker status, no 
additional corrections will be made for multiplicity for any additional analyses of the 
effects of treatment on CAL and BOP by smoker status. These analyses will be 
performed once all the subjects (excluding those withdrawn) completed their 270-Day 
Visit. 
All primary and secondary analyses performed on the ITT population will be repeated 
using the per protocol population. 
8.3.3 Efficacy Analyses at Other Time Points 
The same technique used for the primary and secondary endpoints will be used for the 
other assessed time points.  Point estimates and 95% confidence intervals will be 
presented for change from baseline at each assessment time point.  The p-values will not 
be presented for these analyses. Actual value and change from baseline will be presented 
for each scheduled collection visit for the summarized endpoint.  Please refer to Section 
15.2 for the schedule of assessments. 
8.3.4 Exploratory Efficacy Analyses  
FMPI will be analyzed using the GEE method described in section 8.3.1 at days 90, 180, 
and 270.  Additionally, CAL change from baseline at days 180 and 270 using all tooth-
sites will be analyzed using GEE.  PD change from baseline at days 90, 180, and 270 
using a whole-mouth average will be analyzed using ANCOVA with the model described 
previously. 
Analysis methods for the exploratory efficacy outcomes, (1) inflammatory cytokines in 
GCF and serum, (2) microbial periodontal flora and (3) RBL will be described in a 
separate statistical analysis plan. 
Version:  ST266-Perio-201_SAP_v4.0  Page 25 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
8.4 Examination of Subgroups 
To explore the potential effect of age and gender on response,  and to further explore the 
effect of smoking, PD and CAL in tooth-sites with baseline PD ≥ 6mm will also 
investigated with exploratory analyses using the following categories: 
• Age (< median age; ≥ median age) 
• Gender (male, female) 
• Current disease smoking status (smoker – has smoked within the past two years, 
non-smoker – has never smoked or quit > 2 years ago). 
The model used for the original analyses of these variables will form the basis for 
separate analyses for each of these factors.  However, in addition to the factors in the 
original model, an additional main effect (e.g. gender) and interaction term (e.g. gender 
by treatment) will be included in the model. 
8.5 Exploratory Categorical Analysis of PD  
In addition to analyzing PD as continuous variable, it is often useful to analyze PD 
categorically. The following may also be summarized descriptively:   
• Percent of subjects in each group with a mean PD change from baseline <-4mm, 
<-3mm, <-2mm, <-1mm, -1mm to 1mm, >1mm, >2mm, >3mm, >4mm at 90, 180 
and 270 days 
• Percent of subjects with pockets decreasing by 2mm or more that at baseline were 
< 5mm at 90, 180, and 270 days. 
• Percent of tooth sites in each group with a mean PD change from baseline            
<-4mm, <-3mm, <-2mm, <-1mm, -1mm to 1mm, >1mm, >2mm, >3mm, >4mm at 
90, 180 and 270 days 
• Percent of subjects in each group with a mean PD <5mm, <6mm and < 7mm at 
90, 180 and 270 days 
• Percent of subjects in each group with all PD <5mm, <6mm and < 7mm at 90, 
180 and 270 days 
• Percent of subjects with 75% of pockets < 5mm that at baseline were < 5mm  at 
90, 180, and 270 days. 
• Percent of tooth sites in each group with a mean PD <5mm, <6mm and < 7mm at 
90, 180 and 270 days 
• Percent of subjects in each group with PD <5mm at day 90 by baseline PD 
Version:  ST266-Perio-201_SAP_v4.0  Page 26 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
8.6 Pooled comparisons 
In addition to the above analyses that compare results between each active treatment 
group (N=50/group) and the placebo group (N=50), “pooled” analyses will be performed 
that combine the data from both active treatment groups (N=100) for comparison to the 
placebo group (N=50).  Point estimates and 95% confidence intervals will be presented 
for change from baseline at each assessment time point.  The p-values will not be 
presented for these analyses.    
Version:  ST266-Perio-201_SAP_v4.0  Page 27 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
9. SAFETY EVALUATION 
9.1 Overview of Safety Analysis Methods 
Safety analyses will be presented descriptively on the safety population.  No statistical 
testing will be performed.  
9.2 Extent of Exposure 
Treatment compliance will be presented at each visit and overall by group using both 
continuous summary statistics and the following frequency cut-offs: <50%, 50 - 80%, 80 
- 90%%, >90%. 
Treatment compliance will be calculated as: 
[(# doses completed within X days (within 3 days in the first 60 days; within 5 days at 
Day 90; within 7 days at Day 180) from original scheduled dose date)/(# planned 
doses)]*100 
Duration of therapy will be summarized by treatment group using continuous summary 
statistics.  Duration of therapy in months will be calculated as: 
(last dose date – first dose date + 1)/30.4375. 
Number of doses received will be summarized by treatment group using continuous 
summary statistics.   
Information regarding the extent of exposure will also be presented in a listing presenting 
subject, dosing schedule/treatment group, planned dosing day, whether the subject was 
dose within X days (within 3 days in the first 60 days; within 5 days at Day 90; within 7 
days at Day 180), actual dosing day, treatment compliance, duration of therapy, and 
number of doses received. 
9.3 Adverse Events 
The most recently available MedDRA dictionary version will be used for the 
classification of adverse events. 
On-study AEs are those with a start date on or after the first treatment dose date and prior 
to the last treatment dose date + 30 Days. 
On-study adverse events will be summarized overall by treatment group and by worst 
severity.  Drug-related adverse events will also be tabulated.   
All adverse events will be presented in a listing which includes first treatment dose date, 
onset and resolution date/day (or whether it is ongoing), system organ class and preferred 
term, investigator term, whether the event is serious, whether the adverse event involves 
Version:  ST266-Perio-201_SAP_v4.0  Page 28 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
hematuria or proteinuria, severity grade, relationship to study drug, action taken, 
sequelae, and outcome. 
9.4 Deaths, Serious Adverse Events, and Other Significant Adverse 
Events 
The number of deaths will be presented along with the corresponding reason for death. 
On study serious adverse events will be classified by system organ class and preferred 
term.  They will be presented overall by treatment group and by worst severity.  Drug-
related serious adverse events will also be tabulated.   
On study adverse events leading to discontinuation will be classified by system organ 
class and preferred term.  They will be presented overall by treatment group and by worst 
severity.  Drug-related adverse events leading to discontinuation will also be tabulated.   
9.5 Clinical Laboratory Evaluation 
Blood is to be drawn and urine collected for laboratory analysis at Screening, and on 
Days 90 and 270.  The following clinical laboratory parameters are to be assessed:  
• Hematology: Complete blood count 
• Blood chemistry: serum glucose, C-reactive protein, blood urea nitrogen, 
creatinine, electrolytes, HbA1c (at screening only), and liver function including 
bilirubin and hepatic enzymes 
• Urinalysis: hematuria, proteinuria, pregnancy test (at screening and final visit 
only) 
Tables will present continuous summary statistics for each lab parameter collected by 
visit and treatment group. 
Laboratory values outside the normal range will be flagged as “high” or “low”.  
Percentage of subjects with values falling in high, normal, and low ranges will be 
summarized by lab parameter and visit, by treatment group. 
9.6 Vital Signs, Physical Findings, and Other Observations Related to 
Safety 
9.6.1 Vital Signs 
Systolic blood pressure, diastolic blood pressure, heart rate, respiratory rate, and 
temperature will be collected at screening, baseline, SRP visit, day 1, day 15, day 30, day 
60, Day 90, Day 180 and Day 270 (or end of study).  Height and weight will be collected 
at screening and Day 270 (or end of study). 
Version:  ST266-Perio-201_SAP_v4.0  Page 29 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
Summaries of actual values and change from baseline at each visit will be presented in a 
table.  A listing will also be provided with vital sign value at each visit as well as an 
indicator of the clinical significance of the finding, if any. 
9.6.2 Physical Examinations 
An oral exam will also take place at each visit.  Results will be presented in a listing 
similar to that described in Section 6 of the SAP but will also include the visit associated 
with the exam results. 
9.6.3 Other Safety Measures 
Medical and dental history will be updated at each visit.  Medical history events and 
dental history events since baseline will be presented in a listing similar to that described 
in Section 6 of the SAP but will also include the visit associated with the exam results.  
Version:  ST266-Perio-201_SAP_v4.0  Page 30 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
10. TIMING OF DATA COLLECTION AND ANALYSES 
In this study, subjects will be followed for a total duration of 9 months.  After all subjects 
have completed their Day 270 visit, the database will be locked and Day 270 analysis will 
be performed. Results will be presented as described above with the additional data from 
Days 180 and 270. 
Version:  ST266-Perio-201_SAP_v4.0  Page 31 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
11. REFERENCES 
1. US Federal Register. (1998) International Conference on Harmonization; Guidance 
for Industry: Statistical Principles for Clinical Trials. Department of Health and 
Human Services: Food and Drug Administration.  Federal Register, Vol. 63, No. 179, 
September 16, 1998, page 49583. 
2. US Federal Register. (1996) International Conference on Harmonization; Guidance 
for Industry: Structure and Content of Clinical Study Reports. Department of Health 
and Human Services: Food and Drug Administration.  Federal Register Vol. 61, July 
17, 1996, page 37320. 
3. Yuan YC.  Multiple imputation for missing data: Concepts and new development.  
SAS Institute, Inc. 2000. 
4. Rubin DB. Inference and missing data. Biometrika 1976;63(3):581–90. 
5. Schafer JL. Analysis of incomplete multivariate data. London: Chapman & Hall; 
1997. 
Version:  ST266-Perio-201_SAP_v4.0  Page 32 of 35 
Stemnion, Inc. CONFIDENTIAL Statistical Analysis Plan 
Protocol No. ST266-PERIO-201  02 October 2017 
12. APPENDICES 
12.1 Study Flow Chart 
 
Version:  ST266-Perio-201_SAP_v4.0  Page 33 of 35 
Stemnion, Inc.  CONFIDENTIAL                  Statistical Analysis Plan 
Protocol No. ST266-PERIO-201                                   02 October 2017 
 
12.2 Schedule of Events 
         Page 34 of 35 
Version:  ST266-Perio-201_SAP_v4.0  Page 34 of 35 
 
 
THIS PAGE HAS BEEN INTENTIONALLY LEFT BLANK 
             
Version:  ST266-Perio-201_SAP_v4.0  Page 35 of 35 
 