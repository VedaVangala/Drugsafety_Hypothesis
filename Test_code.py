# Import packages
import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
import pingouin as pg
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
drug_safety = pd.read_csv("drug_safety.csv")

# Create a DataFrame "df" for better readability
df = pd.DataFrame(drug_safety)

# Group data "GD" by adverse effects and treatment groups, and count occurrences
GD = df.groupby("adverse_effects")["trx"].value_counts()
print(GD)

# Group data "GD1" by treatment group and calculate total counts
GD1 = GD.groupby('trx').sum()
print(GD1)

# Extract counts of "Yes" (adverse effects) for the proportions z-test
Yes = GD["Yes"]
print(Yes)

# Perform two-sample proportions z-test
two_sample_results = proportions_ztest(Yes, GD1)
print(two_sample_results[1])

# Perform chi-square independence test for association between num_effects and trx
stats = pg.chi2_independence(data=df, x='num_effects', y='trx')
print(stats)

# Extract p-value from chi-square test results
num_effects_p_value = stats[2]["pval"][0]
print(num_effects_p_value)

# Visualize age distribution using histograms
sns.histplot(data=df, x="age")
sns.histplot(data=df, x="age", hue="trx")
plt.savefig('plot.png')  # Save the histogram plot
# plt.show()

# Extract age data for Drug and Placebo groups
age_placebo = df.loc[df['trx'] == 'Placebo', 'age']
print(age_placebo)
age_trx = df.loc[df['trx'] == 'Drug', 'age']
print(age_trx)

# Perform Mann-Whitney U test to compare age between groups
age_grp = pg.mwu(age_placebo, age_trx)
print(age_grp)

# Extract p-value from Mann-Whitney U test results for age comparison
age_group_effects_p_value = age_grp['p-val']
print(age_group_effects_p_value)
