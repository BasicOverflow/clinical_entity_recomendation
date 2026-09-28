Version 1 Improve SCA Statistical Analysis Plan Page 1 of 26  
11 NOV 2015 Medtronic Confidential  
 
 
 
 
 
 
 
 
IMPROVE SCA 
 
Statistical Analysis Plan 
 
 
 
 
 
Version 1 
11 NOV 2015 
 
 
 
 
 
 
 
 
 
 
 
Study Statisticians: Jeff Cerkvenik, Joao Monteiro  

Version 1 Improve SCA Statistical Analysis Plan Page 2 of 26  
11 NOV 2015 Medtronic Confidential  
 
TABLE OF CONTENTS 
1 PURPOSE ................................................................................................................................ 3 
2 STUDY OVERVIEW ................................................................................................................. 3 
3 DESCRIPTION OF ANALYSIS ................................................................................................ 3 
3.1 General Summaries ........................................................................................................... 3 
3.1.1 Description of Baseline Variables ........................................................................... 3 
3.1.2 Special Considerations ........................................................................................... 3 
3.1.3 Reports for which this Statistical Analysis Plan applies .......................................... 4 
3.2 Primary Objective: Appropriate Therapy ........................................................................... 4 
3.3 Secondary Objective: Mortality .......................................................................................... 7 
3.3.1 Power ...................................................................................................................... 9 
3.3.2 Determination of Patients/Data for Analysis ......................................................... 10 
 
  
  
  
4 REFERENCES ....................................................................................................................... 11 
5 APPENDIX ............................................................................................................................. 12 
 

Version 1 Improve SCA Statistical Analysis Plan Page 3 of 26  
11 NOV 2015 Medtronic Confidential  
 
1 PURPOSE 
This Statistical Analysis Plan has been designed to document, before data is analyzed, the rationale for 
the study design, and the planned analyses that will be included in study reports.  This plan does not limit 
the analysis provided in reports, and additional analysis of the study data beyond this plan is expected.  
 
The Statistical Analysis Plan was developed based on version 1.0 of the Improve SCA Study Clinical 
Investigation Plan dated December 23, 2013. 
 
2 STUDY OVERVIEW 
The study design and rationale can be found in the Clinical Investigational Plan (CIP). The Improve SCA 
study is a prospective, non-randomized, non-blinded, global, interventional, multi-site post-market study.   
The study purpose is to demonstrate that primary prevention patients with one or more additional risk 
factors (1.5 prevention criteria: syncope/pre-syncope, non-sustained ventricular tachycardia (NSVT), 
frequent pre-ventricular contractions (PVCs), and low left ventricular ejection fraction (LVEF)) are at a 
similar risk of life-threatening ventricular arrhythmias (LTVA) when compared to secondary prevention 
patients, and would receive similar benefit from an implantable cardioverter defibrillator (ICD), or cardiac 
resynchronization therapy- defibrillator (CRT-D) implant. Additional objectives evaluating mortality, cost 
effectiveness, reason for implant refusal, and Chagas disease will be analy zed. 
 
3 DESCRIPTION OF ANALYSIS 
3.1 General Summaries 
The Medtronic statisticians who are assigned to the project will conduct all statistical analyses.  The 
primary objective is to compare 1.5 prevention patients with secondary prevention patients regarding the 
time to first appropriately treated VT/VF.  There is also a secondary objective to compare the mortality 
rates between patients with an implanted device (ICD/ CRT-D) and those without, for patients meeting 1.5 
prevention criteria.   
 
 
3.1.1 Description of Baseline Variables 
A number of characteristics will be reported for each enrolled subject at time of enrollment.  The variables 
collected will include demographics, medical history, NYHA classification, and cardiovascular 
medications. Tables and descriptive statistics will be used to summarize subject data with respect to 
these variables.  
 
3.1.2 Special Considerations 
Medtronic statisticians will perform the statistical analyses.  Sample size estimates were calculated using 
SAS Version 9.2 (SAS Institute Inc.). 
 
Analysis Cohort 
Patients with any of the following deviations from the study protocol will be excluded from all statistical 
analysis, as if they were never enrolled in the study: 
• Patients that violate any of the inclusion/exclusion criteria. 

Version 1 Improve SCA Statistical Analysis Plan Page 4 of 26  
11 NOV 2015 Medtronic Confidential  
 
• Primary prevention patients that did not have LVEF measured at baseline or the 1.5 criteria 
assessment 
• Patients with LVEF measured prior to 40 days post-MI OR prior to 90 days post-MI with 
revascularization. 
• Primary ICD indication patient that is not Class I. 
• Primary prevention patients without history of any 1.5 criteria and no Holter test performed  
• Primary prevention patients without history of any 1.5 criteria and Holter test performed more than 
12 months prior to enrollment or more than 3 months after enrollment. 
• Primary prevention patients with no 1.5 criteria assessment. 
• Patients with a Baseline or Medical History CRF dated after implant. 
• Patients with consent date after implant decision date. 
• Patients with previous ICD or CRT-D. 
• Patients implanted with a Non-Medtronic device. 
• Patients exiting the study or dying prior to completing the Medical History CRF, or the Implant 
CRF. 
 
3.1.3 Reports for which this Statistical Analysis Plan applies 
 
This analysis plan shall apply to the final report. Statistical analysis for study relate d publications will not 
be limited to this plan.  However, it is the intent that the main study publication will follow the methods 
detailed in this plan, which in some cases supersede the investigational plan. 
3.2 Primary Objective: Appropriate Therapy 
The primary objective is to demonstrate that appropriate VT/VF therapy rates (shock and ATP) for 
subjects meeting 1.5 prevention criteria implanted with a Medtronic device (ICD/CRT -D) are equivalent 
(within 30%) to rates in subjects meeting secondary prevention criteria. 
 
The primary objective will be evaluated by using post-implant time to first appropriate VT/VF therapy 
(shock and ATP). More specifically, the following hypothesis will be tested: 
 
Hypothesis 
Ho:  Hazard ratio of Implanted 1.5 patients to implanted secondary patients ≤ 0.70 
Ha:  Hazard ratio of Implanted 1.5 patients to implanted secondary patients > 0.70  
 
 
Endpoint Definition 
The event of interest for this objective is appropriate VT/VF therapy.  To qualify as an event, a VT/VF 
event observed by the ICD/CRT must be adjudicated to be one of the following by the Episode Rev iew 
Committee: 
o Polymorphic VT/VF 
o Monomorphic VT 
o Non-sustained VT/VF 
o Other VT/VF, specify: 
Additionally, the episode must have been treated either by ATP, shock, or both by t he device. 
  
 
Version 1 Improve SCA Statistical Analysis Plan Page 5 of 26  
11 NOV 2015 Medtronic Confidential  
 
Performance Requirement 
The null hypothesis will be rejected if the one-sided 95% lower confidence bound of the hazard ratio of 
implanted 1.5 subjects to implanted secondary prevention subjects is greater than 0.70.  
 
 
Analysis Methods 
A Cox proportional hazard model will be used to compare the hazard rates of first appropriate VT/VF 
therapy between implanted subjects meeting 1.5 prevention criteria and secondary prevention subjects.  
Because secondary and 1.5 patients are known to be different in many potential covariates, the Cox 
proportional hazards model will not include any covariates. The one-sided hypothesis test will be 
performed by computing a 90% two-tailed confidence interval for the hazard ratio between the groups and 
using the lower limit of this estimated 90% CI as a rejection boundary of the null hypothesis. In particular, 
if the 90% CI lower limit is greater than 0.7 then the null hypothesis will be rejected.  
 
The analysis will be performed using SAS code similar to: 
 
proc phreg data = alldata; 
where group in (‘A’,’C’); 
class group (ref = ‘A’); 
model time2event*eventStatus(0)= group/ rl alpha = 0.1; 
run; 
 
Additionally, Kaplan-Meier estimates of the survival curves will be displayed for each prevention criteria 
group.  
 
 
Determination of Patients/Data for Analysis 
 
• All 1.5 prevention and secondary prevention subjects with an ICD/CRT-D implant and at least one 
device interrogation available in the database will be included in the primary analysis hypothesis 
test. This includes subjects implanted with a device after the initial enrollment period. These later 
implants will be included if they are secondary or 1.5 at the time of implant.  
• Time 0 is the implant date and, if no events occur, subjects will be censored on the date of their 
latest device interrogation.  
• VT/VF episodes that cannot be adjudicated (due to not saving full episode data or any other 
reason) will be ignored. Often, these episodes are followed by episodes that can be adjudicated, 
and since the endpoint is time to first episode, effects on the results from these events will be 
minimal. In addition, these should be balanced between the comparison groups . 
 
Version 1 Improve SCA Statistical Analysis Plan Page 6 of 26  
11 NOV 2015 Medtronic Confidential  
 
Sample Size Calculation 
The minimum required sample size for this study has been estimated to be 4800 subjects based on the 
following: 
 
• 60% of enrollments will be secondary prevention and 40% primary prevention  
• 50% of primary subjects will be in the 1.5 group 
• 57% of secondary subjects will get an ICD (includes CRT-D) 
• 45% of 1.5 subjects will get an ICD 
• 22% of 1.0 subjects will get an ICD 
• Annual attrition (includes exits and deaths) will be 10% 
• The study will end two years after the last enrollment 
• 4000 patients will take 2 years to enroll with enrollment beginning slowly, and then accelerating to 
a steady 246 per month 
• Expected rates of appropriately treated VT/VF in secondary subjects follow Figure 2, with a 
higher rate in the first year (22.5%), then a constant rate (11.1%) thereafter 
• The hazard ratio of 1.5 to secondary is 0.91  
 
Under the above assumptions and using the hypothesis test stated above, 4800 subjects will have 80% 
power to reject the null hypothesis. With 4800 enrolled patients, it is expected that appr oximately 1650 
secondary prevention subjects will be implanted, 430 1.5 prevention subjects will be implanted, and 200 
1.0 subjects will be implanted.  
 
More details, including the simulation program can be found in the Appendix. 
 
 
Sample Size Re-estimation 
Because most of the assumptions above are based only on investigator opinion, the sample size will be 
re-estimated during the study using the same simulation methods, but changing the following 
assumptions using the study data: 
 
• % of enrollments will be secondary prevention  
• % of primary patients in the 1.5 group 
• % of secondary patients who will get an ICD (includes CRT-D) 
• % of 1.5 patients who will get an ICD 
• % of 1.0 patients who will get an ICD 
• Annual attrition (includes exits and deaths) 
• Enrollment rate 
 
With this re-estimation of sample size, the length of follow-up after the last enrollment may be changed as 
well. Because no comparisons will be done at the point of re-estimation, alpha is not affected and the final 
analysis can compare the p-value to a 0.05 alpha level. 
 
The sample size re-estimation will occur at the later of: 
• One year after the 400th subject has been enrolled 
• The time of the 2000th enrollment.  
 
The database will be frozen for the sample size re-estimation with a visit cut-off date of 4 weeks after the 
2000th enrollment, and an enrollment cut-off of the date of the 2000th enrollment.  That will allow collection 
of 1.5 Criteria and implant/implant refusal data for the last subjects enrolled prior to the enrollment c ut-off.  
The enrollment cut-off means any subject consented after that date will not be included in analysis.  
 
Subjects who meet the “excluded” criteria in section 3.1.2 will not be included in the sample size re -
estimation calculations.  This will mean less than 2000 subjects will be included.  Additionally, the new 
sample size will add subjects to replace the excluded subjects.  For example, if 1900 subjects are not 
Version 1 Improve SCA Statistical Analysis Plan Page 7 of 26  
11 NOV 2015 Medtronic Confidential  
 
excluded at the time of database freeze and the sample size re-estimate calls for 3000 subjects, then 
1100 more non-excluded subjects will need to be enrolled in the study. 
 
It is the study sponsor’s discretion to increase (to a maximum of 8000 subjects) or decrease the sample 
size, or increase or decrease the length of follow-up after last enrollment.  
 
If fewer subjects are required, the study sponsor may either lower the sample size, or increase the power 
of the study (possibly keeping the original sample size).  If more subjects are required, the study sponsor 
may elect to not increase the sample size, but may increase the length of follow-up to ensure adequate 
power for the study.   
 
Study sites will be notified of any change in sample size and length of follow-up (if applicable) at that time. 
The investigational plan will not be changed. 
 
3.3 Secondary Objective: Mortality 
The secondary objective is to compare the mortality rates for patients meeting 1.5 prevention criteria 
between those implanted with a device (ICD/CRT-D) and those not implanted. 
 
Hypothesis 
Although this is an exploratory objective and is not powered, a hypothesis test will be done and compared 
to an alpha level of 0.05.  
 
Ho:  Hazard ratio of non-implanted to implanted 1.5 patients = 1 
Ha:  Hazard ratio of non-implanted to implanted 1.5 patients ≠ 1 
 
Analysis Methods 
A Cox proportional hazards model will be used to compare the mortality rates between subjects with 
device implant and without, in subjects who meet the 1.5 prevention criteria. In addition to the implant/no 
implant variable, the Cox proportional hazards model will include baseline covariates that are known to be 
associated with mortality and that might be unbalanced between the groups due to the non -randomized 
study design. These covariates are: 
• age at consent 
• sex 
• QRS duration 
• ischemic cardiomyopathy (yes/no) 
• left bundle branch block (LBBB) (yes/no) 
• NYHA Classification (treated as an ordinal variable, including 0 for those without HF) 
• diabetes (Type 1 or 2 only, gestational not counted) (yes/no) 
• LVEF (taken from the 1.5 Visit CRF, if it exists, or from the Baseline CRF) 
• syncope qualifying as 1.5 (yes/no) 
• NSVT qualifying as 1.5 (yes/no) 
• PVCs qualifying as 1.5 (yes/no)  
 
Note that all 3 categorical 1.5 covariates can be found at the end of the 1.5 Criteria  CRF.  The NSVT and 
PVC variables on the Baseline CRF do not include the minimum thresholds of 3 consecutive >100 bpm 
beats for NSVT and 10 or more PVCs per hour. 
 
Country of enrollment was to be included as a covariate according to the CIP, but it will not be  included 
as subjects in the study (who all have medical care) may not have significantly different mortality rates 
between countries.  Also, some countries may have a small number of enrollments.  The idea was to 
have covariates with known mortality risks. 
Version 1 Improve SCA Statistical Analysis Plan Page 8 of 26  
11 NOV 2015 Medtronic Confidential  
 
LBBB and diabetes are added covariates from the CIP based on steering committee input.  LBBB was 
added because it is a well-known mortality risk factor.  Diabetes was not originally collected in the study, 
but was added later and is being collected for all subjects, including those enrolled prior to it being added 
to the Medical History CRF. 
 
Due to the large sample size, it is likely that some subjects will have covariates missing.  To circumvent 
this problem, multiple imputation methods will be used. More specifically:  
 
• The number of imputed datasets to be created will be 20. 
• The imputation of missing values will be done using the fully conditional specification (FCS) 
method, where the covariates in the imputation model are the same covariates in the Cox 
proportional model (except the covariate being imputed) plus implant/no implant, the event 
indicator and the Nelson-Aalen estimator of the cumulative hazard function as suggested by 
White and Royston (2009).  
• The imputation for missing binary variables (e.g., gender) will be done via the FCS logistic 
regression method, and for missing continuous variables (e.g., QRS) it will be done via the FCS 
linear regression method.  
• Missing NYHA will be imputed via FCS ordinal logistic regression. 
• All continuous variables will be standardized before the imputation phase, in order to avoid the 
FCS linear regression imputing values that are not realistic (e.g., negative LVEF). 
• The null hypothesis will be rejected if the pooled p-value for the implant/no-implant covariate is 
less than 0.05. 
 
The analysis will be performed using SAS code similar to: 
 
/*Nelson-Aalen Estimates for Cumulative Hazard Function*/ 
 
proc phreg data=alldataneeded1p5 noprint; 
  model SURVTIME*EVENT(0) =; 
  output out=alldataneeded1p5_2 logsurv=logs / method=emp; 
run; 
 
data Alldataneeded1p5_2; 
  set Alldataneeded1p5_2; 
  cumhaz = -logs; 
run; 
 
proc standard  data = Alldataneeded1p5_2 mean = 0 std=1 out=      
Alldataneeded1p5_3; 
  var AGE LVEF0 QRS; 
run; 
 
/*Imputation Phase*/ 
proc mi data= Alldataneeded1p5_3 nimpute = 5 out = mi_alldata_1p5 ; 
class SEXCHAR CMYISCH LBBB NYHA0 DIABETES CRIT15SYNC CRIT15NSVT CRIT15PVC 
GROUP EVENT;  
var AGE SEXCHAR QRS CMYISCH LBBB NYHA0 DIABETES LVEF0 CRIT15SYNC CRIT15NSVT 
CRIT15PVC GROUP CUMHAZ EVENT; 
fcs logistic(SEXCHAR CMYISCH LBBB NYHA0 DIABETES CRIT15SYNC CRIT15NSVT 
CRIT15PVC GROUP EVENT);  
run; 
 
/*Analysis Phase*/ 
proc phreg data = mi_alldata_1p5; 
class SEXCHAR CMYISCH LBBB NYHA0 DIABETES CRIT15SYNC CRIT15NSVT CRIT15PVC 
GROUP EVENT;  
Version 1 Improve SCA Statistical Analysis Plan Page 9 of 26  
11 NOV 2015 Medtronic Confidential  
 
model SURVTIME*EVENT(0) = AGE SEXCHAR QRS CMYISCH LBBB NYHA0 DIABETES LVEF0 
CRIT15SYNC CRIT15NSVT CRIT15PVC GROUP ; 
by _Imputation_; 
ods output ParameterEstimates=coxReg_fcs; 
ods output Type3=type3table; 
run; 
 
/*Pooling Phase*/ 
proc mianalyze parms(classvar=ClassVal) = coxReg_fcs; 
class SEXCHAR CMYISCH LBBB NYHA0 DIABETES CRIT15SYNC CRIT15NSVT CRIT15PVC 
GROUP;  
modeleffects  AGE SEXCHAR QRS CMYISCH LBBB NYHA0 DIABETES LVEF0 CRIT15SYNC 
CRIT15NSVT CRIT15PVC GROUP ; 
run; 
 
Kaplan-Meier estimates of the survival curves will be displayed for each group.  
 
The same analysis will be performed comparing implanted and not implanted 1.0 subjects.  
 
Time to Event Considerations 
 
• Time 0 is the enrollment date and subjects will be censored on the last date they were confirmed 
to be alive.  
• Non-implanted patients that later decided to implant the ICD/CRT-D, will have their time to event 
censored at the day of the implant procedure. 
• Implanted patients that explanted the device (without replacement) will continue to be followed as 
part of the implanted group.  These cases will be rare, and unless the explant is completely 
voluntary (i.e., not due to infection, or imminent subject end-of-life), censoring subjects at explant 
would bias the results in favor of implant.  This is an intention-to-treat approach. 
• Patients that had heart transplant will have their time to event censored at the day of the 
transplant. 
3.3.1 Power 
This objective is not powered and the likelihood of a statistically significant test is not known. Therefore, it 
should not be a surprise if the endpoint is not statistically significant. 
The following table shows what the power of the endpoint would be under various scenarios if doing a 
log-rank test (see PASS screen shot in the appendix for details). It is not known what effect adding 
covariates in a Cox proportional hazards model will have on the power.   
In a retrospective analysis of SCD-HeFT, 1.5 prevention subjects without an ICD had a 25.7% mortality 
rate at 3 years compared to 18.5% for 1.5 subjects with an ICD. Under the sample size assumptions, it is 
expected that approximately 430 1.5 subjects will be implanted and 540 will not.  
Power for 1.5 Prevention Mortality Endpoint 
1.5 
implanted 
sample 
size 
1.5 not 
implanted 
sample 
size 
Assumed 3-year Mortality 
26% no 
ICD 
18% ICD 
26% no 
ICD 
20% ICD 
26% no 
ICD 
22% ICD 
22% no 
ICD 
14% ICD 
30% no 
ICD 
22% ICD 
450 550 88% 63% 32% 93% 82% 
350 650 85% 60% 30% 91% 79% 
360 440 80% 53% 27% 87% 73% 
350 350 74% 48% 24% 83% 67% 
Version 1 Improve SCA Statistical Analysis Plan Page 10 of 26  
11 NOV 2015 Medtronic Confidential  
 
3.3.2 Determination of Patients/Data for Analysis  
All subjects in the 1.5 prevention cohort at the time of enrollment who do not meet the criteria in section 
3.1.2 of this document will be included. The same criteria apply for the 1.0 subjects in their mortality 
analysis. 
  
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
  
 
 
 
 
 
 
  
 
 
 
 
  
 
Hypothesis 
Although this is an exploratory objective and is not powered, a hypothesis test will be done and compared 
to an alpha level of 0.05.  

Version 1 Improve SCA Statistical Analysis Plan Page 11 of 26  
11 NOV 2015 Medtronic Confidential  
 
 
Ho:  Hazard ratio of patients with Chagas disease to patients without Chagas disease = 1 
Ha:  Hazard ratio of patients with Chagas disease to patients without Chagas disease ≠ 1 
 
Only subjects with implant (regardless the prevention criteria group) will be included  in the analysis. 
Subjects with missing information regarding Chagas disease will not be included.  
 
 
The hypothesis will be tested separately for 1.0, 1.5, and secondary groups.  
 
Analysis Methods 
A Cox proportional hazard model will be used to compare the hazard rates of first appropriate VT/VF 
therapy between subjects with Chagas disease and subjects without Chagas disease within each group 
(1.0, 1.5, and secondary). The Cox proportional hazards model will only include the Chagas disease 
indicator. The null hypothesis will be rejected if the p-value for the Chagas disease indicator covariate is 
less than 0.05. 
The analysis will be performed using SAS code similar to: 
 
proc phreg data=alldataneeded ; 
  class chagas; 
  model firstVTVFappropTreat*event(0) = chagas;   
run; 
 
Time to Event Considerations 
 
• Time 0 is the implant date and, if no events occur, subjects will be censored on the date of their 
latest device interrogation. Only spontaneous, appropriately treated VT/VF episodes as 
adjudicated by the episode review committee will count toward the endpoint.   
• VT/VF episodes that cannot be adjudicated (due to not saving full episode data or any other 
reason) will be ignored. Often, these episodes are followed by episodes that can be adjudicated, 
and since the endpoint is time to first episode, effects on the results from these events will be 
minimal. In addition, these should be balanced between the comparison groups . 
 
4 REFERENCES 
 
1. White, I.R. and Royston P. (2009) Imputing missing covariate values for the Cox model. Statistics 
in Medicine 28: 1982 – 1998.  
 
 
  
Version 1 Improve SCA Statistical Analysis Plan Page 12 of 26  
11 NOV 2015 Medtronic Confidential  
 
5 APPENDIX 
Sample size details 
The % in each study group was based on estimates from the steering committee.  It was assumed 1/3 
would be enrolled in India, 1/3 in China, and 1/3 in the rest of the world.  The table below shows the 
estimates from steering committee members, and the overall estimate, which was derived in a non-
formulatic way from the physicians’ estimates. 
 
 
   % Implanted 
 %Secondary Secondary 1.5 1.0 
Physician My center 
Others in 
my 
country My center 
Other 
centers in 
my 
country My center 
Other 
centers in 
my 
country My center 
Other 
centers in 
my 
country 
Chasnoits 
(Belarus) 75 No ans. 98 90 65 65 40 40 
Singh 
(India) 70 80 80 10-80 No answer 15 15 
Zhang 
(China) 50 50 50 15 60 25 40 10 
Huang 
(China) 30 55 50 30 40 30 30 30 
Overall 
estimate 60* 57 45 22 
* Takes into account efforts to promote enrolling primary prevention subjects.  
 
 
The program sim.sas produced power calculations based on the sample size assumptions.  The program 
was run feeding in sample sizes from 4000-5000.  Each study sample size was simulated 10,000 times, 
and the resulting power (% of time the lower one-sided 95% confidence limit of the hazard ratio (HR) was 
above 0.70) and the average hazard ratio for the 10,000 simulations are shown.  
 
Sample size Power HR 
4000 73.6 0.904 
4050 74.9 0.904 
4100 75.2 0.904 
4150 74.6 0.903 
4200 76.0 0.905 
4250 75.6 0.904 
4300 77.6 0.905 
4350 76.7 0.903 
4400 77.7 0.904 
4450 78.1 0.903 
4500 78.2 0.903 
4550 79.2 0.904 
4600 79.0 0.904 
4650 79.5 0.905 
4700 79.9 0.903 
4750 80.5 0.903 
4800 80.4 0.903 
4850 80.6 0.902 
4900 81.6 0.904 
4950 81.8 0.904 
5000 82.3 0.903 
Version 1 Improve SCA Statistical Analysis Plan Page 13 of 26  
11 NOV 2015 Medtronic Confidential  
 
HR is included because those further away from 0.91 are under-estimating power. 
 
4800 was chosen because the 4750 estimate of 80.5 may be too high (compared to 4700 and 4800). 
 
 
 
 
Here is a screen shot of PASS mortality calculations 
 
 
  

Version 1 Improve SCA Statistical Analysis Plan Page 14 of 26  
11 NOV 2015 Medtronic Confidential  
 
PROGRAM SIM.SAS 
/****************************************************************************
********************************** 
  Program Name: SIM.SAS 
 
  Study: IMPROVE SCA 
 
  Purpose: Determing study sample size 
          
  Inputs: None 
 
  Outputs: None 
 
  Cautions: None 
 
  Revision                                         
  History:      Version     Date        Author                  Description 
                -------     ---------   -------------------     -------------
------------------------------ 
                      1     09DEC13     Jeff Cerkvenik         Initial 
Version 
*****************************************************************************
********************************/ 
 
OPTIONS PS=56; 
 
/* 
SS: TOTAL SAMPLE SIZE OF STUDY 
PROBSEC: PROBABILITY OF SECONDARY (AS OPPOSED TO PRIMARY) PREVENTION 
PROB15: PROBABILITY OF BEING 1.5 GIVEN THEY ARE PRIMARY 
IMPSEC: PROBABILITY THAT A SECONDARY PREVENTION PATIENT GETS AN IMPLANT 
IMP15: PROBABILITY THAT A 1.5 PATIENT GETS AN IMPLANT 
IMPPRIM: PROBABILITY THAT A PRIMARY (NON-1.5) PATIENT GETS AN IMPLANT 
FAILA12: PROBABILITY THAT A GROUP A PATIENT WILL HAVE AN APPROPRIATE VT/VF IN 
THE FIRST 12 MONTHS 
FAILALONG: PROBABILITY THAT A GROUP A PATIENT WILL HAVE AN APPROPRIATE VT/VF 
IN A GIVEN YEAR IN ANY YEAR AFTER THE FIRST 12 YEAR 
HRAC: ASSUMED HAZARD RATIO OF GROUP A TO GROUP C 
HRCE: ASSUMED HAZARD RATIO OF GROUP C TO GROUP E 
YEARSENROLL: YEARS TO GET FULL ENROLLMENT 
YEARLYATTRITION: ANNUAL ATTRITION DUE TO DEATH OR EXIT (IMPLANTED GROUPS A, 
C, AND E ONLY) 
YEARSFOLLOW: YEARS OF FOLLOW-UP FOLLOWING THE LAST ENROLLMENT 
*/ 
 
%MACRO STUDY ( 
SS, 
PROBSEC, 
PROB15, 
IMPSEC, 
IMP15, 
IMPPRIM, 
FAILA12, 
FAILALONG, 
HRAC, 
HRCE, 
YEARSENROLL, 
Version 1 Improve SCA Statistical Analysis Plan Page 15 of 26  
11 NOV 2015 Medtronic Confidential  
 
YEARLYATTRITION, 
YEARSFOLLOW); 
 
DATA STUDY; 
DO PT=1 TO &SS; 
   IMPDT=.; ENDDT=.; ATRTIME=.; FAILTIME=.; FAIL=.; SURVTIME=.; 
   *ICD INDICATION; 
   A=RAND('UNIFORM'); 
   IF A<&PROBSEC THEN IND='SECONDARY'; ELSE IND='PRIMARY'; 
 
   *1.0 OR 1.5?; 
   B=RAND('UNIFORM'); 
   IF B<&PROB15 THEN LEVEL='1.5'; ELSE LEVEL='1.0'; 
 
   *ACCEPT IMPLANT?; 
   C=RAND('UNIFORM'); 
   IF IND='SECONDARY' THEN DO; 
      IF C<&IMPSEC THEN IMP=1; ELSE IMP=0; 
   END; 
   IF IND='PRIMARY' THEN DO; 
      IF LEVEL='1.5' THEN DO; 
         IF C<&IMP15 THEN IMP=1; ELSE IMP=0; 
      END; 
      IF LEVEL='1.0' THEN DO; 
         IF C<&IMPPRIM THEN IMP=1; ELSE IMP=0; 
      END; 
   END; 
 
   IF IND='SECONDARY' AND IMP=1 THEN GROUP='A'; 
   IF IND='SECONDARY' AND IMP=0 THEN GROUP='B'; 
   IF IND='PRIMARY' AND LEVEL='1.5' AND IMP=1 THEN GROUP='C'; 
   IF IND='PRIMARY' AND LEVEL='1.5' AND IMP=0 THEN GROUP='D'; 
   IF IND='PRIMARY' AND LEVEL='1.0' AND IMP=1 THEN GROUP='E'; 
   IF IND='PRIMARY' AND LEVEL='1.0' AND IMP=0 THEN GROUP='F'; 
 
   *GET 10-YEAR PROBABILITY OF APPROPRIATE THERAPY (ASSUMING NO DEATH, EXIT, 
OR END OF STUDY); 
       FAILMONTH=.; 
       DO MONTH=1 TO 120;  *MONTHS; 
          *MORE FAILURES IN FIRST YEAR; 
          D=RAND('UNIFORM'); 
          IF GROUP='A' AND FAILMONTH=. THEN DO; 
             IF MONTH LE 12 THEN DO; 
                IF D<1-(1-&FAILA12)**(1/12) THEN FAILMONTH=MONTH; 
             END; 
             IF MONTH>12 THEN DO; 
                IF D<1-(1-&FAILALONG)**(1/12) THEN FAILMONTH=MONTH; 
             END; 
          END; 
          IF GROUP='C' AND FAILMONTH=. THEN DO; 
             IF MONTH LE 12 THEN DO; 
                IF D<1-(1-&FAILA12*&HRAC)**(1/12) THEN FAILMONTH=MONTH; 
             END; 
             IF MONTH>12 THEN DO; 
                IF D<1-(1-&FAILALONG*&HRAC)**(1/12) THEN FAILMONTH=MONTH; 
             END; 
          END; 
Version 1 Improve SCA Statistical Analysis Plan Page 16 of 26  
11 NOV 2015 Medtronic Confidential  
 
          IF GROUP='E' AND FAILMONTH=. THEN DO; 
             IF MONTH LE 12 THEN DO; 
                IF D<1-(1-&FAILA12*&HRAC*&HRCE)**(1/12) THEN FAILMONTH=MONTH; 
             END; 
             IF MONTH>12 THEN DO; 
                IF D<1-(1-&FAILALONG*&HRAC*&HRCE)**(1/12) THEN 
FAILMONTH=MONTH; 
             END; 
          END; 
       END; 
 
       E=RAND('UNIFORM'); 
       FAILTIME=ROUND((FAILMONTH-1)*365.25/12+E*30); 
 
 
 
 
   *CENSOR PATIENTS ALONG THE WAY; 
       *JAN 1, 2014 IS FIRST POSSIBLE DATE OF IMPLANT; 
       FORMAT IMPDT ENDDT LASTSTUDYDT DATE7.; 
       IF GROUP IN ('A','C','E') THEN DO; 
          *ASSUME SLOW ENROLLMENT TO BEGIN, WITH INCREASING ENROLLMENT OVER 
REST OF TIME PERIOD; 
              F=RAND('CHISQ',2); 
              IF F>4 OR F<0.1 THEN F=RAND('CHISQ',2); 
              IF F>4 OR F<0.1 THEN F=RAND('CHISQ',2); 
              IF F>4 OR F<0.1 THEN F=RAND('CHISQ',2); 
              *ABOVE WILL CAPTURE>99%.  FOR A FEW, JUST GIVE A MIDDLE VALUE; 
              IF F>4 OR F<0.1 THEN F=1+E; 
              XX=(F*(-1/3.9)+4/3.9); 
              IMPDT='01JAN14'D+ROUND((F*(-
1/3.9)+4/3.9)*(&YEARSENROLL*365.25)); 
 
           *ATTRITION DUE TO DEATH/EXIT; 
              ATRMONTH=.; 
              DO MONTH=1 TO 120; 
                 G=RAND('UNIFORM'); 
                 IF ATRMONTH=. AND G<1-(1-&YEARLYATTRITION)**(1/12) THEN 
ATRMONTH=MONTH; 
              END; 
              H=RAND('UNIFORM'); 
              ATRTIME=ROUND((ATRMONTH-1)*365.25/12+H*30); 
 
         *FIND OUT ATRITION DATE AND EVENT DATE, THEN USE THE EARLIER OF THE 
TWO; 
           IF FAILTIME NE . AND ATRTIME NE . THEN 
ENDDT=IMPDT+MIN(FAILTIME,ATRTIME); 
           IF FAILTIME = . AND ATRTIME NE . THEN ENDDT=IMPDT+ATRTIME; 
           IF FAILTIME NE . AND ATRTIME = . THEN ENDDT=IMPDT+FAILTIME; 
           IF FAILTIME = . AND ATRTIME = . THEN ENDDT=IMPDT+3653; 
           IF ENDDT=IMPDT+FAILTIME AND FAILTIME NE . THEN FAIL=1; ELSE 
FAIL=0; 
 
         *GET END OF STUDY; 
           ENDSTUDYDT='01JAN14'D+INT((&YEARSENROLL+&YEARSFOLLOW)*365.25); 
           *ASSUME LAST FOLLOW-UP WILL BE WITHIN 3 MONTHS OF END STUDY; 
           I=RAND('UNIFORM'); 
Version 1 Improve SCA Statistical Analysis Plan Page 17 of 26  
11 NOV 2015 Medtronic Confidential  
 
           LASTSTUDYDT=ENDSTUDYDT-INT(I*91); 
 
           IF ENDDT>LASTSTUDYDT THEN DO; 
              ENDDT=LASTSTUDYDT; 
              FAIL=0; 
           END; 
 
           SURVTIME=(ENDDT-IMPDT)/365.25*12; 
       END; 
 
*FOR PHREG SO THE HR IS C/A; 
GROUP2='   '; 
IF GROUP='C' THEN GROUP2=' C'; 
IF GROUP='A' THEN GROUP2='A'; 
IF GROUP='E' THEN GROUP2='  E'; 
 
OUTPUT; 
END; 
RUN; 
 
ODS LISTING CLOSE; 
PROC LIFETEST timelist=(12,24,36) DATA=STUDY; 
STRATA GROUP; 
TIME SURVTIME*FAIL(0); 
SURVIVAL out=CI conftype=loglog stderr; 
RUN; 
 
DATA CI; 
SET CI; 
FAILURE=1-SURVIVAL; 
FUCL=1-SDF_LCL; 
FLCL=1-SDF_UCL; 
RUN; 
 
DATA CI12; 
SET CI; 
WHERE SDF_LCL NE . AND SURVTIME<12; 
RUN; 
 
PROC SORT; 
BY GROUP SURVTIME; 
RUN; 
 
DATA CI12; 
SET CI12; 
BY GROUP SURVTIME; 
IF NOT LAST.GROUP THEN DELETE; 
RUN; 
 
DATA CI24; 
SET CI; 
WHERE SDF_LCL NE . AND SURVTIME<24; 
RUN; 
 
PROC SORT; 
BY GROUP SURVTIME; 
RUN; 
Version 1 Improve SCA Statistical Analysis Plan Page 18 of 26  
11 NOV 2015 Medtronic Confidential  
 
 
DATA CI24; 
SET CI24; 
BY GROUP SURVTIME; 
IF NOT LAST.GROUP THEN DELETE; 
RUN; 
 
DATA CI36; 
SET CI; 
WHERE SDF_LCL NE . AND SURVTIME<36; 
RUN; 
 
PROC SORT; 
BY GROUP SURVTIME; 
RUN; 
 
DATA CI36; 
SET CI36; 
BY GROUP SURVTIME; 
IF NOT LAST.GROUP THEN DELETE; 
RUN; 
 
PROC PHREG DATA=STUDY; 
WHERE GROUP IN ('A','C'); 
CLASS GROUP2; 
*ALPHA=0.1 GIVES ONE-SIDED 95% CONFIDENCE INTERVAL; 
MODEL SURVTIME*FAIL(0)=GROUP2 / RL ALPHA=0.1; 
ODS OUTPUT ParameterEstimates=HRAC; 
RUN; 
 
PROC PHREG DATA=STUDY; 
WHERE GROUP IN ('E','C'); 
CLASS GROUP2; 
MODEL SURVTIME*FAIL(0)=GROUP2 / RL; 
ODS OUTPUT ParameterEstimates=HRCE; 
RUN; 
 
PROC PHREG DATA=STUDY; 
WHERE GROUP IN ('A','E'); 
CLASS GROUP2; 
MODEL SURVTIME*FAIL(0)=GROUP2 / RL; 
ODS OUTPUT ParameterEstimates=HRAE; 
RUN; 
 
PROC LIFETEST DATA=STUDY; 
WHERE GROUP IN ('A','E'); 
STRATA GROUP; 
TIME SURVTIME*FAIL(0); 
ODS OUTPUT HomTests=LOGRANKAE; 
RUN; 
 
PROC LIFETEST DATA=STUDY; 
WHERE GROUP IN ('C','E'); 
STRATA GROUP; 
TIME SURVTIME*FAIL(0); 
ODS OUTPUT HomTests=LOGRANKCE; 
RUN; 
Version 1 Improve SCA Statistical Analysis Plan Page 19 of 26  
11 NOV 2015 Medtronic Confidential  
 
 
PROC FREQ DATA=STUDY NOPRINT; 
TABLES GROUP / OUT=GROUPN; 
RUN; 
ODS LISTING; 
 
DATA STUDYRES; 
MERGE  
CI12 (WHERE=(GROUP='A') RENAME=(FAILURE=FAIL_A12 FLCL=FLCL_A12 FUCL=FUCL_A12) 
KEEP=GROUP FAILURE FLCL FUCL) 
CI12 (WHERE=(GROUP='C') RENAME=(FAILURE=FAIL_C12 FLCL=FLCL_C12 FUCL=FUCL_C12) 
KEEP=GROUP FAILURE FLCL FUCL) 
CI12 (WHERE=(GROUP='E') RENAME=(FAILURE=FAIL_E12 FLCL=FLCL_E12 FUCL=FUCL_E12) 
KEEP=GROUP FAILURE FLCL FUCL) 
CI24 (WHERE=(GROUP='A') RENAME=(FAILURE=FAIL_A24 FLCL=FLCL_A24 FUCL=FUCL_A24) 
KEEP=GROUP FAILURE FLCL FUCL) 
CI24 (WHERE=(GROUP='C') RENAME=(FAILURE=FAIL_C24 FLCL=FLCL_C24 FUCL=FUCL_C24) 
KEEP=GROUP FAILURE FLCL FUCL) 
CI24 (WHERE=(GROUP='E') RENAME=(FAILURE=FAIL_E24 FLCL=FLCL_E24 FUCL=FUCL_E24) 
KEEP=GROUP FAILURE FLCL FUCL) 
CI36 (WHERE=(GROUP='A') RENAME=(FAILURE=FAIL_A36 FLCL=FLCL_A36 FUCL=FUCL_A36) 
KEEP=GROUP FAILURE FLCL FUCL) 
CI36 (WHERE=(GROUP='C') RENAME=(FAILURE=FAIL_C36 FLCL=FLCL_C36 FUCL=FUCL_C36) 
KEEP=GROUP FAILURE FLCL FUCL) 
CI36 (WHERE=(GROUP='E') RENAME=(FAILURE=FAIL_E36 FLCL=FLCL_E36 FUCL=FUCL_E36) 
KEEP=GROUP FAILURE FLCL FUCL) 
HRAC (RENAME=(HAZARDRATIO=HR_AC HRLOWERCL=HRL_AC HRUPPERCL=HRU_AC) 
KEEP=HAZARDRATIO HRLOWERCL HRUPPERCL) 
HRCE (RENAME=(HAZARDRATIO=HR_CE HRLOWERCL=HRL_CE HRUPPERCL=HRU_CE) 
KEEP=HAZARDRATIO HRLOWERCL HRUPPERCL) 
HRAE (RENAME=(HAZARDRATIO=HR_AE HRLOWERCL=HRL_AE HRUPPERCL=HRU_AE) 
KEEP=HAZARDRATIO HRLOWERCL HRUPPERCL) 
LOGRANKAE (WHERE=(TEST='Log-Rank') RENAME=(ProbChiSq=LOGRANKAE) KEEP=TEST 
ProbChiSq) 
LOGRANKCE (WHERE=(TEST='Log-Rank') RENAME=(ProbChiSq=LOGRANKCE) KEEP=TEST 
ProbChiSq) 
GROUPN (WHERE=(GROUP='A') RENAME=(COUNT=GROUPA_SS) KEEP=GROUP COUNT) 
GROUPN (WHERE=(GROUP='B') RENAME=(COUNT=GROUPB_SS) KEEP=GROUP COUNT) 
GROUPN (WHERE=(GROUP='C') RENAME=(COUNT=GROUPC_SS) KEEP=GROUP COUNT) 
GROUPN (WHERE=(GROUP='D') RENAME=(COUNT=GROUPD_SS) KEEP=GROUP COUNT) 
GROUPN (WHERE=(GROUP='E') RENAME=(COUNT=GROUPE_SS) KEEP=GROUP COUNT) 
GROUPN (WHERE=(GROUP='F') RENAME=(COUNT=GROUPF_SS) KEEP=GROUP COUNT) 
; 
 
DROP GROUP TEST; 
RUN; 
 
%MEND; 
 
 
*% ASSUMPTIONS CAME FROM QUESTIONS ASKED OF 2 CHINESE, 1 INDIAN, AND 1 
BELARUSSION PHYSICIANS.  THEY WERE ASKED TO ESTIMATE % 
    AT THEIR CENTER, THEN IN THE REST OF THEIR COUNTRY.  iT IS ASSUMED THAT 
1/3 OF THE PTS WILL BE CHINA, 1/3 INDIA, AND 1/3 THE REST. 
 
% OF SECONDARY: 
Chasnoits: 75% HIS CENTER / 75% OTHERS 
Version 1 Improve SCA Statistical Analysis Plan Page 20 of 26  
11 NOV 2015 Medtronic Confidential  
 
BALBIR: 70/80 
ZHANGE: 50/50 
HUANG: 30/55 
52% CHINA, 78% INDIA, AND 75% ROW = 68% 
 
% OF SECONDARY THAT GET IMPLANTED: 
Chasnoits: 98/90 
BALBIR: 80/45 
ZHANGE: 50/15 
HUANG: 50/30 
30% CHINA, 50% INDIA, 91% ROW = 57% 
 
% OF 1.5 THAT GET IMPLANTED: 
Chasnoits: 65/65 
BALBIR: NO GUESS 
ZHANGE: 60/25 
HUANG: 40/30 
30% CHINA, 40% INDIA, 65% ROW = 45% 
 
% OF 1.0 THAT GET IMPLANTED: 
Chasnoits: 40/40 
BALBIR: 15/5 
ZHANGE: 40/10 
HUANG: 30/30 
20% CHINA, 6% INDIA, 40% ROW = 22% 
; 
 
%MACRO LOOP(NUM,SS,PROBSEC,YEARSENROLL,YEARSFOLLOW); 
DATA ALLSTUDIES; 
RUN; 
 
%DO X = 1 %TO &NUM; 
%STUDY( 
SS=&SS, 
PROBSEC=&PROBSEC, 
PROB15=0.5, 
IMPSEC=0.57, 
IMP15=0.45, 
IMPPRIM=0.22, 
/*FAIL VARIABLES BELOW WERE CHOSEN TO BEST MATCH THE 12-MONTH FAILURE RATES 
AND THE HAZARD RATIOS IN OMNI.  HR OF C TO A WAS 0.909.  HR OF E TO C WAS 
0.678*/ 
FAILA12=0.225, 
FAILALONG=0.1110, 
HRAC=0.91, 
HRCE=0.68, 
YEARSENROLL=&YEARSENROLL, 
YEARLYATTRITION=0.1, 
YEARSFOLLOW=&YEARSFOLLOW); 
 
DATA ALLSTUDIES; 
SET ALLSTUDIES STUDYRES; 
RUN; 
%END; 
 
DATA RESULTS; 
SET ALLSTUDIES; 
Version 1 Improve SCA Statistical Analysis Plan Page 21 of 26  
11 NOV 2015 Medtronic Confidential  
 
WHERE FAIL_A12 NE .; 
 
*IF WE WANT STUDY RESULT TO BE THAT C IS CLOSER TO A THAN IT IS TO E; 
    *BASED ON DIFFERENCES AT 36 MONTHS.  TOO UNSTABLE TO USE: SOMETIMES 
FAIL_E > FAIL_C, YET HR_CE IS STILL <1; 
/*        DIFFAC=FAIL_A-FAIL_C;*/ 
/*        DIFFCE=FAIL_C-FAIL_E;*/ 
/*        IF FAIL_E>0 THEN DO;*/ 
/*            IF DIFFCE>DIFFAC THEN OBS_SUCCESS=1; ELSE OBS_SUCCESS=0;*/ 
/*        END;*/ 
/*        ELSE DO;*/ 
/*            IF DIFFAC<0.04 THEN OBS_SUCCESS=1; ELSE OBS_SUCCESS=0;    */ 
/*        END;*/ 
 
    IF HR_AC>1 THEN OBS_SUCCESS2=1;  
    ELSE IF FAIL_E12>0 THEN DO; 
        IF HR_AC > HR_CE THEN OBS_SUCCESS2=1; ELSE OBS_SUCCESS2=0; 
    END; 
    ELSE DO; 
        IF HR_AC> 0.9 THEN OBS_SUCCESS2=1; ELSE OBS_SUCCESS2=0;     
    END; 
    LABEL OBS_SUCCESS2='SUCEESSFUL TRIAL?  SUCCESS BASICALLY DEFINED AS HR OF 
C TO A HIGHER THAN E TO C'; 
 
*NON-INFERIORITY TEST - MARGINS OF 20, 25, AND 30%; 
    IF HRL_AC>0.7 THEN NONINF70=1; ELSE NONINF70=0; 
    IF HRL_AC>0.75 THEN NONINF75=1; ELSE NONINF75=0; 
    IF HRL_AC>0.8 THEN NONINF80=1; ELSE NONINF80=0; 
    IF HRL_AC>0.85 THEN NONINF85=1; ELSE NONINF85=0; 
    IF HRL_AC>0.9 THEN NONINF90=1; ELSE NONINF90=0; 
 
*SUCCESS IF 2.0 IS HIGHER THAN 1.0 AND 1.5 IS HIGHER THAN 1.0; 
    IF LOGRANKAE<0.05 AND LOGRANKCE<0.05 AND HR_CE<1 THEN SUPSUCCESS=1; 
    ELSE IF LOGRANKAE<0.05 AND HR_AE<1 THEN SUPSUCCESS=0.2; 
    ELSE IF LOGRANKCE<0.05 AND HR_CE<1 THEN SUPSUCCESS=0.1; 
    ELSE SUPSUCCESS=0; 
 
*OPC SUCCESS; 
IF FLCL_C12>0.15 THEN OPC15SUCCESS12=1; ELSE OPC15SUCCESS12=0; 
IF FLCL_C24>0.15 THEN OPC15SUCCESS24=1; ELSE OPC15SUCCESS24=0; 
IF FLCL_C36>0.15 THEN OPC15SUCCESS36=1; ELSE OPC15SUCCESS36=0; 
IF FLCL_C12>0.20 THEN OPC20SUCCESS12=1; ELSE OPC20SUCCESS12=0; 
IF FLCL_C24>0.20 THEN OPC20SUCCESS24=1; ELSE OPC20SUCCESS24=0; 
IF FLCL_C36>0.20 THEN OPC20SUCCESS36=1; ELSE OPC20SUCCESS36=0; 
IF FLCL_C12>0.25 THEN OPC25SUCCESS12=1; ELSE OPC25SUCCESS12=0; 
IF FLCL_C24>0.25 THEN OPC25SUCCESS24=1; ELSE OPC25SUCCESS24=0; 
IF FLCL_C36>0.25 THEN OPC25SUCCESS36=1; ELSE OPC25SUCCESS36=0; 
 
*NARROW CONFIDENCE INTERVAL SUCCESS; 
CIWIDTH12=FUCL_C12-FLCL_C12; 
CIWIDTH24=FUCL_C24-FLCL_C24; 
CIWIDTH36=FUCL_C36-FLCL_C36; 
IF CIWIDTH12<0.05 THEN CI05SUCCESS12=1; ELSE CI05SUCCESS12=0;  
IF CIWIDTH24<0.05 THEN CI05SUCCESS24=1; ELSE CI05SUCCESS24=0; 
IF CIWIDTH36<0.05 THEN CI05SUCCESS36=1; ELSE CI05SUCCESS36=0; 
IF CIWIDTH12<0.08 THEN CI08SUCCESS12=1; ELSE CI08SUCCESS12=0;  
IF CIWIDTH24<0.08 THEN CI08SUCCESS24=1; ELSE CI08SUCCESS24=0; 
Version 1 Improve SCA Statistical Analysis Plan Page 22 of 26  
11 NOV 2015 Medtronic Confidential  
 
IF CIWIDTH36<0.08 THEN CI08SUCCESS36=1; ELSE CI08SUCCESS36=0; 
IF CIWIDTH12<0.10 THEN CI10SUCCESS12=1; ELSE CI10SUCCESS12=0;  
IF CIWIDTH24<0.10 THEN CI10SUCCESS24=1; ELSE CI10SUCCESS24=0; 
IF CIWIDTH36<0.10 THEN CI10SUCCESS36=1; ELSE CI10SUCCESS36=0; 
IF CIWIDTH12<0.12 THEN CI12SUCCESS12=1; ELSE CI12SUCCESS12=0;  
IF CIWIDTH24<0.12 THEN CI12SUCCESS24=1; ELSE CI12SUCCESS24=0; 
IF CIWIDTH36<0.12 THEN CI12SUCCESS36=1; ELSE CI12SUCCESS36=0; 
IF CIWIDTH12<0.15 THEN CI15SUCCESS12=1; ELSE CI15SUCCESS12=0;  
IF CIWIDTH24<0.15 THEN CI15SUCCESS24=1; ELSE CI15SUCCESS24=0; 
IF CIWIDTH36<0.15 THEN CI15SUCCESS36=1; ELSE CI15SUCCESS36=0; 
RUN; 
 
TITLE "SAMPLE SIZE IS &SS, PROBSEC=&PROBSEC, YEARS OF ENROLLMENT: 
&YEARSENROLL, YEARS OF FOLLOW-UP: &YEARSFOLLOW"; 
 
PROC FREQ; 
TABLES OBS_SUCCESS2 NONINF70 NONINF75  
OPC15SUCCESS12 OPC15SUCCESS24 OPC15SUCCESS36 
OPC20SUCCESS12 OPC20SUCCESS24 OPC20SUCCESS36 
OPC25SUCCESS12 OPC25SUCCESS24 OPC25SUCCESS36 
CI05SUCCESS12 CI05SUCCESS24 CI05SUCCESS36 
CI08SUCCESS12 CI08SUCCESS24 CI08SUCCESS36 
CI10SUCCESS12 CI10SUCCESS24 CI10SUCCESS36 
CI12SUCCESS12 CI12SUCCESS24 CI12SUCCESS36 
CI15SUCCESS12 CI15SUCCESS24 CI15SUCCESS36; 
RUN; 
 
PROC MEANS N MEAN MEDIAN MAXDEC=3 DATA=ALLSTUDIES; 
VAR FAIL_A12 FAIL_C12 FAIL_E12 FAIL_A24 FAIL_C24 FAIL_E24 HR_AC HR_CE 
GROUPA_SS GROUPB_SS GROUPC_SS GROUPD_SS GROUPE_SS GROUPF_SS; 
RUN; 
%MEND; 
 
 
 
%LOOP(10000,SS=4000,PROBSEC=0.6,YEARSENROLL=1.97,YEARSFOLLOW=2); 
%LOOP(10000,SS=4050,PROBSEC=0.6,YEARSENROLL=1.99,YEARSFOLLOW=2); 
%LOOP(10000,SS=4100,PROBSEC=0.6,YEARSENROLL=2.01,YEARSFOLLOW=2); 
%LOOP(10000,SS=4150,PROBSEC=0.6,YEARSENROLL=2.02,YEARSFOLLOW=2); 
%LOOP(10000,SS=4200,PROBSEC=0.6,YEARSENROLL=2.04,YEARSFOLLOW=2); 
%LOOP(10000,SS=4250,PROBSEC=0.6,YEARSENROLL=2.06,YEARSFOLLOW=2); 
%LOOP(10000,SS=4300,PROBSEC=0.6,YEARSENROLL=2.07,YEARSFOLLOW=2); 
%LOOP(10000,SS=4350,PROBSEC=0.6,YEARSENROLL=2.09,YEARSFOLLOW=2); 
%LOOP(10000,SS=4400,PROBSEC=0.6,YEARSENROLL=2.11,YEARSFOLLOW=2); 
%LOOP(10000,SS=4450,PROBSEC=0.6,YEARSENROLL=2.12,YEARSFOLLOW=2); 
%LOOP(10000,SS=4500,PROBSEC=0.6,YEARSENROLL=2.14,YEARSFOLLOW=2); 
%LOOP(10000,SS=4550,PROBSEC=0.6,YEARSENROLL=2.16,YEARSFOLLOW=2); 
%LOOP(10000,SS=4600,PROBSEC=0.6,YEARSENROLL=2.18,YEARSFOLLOW=2); 
%LOOP(10000,SS=4650,PROBSEC=0.6,YEARSENROLL=2.19,YEARSFOLLOW=2); 
%LOOP(10000,SS=4700,PROBSEC=0.6,YEARSENROLL=2.21,YEARSFOLLOW=2); 
%LOOP(10000,SS=4750,PROBSEC=0.6,YEARSENROLL=2.23,YEARSFOLLOW=2); 
%LOOP(10000,SS=4800,PROBSEC=0.6,YEARSENROLL=2.24,YEARSFOLLOW=2); 
%LOOP(10000,SS=4850,PROBSEC=0.6,YEARSENROLL=2.26,YEARSFOLLOW=2); 
%LOOP(10000,SS=4900,PROBSEC=0.6,YEARSENROLL=2.28,YEARSFOLLOW=2); 
%LOOP(10000,SS=4950,PROBSEC=0.6,YEARSENROLL=2.29,YEARSFOLLOW=2); 
%LOOP(10000,SS=5000,PROBSEC=0.6,YEARSENROLL=2.31,YEARSFOLLOW=2); 
 
Version 1 Improve SCA Statistical Analysis Plan Page 23 of 26  
11 NOV 2015 Medtronic Confidential  
 
 
 
 
 
 
 
 
/* 
 
 
%macro plot(name); 
%LOOP(1,SS=3000,YEARSENROLL=1.6,YEARSFOLLOW=1); 
DATA JJJ; 
SET STUDY; 
IF SURVTIME=. THEN DELETE; 
IF GROUP='A' THEN G=1; 
IF GROUP='C' THEN G=2; 
IF GROUP='E' THEN G=3; 
RUN; 
 
PROC FORMAT; 
VALUE type 1='A' 2='C' 3='E'; 
RUN; 
 
PROC PRINT DATA=RESULTS; 
VAR HR_AC   HR_CE; 
RUN; 
 
%MKMPlot(indata=JJJ, 
        TRT=G, 
  TRTfmt= TYPE., 
        PlotType=failure, 
  SubjectID=PT,  
  TimeToEvent=SURVTIME, 
  EventIND=FAIL, 
  Censored=0, 
        ShowHazardRatio=Y, 
        ShowLogRankPvalue=n, 
        ShowCI=Y, 
        SurvivalRateDataPointsSwap=y, 
  xaxismax=36,xaxisby=6,  
  Yaxismax=0.50,Yaxisby=.10,  
        yaxislabel=%nrbquote(% with Appropriately Treated VT/VF),              
        xaxislabel=%nrbquote(Months Since Implant),              
  SubjectsatRiskBy=6, 
  GraphfilePath=V:\Improve SCA\Sample Size, 
        GraphFilename=&name, 
        SurvivalRateDataPoints=12$24$36$48$60$72, 
        StopPlotCount=20, 
        AtRiskText=%str(Number Reamining) 
             ); 
%mend; 
 
%PLOT(SIM1); 
%PLOT(SIM2); 
%PLOT(SIM3); 
%PLOT(SIM4); 
Version 1 Improve SCA Statistical Analysis Plan Page 24 of 26  
11 NOV 2015 Medtronic Confidential  
 
%PLOT(SIM5); 
%PLOT(SIM6); 
%PLOT(SIM7); 
%PLOT(SIM8); 
%PLOT(SIM9); 
%PLOT(SIM10); 
%PLOT(SIM11); 
%PLOT(SIM12); 
%PLOT(SIM13); 
%PLOT(SIM14); 
%PLOT(SIM15); 
%PLOT(SIM16); 
%PLOT(SIM17); 
%PLOT(SIM18); 
%PLOT(SIM19); 
%PLOT(SIM20); 
 
 
 
 
 
/* 
 
 
 
 
 
PROC LIFETEST DATA=STUDY; 
STRATA GROUP; 
TIME SURVTIME*FAIL(0); 
RUN; 
 
PROC FREQ DATA=STUDY; 
TABLES IMPDT; 
RUN; 
 
PROC PRINT DATA=STUDY; 
WHERE GROUP IN ('A','C','E') AND SURVTIME=.; 
RUN; 
 
PROC SORT DATA=STUDY; 
BY IMPDT; 
RUN; 
 
PROC PRINT DATA=STUDY; 
VAR PT IMPDT ENDDT FAILMONTH ATRMONTH SURVTIME FAIL; 
RUN; 
 
 
 
 
*GET A VS. C ONLY; 
DATA JJJ; 
SET STUDY; 
IF SURVTIME=. THEN DELETE; 
IF GROUP='E' THEN DELETE; 
IF GROUP='A' THEN G=1; 
Version 1 Improve SCA Statistical Analysis Plan Page 25 of 26  
11 NOV 2015 Medtronic Confidential  
 
IF GROUP='C' THEN G=2; 
IF GROUP='E' THEN G=3; 
RUN; 
 
PROC FORMAT; 
VALUE type 1='A' 2='C' 3='E'; 
RUN; 
 
%MKMPlot(indata=JJJ, 
        TRT=G, 
  TRTfmt= TYPE., 
        PlotType=failure, 
  SubjectID=PT,  
  TimeToEvent=SURVTIME, 
  EventIND=FAIL, 
  Censored=0, 
        ShowHazardRatio=Y, 
        ShowLogRankPvalue=y, 
        ShowCI=Y, 
        SurvivalRateDataPointsSwap=y, 
  xaxismax=36,xaxisby=6,  
  Yaxismax=0.50,Yaxisby=.10,  
        yaxislabel=%nrbquote(% with Appropriately Treated VT/VF),              
        xaxislabel=%nrbquote(Months Since Implant),              
  SubjectsatRiskBy=6, 
  GraphfilePath=V:\Improve SCA\Sample Size, 
        GraphFilename=SIMULATIONAC, 
        SurvivalRateDataPoints=12$24$36$48$60$72, 
        StopPlotCount=20, 
        AtRiskText=%str(Number Reamining) 
             ); 
 
 
 
 
*GET C VS. E ONLY; 
DATA JJJ; 
SET STUDY; 
IF SURVTIME=. THEN DELETE; 
IF GROUP='A' THEN DELETE; 
IF GROUP='A' THEN G=1; 
IF GROUP='C' THEN G=2; 
IF GROUP='E' THEN G=3; 
RUN; 
 
PROC FORMAT; 
VALUE type 1='A' 2='C' 3='E'; 
RUN; 
 
%MKMPlot(indata=JJJ, 
        TRT=G, 
  TRTfmt= TYPE., 
        PlotType=failure, 
  SubjectID=PT,  
  TimeToEvent=SURVTIME, 
  EventIND=FAIL, 
  Censored=0, 
Version 1 Improve SCA Statistical Analysis Plan Page 26 of 26  
11 NOV 2015 Medtronic Confidential  
 
        ShowHazardRatio=Y, 
        ShowLogRankPvalue=y, 
        ShowCI=Y, 
        SurvivalRateDataPointsSwap=y, 
  xaxismax=36,xaxisby=6,  
  Yaxismax=0.50,Yaxisby=.10,  
        yaxislabel=%nrbquote(% with Appropriately Treated VT/VF),              
        xaxislabel=%nrbquote(Months Since Implant),              
  SubjectsatRiskBy=6, 
  GraphfilePath=V:\Improve SCA\Sample Size, 
        GraphFilename=SIMULATIONCE, 
        SurvivalRateDataPoints=12$24$36$48$60$72, 
        StopPlotCount=20, 
        AtRiskText=%str(Number Reamining) 
             ); 
 