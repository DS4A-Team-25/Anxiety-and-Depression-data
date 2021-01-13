# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# TJ ADDED THIS CELL

# +
# TJ Also added this cell 
# -

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df_symptoms = pd.read_csv("data/Indicators_of_Anxiety_or_Depression_Based_on_Reported_Frequency_of_Symptoms_During_Last_7_Days.csv")

df_symptoms

df_symptoms.info()

# +
variables = ['Indicator', 'Group']

for x in variables:
    print('Variables for',x,":")
    print(df_symptoms[x].value_counts() )
# -

df_symptoms.groupby(by = 'Phase').mean()

df_symptoms.pivot_table(values = 'Value', index = 'State', columns = 'Phase', aggfunc = np.mean)

hips = df_symptoms.groupby(['Phase','Indicator','Group','Subgroup',])
hips.describe()

fase1_edad = df_symptoms[(df_symptoms['Phase'] == 1) & (df_symptoms['Indicator']== 'Symptoms of Anxiety Disorder') 
                         & (df_symptoms['Group'] == 'By Age')]
fase1_edad

# +
subgrp_variables = [subgroups for subgroups in df_symptoms['Subgroup']]

def filtering(phase, indicator, group, subgroup = subgrp_variables):
    "This filters the data set by: Phase of Coronavirus Pandemic (1, 2, or 3), Indicator (Symptom of Anxiety Disorder or Symptoms of Depressive Disorder), Groups (By: Age, Education, Gender, Race/Hispanic ethnicity). Optional- Subgroup.  "
    filtered_table = df_symptoms[(df_symptoms['Phase'] == phase) & (df_symptoms['Indicator']== indicator) & (df_symptoms['Group'] == group) & (df_symptoms['Subgroup'] == subgroup)]
    return filtered_table



# -

# # Depressive Disorder

# ## By Age

# **Examining percentages of people across Age groups that have Symptoms of Depressive Disorder in Phase 1**

# +
#Examining percentages of people across age groups that have Symptoms of Depressive Disorder in Phase 1
filtered_DepP1_age = filtering(1,'Symptoms of Depressive Disorder', 'By Age')

viz_DepP1_age = sns.catplot(x="Value", y="Subgroup", data= filtered_DepP1_age, kind = "violin", hue = 'State')
# -

# **Examining percentages of people across Age groups that have Symptoms of Depressive Disorder in Phase 2**

# +
filtered_DepP2_age = filtering(2,'Symptoms of Depressive Disorder', 'By Age')

viz_DepP2_age = sns.catplot(x="Value", y="Subgroup", data= filtered_DepP2_age, kind = "violin", hue = 'State')
# -

# ## By Gender

# **Examining percentages of people across gender groups that have Symptoms of Depressive Disorder in Phase 1**

# +
filtered_DepP1_gender = filtering(1,'Symptoms of Depressive Disorder', 'By Gender')

viz_DepP1_gender = sns.catplot(x="Value", y="Subgroup", data= filtered_DepP1_gender, kind = "violin", hue = 'State')
# -

# **Examining percentages of people across gender groups that have Symptoms of Depressive Disorder in Phase 1**

# +
filtered_DepP2_gender = filtering(2,'Symptoms of Depressive Disorder', 'By Gender')

viz_DepP2_gender = sns.catplot(x="Value", y="Subgroup", data= filtered_DepP2_gender, kind = "violin", hue = 'State')
# -

# # Anxiety Disorder

# ## By Age

# **Examining percentages of people across Age groups that have Symptoms of Depressive Disorder in Phase 1**

# +
filtered_AnxP1_age = filtering(1,'Symptoms of Anxiety Disorder', 'By Age')

viz_AnxP1_age = sns.catplot(x="Value", y="Subgroup", data= filtered_AnxP1_age, kind = "violin", hue = 'State')
# -

# **Examining percentages of people across Age groups that have Symptoms of Depressive Disorder in Phase 2**

# +
filtered_AnxP2_age = filtering(2,'Symptoms of Anxiety Disorder', 'By Age')

viz_AnxP2_age = sns.catplot(x="Value", y="Subgroup", data= filtered_AnxP2_age, kind = "violin", hue = 'State')
# -

# **Examining percentages of people across gender groups that have Symptoms of Anxiety Disorder in Phase 1**

# ## By Gender

# +
filtered_AnxP1_gender = filtering(1,'Symptoms of Anxiety Disorder', 'By Gender')

viz_AnxP1_gender = sns.catplot(x="Value", y="Subgroup", data= filtered_AnxP1_gender, kind = "violin", hue = 'State')
# -

# **Examining percentages of people across gender groups that have Symptoms of Depressive Disorder in Phase 2**

# +
filtered_AnxP2_gender = filtering(2,'Symptoms of Anxiety Disorder', 'By Gender')

viz_AnxP2_gender = sns.catplot(x="Value", y="Subgroup", data= filtered_AnxP2_gender, kind = "violin", hue = 'State')
# -

dips = df_symptoms.groupby(['State','Indicator'])
dips.describe()


# +
# Define a function
def show_me_your_contents(group):
    group_by_values = group[0] # group[0] is the values used to group by
    head_of_df = group[1].head() # group[1].head() is the DataFrame (only the head)
    return [group_by_values, head_of_df]

# Loop through groups

[ show_me_your_contents(group) for group in dips ] # Using list comprehension


# +
# Define a function
def plot_state_over_time(group):
    group_by_values = group[0] # group[0] is the values used to group by
    state_df = group[1] # group[1] is the DataFrame 
    #plot line graph of value over time period
    state_df.plot.line(x='Time Period', y='Value') 
    plt.title(group_by_values)
    plt.xlabel("Time Period")
    plt.ylabel("Value")

# Loop through groups

[ plot_state_over_time(group) for group in dips ] # Using list comprehension
# -

wips = df_symptoms.groupby(['State'])
wips.describe()


# Define a function
def plot_state_over_time_stacked(group):
    group_by_values = group[0] # group[0] is the values used to group by
    state_df = group[1] # group[1] is the DataFrame 
    df_to_plot = state_df.pivot_table(values = 'Value', index = 'Time Period', columns = 'Indicator', aggfunc = np.mean)
    #plot line graph of value over time period
    plt.plot( x='Time Period', y='Symptoms of Depressive Disorder', data=df_to_plot)
    plt.plot( x='Time Period', y='Symptoms of Anxiety Disorder or Depressive Disorder', data=df_to_plot)
    plt.plot( x='Time Period', y='Symptoms of Anxiety Disorder', data=df_to_plot)
    #plt.legend()
    #plt.title(state_df['State'])
    plt.xlabel("Time Period")
    plt.ylabel("Value")
  
