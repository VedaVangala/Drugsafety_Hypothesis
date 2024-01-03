# **Drugsafety_Hypothesis**


## Objective:
Explore and analyze a drug safety dataset from a randomized controlled trial conducted by the pharmaceutical company. The primary focus is on adverse reactions to the drug and understanding if there are significant differences between the treatment groups (Drug and Placebo).


## Data Exploration:
The dataset drug_safety.csv was obtained from Hbiostat courtesy of the Vanderbilt University Department of Biostatistics. The dataset includes information on adverse effects which are required to test drug safety. It contained five adverse effects: headache, abdominal pain, dyspepsia, upper respiratory infection, chronic obstructive airway disease, demographic data, vital signs, lab measures, etc. For this project, the dataset has been modified to reflect the presence and absence of adverse effects adverse_effects and the number of adverse effects in a single individual num_effects. Ratio of drug to placebo observations in this trial is 2 to 1.


## **Two-Sample Proportions Z-Test**
- Conducted a two-sample proportions Z-test to compare adverse effect proportions between the Drug and Placebo groups.
- *Result*: No significant difference in adverse effect proportions (p-value = 0.9639).


## **Association between Adverse Effects and Groups (Chi-Square Test)**
- Investigated the association between the number of adverse effects (num_effects) and treatment groups (trx) using a chi-square test.
- *Result*: No significant association between num_effects and trx groups (p-value = 0.6150).


## **Inspecting Whether Age is Normally Distributed**##
### Histogram Visualization
- Created histograms to inspect the distribution of ages for both Drug and Placebo groups.
- *Result*: The left-skewed age distribution suggests that a significant portion of the participants in the study are older, with fewer participants in the younger age groups. 
### Mann-Whitney U Test
- Conducted a Mann-Whitney U test to determine if there's a significant difference in age between the Drug and Placebo groups.
- *Result*: No significant difference in age between the groups (p-value = 0.256963).


## **Overall Findings**

### Adverse Effects: No significant difference in proportions between Drug and Placebo groups.
### Association: No significant association between num_effects and trx groups.
### Age: No significant difference in age between Drug and Placebo groups.
